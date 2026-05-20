# Alta automática de bienes para Activo Fijo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=5901/

## Contenido

# Alta automática de bienes para Activo Fijo

Opcionalmente es posible crear automáticamente bienes en el módulo Activo Fijo, cuando en el comprobante registrado se especifican renglones de artículos que estén identificados como bienes.

El alta automática se puede realizar desde la registración de comprobantes de los procesos de:

  * Factura-Remito, factura, factura de importación.
  * Nota de débito.



En caso de confirmar el alta automática, se abrirá una nueva pantalla con los artículos contenidos en el comprobante que estén identificados como bienes. Se mostrará y podrá generar por cada unidad de producto comprada del artículo, un determinado bien (según la cantidad especificada para el artículo en el renglón del comprobante).

Otros datos necesarios para el alta del bien son los siguientes:  
Los datos del comprobante de compras (Código y Razón Social del Proveedor, Tipo y número del comprobante, Fecha de compra) quedan registrados en la solapa de [Origen del bien](?p=5033) disponible en la ficha del Bien del módulo Activo Fijo.

Fecha de alta: se registra la fecha de sistema al momento de la carga del comprobante.

Fecha de compra: corresponde a la fecha de emisión del comprobante de Compras.

Moneda del bien, cotización y valor del bien: la moneda de registración del comprobante de compras determina la moneda del bien dado de alta. En caso que el comprobante de compras se haya registrado en moneda extranjera, en el bien se guardará la cotización en relación a la moneda corriente. El valor del bien quedará expresado siempre en la moneda corriente (es decir, en la Moneda base definida en el módulo Procesos Generales.

Genera: se proponen tantos bienes como cantidades se haya indicado en el renglón del comprobante para cada artículo. Se podrá marcar o desmarcar los bienes que correspondan crear en el módulo Activo Fijo.

Código del bien: es un código obligatorio con el que se identificará unívocamente el bien creado en Activo Fijo. Se puede especificar manualmente al momento de realizar el alta automática de bienes, como así también es posible generarlo automáticamente según se haya indicado en los [Parámetros de Activo Fijo](?p=5948).

Descripción del bien: por defecto se propone la descripción del artículo. En caso que no se modifiquen las descripciones, todos los bienes creados tendrán la misma descripción, y podrán modificarse desde el item [Bienes](?p=5033) en el módulo Activo Fijo.

Tipo de bien: se asigna por defecto el tipo de bien indicado para el artículo. Los bienes creados conservan por defecto los siguientes datos especificados en el tipo de bien:

  * **Características para depreciación:** se parametriza si el bien está habilitado para el cálculo de depreciación o no, y en caso de corresponder, los valores para el método de depreciación, unidad para la vida útil, vida útil, el método de depreciación, porcentaje depreciable, frecuencia y valor fin vida útil.
  * **Cuentas contables para movimientos:** cuenta del bien, cuenta de compra, cuenta depreciación, cuenta depreciación extraordinaria, cuenta depreciación acumulada, cuenta para mejoras, cuenta revalúo, cuenta de baja, cuenta resultado ajuste, cuenta resultado por tenencia.
  * **Identificaciones adicionales:** se asignan al bien las características comunes indicadas para el tipo de bien. Puede especificar cada valor particular referente al bien, en forma posterior al alta automática, desde el item [Bienes](?p=5033) en el módulo **Activo Fijo**.



Número de serie: este dato es único por cada bien. Es posible modificar o cargar las series en caso que en los Parámetros de Stock no se haya parametrizado un Ingreso de Series Obligatorio, caso contrario se visualizan las series indicadas en el comprobante para los artículos definidos con 'Lleva serie'.

Costo: por defecto se propone como importe que afecta al valor de origen del bien, el precio neto del artículo para el comprobante. Este importe puede modificarse para el alta de bienes. En caso de indicarse otro importe, en el ítem [Bienes](?p=5033) en el módulo Activo Fijo, se visualizará el Importe del renglón original para el comprobante, y el Importe indicado para afectar el valor de origen del bien. El importe está expresado en la moneda del comprobante.

**Ejemplo...**  
Factura de compra

  * Artículo 1 código 0200200031 cantidad 3 unidades (identificado como bien)
  * Artículo 2 código 0200200032 cantidad 2 unidades (identificado como bien)
  * Artículo 3 código 0200200033 cantidad 1 unidad (no representa un bien)  
En este ejemplo, la codificación automática de bienes es según el código de artículo, con "-" como separador y completando con ceros a izquierda.



Al confirmar el alta automática de bienes luego del ingreso de la factura de compras, se sugiere el alta de los siguientes bienes para el módulo de Activo Fijo, con las siguientes características:

Artículo 1 código 0200200031: se sugiere la creación de 3 códigos de bienes:

  * código bien 0200200031-00001
  * código bien 0200200031-00002
  * código bien 0200200031-00003



Artículo 2 código 0200200032: se sugiere la creación de 2 códigos de bienes:

  * código bien 0200200032-00001
  * código bien 0200200032-00002



Para más información sobre la creación automática de bienes consulte [Integración de artículos con el módulo Activo Fijo](?p=5938/#integracion-de-activo-fijo-con-stock).  
Para más información sobre la afectación de gastos a los datos de origen de bienes consulte Ingreso de factura de conceptos.  
Para más información sobre la integración con el módulo Activo Fijo y la administración de los bienes consulte [Guía sobre administración de bienes](?p=5922) con el módulo Activo Fijo.
