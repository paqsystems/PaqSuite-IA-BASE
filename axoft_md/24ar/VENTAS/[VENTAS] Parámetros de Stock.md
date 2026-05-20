# Parámetros de Stock

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=17198/

## Contenido

# Parámetros de Stock

Utilice este proceso para definir una serie de parámetros y valores iniciales que le permitan adaptar el comportamiento del sistema a sus necesidades particulares.

Este proceso le permite configurar el sistema a su medida, agilizando la operatoria diaria.  
Detallamos a continuación, los parámetros de stock a aplicar.

##### Principal

Tipos de artículos que se utilizan

Con partidas: indica si se utilizarán artículos con partidas. Para más información consulte el [Circuito de partidas](?p=17128).

Con series: indica si utilizan artículos con números de serie asociados. En el capítulo correspondiente a [Series](?p=17149) detallamos su forma de empleo.

Con escalas: indica si utiliza artículos con escalas (por ejemplo: talle y color). En el proceso correspondiente a [Artículos con escalas](https://ayudas.axoft.com/24ar/articulo_carp_st/#escalas) explicamos en detalle su funcionamiento.  
El sistema permite comenzar a trabajar con escalas aun cuando existan artículos ingresados. Para la operación inversa es necesario que no existan escalas definidas ni artículos con escalas.

Con doble unidad de medida: defina si el sistema va a utilizar doble unidad de medida. La habilitación de este parámetro brinda la posibilidad de llevar el stock por artículo en dos unidades de medida.

Unidades de medida

Defina las unidades de medida habituales. Las mismas son de ingreso obligatorio al dar de alta un artículo. Las unidades a ingresar son:

  * Stock 1 (unidad de precios y costos).
  * Presentación de Ventas.
  * Presentación de Compras.



Tenga en cuenta:

Estos valores por defecto se aplicarán únicamente en la carga de artículos nuevos. Si desea definir diferentes valores por defecto (por ejemplo, para diferentes familias de artículos), utilice [Valores por defecto para artículos](https://ayudas.axoft.com/24ar/valordefectoartic_st).

Etiquetas para artículos

Defina los valores habituales correspondientes a la generación de etiquetas.

Código de modelo de impresión: defina la etiqueta que se utilizará para los artículos en caso de utilizar código de barra.

Código de lista de precios: defina la lista a utilizar para imprimir etiquetas del artículo, cuando desee incluir precios en la impresión.

Otras opciones

Considera stock comprometido en los comprobantes de egreso: al tildar esta opción el sistema valida que exista stock disponible, considerando el stock comprometido que surge de los pedidos aprobados pendientes de remitir.

Permite alta de artículos desde procesos: el sistema brinda la posibilidad de dar de alta nuevos artículos desde los distintos procesos de ingreso de comprobantes, en los que se ingresan renglones de artículos (stock, compras y ventas).

Asignación obligatoria de perfiles: defina si un usuario que no tiene un perfil asignado, puede ingresar a los procesos que utilizan perfiles en el módulo Stock.

Modifica movimientos entre depósitos en revisión: indica si se permite modificar los movimientos entre depósitos que se encuentran en revisión antes de confirmar el ingreso.

Longitud de código de barras: indique 13, 18 o 40 si trabaja con códigos de barras de hasta esos valores.

Modalidad de bloqueo en toma de inventario: indica el bloqueo que se realizará en la toma de inventario.  
Si elige 'Artículo/Depósito', el sistema bloqueará el artículo del depósito a inventariar. En cambio, si la selección es 'Depósito', el sistema bloqueará el depósito en forma completa.  
Si el bloqueo es 'Artículo/Depósito', no podrá realizar movimientos desde los procesos que afecten el saldo de stock de ese artículo en el depósito indicado, permitiendo actualizar el inventario para otras líneas de producto del mismo depósito. En cambio si el bloqueo es por 'Depósito', no será posible actualizar el inventario desde ningún proceso que afecte el o los depósitos involucrados en la toma de inventario.

Longitud de agrupaciones

Los códigos pueden dividirse en tres partes: familia, grupo e individuo.  
Mediante esta opción se definirá la longitud dentro del código que será asignada a la familia, al grupo y al individuo. La longitud total es de 15 dígitos. Definiendo la cantidad de dígitos a utilizar para la familia y para el grupo, automáticamente quedará definida la longitud del individuo.

Escalas: en caso de trabajar con escalas ingrese la longitud de cada una de ellas (máximo 2 escalas).  
La longitud de una escala determina la cantidad máxima de caracteres del código de artículo a asignar para los valores de la escala.  
La suma de las longitudes de la escala 1 y de la escala 2 no será superior a 10 ni sobrepasará la longitud del individuo.  
Se definirá una sola escala de hasta 10 dígitos (escala 1) o dos escalas cuya suma de longitudes sea menor o igual a 10 dígitos.  
Las longitudes de las escalas se podrán modificar hasta tanto no se definan las escalas en el proceso correspondiente.  
La estructura de los artículos, al asociarle escalas, quedará conformada de la siguiente manera:

_Familia + Grupo + Individuo + Escala 1 + Escala 2 = 15_

Al utilizar artículos con escalas será posible hacer referencia en ciertos procesos a los códigos base.  
El código base representa la partición del código de artículo que no incluye los valores de las escalas. Por cada código base podrán existir 1 a n valores de escalas.  
La longitud del código base se definirá automáticamente como la suma de la longitud de la familia, la longitud del grupo y la longitud del individuo, sin las escalas, de la siguiente manera:

_Familia + Grupo + Individuo = 15_

_Código Base = 15 - (Escala 1 + Escala 2)_

**Ejemplo...**

Longitud Familia | 1  
---|---  
Longitud Grupo | 2  
Longitud Individuo | 12 (cálculo automático)  
  
Al individuo se le asignan dos escalas, de la siguiente manera:

Longitud Escala 1: | 2  
---|---  
Longitud Escala 2: | 4  
Longitud Código Base: | 9 (cálculo automático)  
  
La estructura de un artículo queda entonces:

Código de Artículo:533000000XLROJO  
Código Base:533000000  
Escala 1: XL  
Escala 2: ROJO

El código base formado será el código a utilizar en los distintos procesos de ingreso de renglones de artículos, para el que luego se seleccionarán los valores de escalas deseados.

En el proceso [Artículos con escalas](https://ayudas.axoft.com/24ar/articulo_carp_st/#escalas) detallamos las especificaciones sobre el uso de escalas.

##### Partidas

Los parámetros de esta solapa se activarán sólo si usted activó el parámetro Artículos con partidas, que se encuentra en la solapa principal.  
En el capítulo especial de [Partidas](?p=17128) explicamos en forma detallada su funcionamiento.

##### Series

Los parámetros de esta solapa se activarán sólo si usted activó el parámetro Artículos con series, que se encuentra en la solapa principal.  
Para más información, consulte el capítulo [Circuito de Series](?p=17149).

##### Doble unidad de medida

Código de UM de stock 2 habitu: defina la unidad de medida habitual para la unidad de stock 2. La misma es de ingreso obligatorio al dar de alta un artículo que use doble unidad de medida.

Tenga en cuenta:

Este valor por defecto se aplicará únicamente en la carga de artículos nuevos. Si desea definir diferentes valores por defecto (por ejemplo, para diferentes familias de artículos), utilice [Valores por defecto para artículos](https://ayudas.axoft.com/24ar/valordefectoartic_st).

Fraccionamiento de artículo

Permite fraccionar artículos desde procesos: en caso de utilizar artículos con doble unidad de medida y mediante la utilización las teclas <Ctrl + H>, usted podrá fraccionar artículos desde los comprobantes del módulo Ventas y movimientos relacionados con el ingreso, egreso y transferencia de stock.

Código de tipo de comprobante de ajuste: ingrese el tipo de ajuste a utilizar para reflejar el movimiento del fraccionamiento de artículos

Valoriza artículos por: si el [Tipo de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_st) seleccionado fue definido como valorizado, se ingresará un precio unitario. Este permite valorizar el movimiento y afectará los costos del artículo, según la parametrización del tipo de comprobante.

Código de lista de precios: informe la lista de precios de ventas, si seleccionó para valorizar artículos según lista de precios de ventas.

##### Impuestos

Impuestos por defecto: esta parametrización es de suma utilidad para agilizar la carga de artículos, asignando las referencias impositivas habituales. El ingreso de estos campos no es obligatorio. Es posible consignar valores diferentes para las operaciones de Ventas y las de Compras. Dado que estos datos son obligatorios para el alta de artículos, es útil definirlos en este proceso de manera que sólo se confirmen o modifiquen puntualmente al ingresar un nuevo artículo.  
Se presenta una ventana para indicar con qué tasas son gravados habitualmente los artículos en el momento de facturarlos (módulo Ventas) y, las tasas por defecto para proponer valores en los comprobantes de Compras.  
Si se parametriza un modelo de percepciones, este valor será propuesto en el ingreso de artículos.  
Para cada tipo de impuesto existe un rango válido de códigos. En el proceso alícuotas de Ventas y Compras, se definen las tasas posibles para cada tipo de impuesto. En el caso del modelo, este se da de alta desde el proceso [Modelos de percepciones para artículos](?p=13058) del módulo Ventas. 

Los rangos válidos en el módulo Ventas son:

**Código** | **Significado**  
---|---  
1 al 10 | Tasas de IVA General  
11 al 20 | Sobretasas / Subtasas de IVA  
21 al 39 | Tasas de impuestos internos  
40, 82 | Impuestos internos por importe fijo  
41 al 50 | Sobretasas / Subtasas de impuestos internos  
51 al 80 | Percepciones de Ingresos Brutos  
91 | IVA Liberado  
  
Usa percepción de Ingresos Brutos: si no activa este parámetro, no se ingresará la alícuota y los artículos no generarán el cálculo de percepción.

Los rangos válidos en el módulo Compras son:

**Código** | **Significado**  
---|---  
1 al 20 | Tasas de IVA General, Sobretasas / Subtasas de IVA  
40, 82 | Impuestos internos por importe fijo  
51 al 99 | Otros Impuestos  
  
Importante:

Los cálculos impositivos dependen también de otros parámetros, definidos a nivel de "cliente o proveedor". Por ejemplo, en el caso de percepción de ingresos brutos, también es posible indicar el código de alícuota en el cliente; de esa manera se utilizará dicho código para todos los artículos del comprobante.

##### Valorización

Costos

Modo de actualización de costos: indique bajo que modalidad desea actualizar los costos de los artículos vendidos.  
Esta opción es de utilidad si registra comprobantes de compras o de stock (que afecten costo) con fecha retroactiva, y desea actualizar el costo de las ventas efectuadas con fecha igual o posterior a la del comprobante ingresado.

Importante:

En las facturas de compras se considera la fecha contable, mientras que para los ingresos valorizados se considera la fecha de emisión.

Puede optar entre dos modalidades:

  * Por Comprobante: en caso de desear actualizar costos en forma automática al registrar cada comprobante de ingreso valorizado. (factura de compra o ingresos de stock configurados como Actualiza precios de última compra = 'Sí').  
Tenga en cuenta que con esta modalidad no se recalculan los costos de los artículos con armado previo, y no se tiene en cuenta los importes de fletes y/o intereses ingresados en las facturas de compras.
  * Batch: en caso de preferir actualizar el costo de los artículos vendidos en forma diferida y manual desde el proceso [Actualización de costos](?p=17023).



Con esta modalidad podrá incluir importes de flete e intereses, recalcular costos de los artículos con armado previo, e imprimir el detalle de la modificación realizada.  
Para más información consulte [Actualización de costos](?p=17023).

Recuerde que, aunque seleccione la modalidad por comprobante también podrá utilizar el proceso [Actualización de Costos](?p=17023).

Precio promedio ponderado

Calcula precio promedio ponderado: indica si utiliza el cálculo de precio promedio ponderado (PPP) como método de valuación de salidas e inventario. Este campo puede ser modificado posteriormente.

Tipo de cierre: indica el tipo de PPP con el que desea trabajar.  
Si elige 'Mensual', el sistema realiza un cierre mensual de PPP. En cualquier informe de valorización, todos los comprobantes del mes "xx" serán valuados al PPP del mes anterior a "xx".  
Si opta por 'Mensual con valor diario', además de realizar el cierre mensual, se asigna a cada comprobante de salida el PPP que le correspondió durante el proceso de cierre. En cualquier informe de valorización, cada comprobante se valuará al PPP que tenga grabado.

Fecha último cierre: cada vez que se realice el cálculo de PPP (cierre), el sistema generará los valores y exhibirá en este campo, la fecha del último cierre efectuado. Si se anulan cierres, la fecha se corregirá automáticamente. Este campo no puede modificarse en forma manual. Se lo utilizará como control y el sistema no permite ingresar comprobantes que afectan stock con fecha anterior a la del último cierre.

##### Observaciones

Informe los títulos que desea asignarle a las leyendas que serán utilizados desde los movimientos de inventario.

##### Contenidos relacionados

  * [Video sobre administración de artículos](https://ayudas.axoft.com/24ar/videos/st_carp_vid/adminarticulos_st_vid/)

  * [Video sobre parámetros de stock](https://ayudas.axoft.com/24ar/videos/st_carp_vid/parametrostock_st_vid/)
