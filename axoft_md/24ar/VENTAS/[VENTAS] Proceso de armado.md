# Proceso de armado

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_kit_gv/?p=17237/

## Contenido

# Proceso de armado

Mediante este proceso es posible armar los artículos que tengan una composición definida en el proceso Fórmulas.

Se indicará el Tipo y Número de comprobante de armado. Bajo este comprobante se generará un movimiento de entrada (el artículo a armar) y varios movimientos de salida (los insumos utilizados).  
El Tipo de comprobante habrá sido definido previamente en el proceso [Tipos de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_st) y corresponderá a un Tipo de movimiento = 'A' (armado).

Número de comprobante: el sistema propone por defecto, el próximo número a emitir correspondiente al talonario asociado al tipo de comprobante. Se lo podrá editar de acuerdo a cómo esté parametrizado dicho talonario. Si el próximo número existe, el sistema buscará el siguiente válido para el mismo tipo de comprobante.

Depósito de origen: es el depósito desde el que se toman los insumos necesarios para el armado.  
En este proceso, el sistema solicitará su confirmación en el caso que el stock de algún insumo sea inferior a la cantidad necesaria para armar la cantidad solicitada de artículos.  
Para verificar si existen insumos suficientes para armar la cantidad solicitada en el depósito de origen puede utilizar el proceso Control de Insumos.

Depósito destino: depósito en el que se almacenará el artículo armado. No es posible seleccionar un depósito que se encuentre inhabilitado.

Valorizar salidas por: se refiere al precio de costo a considerar para cada uno de los insumos a utilizar. Se utilizará este valor para calcular el costo de armado y valorizar el movimiento de salida. Los valores posibles son:

  * Precio de Ultima Compra
  * Precio de Reposición
  * Precio Promedio Ponderado
  * Sin Valorizar



En el caso de seleccionar 'Precio Promedio Ponderado', tomará el PPP de acuerdo al siguiente criterio: si utiliza PPP con cierre mensual, el sistema considerará el PPP del último cierre realizado; mientras que si utiliza cierre mensual con valor diario, el sistema utilizará el PPP asignado a la Fecha hasta, independientemente del valor del cierre.

Arma: indica el método a utilizar para el proceso de armado.

Número de partida a generar: si el artículo a armar lleva partidas, se ingresarán los datos correspondientes a la partida de ingreso.  
El comportamiento para la numeración de las partidas se adecuará a lo indicado en el proceso [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st). Sin embargo, el comando Partidas permite modificar la modalidad vigente (solamente para los artículos armados sin salir del proceso). En el capítulo correspondiente a [Partidas](?p=17128) explicamos en detalle el ingreso de los datos correspondientes.  
Desde Descarga para partidas de insumos se define el comportamiento de esta descarga. Con la opción Método de Descarga del Artículo respetará la configuración establecida en el parámetro del artículo. Sin embargo se permite modificar esa modalidad vigente por los métodos: 'Manual', 'Número interno', 'Fecha ingreso', 'Fecha vencimiento'. Esta modificación sólo tendrá validez para la descarga de los artículos a armar, sin salir del proceso.

**Ejemplo...  
**Artículo 001 (siendo éste uno de los insumos a utilizar para el artículo a armar)

Lleva Partidas: SI

_Método de Descarga: Número Interno Orden de Descarga: Ascendente_

Ingresando al Proceso de armado, el comando Partidas, el sistema mostrará el método de descarga a utilizar para las partidas de insumos. El método ART corresponde al método del Artículo y se carga por defecto, es decir, el criterio y el orden establecido dentro de los parámetros del artículo. Siguiendo con el ejemplo el proceso de armado mantendrá el siguiente método:

_Método de Descarga: Número Interno Orden de Descarga: Ascendente_

Es posible modificar el método y el orden de descarga para partidas de insumos. Las opciones son: 'Manual', 'Número interno', 'Fecha ingreso', 'Fecha vencimiento'.

En el caso de modificar el método de descarga:

_Método de Descarga: Fecha de Ingreso Orden de Descarga: Ascendente_

El Proceso de Armado utilizará para este caso el siguiente método y orden:

_Método de Descarga: Fecha de Ingreso Orden de Descarga: Ascendente_

Una vez utilizado y cerrado el Proceso de armado se perderá ésta modificación respecto del método de descarga para partidas de insumo. Por lo tanto, cada vez que desea realizar un proceso de armado y no quiere utilizar el método y orden de descarga establecido dentro del parámetro del artículo deberá modificarlo por medio del comando Partidas.

