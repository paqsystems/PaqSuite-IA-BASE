# Guía de Punto de Venta sobre facturación y remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv2/guia_circfactremito_gv2/

## Contenido

# Guía de Punto de Venta sobre facturación y remitos

El sistema contempla distintos circuitos posibles para la emisión de facturas y remitos.

En cuanto a los remitos, existen dos situaciones diferentes para su generación:

  1. Si el parámetro Descarga stock al facturar está activo, el movimiento de stock se asociará a la factura (modalidad factura-remito).
  2. Utilizar el proceso [Emisión de remitos](?p=19291) para generar el egreso del stock. Estos remitos pueden ser facturados posteriormente. Este sería el caso en que se utiliza la descarga de stock diferida (en un momento se remite la mercadería y en otro se factura). El modelo de formulario a utilizar en el proceso [Emisión de remitos](?p=19291) será RESK.TYP. Utilizando este proceso, los movimientos de stock quedan registrados con tipo de comprobante igual a 'REM' y el número de remito correspondiente.



Más información:

Según el circuito de facturación de su empresa, determine la emisión de facturas y remitos.

__Nota

Recuerde que la tecla rápida _**< F3>**_ permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

##### Contenidos relacionados

No se ha encontrado ninguno
