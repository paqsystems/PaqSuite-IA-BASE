# Ajustes de inventario

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_series_st/?p=17028/

## Contenido

# Ajustes de inventario

A través de este proceso es posible registrar comprobantes de ajuste. Estos indican las entradas y salidas de stock.

Se utiliza, por ejemplo, para el ingreso de diferencias de inventario y disminución de stock por robo, rotura o mercadería en mal estado.  
El sistema permite imprimir un comprobante como reflejo del movimiento generado, aplicando el formulario definido en el talonario asociado al tipo de comprobante de ajuste utilizado. Si no se ha definido el formulario, el ajuste será ingresado al sistema sin emitirse la impresión.  
Si el sistema está configurado para que Lleve doble unidad de medida desde [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st) y el tipo de comprobante de ajuste está configurado para que permita ajustar una unidad de stock, no se aplica el control entre las unidades de stock durante el ingreso de comprobantes.

##### Encabezado

Tipo de comprobante: corresponderá a un código definido con Tipo de movimiento = 'J' (ajuste de stock).

Depósito general: si indica un código de depósito, todos los renglones del comprobante se asignarán a éste. En cambio, si este campo se deja en blanco, los renglones del comprobante se referenciarán a distintos depósitos, generando salidas para cada uno de ellas. No es posible seleccionar un depósito que se encuentre inhabilitado.

Sucursal destino: indique la sucursal destino en la que se exportará el comprobante. Este dato es opcional, pero no se debe omitir su ingreso si es un comprobante que se exportará. Este dato se utiliza en el proceso de exportación de movimientos de stock.  
Si el comprobante es valorizado, los importes quedarán expresados en la moneda seleccionada. La reexpresión bimonetaria se realizará de acuerdo a la cotización vigente, la que puede modificarse desde este proceso.

##### Renglones

Código de artículo: código de identificación correspondiente al artículo. Es posible referenciar al artículo por su código, sinónimo o código de barras.

E/S: en este campo se indicará, por cada renglón, si el movimiento corresponde a una entrada o a una salida de stock.

Depósito: si no indicó un depósito general en el encabezado, seleccione el depósito del renglón. No será posible elegir un depósito que se encuentre inhabilitado.

Cantidad: ingrese la cantidad de unidades, expresada siempre en unidades de stock.

Unidad de medida: se exhibe la sigla de la unidad de medida de stock del [artículo](https://ayudas.axoft.com/24ar/articulo_carp_st). Para los artículos que llevan doble unidad de medida, se exhibe la unidad de stock definida como la unidad que controla el stock.

Precio unitario: si el tipo de comprobante seleccionado fue definido como valorizado, se ingresará un precio unitario. Este permite valorizar el movimiento y afectará los costos del artículo, según la parametrización del tipo de comprobante.

Aclaración:

En el caso que se ingrese un renglón con un artículo que lleve doble unidad de medida, y a su vez, controle con la unidad de stock 2, el precio unitario corresponderá al precio de la unidad de stock 1.

<F7> Partidas  
Si utiliza partidas, y se incluye en el comprobante algún artículo con partida, se ingresarán las partidas de ingreso o egreso según corresponda.  
Si es una entrada, se visualizará una ventana con todos los datos de las partidas. Indicando un número de partida existente, el ingreso actualizará el saldo de la partida. Si el número ingresado no existe se creará la partida, siendo entonces necesario ingresar todos sus datos.  
Si es una salida, será posible seleccionar la partida de egreso de las existentes para el artículo y el depósito. En este caso, sólo podrá ingresarse una partida por renglón.  
Además es posible ingresar partidas existentes en un despacho de importación; pero tenga en cuenta que no afectará al costo de la partida.

<F8> Series  


Pulsando <F8> sobre alguno de los renglones del comprobante, podrá ingresar las series en caso de haber configurado desde parámetros de Stock el ingreso de serie no obligatorio, o para consultar las series que han sido cargadas en el renglón

<F3> Cambia edición  
Durante el ingreso de los renglones del comprobante, es posible modificar la descripción o agregar renglones con descripciones adicionales. Estas descripciones podrán ser impresas en el comprobante.

##### Auditoría de comprobantes

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Video sobre permisos eventuales](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/permisoevent_gral_vid/)

  * [Videos sobre toma de inventario](https://ayudas.axoft.com/24ar/videos/st_carp_vid/tomainventario_st_vid/)
