# Facturas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_ivasimple_gv/?p=15368/

## Contenido

# Facturas

Existen tres procesos para el ingreso de facturas de proveedores, el uso de cada uno de ellos dependerá de las características del comprobante a ingresar.

Los procesos de ingreso de facturas son: [Factura - Remito](https://ayudas.axoft.com/24ar/comprobingrfact_cp2) (con movimiento de stock), [Factura](https://ayudas.axoft.com/24ar/factura1_carp_cp2) (sin movimiento de stock), [Factura de Conceptos](https://ayudas.axoft.com/24ar/factconcepto_cp2) y [Factura de Importación](https://ayudas.axoft.com/24ar/factimport_cp2).

Con respecto a la integración con el módulo de Activo Fijo, consulte los siguientes temas:

  * Integración de artículos con el módulo Activo Fijo.
  * Integración de gastos de compras con el módulo Activo Fijo.
  * Alta automática de bienes para Activo Fijo.
  * Alta automática de gastos para bienes de Activo Fijo.



##### Aclaraciones generales de cada opción

###### Factura - Remito

Si la factura actualiza el saldo de stock, debe ingresarla mediante el proceso [Factura - Remito](https://ayudas.axoft.com/24ar/comprobingrfact_cp2). En este proceso, además de registrar la transacción en cuenta corriente se genera un movimiento de entrada de stock.  
Es importante aclarar que la actualización del saldo de stock se refiere al comprobante en general, independientemente de que un artículo lleve stock asociado.  
Si desea ingresar una factura de artículos definidos para no llevar stock asociado, pero el comprobante no tiene ninguna relación con remitos, se ingresará a través del proceso [Factura - Remito](https://ayudas.axoft.com/24ar/comprobingrfact_cp2).

###### Factura

Si la factura a ingresar no mueve stock porque se imputa a remitos previamente ingresados, o aún no se recibió la mercadería (pendiente de recepción), debe ingresarla por el proceso [Facturas](https://ayudas.axoft.com/24ar/factura1_carp_cp2). Este proceso no genera movimiento de stock.  
Siempre podrán ingresarse por este proceso facturas con referencia a remitos o a órdenes de compra, pero una factura pendiente de recepción podrá ingresarse o no según el valor del parámetro correspondiente del proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) o el [perfil de facturas de compra](https://ayudas.axoft.com/24ar/perffacturacp_cp2).

###### Factura de Conceptos

Si la factura no está relacionada con artículos sino que corresponde a conceptos de compras, debe ingresarla por el proceso [Facturas de conceptos](https://ayudas.axoft.com/24ar/factconcepto_cp2).  
En los siguientes gráficos se detallan los circuitos y relaciones entre comprobantes de compras previstos en el sistema:

##### Perfiles de factura de compra

Mediante el uso de perfiles puede variar el comportamiento de los diferentes procesos de ingreso de facturas de compras, ya sea para agilizar la carga de información como para restringir el acceso a diferentes opciones.  
Para configurar perfiles ingrese al proceso de [Factura de compras](https://ayudas.axoft.com/24ar/perffacturacp_cp2) ingrese a Carga inicial | Perfiles | Factura de compra.  
Los perfiles afectan a los siguientes procesos: [Factura - Remito](https://ayudas.axoft.com/24ar/comprobingrfact_cp2), [Factura](https://ayudas.axoft.com/24ar/factura1_carp_cp2) y [Factura de conceptos](https://ayudas.axoft.com/24ar/factconcepto_cp2).  
Entre otras cosas, puede configurar:

  * El comportamiento de los diferentes campos de pantalla, indicando si se editan, muestran u ocultan.
  * El valor por defecto para cada campo.
  * Los controles a efectuar en diferentes campos, por ejemplo los campos de ingreso de fechas.
  * El tipo de artículos que puede utilizar el usuario, por ejemplo indicar si utiliza artículos que identifican bienes (Activo fijo), o indicar el perfil de artículo que puede seleccionar (Compras o Compra/Venta).
  * El comportamiento para referenciar comprobantes (ordenes de compra, remitos, etc.).
  * La posibilidad de asociar datos adjuntos.



##### Contenido dependiente

  * [Factura - Remito de Compras](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/comprobfactura_cp2/comprobingrfact_cp2/)
  * [Facturas de compras](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/comprobfactura_cp2/facturacompras_carp_cp2/)
  * [Facturas de importación](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/comprobfactura_cp2/factimport_cp2/)
  * [Factura de conceptos](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/comprobfactura_cp2/factconcepto_cp2/)
  * [Ingreso de comprobantes T](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/comprobfactura_cp2/factingrcomprobt_cp2/)
