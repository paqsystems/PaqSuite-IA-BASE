# Asignación de partidas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=17040/

## Contenido

# Asignación de partidas

Mediante este proceso se asignan los saldos de un artículo a diferentes partidas. Utilice este proceso para indicar que un artículo con movimientos lleva partidas.  


Una vez finalizado el proceso se activará automáticamente el parámetro Lleva Partidas del artículo.  
Este proceso es de suma utilidad para llevar partidas de un artículo con saldos de stock existente, ya que la modificación del parámetro no será posible desde el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st).  
Para la correcta asignación de las partidas, se generará un comprobante de stock no valorizado, en el que se registrarán las salidas de artículos por los saldos asignados y las entradas a las partidas correspondientes.  
Para generar el comprobante de asignación se ingresará un Tipo y Número de comprobante.  
El Tipo de comprobante corresponderá a un código definido con Tipo de movimiento = 'J' (ajuste) y no valorizado.  
Al seleccionar un artículo, indique el método de descarga y el orden a aplicar. El proceso muestra en pantalla la composición del saldo en los diferentes depósitos.  
Pulsando <F7> se abre una ventana para la asignación del saldo del artículo correspondiente al depósito del renglón seleccionado. Será posible indicar partidas existentes en el sistema. Si la partida existe, se exhibirán en pantalla los datos relacionados con ésta (número de despacho, país de origen, aduana), permitiendo la modificación de su costo unitario. Pero, si se trata de una nueva partida, se permitirá el ingreso de los datos correspondientes.

__Nota

No se puede asociar artículos a partidas originadas por un despacho de importación.

De esta manera se asignará la totalidad del saldo de cada depósito a una o varias partidas.  
Para cada partida asignada por artículo será posible ingresar un costo, el que estará expresado en la moneda seleccionada en el encabezado del comprobante. La reexpresión bimonetaria se realizará de acuerdo a la cotización vigente.  
Una vez generado el comprobante de asignación, el artículo queda parametrizado para llevar partidas. Por tal motivo, cada vez que se realice un movimiento de ingreso o egreso de stock, el sistema pedirá la referencia de la partida correspondiente.  
Para los artículos que llevan doble unidad de medida, se debe asignar la totalidad del saldo en stock 1 como de stock 2 de cada depósito a una o varias partidas.

Artículos que usan serie  
Mediante este proceso no quedarán relacionadas las partidas a las series. Para relacionarlas acceda a los siguientes procesos que se encuentran en el módulo Stock:

  * [Mantenimiento de series por artículo](?p=17183).
  * [Visor de series y partidas pendientes de relacionar](https://ayudas.axoft.com/25ar/visorserpartpendrelac_st).
