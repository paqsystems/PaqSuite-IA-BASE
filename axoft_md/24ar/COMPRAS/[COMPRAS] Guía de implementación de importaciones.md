# Guía de implementación de importaciones

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_importac_cp2/

## Contenido

# Guía de implementación de importaciones

Esta guía le permitirá conocer todos los requisitos y configuraciones necesarias para el circuito de importaciones.

A continuación se detalla el orden de configuración y los pasos a seguir para utilizar el circuito de importaciones.

##### Puesta en marcha

Para utilizar el circuito de importaciones, siga estos pasos:

  * Talonarios:
    * Configure los talonarios para los comprobantes a utilizar en el circuito de importaciones (carpetas y despachos). Los talonarios asignados facilitan el control de la impresión y la numeración de los comprobantes. Para más información consulte [Talonarios](https://ayudas.axoft.com/24ar/talonario_cp2).
  * Proveedores:
    * Configure que proveedores van a asociar carpetas. Para más información consulte [Proveedores](https://ayudas.axoft.com/24ar/proveedores_cp2).
  * Artículos con partidas de importación:
    * Configure los artículos a importar indicando que estos utilizan partidas, las que se asignaran al momento de generar el despacho, identificando de esta manera el ingreso al stock.  
Opcionalmente vinculará el artículo a los proveedores deseados, con el fin de agilizar la búsqueda de estos en las carpetas. Para más información consulte Artículos y la guía sobre implementación de partidas.
  * Parámetros de Compras:
    * Configure los parámetros relacionados a importaciones para definir el funcionamiento del sistema referido a la actualización de precios, numeración de embarques, agrupación de artículos y distribución de gastos. Para más información consulte [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2).



##### Detalle del circuito

Para implementar el circuito de importaciones, siga estos pasos:

  * Carpeta de importación:
    * Defina el detalle de la compra a realizar y dará comienzo al circuito de importaciones. Para más información, consulte [Carpetas de importación](https://ayudas.axoft.com/24ar/carpimport_carp_cp2).
  * Asociación de comprobantes:
    * Mediante este proceso vincule distintos comprobantes a una o varias carpetas de importación.  
Los comprobantes vinculados a las carpetas se toman en cuenta para calcular el costo de los artículos importados (por ejemplo la factura de un transporte). Para más información consulte [Asociación de comprobantes a carpetas de importación](https://ayudas.axoft.com/24ar/importasoccomprcarp_cp2).
  * Embarque:
    * Mediante el comprobante de embarque usted realiza el seguimiento de la mercadería en tránsito, indicando información de la embarcación, fecha de partida, fecha de arribo y las carpetas asociadas al embarque. Para más información consulte [Embarques](https://ayudas.axoft.com/24ar/embarqingreso_cp2).
  * Despacho:
    * Realice la nacionalización de la mercadería y el ingreso en el sistema de todos los gastos realizados en la importación. Para más información, consulte [Despachos](https://ayudas.axoft.com/24ar/despingreso_cp2).
  * Factura de importación:
    * Mediante este comprobante, registre los importes abonados al proveedor del exterior por la mercadería importada. Para más información, consulte [Facturas de importación](https://ayudas.axoft.com/24ar/factimport_cp2).
  * Costos de importación:
    * Mediante este proceso, realice el cálculo de los costos de los artículos importados, considerando el precio abonado y los gastos intervinientes en la importación de la mercadería. Para más información, consulte [Costos de importación](https://ayudas.axoft.com/24ar/costos_cp2).
