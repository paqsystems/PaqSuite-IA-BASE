# Alta automática de gastos para bienes de Activo Fijo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=5902/

## Contenido

# Alta automática de gastos para bienes de Activo Fijo

Opcionalmente es posible asociar automáticamente importes de comprobantes de conceptos a bienes existentes en el módulo Activo Fijo, cuando en el comprobante registrado se especifican renglones de conceptos que estén identificados.

El alta automática se puede realizar desde la registración de comprobantes de los procesos de

  * Factura de conceptos
  * Nota de débito de conceptos



__Nota

Mediante esta opción no se realiza creación de bienes; es posible realizar una asociación de importes de comprobantes para la puesta en marcha de bienes. Indique mediante la opción Considera el importe del gasto para el cálculo del valor de origen si el importe imputado a cada bien incrementa el valor de origen de cada bien.  
Los bienes posibles de seleccionar para la afectación de gastos son aquellos existentes en el módulo Activo Fijo (ya sea se hayan creado desde [Bienes](?p=5033) o bien desde el [Alta automática de bienes para Activo Fijo](?p=5901)), siempre y cuando estén pendientes de activar.

Mediante esta opción no se realiza creación de bienes; es posible realizar una asociación de importes de comprobantes para la puesta en marcha de bienes.  
Indique mediante la opción Considera el importe del gasto para el cálculo del valor de origen si el importe imputado a cada bien incrementa el valor de origen de cada bien.  
Los bienes posibles de seleccionar para la afectación de gastos son aquellos existentes en el módulo Activo Fijo (ya sea se hayan creado desde [Bienes](?p=5033) o bien desde el [Alta automática de bienes para Activo Fijo](?p=5901)), siempre y cuando estén pendientes de activar.  
En caso de confirmar la afectación de gastos, se abrirá una nueva pantalla con los conceptos contenidos en el comprobante que estén identificados para Activo Fijo.  
Se podrá afectar el 100% o una parte del gasto a uno o varios bienes existentes en el módulo de Activo Fijo.

Moneda del bien, cotización y valor del bien: la moneda de registración del comprobante de Compras determina la moneda del bien dado de alta. En caso que el comprobante de Compras se haya registrado en moneda extranjera, en el bien se guardará la cotización en relación a la moneda corriente. El valor del bien quedará expresado siempre en la moneda corriente (es decir, en la Moneda base definida en el módulo Procesos generales).

Otros datos necesarios para la distribución de gastos a bienes son los siguientes:

Los datos del comprobante de compras (Código y Razón Social del Proveedor, Tipo y número del comprobante, Fecha de compra, Concepto de compra) quedan registrados en la solapa de Origen del bien disponible en [Bienes](?p=5033) del módulo Activo Fijo.

Código del bien: seleccione los bienes pendientes de activar, que desea afectar los importes de los conceptos de compras.

Porcentaje e Importe: para cada bien indique el porcentaje o el importe de participación que corresponde del total del importe del concepto de compras.

Si se indica el 100% significa que la totalidad del concepto se afectará al bien seleccionado.  
Por defecto se propone el 100% del precio neto del concepto del comprobante como importe que afecta a los datos de origen del bien. Este importe puede modificarse.  
La suma total de los porcentajes asignados no debe superar el 100% para cada concepto de compras.  
Si el porcentaje es inferior al 100%, quedará un porcentaje restante pendiente de imputación (sin asignar a ningún bien). Este porcentaje pendiente de imputación podrá afectarse con posterioridad al alta automática de gastos, seleccionando el comprobante de compras desde la solapa _Origen del bien_ disponible en el ítem [Bienes](?p=5033) del módulo Activo Fijo, y se visualizará en este caso el Importe del renglón original para el comprobante y el Importe afectado a los datos de origen del bien.  
El importe está expresado en la moneda del comprobante.

__Nota

Cuando en el mismo comprobante existen varios conceptos afectados al módulo Activo Fijo, para agilizar la distribución, es posible seleccionar -previamente a la distribución propiamente dicha- los bienes que se desean afectar, indicando para cada uno un porcentaje determinado por defecto.  
Luego presione el botón "Completar distribución de gastos…" y los importes de los conceptos de compras se distribuirán con la misma proporción entre los bienes indicados. Luego es posible modificar la distribución de gastos a generar por bien.

**Ejemplo...**

Factura de conceptos

Concepto HONORARIOS | Importe = 500 | (afectado a Activo Fijo)  
---|---|---  
Concepto SEGURO | Importe = 600 | (afectado a Activo Fijo)  
  
(afectado a Activo Fijo)

Al confirmar el alta automática de gastos para bienes, luego del ingreso de la factura de compras, se realiza la siguiente distribución:

Concepto HONORARIOS (Importe = 500):

  * código bien 0200200031-00001 90% = 450
  * código bien 0200200031-00002 10% = 50



Concepto SEGURO (Importe = 600):

  * código bien 0200200032-00001 90% = 540
  * código bien 0200200032-00002 10% = 60



Para más información sobre la creación automática de bienes consulte [Integración de artículos con el módulo de Activo Fijo](?p=5938/#integracion-de-activo-fijo-con-stock) e Ingreso de factura de artículos.  
Para más información sobre la afectación de gastos a los datos de origen de bienes consulte Ingreso de factura de conceptos.  
Para más información sobre la integración con el módulo Activo Fijo y la administración de los bienes consulte [Guía sobre administración de bienes](?p=5922) con el módulo Activo Fijo.
