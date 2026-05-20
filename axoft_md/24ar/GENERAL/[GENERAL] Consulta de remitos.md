# Consulta de remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=19261/

## Contenido

# Consulta de remitos

Este proceso permite consultar remitos o devoluciones previamente emitidos.

Mediante el comando Listar es posible reimprimir los remitos generados desde los procesos [Emisión de remitos](?p=19291) o el [Facturador](?p=18393), aplicando filtros por cliente, tipo y número de comprobante y fecha.  
Para reimprimir los remitos generados desde el proceso [Emisión de remitos](?p=19291) seleccione la opción 'Remito' en el campo Tipo de comprobante.  
Para reimprimir los remitos generados desde el Facturador y/o desde Facturación de pedidos, elija la opción 'Factura-Remito' en el campo Tipo de comprobante.  
El número a seleccionar corresponde al número de factura con la que se generó el remito.

**Ejemplo...  
**Desde el Facturador se ingresaron facturas-remito para varios clientes, y se necesita reimprimir uno de esos remitos. Para ello, se ejecutan los siguientes pasos:

  1. Ingrese al proceso Consulta de remitos y seleccione la opción Listar.
  2. Seleccione la opción 'Rango'.
  3. En Desde cliente / Hasta cliente, elija el código de cliente a procesar.
  4. En Desde fecha / Hasta fecha, ingrese la fecha del comprobante.
  5. En Tipo de comprobante, elija la opción 'Factura-Remito'.
  6. En Desde / Hasta número de comprobante, seleccione el número a reimprimir.



Tenga en cuenta:

Podrá reimprimir los remitos generados a partir de la versión **23.01.000**.  
Los destinos de impresión disponibles son: Pantalla, Impresión rápida, Acrobat PDF, Archivo de texto y Seleccionar impresora.  
No se reimprimirán los remitos exportados ni los anulados.  
En relación con los remitos que provienen de otra sucursal, éstos podrán ser reimpresos en la sucursal de destino, con la salvedad que no tendrán imagen de fondo (si ésta fue incluida en la sucursal de origen).  
Es posible obtener un informe de los remitos seleccionados que no pudieron ser reimpresos. Los motivos por los que un remito no puede ser reimpreso son:

  * El remito fue ingresado en una versión anterior a la **23.01.000** (se indica: 'NO ES POSIBLE REIMPRIMIR EL COMPROBANTE').
  * El remito fue exportado a otra sucursal (se indica: 'REMITO EXPORTADO').
  * El remito fue anulado mediante el proceso Anulación de remitos (se indica: 'REMITO ANULADO').



En el sector del encabezado se indica el estado del comprobante con relación al stock. Los valores posibles son:

  * Pendiente: tiene cantidades pendientes de facturar.
  * Cerrado: el comprobante se encuentra totalmente facturado o devuelto, o fue emitido con referencia a un pedido.
  * Anulado: el comprobante fue anulado.



Inf. Rentas: indica si el comprobante tiene asociado un Código de Operación de Traslado (C.O.T.) o bien, un Código de Integridad. Es decir, indica si el comprobante ha sido informado a Rentas Bs. As.  
Las cantidades de cada renglón del remito se visualizarán siempre en unidades de stock.  
Puede consultar la descripción adicional correspondiente a cada renglón del comprobante presionando la tecla <F3>.  
Pulse la tecla <F6> para ingresar y/o consultar los datos asociados con el transporte o traslado de bienes - Rentas Bs.As. Para más información, consulte en la ayuda o manual del módulo Ventas, el proceso [Modificación de comprobantes](https://ayudas.axoft.com/24ar/modifcomprobante_gv).  
Usted puede consultar en forma masiva esta información mediante el Informe de Remitos electrónicos / COT desde Tango Live.  
Si utiliza partidas, es posible consultarlas pulsando <F7> desde los renglones del comprobante.  
Pulse <F8> para consultar los números de series. Las cantidades del renglón que se muestran en la consulta están expresadas en la unidad de control de stock. Para el caso de los artículos que no llevan doble unidad de medida, es la unidad de stock 1. Para los artículos que llevan doble unidad de medida, es la unidad de medida de stock de control definida desde el proceso de carga de artículos.

<ALT+A> \- Observación del artículo  
Es posible consultar la observación del artículo (ingresada en el proceso [Emisión de remitos](?p=19291) o en el comprobante de referencia).

<Ctrl + F10> \- Consulta Integral de Clientes  
Usted puede acceder a toda la información comercial y financiera que le brinda la [Consulta integral de clientes](https://ayudas.axoft.com/24ar/consintegralcliente_gv).