Ingresa números de serie: tilde esta opción cuando quiera ingresar los números de serie generados (y utilizados) durante el armado del artículo. Si opta por ingresarlos, lo deberá hacer una vez confirmado el armado, indicando primero los números de serie generados y a continuación, las series utilizadas para cada insumo. De lo contrario (opta por no ingresarlos), los podrá incorporar en el proceso [Mantenimiento de series por comprobante](https://ayudas.axoft.com/24ar/mantenseriecomprobante_st) (si desea tener registrado qué comprobante generó dichas series) o en el de [Mantenimiento de series por artículo](?p=17183) (si únicamente desea que los números de serie figuren como "series activas").

__Nota

Si está tildado el parámetro general Ingreso de series obligatorio, no podrá editar este campo y deberá ingresar las series generadas y utilizadas durante el proceso de armado.

Cada número de serie está asociado a un depósito. En el capítulo correspondiente a [Series](?p=17149) explicamos en detalle su utilización.

Artículos que usan series y partidas

Para los artículos de tipo insumo: si se configuró el [parámetro](https://ayudas.axoft.com/24ar/parametrogeneral_st) Criterio de búsqueda habitual de partidas y series en comprobantes de egreso como estricto o flexible, los siguientes parámetros se interpretan de la siguiente manera:

  * _Ingreso de serie obligatorio = Si_
  * _Valida series en egreso = Si_



El orden de carga de series y partidas que se configura desde [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st) no será tenido en cuenta en el proceso de armado y tampoco podrá ser modificado desde el proceso de armado.  
Una vez especificada la moneda del comprobante, se emitirá un informe con los insumos faltantes, detallando la cantidad necesaria y la cantidad existente para cada uno. Si existen faltantes y se confirma el proceso, los insumos faltantes quedarán en el sistema con saldo negativo. 

Costo unitario: el sistema calculará por defecto, el costo unitario de armado (calculado en base al tipo de valorización, el método de armado y los costos asociados en las fórmulas de composición de artículos) para que sea confirmado o modificado. Con este costo unitario se generará el ingreso de las unidades armadas.

Finalmente, podrá confirmar el armado realizado y se emitirá el comprobante correspondiente, si así se indicó en el talonario asociado al tipo de comprobante.  
Si algunos artículos se compran y venden y otros se arman, es de utilidad generar en el armado, el precio de última compra y el de reposición. De este modo, para los informes de [Valorización](https://ayudas.axoft.com/24ar/valorizexistencias_st) y [Costo de Ventas](https://ayudas.axoft.com/24ar/costoventas_st) se podrán utilizar uno de estos criterios. Así, se valorizarán los artículos que se arman por el costo estándar, que será igual al precio de reposición.

##### Métodos de armado

A continuación, se detallan las distintas opciones con ejemplos en los que se emplea el lavarropas definido en la explicación del proceso Fórmulas.  
Tenga en cuenta que las cantidades brutas en la fórmula son las que se considerarán para la descarga del stock. Luego, desde el [Listado de scrap](https://ayudas.axoft.com/24ar/listadoscrap_st), podrá consultar las cantidades correspondientes a scrap.

**Con Explosión  
**Considerando la fórmula de un artículo como un árbol jerárquico, se descargarán de stock los insumos correspondientes al último nivel de cada rama del árbol. Dicho de otra forma, con este método se arman todos los insumos que posean fórmulas.

__Nota

La opción 'Con explosión' utiliza solamente insumos para el armado de productos.

Por ejemplo: si se arma el lavarropas con explosión, la estructura de lavarropas, la sección motor de lavarropas, el tambor de lavarropas y el tablero de control; y por lo tanto, no se generarán movimientos de stock para esos insumos intermedios.

**Sin Explosión  
**Considerando la fórmula de un artículo como un árbol jerárquico, se descargarán del stock los insumos correspondientes al primer nivel de cada rama del árbol. Dicho de otra forma, con este método se descargan de inventario todos los insumos detallados en la fórmula del artículo a armar, independientemente de que éstos posean a su vez fórmula asociada. Por lo tanto, ningún insumo es armado.

__Nota

La opción 'Sin explosión' utiliza insumos y artículos semielaborados para el armado de productos.

_Por ejemplo:_ si se arma el lavarropas sin explosión, la estructura de lavarropas, la sección motor de lavarropas, el tambor de lavarropas y el tablero de control son tomados de stock y por lo tanto, se generan movimientos de inventario para esos insumos. Todos los insumos necesarios para armar la estructura del lavarropas, la sección motor de lavarropas, etc. no generan movimientos de stock.

**Detallado  
**Este método es una opción intermedia a las anteriores. Es usted quien decide qué artículo intermedio se armará.  
Si opta por este método, se desplegará una pantalla con los artículos que pueden ser armados y se dará opción a armar o tomar de stock cada uno de ellos. Por cada componente que se decida armar se desplegará luego una ventana, en la que se mostrará en su parte superior, qué artículo se está armando y como se compone. De esta manera se trabajará con cada nivel de cada rama de la fórmula de armado.

__Nota

La opción 'Detallado' le permite controlar paso a paso el proceso de armado.

**Por ejemplo** ; al armar el lavarropas con el método detallado:

Artículo a Armar: 30104 LAVARROPAS  
Insumo de: 30104

**Insumo** | **Descripción** | **Cantidad** | **Arma**  
---|---|---|---  
40044 | ESTRUCTURA LAVARROPAS | 1.00 | S  
40033 | MAQUINARIA LAVARROPAS | 1.00 | S  
40057 | TAMBOR LAVARROPAS | 1.00 | S  
40045 | TABLERO DE CONTROL | 1.00 | S  
  
En "Insumo de" muestra 30104, que es el código de artículo del lavarropas.  
Si, por ejemplo, la maquinaria del lavarropas está constituida por algún producto semielaborado factible de ser armado y, se decide armar la maquinaria de lavarropas en vez de tomarla del stock, se desplegará otra pantalla en la que se confirmará el armado de ese producto semielaborado. En "Insumo de" se mostrará 3010440033 (lavarropas maquinaria de lavarropas).

**Detalle del cálculo del costo unitario del artículo armado**

_Costo unitario = costo de insumos + costo de armado_

Para cada artículo / insumo que se arma...

_Para cada costo asociado al artículo_

_Costo de armado = costo de armado + (cantidad de insumo * costo de armado)_

_Para cada insumo del artículo_

_Costo de insumos = costo de insumo + (cantidad de insumo * costo del insumo)_

"Cantidad de insumo" hace referencia a cada componente del insumo a armar. Por ejemplo, en el caso de la estructura del lavarropas, sus componentes son la tapa, los laterales, el piso del lavarropas, etc.  
El costo unitario generado en el proceso Armado se registrará como costo estándar del artículo. Además, según la parametrización del tipo de comprobante, este costo puede actualizar el precio de última compra y el precio de reposición.

**Ejemplo...**  
Para el lavarropas definido en el proceso [Fórmulas](https://ayudas.axoft.com/24ar/formulas_st), se asignan los costos (expresados en pesos) de los insumos, de la siguiente forma:

**Insumos** | **Costo**  
---|---  
BOMBA DE AGUA MOD. WER | $31.00  
EJE TRANS. LAVARROPAS | $28.00  
ESTR. TABLERO LAVARROPAS | $ 3.80  
LATERAL LAVARROPAS | $ 7.00  
LLAVE TERMICA | $ 4.50  
MANGUERA 1" | $ 1.25  
MOTOR 1/2 HP | $85.00  
PALETA LAVARROPAS 4P | $ 6.45  
PATA LAVARROPAS 5 x 5 mm | $ 2.00  
PERILLA SELEC. DE CICLO | $ 0.50  
PISO LAVARROPAS | $ 8.50  
PLACA ALUMINIO 30 x 50 x 1 cm | $ 8.20  
PLAQ. CONTROL DE CICLO | $17.00  
POLEA 30 cm | $ 1.45  
TAMBOR ACERO 50 cm | $23.00  
TAPA LAVARROPAS | $ 7.35  
TORNILLO 1" x 4 mm | $ 0.09  
TORNILLO 1" x 5 mm | $ 0.11  
TORNILLO 1/2" x 3 mm | $ 0.05  
TORNILLO 2" x 5 mm | $ 0.25  
TUERCA 4 mm | $ 0.07  
TUERCA 5 mm | $ 0.09  
  
Para armar la estructura del lavarropas, el cálculo de costos es el siguiente:

**Insumos** | **Costo Unitario * Cant. Insumo** | **Costo total**  
---|---|---  
1 Tapa Lavarropas | $7.35 * 1 | $ 7.35  
4 Patas 5 x 5 cm | $2 * 4 | $ 8.00  
1 Piso Lavarropas | $8.5 * 1 | $ 8.50  
4 Laterales Lavarropas | $7 * 4 | $28.00  
8 Tornillos 1" x 4 mm | $0.09 * 8 | $ 0.72  
8 Tuercas 4 mm | $0.07 * 8 | $ 0.56  
2 Tornillos 2" x 5 mm | $0.25 * 2 | $ 0.50  
2 Tuercas 5 mm | $0.09 * 2 | $ 0.18  
**Otros costos**  
Mano de Obra Operario |  | $ 8.00  
**Total** |  | **$61.81**  
  
Para armar la maquinaria, el tambor y el tablero de control se utiliza el mismo procedimiento que el desarrollado para la estructura. Como resultado, se obtienen lo siguientes costos:

Maquinaria$146.55  
Tambor$ 31.95  
Tablero de Control$ 29.20

Finalmente, para armar el lavarropas, el cálculo de costos es el siguiente:

**Insumos** | **Costo Unitario * Cant. Insumo** | **Costo total**  
---|---|---  
1 Estructura Lavarropas | $61.8 * 1 | $ 61.80  
1 Sección motor | $146.55 * 1 | $146.55  
1 Eje Transmisor | $28 * 1 | $ 28.00  
1 Tambor Lavarropas | $31.95 * 1 | $ 31.95  
1 Tablero de Control | $29.2 *1 | $ 29.20  
2 Tornillos 2" x 5 mm | $0.25 * 2 | $ 0.50  
8 Tornillos ½" x 3 mm | $0.05 * 8 | $ 0.40  
4 Tornillos 1" x 5 mm | $0.11 * 4 | $ 0.44  
6 Tuercas 5 mm | $0.09 * 6 | $ 0.54  
**Otros Costos**  
Mano de Obra Calificada |  | $ 25.00  
Costos indirectos |  | $ 8.30  
**Total** |  | **$332.68**  
  
##### 

##### Auditoría de comprobantes

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.
