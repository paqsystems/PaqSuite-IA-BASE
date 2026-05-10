# Guía sobre artículos que usan series y partidas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_serpart_st/

## Contenido

# Guía sobre artículos que usan series y partidas

**Tango** incorpora la relación de las series con las partidas a fin de mejorar la trazabilidad de los productos. Esto implica que para los artículos que usan series y partidas, las series quedarán relacionadas a las partidas en todas las operaciones de entradas de stock que se realicen, de manera que al generar una salida de stock al seleccionar la serie se completará de manera automática la partida relacionada.

##### Preguntas frecuentes

**¿Dónde se configuran los parámetros nuevos sobre la relación de series y partidas?  
**Acceda a la solapa [Partidas](?p=17198/#partidas) de parámetros generales para configurar la modalidad de trabajo para los artículos que usan series y partidas.

**¿Cuáles son los parámetros nuevos de relación de series y partidas?  
**Acceda a consultar esta información desde [artículos con partidas y series](?p=17128/#articulos-con-partidas-y-series).

**¿Cuál es el impacto funcional para artículos con series y partidas?  
**Para mantener la trazabilidad de la relación de series y partidas, podrá configurar el [parámetro general](?p=17198) Criterio de búsqueda habitual para partidas y series en comprobantes de egreso con los valores estricto o flexible. Al realizar esta configuración, los parámetros generales Ingreso de serie obligatorio y Valida series en egreso, que se encuentran en la solapa de series, serán interpretados como obligatorios.  
Criterio de búsqueda habitual para partidas y series en comprobantes de egreso:

  * **Control estricto:** sólo puede utilizar series que pertenezcan a la partida previamente seleccionada.
  * **Control flexible:** puede utilizar series que pertenezcan a la partida previamente seleccionada o aquellas no asociadas a ninguna partida. Esta es la opción por defecto que asume el sistema.
  * **Sin control:** permite utilizar cualquier número de serie. Tenga en cuenta que esta opción afecta el concepto de trazabilidad de productos ya que permite que por ejemplo la serie XXX asociada inicialmente con la partida "P1" salga de su empresa asociada a la partida "P3".



**¿Cómo se relacionan las series y partidas de artículos que no están relacionadas?  
**El proceso que se encuentra en el [Visor de series y partidas pendientes de relacionar](?p=17398) le permite relacionar las series y partidas de artículos que no se encuentran relacionadas.

**¿Se pueden reasignar series y partidas de artículos que están mal relacionadas?  
**Si, puede hacerlo mediante el proceso [Ajustes de inventario](?p=17028).

**¿Se pueden cargar series en forma diferida?  
**Si, se pueden cargar series en forma diferida, siempre que se tenga la siguiente configuración en los [Parámetros de Stock](?p=17198):

  * Para artículos con series y partidas: 
    * _Criterio de búsqueda habitual para partidas y series en comprobantes de egreso = No controla_
    * _Orden de carga habitual de partidas y series en comprobantes = Partida / Serie_
    * _Ingreso de serie es obligatorio = No_
  * Para artículos con series: 
    * _Ingreso de serie es obligatorio = No_



**¿Dónde se cargan las series diferidas?  
**Puede hacerlo desde el proceso [Mantenimiento de series por comprobante](?p=17184).

##### Ingreso al stock de un artículo que usa series y partidas

Proceso | Módulo  
---|---  
[Ingresos a inventario](?p=17165) | Stock  
[Ingreso de remitos de Proveedores](?p=15394) | Compras  
[Ingreso de facturas / remito](?p=15372) | Compras  
[Ingreso de notas de débito](?p=15397) | Compras (si afecta stock)  
  
En cada proceso podrá indicar, desde una opción de la barra de herramientas, si desea comenzar a cargar la serie y luego la partida, o viceversa.  
En estos procesos que generan ingresos a stock, se realizará el movimiento de entrada de la partida y su serie relacionada.  
Si el orden de carga seleccionado es partida / serie, cuando se ingrese el primer artículo que lleva partidas y series en el momento de ingresar los renglones del comprobante, se desplegará automáticamente una ventana donde debe indicar los datos de la partida y luego complete la/las serie correspondientes.  
El ingreso de las series dependerá del [parámetro de Stock](?p=17198) de ingreso de serie obligatorio, como fue explicado en la [guía sobre implementación de series](?p=17149).  
Si el orden de carga seleccionado es serie / partida y se configuró desde [parámetros de Stock](?p=17198) el ingreso de serie obligatorio en 'no'. Desde los comprobantes de ingresos al stock se limita el orden de carga a partida / serie, desapareciendo de esta manera la posibilidad de cambiar el orden de carga desde la barra de herramientas del comprobante.  
En caso que desee completar las series, puede hacerlo desde cada renglón de partida pulsando <F8>.  
En caso que la numeración de la partida sea automática y el ingreso de serie sea obligatorio, luego de cargar la cantidad del renglón del comprobante se desplegará la pantalla de las series. Por cada serie ingresada el sistema completará la partida en forma automática.

__Nota

Tenga en cuenta que el sistema controlará que la suma de las cantidades de las partidas coincida con la cantidad de unidades ingresadas en el renglón y la suma de las series coincida con la cantidad ingresada en la partida.

Pulsando <F7> sobre alguno de los renglones del comprobante, podrá consultar las partidas ingresadas.  
Pulsando <F8> sobre alguno de los renglones del comprobante o sobre alguno de los renglones de la partida, podrá consultar las series ingresadas.

##### Egreso de stock de un artículo que usa series y partidas

Procesos de egreso de artículos que usan series y partidas:

Proceso | Módulo  
---|---  
[Egresos de stock](?p= 17089) | Stock  
[Notas de crédito](?p=15395) | Compras  
[Emisión de remitos](?p=19291) | Ventas  
[Facturas](?p=19302) | Ventas  
[Emisión de notas de débito](?p=19290) | Ventas  
  
Del mismo modo que en un ingreso de stock, podrá seleccionar el orden de carga de series y partidas o cambiar el orden pulsando <F12>.  
En caso que el orden de carga sea partida / serie y el método de descarga de partidas sea automático, esta pantalla se abrirá la pantalla de las series si es que su ingreso es obligatorio, usted podrá seleccionar las series relacionadas a cada partida. Pulsando <Enter> en el número de partida, se desplegará una lista de todas las partidas existentes para el artículo en el depósito de egreso, para que seleccione la partida deseada.  
La edición del número de partida se verá condicionada por el parámetro del artículo: Permite modificar la partida, donde podrá optar por modificar o no la partida que propone el sistema en el caso de descarga automática de partidas.  
Si el método de descarga es manual, debe ingresar primero seleccionar las partidas y por cada una indicar la o las series a descargar.

__Nota

Tenga en cuenta que el sistema controlará que la suma de las cantidades de las partidas coincida con la cantidad de unidades ingresadas en el renglón y la suma de las series coincida con la cantidad ingresada en la partida, este último control lo realizará en caso de haber activado el [parámetro de Stock](?p=17198) _Ingreso de serie obligatorio_.

Pulsando <F7> sobre alguno de los renglones del comprobante, podrá consultar las partidas ingresadas.  
Pulsando <F8> sobre alguno de los renglones del comprobante o sobre alguno de los renglones de la partida, podrá consultar las series ingresadas.

##### Casos de aplicación en egreso de comprobantes según la configuración de los parámetros de Stock

**Caso 1: Generar una factura de ventas que afecta stock  
**La configuración de [Parámetros de Stock](?p=17198) es la siguiente:

  * _Criterio de búsqueda habitual para partidas y series en comprobantes de egreso = Estricto._
  * _Orden de carga habitual de partidas y series en comprobantes = Partida / Serie._



Los siguiente parámetros toman ese valor por tener configurado los [Parámetros de Stock](?p=17198):

  * _Criterio de búsqueda habitual para partidas y series en comprobantes de egreso como 'Estricto' o 'Flexible'._
  * _Ingreso de serie es obligatorio = Si_
  * _Valida serie en egreso = Si_



**Resultado:**  
El operador va a cargar los números de partidas y por cada renglón de partida el sistema va a proponer las series disponibles para el artículo, depósito y partida ingresada.  
No se podrá generar la factura hasta que no se completen todas las series y partidas de los artículos que usen series y partidas.

**Caso 2: Generar una factura de ventas que afecta stock  
**La configuración de [Parámetros de Stock](?p=17198) es la siguiente:

  * _Criterio de búsqueda habitual para partidas y series en comprobantes de egreso = No controla_
  * _Orden de carga habitual de partidas y series en comprobantes = Partida / Serie_
  * _Ingreso de serie es obligatorio = No_
  * _Valida serie en egreso = No_



**Resultado:**  
El operador va a cargar los números de partidas y por cada renglón de partida el sistema va a proponer todas las series disponibles del artículo y el depósito ingresado sin importar si las series están relacionadas a otra partida. Además podrá optar por no ingresar las series por tener el parámetro general Ingreso de serie obligatorio en 'No', o en caso de ingresarlas podrá ingresar una series que no se encuentre activa en el sistema por tener configurado el parámetro de stock Valida serie en egreso en 'No'.

Más información:

  * **Consideraciones generales:**
    * Cuando orden de carga de series y partidas es: Serie / Partida, desde el renglón del comprobante siempre se accede primero a la pantalla de las series y desde allí se consultan las partidas.
    * Cuando orden de carga de series y partidas es: Partida / Serie, desde el renglón del comprobante siempre se accede primero a la pantalla de la partida y desde allí se consultan las series.
  * **Consideraciones para egresos del inventario:**
    * Cuando la descarga de partida es automática, el orden de carga de series y partidas se limita a: Partida / Serie.
    * Cuando el orden de carga de series y partidas es: Series / Partidas y además el ingreso de series no es obligatorio, no se habilita la opción de cambiar el orden de carga de series y partidas desde la barra de herramientas (Tecla de función: _< F12>_).
  * **Consideraciones para ingresos al inventario:**
    * Cuando el ingreso de series no es obligatorio y orden de carga de series y partidas es: Serie / Partida, el orden de carga de series y partidas se limita a Partida / Serie.
    * Al cargar el comprobante, no se podrá cambiar el orden de carga de series y partidas.
    * En caso de querer cargar las series cuando el ingreso de series no sea obligatorio, primero debe cargar las partidas y desde allí acceder al ingreso de las series.
