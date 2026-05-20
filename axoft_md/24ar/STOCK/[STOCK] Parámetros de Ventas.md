# Parámetros de Ventas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_artescala_st/?p=19401/

## Contenido

# Parámetros de Ventas

Mediante este proceso se define una serie de parámetros y valores iniciales, que permiten adaptar el comportamiento del sistema a las necesidades de cada empresa en particular.

Detallamos a continuación, los parámetros de ventas a aplicar.

#### Parámetros para empresa

En esta sección usted podrá parametrizar los datos referentes a su empresa.  
Por ejemplo: razón social, número de CUIT (o identificación tributaria), fecha de inicio de actividades, número de inscripción de ingresos brutos y domicilio de la empresa.  
Asimismo, el sistema prevé la posibilidad de parametrizar ciertos nombres que son propios del país donde se está trabajando. Como por ejemplo, sigla para el subdiario de IVA Ventas (sigla para el listado del IVA), sigla para la identificación tributaria, leyenda para la moneda corriente y leyenda para la moneda extranjera.

#### Parámetros para impuestos

En esta sección usted debe parametrizar los valores posibles y datos necesarios para el cálculo de impuestos.

Impuestos para flete e intereses 

Indica las tasas de IVA a utilizar en el cálculo del impuesto para estos conceptos.  
Indica las tasas de percepción de IVA a utilizar en el cálculo del impuesto para estos conceptos.  
Por defecto, se propone la 'tasa general'.

Base de cálculo de IVA para intereses: se puede optar entre dos métodos:

  * Sobre el total de intereses: calculará el IVA sobre el total de intereses, sin considerar si los ítems facturados son gravados.
  * Sobre los intereses de importes gravados: calculará el IVA de la parte de intereses correspondiente a los ítems gravados del comprobante (aquellos en los que se calcule IVA).



Calcular según IVA de artículos (Solo Facturador): Si activa esta opción, al realizar cualquier emisión de comprobantes desde el Facturador, la alícuota de IVA correspondiente al interés de cada artículo tomará su mismo porcentaje de IVA.

Base de cálculo de IVA del flete: permite seleccionar uno de los dos criterios anteriores (sobre los fletes de importes gravados o sobre el total del flete) para el cálculo de IVA del flete en facturación.

Más información:

Los parámetros definidos para la base de cálculo a considerar para el IVA de intereses y flete se utilizan en los procesos de de facturación.

IVA Simple – fletes e intereses

Código de clasificación - Fletes: permite seleccionar la clasificación que se informará en concepto de fletes. Por defecto, se propone el código 'V1' cuya descripción es Venta de bienes y servicios.

Código de actividad económica - Fletes: permite seleccionar la actividad económica que se informará en concepto de fletes. Por defecto, se deja vacío.

__Nota

Si no se especifica un código aquí al generar el archivo de IVA simple, el sistema intentará obtenerlo del tipo de comprobante; y si tampoco está definido allí, utilizará la actividad económica principal de la empresa.  


Código de clasificación - Intereses: permite seleccionar la clasificación que se informará en concepto de intereses. Por defecto, se propone el código 'V1' cuya descripción es Venta de bienes y servicios.

Código de actividad económica - Intereses: permite seleccionar la actividad económica que se informará en concepto de intereses. Por defecto, se deja vacío.

__Nota

Si no se especifica un código aquí al generar el archivo de IVA simple, el sistema intentará obtenerlo del tipo de comprobante; y si tampoco está definido allí, utilizará la actividad económica principal de la empresa.  


Valores por defecto para el cálculo de impuestos en el alta de clientes

Los valores ingresados en esta pantalla serán sugeridos en el alta de clientes, siendo posible su modificación.  
Recomendamos ingresar los valores habituales, es decir, aquellos que más se repetirán en varios clientes.  
Indique para cada uno de los impuestos, si se calcularán y si se discriminarán en los comprobantes. En la explicación del proceso [Clientes](https://ayudas.axoft.com/24ar/clientes_carp_gv) detallamos el uso de estos campos.  
Cabe recordar que el cálculo de impuestos en los comprobantes surgirá siempre de la combinación de las alícuota ingresadas en los artículos con los parámetros del cliente.

Percepciones

Edita percepciones definibles: si activa este parámetro y corresponde el cálculo de la percepción, según lo indicado en los campos correspondientes a los artículos y clientes, será posible agregar o eliminar los códigos de percepción parametrizados en el cliente o modificar la alícuota asignada.  
Esta opción es de utilidad para aquellos comprobantes en los cuales no corresponda calcular la percepción o se aplique otro porcentaje.

Edita percepción de ingresos brutos: en los procesos [Facturas](https://ayudas.axoft.com/24ar/facturas_gv), [Notas de crédito](https://ayudas.axoft.com/24ar/emisionc_gv) y [Notas de débito](https://ayudas.axoft.com/24ar/emisionnd_gv) es posible modificar en forma manual el código de percepción de ingresos brutos adicional del cliente.  
Si activa este parámetro y corresponde el cálculo de la percepción (según lo indiquen los campos correspondientes de los artículos y el cliente), se podrá modificar la alícuota adicional de percepción a utilizar para el comprobante. Esta opción es de utilidad para aquellas jurisdicciones en las que se calculan dos percepciones de ingresos brutos, y puede ser necesaria la modificación de la alícuota en el comprobante según la dirección de entrega del cliente.

Completa fecha de percepción con la fecha de emisión de la factura en la generación del archivo de presentación de percepciones de ingresos brutos: si activa este parámetro se modificará el formato del archivo generado en la opción Generación Archivo SIAp - Percepciones IB Bs. As., para ser procesado por el método percibido del aplicativo de ARBA.

#### Parámetros para clientes

##### General

Ingreso obligatorio de CUIT: defina si es obligatorio el ingreso de un CUIT válido durante el alta o modificación de clientes.

##### Clientes habituales

Codificación automática de clientes / Próximo código de cliente: elija si utiliza la codificación automática de clientes.  
En el caso de optar por esta modalidad, se propone el próximo código de cliente a generar. Para más información, consulte la documentación de [Clientes](?p=19444).  
Una vez ingresado este dato, se realizan las siguientes validaciones:

  * Si el código de cliente existe, deberá ingresar otro código;
  * Si existen códigos mayores al ingresado, se solicita su confirmación.



__Nota

Cuando se activa el parámetro _"Codificación automática de clientes"_ , se asigna automáticamente un código en el parámetro _"Próximo código de cliente"_ , que resulta ser el mayor código de cliente existente en el proceso "Clientes" e incrementado en una unidad.  
Por ejemplo, si el mayor código de cliente existente es 100802, entonces el próximo código de cliente es 108003.  
Por ejemplo, si el mayor código de cliente existente es V00002, entonces el próximo código de cliente es V00003.

Tenga en cuenta que los códigos de cliente son de tipo alfanumérico.

__Nota

Para las altas de clientes por API o **Excel** el funcionamiento es diferente. Para más información consulte la documentación de [Clientes](?p=19444/#principal).

**Consideraciones para la codificación automática de clientes** :

Código de cliente = Longitud máxima de 6 caracteres.

Cuando en el código de cliente no se usa un prefijo porque el parámetro Utiliza prefijo para codificación tiene definida la opción 'No controla', todo el código de cliente corresponde a la parte variable que se autoincrementa con caracteres alfanuméricos y se autocompleta con ceros a la izquierda.

_CODIGO CLIENTE = PARTE VARIABLE AUTOINCREMENTAL_

En cambio, si en el código de cliente se usa un prefijo porque el parámetro Utiliza prefijo para codificación tiene seleccionada la opción 'Control estricto', el código de cliente se compone por un prefijo (de 1 a 3 caracteres alfanuméricos) más la parte variable que se autoincrementa (de 3 a 5 caracteres alfanuméricos según la cantidad del prefijo) y se completa con ceros a la izquierda.

_CODIGO CLIENTE = PREFIJO + PARTE VARIABLE AUTOINCREMENTAL_

__Ejemplos...

  * Si se usa 1 carácter para el prefijo entonces la parte variable que se autoincrementa tiene una longitud máxima de 5 caracteres (autocompleta con ceros a la izquierda).
  * Si se usa 2 caracteres para el prefijo entonces la parte variable que se autoincrementa tiene una longitud máxima de 4 caracteres (autocompleta con ceros a la izquierda).
  * Si se usa 3 caracteres para el prefijo entonces la parte variable que se autoincrementa tiene una longitud máxima de 3 caracteres (autocompleta con ceros a la izquierda).



Para la codificación automática de la parte variable del código del cliente, se utiliza el siguiente criterio:

  * Se autoincrementa en forma "numérica" si el próximo código de cliente es numérico y menor al "máximo número posible" (*), por ejemplo, 124.
  * Se autoincrementa en forma "alfanumérica" si el próximo código de cliente es igual al "máximo número posible" (*) o contiene al menos un carácter alfabético (por ejemplo, 10089Z).



Unidades alfanuméricas para el autoincremento del código de cliente   
_(por orden ascendente):_  
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z. 

(*) Máximo número posible (parte variable del código de cliente):

**Utiliza prefijo para codificación** | **Cantidad carácter del prefijo** | **Máximo número posible**  
****  
---|---|---  
No controla | - | Existencia del código de cliente 999999  
Control estricto | 1 | Existencia del código de cliente 99999  
Control estricto | 2 | Existencia del código de cliente 9999  
Control estricto | 3 | Existencia del código de cliente 999  
  
Utiliza prefijo para codificación / Valor del prefijo: usted podrá utilizar un prefijo para la codificación de clientes. En dicho caso, el código de cliente se conformará por un prefijo (de 1 a 3 caracteres alfanuméricos), y la parte variable que se autoincrementa (de 3 a 5 caracteres alfanuméricos) que corresponde al Próximo código de cliente.  
Por ejemplo:

  * Si el prefijo tiene 1 carácter, entonces la parte variable tiene un máximo de 5 caracteres.
  * Si el prefijo tiene 2 caracteres, entonces la parte variable tiene un máximo de 4 caracteres.
  * Si el prefijo tiene 3 caracteres, entonces la parte variable tiene un máximo de 3 caracteres.



__Nota

El sistema validará que entre el próximo código de cliente (parte variable incremental) y el prefijo no supere los 6 caracteres.

Permite alta de clientes desde procesos: usted puede dar de alta nuevos clientes desde los distintos procesos de ingreso de comprobantes (cotizaciones, pedidos, facturas, créditos, débitos, remitos, cobros, composición inicial).  
Si no desea hacer uso de esta facilidad, con el fin de permitir las altas sólo a los usuarios habilitados, no active este parámetro.

Clasifica clientes en altas: si activa este parámetro, al dar de alta un cliente en el sistema, se solicita su confirmación para clasificarlo en ese momento.  
Si confirma esta acción, se abre automáticamente el clasificador de clientes.

Duplicación del tipo y Número de documento: mediante este parámetro configure el tipo de validación a aplicar en el caso de números repetidos para la combinación de tipo y número de documento.  
De esta manera, usted define si aplica un control flexible (habilita el ingreso de números repetidos, de utilidad para aquellas empresas que operan con clientes con sucursales), un control estricto con el que no se permiten valores repetidos para la combinación de ambos campos; o bien, un control estricto (Solo CUIT) para estos campos solamente cuando el tipo de documento es 'CUIT'. Por defecto, se propone la opción 'Control flexible'.  
En el caso de clientes del exterior (si tienen asignado como Tipo y Número de documento, el CUIT de su país), no se aplica el control de duplicidad.  
Cabe aclarar que este control no se tiene en cuenta en clientes ocasionales (con código '000000').

Escenarios de aplicación:

El sistema tiene en cuenta este parámetro al dar de alta un cliente, en las siguientes situaciones:

  1. Desde el proceso [Clientes](https://ayudas.axoft.com/24ar/clientes_carp_gv).
  2. Mediante la tecla <F6> \- Alta de Clientes desde otros procesos, tales como [Facturas](https://ayudas.axoft.com/24ar/facturas_gv).
  3. Al importar clientes desde el proceso [Tablas generales](?p=11992) del módulo Procesos generales o Central.
  4. Al importar [pedidos](?p=9416), [remitos](?p=9418) y/o [comprobantes de facturación](?p=9413) para la Gestión Central del módulo Central.



Y también, al modificar o copiar los datos de un cliente desde el proceso [Clientes](https://ayudas.axoft.com/24ar/clientes_carp_gv).

En el caso de clientes potenciales, el sistema tiene en cuenta la configuración de este parámetro, en las siguientes situaciones:

  1. Desde el proceso [Clientes potenciales](?p=19235) (al agregar, modificar o copiar los datos de un cliente potencial y desde el comando Operaciones, al convertirlo en cliente habitual).
  2. Mediante la tecla <F6> \- Alta de cliente desde el proceso [Generación / Modificación de cotizaciones](?p=19316), en el momento de dar de alta una cotización.
  3. En los procesos de cotizaciones, al generar pedido y convertir el cliente potencial en habitual ([Generación / Modificación de cotizaciones](?p=19316), [Autorización de cotizaciones](?p=19216) y [Aceptación de cotizaciones](?p=19169)).



##### Clientes habituales / ocasionales

Tipo de documento: es el tipo de documento habitual a considerar para el cliente (habitual u ocasional).

Provincia habitual: es la provincia a considerar por defecto, para los clientes habituales y ocasionales, en los procesos de facturación, pedidos y cotizaciones.

Actualiza información con AFIP: mediante estos parámetros, usted define el comportamiento de la actualización de los datos del cliente desde los servidores de AFIP al momento del alta en el Facturador, y también en la modificación solo desde Clientes.  
Los valores posibles a ingresar son los siguientes:

  * Nunca
  * Siempre
  * A pedido



RG 3685 / 4597 - Tipo de operación: seleccione un valor en este proceso que se utilizará en la generación de los archivos de ventas que requiere la resolución general 3685 / 4597 de AFIP.  
Cuando usted genere un comprobante para un cliente ocasional este dato se indicará como sugerencia.  
Para más información, consulte la [Guía de implementación sobre RG 3685 - Régimen informativo de compras y ventas](?p=11914).

Control de clientes inhabilitados: mediante estos parámetros, usted define el comportamiento del uso de la fecha de inhabilitación de clientes. Se controlan las operaciones de cotizaciones: pedidos; facturas / créditos / débitos y remitos. Los valores posibles a ingresar son los siguientes:

  * No permitir operar.
  * Inhabilitar ante fechas posteriores.
  * Confirmar ante fechas posteriores.



El valor por defecto de estos parámetros es 'No permitir operar', que impide operar con clientes inhabilitados.  
En las operaciones mencionadas, con clientes que tengan asignada una fecha de inhabilitación, el sistema se comporta de la siguiente manera:

  * Si el parámetro es igual a 'No permitir operar', se exhibirá el mensaje "EL CLIENTE ESTA INHABILITADO" y no será posible ejecutar la operación.
  * Si el parámetro es igual a 'Inhabilitar ante fechas posteriores' y la fecha del comprobante a emitir es mayor o igual a la fecha de inhabilitación del cliente, se exhibirá el mensaje "EL CLIENTE ESTA INHABILITADO" y no podrá continuar con esa operación. En este caso, para un cliente inhabilitado sólo podrá emitir comprobantes con fecha menor a la de su inhabilitación.
  * Si el parámetro es igual a 'Confirmar ante fechas posteriores' y la fecha del comprobante a procesar es mayor o igual a la fecha de inhabilitación del cliente, se exhibirá un mensaje indicando la fecha a partir de la cual el cliente está inhabilitado y usted tiene la opción de decidir si continúa con la operación. En cambio, podrá emitir sin restricciones comprobantes con fecha menor a la de la inhabilitación del cliente.



##### Clientes potenciales

Codificación automática de clientes potenciales: este parámetro indica si el sistema genera automáticamente los códigos de clientes potenciales.  
En ese caso, el código se genera en base al parámetro Próximo código de cliente. Si no lo activa, deberá ingresar en forma manual el código de cada nuevo cliente potencial.

Próximo código de cliente: sólo se encuentra disponible si activó el parámetro Codificación automática de clientes potenciales.  
En ese caso, defina el próximo número a considerar para el código de un nuevo cliente potencial.

Clasifica clientes potenciales en el alta: indica si al confirmar el alta de un cliente potencial, se presenta la pantalla de [clasificación de clientes potenciales](https://ayudas.axoft.com/24ar/clasifclientpotenclipot_gv).

##### Conversión a cliente habitual

Fecha de conversión a cliente habitual: indique la fecha de alta a considerar cuando convierta un cliente potencial en habitual, desde el proceso [Clientes potenciales](https://ayudas.axoft.com/24ar/clientepotencial_gv) o mediante el comando Generar pedido en los procesos [Generación / Modificación](https://ayudas.axoft.com/24ar/genermodificotizacion_gv), [Autorización](https://ayudas.axoft.com/24ar/autorizcotizacion_gv) o [Aceptación de cotizaciones](https://ayudas.axoft.com/24ar/aceptcotiz_gv).  
Los valores posibles son: 'fecha del día' o 'alta del potencial'.

Condición de venta habitual: es posible ingresar una [condición de venta](https://ayudas.axoft.com/24ar/condicionventa_gv) a considerar como habitual para los [clientes potenciales](https://ayudas.axoft.com/24ar/clientepotencial_gv).

Zona habitual: permite ingresar la [provincia](https://ayudas.axoft.com/24ar/provincia_gv) habitual a considerar por defecto (habitual) para los [clientes potenciales](https://ayudas.axoft.com/24ar/clientepotencial_gv).

##### Parametrización contable para clientes ocasionales

Los valores cuenta cliente y centro de costo del cliente se considerarán por defecto si previamente definió que no integra con Contabilidad cuando se ingresen datos de clientes ocasionales, en los procesos de Facturación, Pedidos y Cotizaciones.  
Al momento de ingresar el cliente ocasional, si estos campos quedan sin especificar, el asiento tomará la cuenta genérica asignada al valor 'TO', según la definición del tipo de asiento utilizado.  
En caso que haya definido que integra con Contabilidad, acceda a [Parametrización contable de clientes](https://ayudas.axoft.com/24ar/clienteparamcont_gv) para realizar esta configuración.

##### Longitud de agrupaciones del cliente

Dentro del código de clientes, es posible definir la longitud que será asignada a la familia, al grupo y al individuo según su agrupación. Este proceso permite definir la longitud de las agrupaciones de los códigos de clientes.

__Nota

Los códigos de los clientes se agrupan, principalmente, para ubicar rápidamente un cliente al realizar un comprobante.

Los códigos de cliente pueden ser divididos en tres agrupaciones: familia, grupo e individuo.  
Mediante este proceso, se definirá la longitud dentro del código que será asignada a la familia, al grupo y al individuo. En el caso de cliente es de 6 dígitos. De esta manera, definiendo la cantidad de dígitos que se van a utilizar para la familia y para el grupo, automáticamente quedará definida la longitud del individuo.

Definición de longitud de agrupaciones:

Si se define:

  * Longitud de Familia: 1
  * Longitud de Grupo: 1



Automáticamente, la longitud del individuo será 4, que resulta de: 6 - (1 + 1).

Si usted no desea agrupar en familias y grupos, defina las longitudes respectivas en 0 (cero).

Tenga en cuenta que la modificación posterior de estos datos puede traer aparejado el mal ordenamiento de los códigos en los listados.

#### Parámetros para artículos

Descarga stock al facturar: este parámetro se utiliza en los procesos de facturación ([Facturas y](https://ayudas.axoft.com/24ar/facturas_gv) [Facturas punto de venta](https://ayudas.axoft.com/24ar/facturapvta_gv)) y se refiere al comportamiento de las facturas con respecto a la descarga de stock.  
Su aplicación depende de las siguientes situaciones en los procesos que generan facturas: 

En los procesos relacionados con la [facturación de pedidos](?p=72911/#facturacion-de-pedidos) la descarga depende directamente de este parámetro.

  * Si el parámetro está activo, se provocará la descarga de stock junto con la factura de cada pedido. Las cantidades facturadas y descargadas serán las que indique el campo [cantidad a facturar](https://ayudas.axoft.com/24ar/ingresopedido_gv) del pedido (cantidad activada).
  * Si el parámetro no está activo, no se provocará la descarga de stock junto con la factura, y solamente se facturarán las cantidades activadas a facturar.



Seleccionar la modalidad de descarga de stock:

En los procesos [Facturas](https://ayudas.axoft.com/24ar/facturas_gv) y [Facturas Punto de Venta](https://ayudas.axoft.com/24ar/facturapvta_gv) l a descarga no depende directamente de la parametrización. Si usted invoca las teclas de función <Alt + F6> \- depósito y descarga podrá cambiar la modalidad de descarga del artículo en edición. Caso contrario, se tomará por defecto el valor del parámetro general.

Las facturas que descargan stock realizan la actualización correspondiente del stock. Por el contrario, si una factura no descarga stock, la actualización se realizará a través de la emisión de un remito.

Ingresa artículos con escala usando matriz durante la emisión del comprobante: active este parámetro para realizar el ingreso de artículos con escala utilizando la matriz.  
Esta funcionalidad se encuentra disponible para el ingreso de pedidos y remitos.

Muestra todas las combinaciones de escala en la matriz: parámetro que permite mostrar u ocultar en la matriz aquellos artículos para los cuales no existen combinaciones de escalas.

Partidas

Descarga partidas en negativo: el sistema realiza el control del saldo de partida en los distintos procesos que generan egresos, emitiendo los mensajes de confirmación correspondiente.  
Si no se activa este parámetro, se bloqueará en forma automática la descarga de unidades si no existe el saldo de stock necesario.  
Este parámetro será considerado en los siguientes procesos:

  * [Facturas](https://ayudas.axoft.com/24ar/facturas_gv)
  * [Facturas punto de venta](https://ayudas.axoft.com/24ar/facturapvta_gv)
  * [Notas de crédito](https://ayudas.axoft.com/24ar/emisionc_gv) / [Notas de débito](https://ayudas.axoft.com/24ar/emisionnd_gv)
  * [Emisión de remitos](?p=19774)



Permite alta de partidas desde factura: active este parámetro para generar el alta de partidas desde la emisión de facturas, siempre que en el renglón se ingrese la cantidad en valores negativos y que afecte stock.

Permite alta de partidas desde nota de crédito: active este parámetro para generar el alta de partidas desde la emisión de notas de crédito, siempre que el comprobante se encuentre configurado para que afecte stock.

Consulta de saldos de stock desde procesos <F9>

Muestra precio del artículo: al activar este parámetro, en la consulta de saldos (a la que accede en los procesos mediante la tecla de función <F9>) se incluirá la columna de precio.

Muestra únicamente el saldo del depósito del comprobante: si no activa este parámetro, en la consulta de saldos (a la que accede en los procesos mediante la tecla de función <F9>) se mostrará el saldo de todos los depósitos para cada uno de los artículos.

Precios

Guardar el historial de precios: permite indicar si se desea grabar en la tabla que almacena las modificaciones de precios a lo largo del tiempo.

Depurar el historial de precios: permite indicar si se desea limpiar la tabla que almacena las modificaciones de precios a lo largo del tiempo.

Conservar los precios históricos por (meses): indique la cantidad de meses (enteros) que desee mantener los precios históricos en la base de datos. La cantidad mínima permitida es 1.

Talonarios de pedido a excluir de la actualización de precios

Desde esta sección, podrá seleccionar los talonarios de pedidos que serán excluidos de la actualización de precios cuando los mismos se modifiquen en una lista o en un artículo.  
Busque el talonario que desea excluir y agréguelo a la grilla. Posteriormente podrá editarlo o eliminarlo.  
Los modelos para realizar pedidos automáticos que utilicen estos talonarios también serán excluidos de la actualización de precios.

#### Parámetros para comprobantes

Dentro de esta sección se encuentran disponibles las siguientes subsolapas.

##### Generales

Descripciones adicionales en créditos / débitos / pedidos automáticos: habilita su ingreso o edición en los procesos [Notas de crédito](https://ayudas.axoft.com/24ar/emisionc_gv), [Notas de débito](https://ayudas.axoft.com/24ar/emisionnd_gv), [Modelos](?p=19369) y [Novedades de pedidos](https://ayudas.axoft.com/24ar/novedadpedido_gv).  
Este parámetro no se utiliza para facturación si se aplican perfiles, ya que considera los valores del parámetro del perfil.  
Valores posibles para este campo:

  * No: limita la edición de las descripciones adicionales y la inserción de líneas.
  * Sólo permite agregar líneas: permite agregar líneas, sin posibilidad de editar el contenido de las descripciones asignadas al artículo.
  * Permite agregar líneas y modificar la descripción del artículo: permite agregar líneas, con la posibilidad de editar el contenido de las descripciones asignadas al artículo.



Método de ingreso de descripciones (Solo Facturador): indique la forma en que se presentarán las descripciones de los artículos al momento de emitir facturas, notas de crédito y notas de débito.  
Valores posibles para este campo:

  * **Dos columnas (30 y 20 caracteres):** si selecciona esta opción, las descripciones de los artículos se presentarán visualmente en campos y renglones separados. Se utilizará la **@DE** para la columna izquierda y **@DA** para la derecha. En el Facturador se permitirá el ingreso de un máximo de 30 caracteres en la carga de la primer columna.
  * **Dos columnas (50 y 20 caracteres):** si selecciona esta opción, las descripciones de los artículos se presentarán visualmente en campos y renglones separados. Se utilizará la **@DE** para la columna izquierda y **@DA** para la derecha. En el Facturador se permitirá el ingreso de un máximo de 50 caracteres en la carga de la primer columna.
  * **Una columna (50 caracteres):** si selecciona esta opción, las descripciones de los artículos se presentarán visualmente en dos campos. En el segundo campo, podrá ingresar o pegar un texto completo. Sin embargo, ambos campos se imprimirán en la ubicación de la variable **@DE** , donde el primer renglón corresponde a la descripción y los siguientes corresponderán a la descripción adicional.



Tenga en cuenta:

La variable **@DE** mantiene como longitud por defecto 30 caracteres. Si selecciona 'Dos columnas (50 y 20 caracteres)' o 'Una columna (50 caracteres)', para imprimir los 50 caracteres de la descripción, en el TYP se deberá configurar la variable @DE=50. En caso de no hacerlo, se imprimirán por defecto los primeros 30 caracteres.  


Actualiza información del cliente con AFIP: mediante estos parámetros, usted define el comportamiento de la actualización de los datos del cliente desde los servidores de AFIP al momento de generar una factura, nota de crédito o débito.  
Los valores posibles a ingresar son los siguientes:

  * Nunca.
  * Siempre.
  * A pedido.



Impuesto interno fijo: indique si al emitir una nota de débito o al facturar pedidos, los importes de los impuestos internos fijos calculados por el sistema pueden ser editados.  
Valores posibles para este campo:

  * Edita: los importes de los impuestos internos podrán editarse.
  * No edita: no se podrán editar los importes de los impuestos internos.
  * Solo cuando el importe es cero: los importes de los impuestos internos serán editables únicamente cuando lo calculado por el sistema sea cero.



Percepciones definibles por importe fijo: indique si al emitir una nota de crédito o al facturar pedidos, pueden ser editados los importes calculados por el sistema de las percepciones definibles que tengan como con base de cálculo importe fijo por cantidad.  
Valores posibles para este campo:

  * Edita: los importes de las percepciones definibles podrán editarse.
  * No edita: no se podrán editar los importes de las percepciones definibles
  * Solo cuando el importe es igual a cero: los importes de las percepciones definibles únicamente serán editables cuando lo calculado por el sistema sea cero.



Dirección de entrega: indique si al ingresar comprobantes puede editar las direcciones de entrega.  
Valores posibles para este campo:

  * Edita: utilice <Ctrl + F1> para editar la dirección de entrega definida como habitual que el sistema propone en el momento de emisión de comprobantes, teniendo la posibilidad de seleccionar otra dirección asociada al cliente.
  * Muestra: mediante <Ctrl + F1> solo se podrá consultar la dirección de entrega 'Habitual' utilizada en la emisión de comprobantes.



Numeración

Numeración automática de remitos: si activa este parámetro, el sistema sugerirá en forma automática el número de remito, sin permitir su modificación.

Facturas de crédito

Imprime facturas de crédito en facturación: al activar este parámetro, en el proceso [Facturas](https://ayudas.axoft.com/24ar/facturas_gv) se imprimirán las facturas de crédito propias que documentarán la factura generada en cuenta corriente.

Próximo número de factura de crédito: indica el próximo número de factura de crédito a emitir por el sistema al generar facturas de crédito propias.

Modelo de recibo para la anulación de facturas de crédito en cobranzas: permite seleccionar el modelo de impresión a utilizar en la anulación de facturas de crédito.  
Las opciones corresponden a los modelos TYP disponibles:

  * Recibo
  * Recibo de factura de crédito



Vencimientos que se registran en días sábado, domingo o feriado

Traslada fecha de vencimiento al siguiente día hábil: al efectuar el cálculo de fechas de vencimiento, es posible que coincidan con un día feriado o fines de semana. Marque este parámetro si desea que sean trasladadas al primer día hábil posible.

**Ejemplo...**  
Factura: con fecha de emisión 08/05/2019.  
Condición de venta: 1 cuota a 20 días de la fecha de factura.  
Fecha de vencimiento calculada: sábado 28/05/2019.  
Si Traslada fecha de vencimiento al siguiente día hábil, la fecha de vencimiento definitiva será 30/05/2019 (lunes).

Diferencias de cambio automáticas / Ajustes por cobro en fechas alternativas automáticos

Genera al cobrar o imputar comprobantes: indique si desea generar notas de débito o crédito por diferencias de cambio o ajustes por cobro en fechas alternativas, en forma automática desde los procesos [Cobranzas](https://ayudas.axoft.com/24ar/ingresocobranza_gv) o [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputcomprobante_gv).  
Valores posibles para este campo:

  * Siempre: en este caso siempre que estén dadas las condiciones para generar los comprobantes se emite una o varias notas de débito/crédito.
  * Nunca: no se generan notas de débito/crédito desde este proceso.
  * Con confirmación: en el caso de que corresponda generar una o varias notas de débito/crédito, se consulta si se desea efectuar esta operación.
  * Sólo avisa: en el caso de que corresponda generar una o varias notas de débito/crédito, se emite un aviso de esta situación, sin posibilidad de emitir los comprobantes.



En todos los casos en que no se llega a generar la o las notas de débito/crédito correspondientes, puede hacerlo posteriormente desde la emisión de [notas de débito](https://ayudas.axoft.com/24ar/emisionnd_gv), [notas de crédito](https://ayudas.axoft.com/24ar/emisionc_gv) haciendo referencia al comprobante que desea ajustar o [imputación de comprobantes](https://ayudas.axoft.com/24ar/imputcomprobante_gv).

Fecha a asignar (para Diferencias de cambio automáticas y para Ajuste por cobro en fechas alternativas automáticos): estos parámetros se habilitan cuando los parámetros Genera al cobrar o imputar comprobantes están configurados como 'Siempre' o 'Con confirmación'.  
Seleccione la fecha que tendrán las diferencias de cambio y/o los comprobantes de ajuste por cobro en fechas alternativas generados desde [Cobranzas](https://ayudas.axoft.com/24ar/ingresocobranza_gv) y [Cobranzas masivas](?p=21355).  
Las opciones posibles de selección son: fecha del recibo (opción por defecto) o fecha del día.

Motivo (sólo para N/C): el motivo ingresado en este ítem se asigna por defecto a todos los comprobantes generados automáticamente desde ambos procesos.

Resoluciones AFIP

RG 3572 - Sujetos vinculados - Genera información de las operaciones de ventas: tilde este parámetro si usted cumple con el Régimen informativo de operaciones en el mercado interno - Sujetos Vinculados.  
Para más información, consulte la [Guía de implementación sobre RG 3572 - Sujetos vinculados](?p=11911).

RG 4520 - IVA - Genera información de las operaciones de ventas clase 'A': tilde este parámetro si usted cumple con el régimen especial establecido por la citada resolución.  
Con la entrada en vigencia de la RG 4520, AFIP realiza los controles pertinentes a través de la facturación electrónica o mediante controladores fiscales (de nueva tecnología).  
La Resolución General 4520 deroga la RG 3668 y sus modificatorias, dejando sin efecto el formulario de Declaración Jurada Nº 8001 (solicitado por los restaurantes y hoteles en oportunidad de emitir facturas 'A').

RG 5003 - Emisión de comprobantes 'A' a Monotributistas: tilde este parámetro si usted cumple con el Régimen de Sostenimiento e Inclusión Fiscal para Pequeños Contribuyentes.  
El sistema valida que la categoría de IVA de la empresa sea 'Responsable Inscripto'.

RG 5616 - Emisión de comprobantes: tilde este parámetro si usted cumple con lo establecido por la citada resolución.  
Mediante la Resolución General 5616/2024 se adecúa la normativa sobre facturación para facilitar las operaciones pautadas, facturadas y abonadas en moneda extranjera.  
Si usted modifica este parámetro y lo destilda, quedará deshabilitado el parámetro Pago en la misma moneda del comprobante.

Pago en la misma moneda del comprobante: este parámetro estará habilitado para su edición si el usuario tildó previamente el parámetro RG 5616 - Emisión de comprobantes. En ese caso, se deberá elegir una las opciones posibles ('Confirma', 'Sí', 'No').

##### Transporte de bienes (COT)

Es posible ingresar o modificar la información para el proceso [Generación de archivo de transporte de Bienes - Rentas Bs. As.](https://ayudas.axoft.com/24ar/genarchtranspbienrentbsas_gv)

Genera remitos electrónicos: este parámetro general habilita la configuración de artículos y el envío de información de los comprobantes a Rentas Bs. As., para obtener el Código de Operación y Traslado (posibilita el uso de la función _< F6> \- Código Transporte Rentas_ en los procesos [Consulta de remitos](?p=19261), [Consulta de comprobantes](?p=21172) y [Modificación de comprobantes](?p=20552)).

Para más información consulte [Generación Archivo Transporte de Bienes - Rentas Bs. As.](?p=21480/#generacion-de-archivo-de-transporte-de-bienes-rentas-bsas)

Planta: indique el número de planta habitual desde donde parten sus envíos.

Puerta: indique el número de puerta habitual desde donde parten sus envíos.

Edita importe total sin impuestos: active este parámetro si usted cumple con la normativa vigente, para ingresar el importe desde la generación de comprobantes. A partir del 05 de agosto del 2019, el importe a informar será neto de componente tributario.  
Desde la emisión de remitos debe informar el importe sin impuestos.  
Desde facturas, notas de crédito y notas de débito, dentro de _Más Acciones_ se visualizará una opción de _Transporte de bienes_ que se completará con el importe total calculado (sin impuestos), pudiendo ser modificado.

Edita cantidad total de kilos: para ingresar el pasaje correspondiente en kilogramos desde la generación de comprobantes, necesario si usted cumple con la Normativa Nº 014/11, vigente desde el 15 de Mayo del 2011.  
Este valor debe ser un valor entero y sin decimales. En la emisión de remitos, facturas, notas de crédito y notas de débito, dentro de _Más Acciones_ se visualizará una opción de _Transporte de bienes_ para ingresar dicho valor.

Para que ambos parámetros estén habilitados, configure en 'Si' el parámetro Genera remitos electrónicos. Si usted no tilda alguno de los parámetros mencionados, y cumple con la Normativa Nº 014/11, podrá ingresar los valores correspondientes desde [Generación Archivo Transp. de Bienes-Rentas BS.AS.](?p=21480/#generacion-de-archivo-de-transporte-de-bienes-rentas-bsas) en las columnas "Importes sin impuestos" y "Total kilogramos", antes de realizar la exportación.  
Al tener tildadas esas opciones, cada vez que emita un remito o una factura que afecte stock tendrá la posibilidad de cargar los datos referidos al importe total sin impuestos y el total de kilos para que esa información sea enviada a ARBA.

Versión: la opción 'Original' se considera por defecto. A partir del día 05 de agosto 2019, deberá seleccionar la opción 'Agosto 2019' como versión de COT a utilizar.

Importe mínimo sin impuestos: es el importe que actúa de filtro en el campo Importe sin impuestos del seleccionador de comprobantes, del proceso Generación Archivo Transp. de Bienes-Rentas Bs.As.

Cantidad total mínima de kilos: es la cantidad en kilos que actúa de filtro en el campo Desde cantidad total de kilos del seleccionador de comprobantes, del proceso Generación Archivo Transp. de Bienes-Rentas Bs.As.

##### Integración con shoppings

Si usted tiene un punto de venta operando en determinados centros comerciales (consulte el listado de centros comerciales compatibles con este proceso) puede generar desde el módulo Ventas la información necesaria para estos centros comerciales.  
En este caso, es necesario definir una serie de parámetros que se tendrán en cuenta en el momento de generar comprobantes de facturación (facturas, notas de crédito y notas de débito).  
Para más información, consulte la [Guía sobre implementación de trabajo en modalidad Shopping](?p=6179).

##### Señas

Utiliza el sistema de facturación con señas: si activa este parámetro, es posible generar una factura de señas al contado y luego, aplicarla en el momento de realizar la factura de la venta.

Respeta precios al aplicar la seña: este parámetro está disponible sólo si está activo el parámetro Utiliza el sistema de facturación con señas.  
Si activa este parámetro, se visualizarán los artículos con los precios definidos en la seña, en el momento de generar una factura de venta. Caso contrario, los precios surgen de la lista de precios indicada para la factura de venta.

Impuestos

Esta información sólo se encontrará disponible si está activo el parámetro Utiliza el sistema de facturación con señas.  
En ese caso, defina los códigos de alícuotas a considerar en el momento de generar y aplicar una seña. Sólo podrá modificar las alícuotas en el caso que no exista una seña con estado 'Ingresado'.

##### Pedidos

Mantiene pedidos facturados y entregados: el objetivo de este parámetro es el definir el tratamiento a aplicar a los pedidos facturados y entregados en su totalidad.  
Si el parámetro está activo, la información de los pedidos facturados y entregados permanecerá en los archivos del sistema.  
Si el parámetro no está activo, la información de los pedidos se borrará automáticamente en el caso que éstos hayan sido facturados y entregados totalmente.

__Importante

Este parámetro es requerido para procesar cancelaciones cuando se trabaja con pedidos de tiendas.  


__Nota

Tenga en cuenta que los pedidos ingresados siempre comprometen stock. Se desea que el ingreso de pedidos no comprometa stock, deberá definir un perfil de facturación e indicar el comportamiento deseado.  


Más información:

Condiciones para la modificación: es posible desactivar este parámetro, sólo si no existen pedidos cumplidos, cerrados o anulados. Caso contrario deberá realizar la depuración correspondiente.  


Aprueba pedidos ingresados: indica que los pedidos ingresados deberán ser aprobados para continuar con el circuito del comprobante.

Más información:

Condiciones para la modificación: es posible activar este parámetro en cualquier momento. Si desea desactivarlo y existen pedidos con estado ingresado, deberá aprobarlos correspondiente para continuar.  


Items a aprobar: si está activo el parámetro Aprueba pedidos ingresados indique los ítems del pedido que requieren aprobación (cantidades, precios o condiciones de facturación). Debe quedar activo al menos uno de estos ítems.  
Todo cambio que realice con respecto a los Items a aprobar será considerado desde el momento de la modificación en adelante. Es decir, los cambios no se aplican con retroactividad.  
Los pedidos aprobados total o parcialmente con anterioridad a estos cambios, no se verán afectados. Si es necesario, [apruebe el comprobante](?p=12515/#aprobar-y-desaprobar). Aconsejamos también, revisar la definición de los [perfiles de aprobación](https://ayudas.axoft.com/24ar/perfilaprobac_gv).

Activa automáticamente las cantidades al aprobar: si está activo el parámetro Aprueba pedidos ingresados tendrá la posibilidad que al aprobar un pedido queden activadas las cantidades a facturar o remitir.  
Active este parámetro si no realiza entregas o facturas parciales de pedidos.  
Los parámetros no podrán ser modificarlos desde el proceso [Perfiles de facturación](https://ayudas.axoft.com/24ar/perfilfacturacion_gv).

Usa planes de entrega: active este parámetro para aplicar planes de entrega a los distintos artículos que componen un pedido.

Cantidad habitual de días para la fecha de entrega: si necesita que la fecha de entrega de sus pedidos se calcule en base a una cantidad de días (contados a partir de la fecha del pedido), indique ese valor en este parámetro. Caso contrario, deje en cero el valor de este parámetro. En ambos casos, es posible modificar la fecha de entrega calculada.

**Ejemplo...**  
Si la fecha de entrega a aplicar es 5 días fecha de pedido, ingrese 5 como cantidad de días. Al ingresar un pedido, el sistema sumará 5 días a la fecha del pedido para calcular su fecha de entrega. Si la fecha de su pedido es 19/11/20, su fecha de entrega será el 24/11/20.  
Si la cantidad de días es igual a cero, la fecha de entrega será igual a la fecha del pedido.

Promociones

Días de vigencia de promociones: utilice esta opción si calcula promociones en pedidos para indicar la cantidad de días que se respetarán las promociones calculadas en el pedido hasta el momento de facturar.  
Si al momento de facturar un pedido con promociones la fecha de vigencia es menor a la de la factura se aplicará el permiso del perfil de facturación.  
Para más información consulte la [guía sobre pedidos con promociones](?p=40079).

Pedidos de Tango Tiendas

Genera pedidos automáticos en base a órdenes de Tango Tiendas: active este parámetro para indicar si desea generar pedidos en base a órdenes de Tango Tiendas sin necesidad de ingresar al proceso de Revisión de pedidos de Tango Tiendas, siempre y cuando se cumplan las condiciones para generar.

Procesa automáticamente órdenes canceladas: active este parámetro para indicar que desea procesar en forma automática las cancelaciones de órdenes y anular los pedidos asociados, si los hubiera, sin necesidad de ingresar al proceso Revisión de pedidos de Tango Tiendas, siempre y cuando se cumplan las condiciones para generar la anulación.

Motivo: si indicó que procesa automáticamente órdenes canceladas podrá configurar un código de motivo por defecto que se asociará a la anulación de los pedidos asociados a órdenes canceladas.

Depura revisión de pedidos de Tango Tiendas: indique si desea activar el proceso de depuración de órdenes de pedidos de Tango Tiendas, solo serán depuradas aquellas órdenes con estado anulada, finalizada, finalizada* y rechazada que estén dentro de la fecha de depuración.

Conservar los pedidos de Tango Tiendas por: este campo permite establecer el número de meses que desea mantener las órdenes de pedidos de Tango Tiendas, y en función a este valor se determina a partir de qué fecha se aplicará la depuración.

  * Para configurar la tarea de depuración debe hacerlo desde el Administrador | Servicios | Depuración.
  * Es importante aclarar que, una vez que la información sea depurada no podrá ser visualizada en ninguna de las consultas Live de ventas, pedidos y Tango nexo. En caso de anular un comprobante que haya referenciado a una orden de pedido de Tango Tiendas, no se podrá optar por reponer las cantidades a la orden de pedido en caso que haya sido depurada.



Facturación de pedidos

RG 3685 /4597 - Tipo de operación: seleccione un valor en este proceso que se utilizará en la generación de los archivos de Ventas que requiere la resolución general 3685 /4597 de AFIP.  
Para más información, consulte la [Guía de implementación sobre RG 3685 - Régimen informativo de compras y ventas](?p=11914).

Promociones

Calcula promociones en pedidos: indique si calcula promociones en pedidos. Las opciones de configuración son las siguientes:

  * **Siempre:** siempre calcula promociones en pedidos.
  * **Nunca:** nunca calcula promociones en pedidos.
  * **A pedido:** para calcular promociones en pedidos debe seleccionar la opción 'Calcular promociones' dentro de Promociones.



Días de vigencia de promociones: indique la cantidad de días de vigencia de las promociones en pedidos.

Información de criterios y selección de búsqueda

Tipo de búsqueda por defecto: defina si al buscar un artículo solo se mostrarán los resultados donde texto ingresado coincida con el comienzo del campo (opción 'Comienza con') o con cualquier parte de este (opción 'Contiene').

**Ejemplo:**  
Si el campo de búsqueda es por "Descripción", el texto a buscar ingresado es "AU" y se encuentra configurado el tipo de búsqueda por defecto con la opción 'Comienza con', entonces el resultado será:  
\- AURICULARES  
En cambio, si el parámetro se encuentra configurado con la opción 'Contiene' el resultado de la búsqueda será:  
\- AURICULARES  
\- KIT AUDIO COMPLETO  
\- LAVARROPAS AUTOM. MOD.BLU  


Campo de búsqueda predeterminado: indique cuál será el campo de búsqueda predeterminado al ingresar un valor ('Código', 'Descripción', 'Descripción adicional', 'Sinónimo', 'Código de barras' o 'Todos'). Puede seleccionar un campo particular o todos ellos.

Agregar automáticamente si hay coincidencia: defina cuál será el campo por el cual se agregará automáticamente el artículo al comprobante si hay coincidencia exacta, siendo sus opciones:

  * **Código de artículo:** cuando hay coincidencia exacta con el código del artículo, lo agrega automáticamente.
  * **Sinónimo:** cuando hay coincidencia exacta con el sinónimo, agrega el artículo al comprobante de forma automática.
  * **Código de barra:** cuando hay coincidencia exacta con el código de barras, agrega el artículo al comprobante de forma automática.
  * **Todos:** valor por defecto. Si el texto ingresado coincide exactamente con código, código de barra o sinónimo, el artículo se agrega automáticamente.



Cantidad de caracteres para coincidencia: indique la cantidad de caracteres para determinar una coincidencia en las búsquedas y agregar automáticamente el articulo al comprobante.

**Ejemplo:**  
Tenemos los códigos de artículos 01001 y 0100100135 .  
Si se tiene configurado 5 caracteres y busco 01001 se seleccionará automáticamente ese artículo, en cambio si se tiene configura 13 caracteres no se seleccionará automáticamente ninguno.  


##### Cotizaciones

Autoriza cotizaciones: indica si utiliza la instancia de autorización.

Si se desactiva este parámetro, las cotizaciones nacerán con estado autorizadas, no permitiendo el acceso al proceso [Autorización de cotizaciones.](https://ayudas.axoft.com/24ar/autorizcotizacion_gv) No será posible emitir cotizaciones no autorizadas.

Más información:

Condiciones para la modificación: es posible activar este parámetro en cualquier momento. Si desea desactivarlo y existen cotizaciones con estado ingresada, deberá autorizarlas previamente.  


Acepta cotizaciones: indica si utiliza la instancia de aceptación por parte del cliente.  
Si se desactiva este parámetro, las cotizaciones autorizadas pasan automáticamente al estado aceptadas.

Más información:

Condiciones para la modificación: es posible activar este parámetro en cualquier momento. Si desea desactivarlo y existen cotizaciones con estado autorizada, deberá aceptarlas previamente.  


Aplica permisos para restringir el acceso a cotizaciones: indica si utiliza permisos para restringir la visualización / consulta de documentos en los diferentes procesos de cotizaciones.  
Si se encuentra activo este parámetro, configure permisos de acceso para cada usuario del sistema. Para más información, consulte el proceso [Permisos para cotizaciones](https://ayudas.axoft.com/24ar/permcotizacion_gv).

Mantiene cotizaciones transformadas en pedidos: indica si se conservan las cotizaciones que son transformadas en pedidos.  
Si activa este parámetro, al pasar una cotización a un pedido, ésta se conserva en el sistema. Caso contrario, la cotización será eliminada al transformarse en pedido.

Más información:

Condiciones para la modificación: es posible activar este parámetro en cualquier momento. Si desea desactivarlo y existen cotizaciones con estado procesada, deberá depurarlas previamente (en proceso _Depuración de cotizaciones_).  


Clasificaciones adicionales

Días de vigencia habitual para cotizaciones: indica la cantidad de días por defecto que se adicionan a la fecha de alta de la cotización, para proponer la fecha de vigencia.

Descripción para fecha adicional 1 y Descripción para fecha adicional 2: texto descriptivo para las dos fechas adicionales de cotizaciones.  
El valor de este campo se visualizará en los diferentes procesos que utilicen las fechas adicionales como referencia. Si el campo se encuentra vacío, se desactivará el uso de la fecha adicional en los procesos de cotización.

Cantidad de días para fecha adicional 1 y Cantidad de días para fecha adicional 2: indica la cantidad de días que se adicionará a la fecha de alta de la cotización.  
Esta se propondrá como valor predeterminado para las fechas adicionales.

Descripción para clasificación 1 y Descripción para clasificación 2: texto descriptivo para las clasificaciones adicionales de cotizaciones.  
El valor de este campo se presenta en los diferentes procesos que utilizan las clasificaciones adicionales como referencia. Si el campo se encuentra vacío, se desactivará el uso de la clasificación adicional en los procesos de cotización.

Emisión de cotizaciones

Imprime cotizaciones no autorizadas: indica si permite la impresión de cotizaciones ingresadas. Este parámetro es de utilidad si autoriza cotizaciones.

Imprime al generar: si activa este parámetro, al generar una cotización nueva (ya sea por el comando Ingresar o el comando Copiar), se presenta automáticamente la pantalla de destinos de impresión, en el caso que la cotización cumpla con las siguientes condiciones:

  * Que se encuentre en estado autorizada, si configuró en 'No' el parámetro Imprime cotizaciones no autorizadas.
  * Que las clasificaciones adicionales (si es que se ingresaron) permitan imprimir la cotización.



Generación de pedidos

Genera pedidos aprobados: si activa este parámetro y se encuentra activo el parámetro general Aprueba pedidos ingresados, será posible generar pedidos con estado aprobado.  
Estos se podrán facturar mediante el comando Generar pedido en los procesos de cotizaciones. Si no lo activa, los pedidos generados quedarán con estado ingresado.

Genera pedidos automáticos desde procesos: indica si es posible utilizar el comando Generar pedido en los procesos de cotizaciones ([Generación / Modificación,](https://ayudas.axoft.com/24ar/genermodificotizacion_gv) [Autorización](https://ayudas.axoft.com/24ar/autorizcotizacion_gv) y [Aceptación](https://ayudas.axoft.com/24ar/aceptcotiz_gv)).

Cantidad habitual de días para la fecha de entrega: es la cantidad de días a considerar para el cálculo de la fecha de entrega, en el momento de generar el pedido en base a una cotización.  
Usted puede dejar en cero este parámetro, para que la fecha de entrega sea igual a la fecha del pedido.

##### Recibos

Defina sus preferencias para el proceso [Cobranzas.](?p=21323) Indique el comportamiento para cada una de las opciones en el momento de la generación.

Moneda: defina el comportamiento para el ingreso de la moneda en el momento de la generación. Los valores posibles son: moneda corriente, extranjera contable, o según la cláusula del cliente.

Orden de carga de datos: elija el orden de ingreso de datos más adecuado a su modo de operar. En el caso que prefiera ingresar en primer lugar los valores, marque Medios de cobro / Comprobantes (*).

(*) Esta opción es de utilidad si usted utiliza la selección automática de los comprobantes cobrados. En este caso el sistema, en base a la prioridad (para asignar comprobantes a cobrar) elegida, le propone los comprobantes que pueden cancelarse de acuerdo a los valores ingresados.

Modo de imputación: indique si el ingreso de los comprobantes a cobrar se realiza de modo automático o por selección manual.  
Si elige imputación manual, usted debe ingresar los comprobantes a cancelar en el proceso Cobranzas, utilizando alguna de estas dos opciones:

  * Detallando individualmente el tipo y número de comprobante, o seleccionándolos de una lista propuesta.
  * Utilizando el seleccionador <F3> para elegir los comprobantes a cancelar.



Utilizando esta opción, los comprobantes se imputarán en el orden en que son ingresados. Se controla que el importe a imputar sea mayor a cero. En este caso, se aplican las siguientes validaciones:

  * El importe del comprobante de crédito no debe superar el importe a pagar de la factura precedente. Si se realiza una imputación parcial, el importe pendiente puede imputarse a otra factura o puede dejarlo a cuenta para se imputado posteriormente.
  * En el caso de utilizar el seleccionador de comprobantes <F3>, si incluye notas de crédito y/o débito, debe decidir a que factura se imputan, antes de confirmar la operación.



Si elige imputación automática e ingresa en primer lugar los valores, el sistema le propone automáticamente los comprobantes pendientes que pueden ser cancelados por el total del importe ingresado, según la prioridad para la asignación de comprobantes a cobrar que haya parametrizado.  
La opción 'automática' brinda, además de la facilidad para imputar comprobantes de modo ágil, la posibilidad de selección automática en función del importe cobrado utilizando el valor con fechas de vencimiento más antiguas para definir la prioridad para asignar comprobantes a cobrar.  
La opción 'por orden' de carga es reemplazada por la de selección manual, contando con las siguientes ventajas por sobre la alternativa anterior:

  * Puede ingresar los comprobantes en cualquier orden, siempre que finalmente defina las imputaciones antes de confirmar la operación.
  * Puede imputar una misma nota de crédito y/o débito a diferentes facturas, siempre que no exceda el importe pendiente del comprobante a imputar.
  * Puede utilizar el seleccionador de comprobantes <F3>.



Modo de imputación cobranzas masivas: elija la modalidad de imputación de los comprobantes en el proceso generación masiva de recibos.  
Las opciones posibles son: 'Automático' o 'A cuenta'. La opción por defecto es 'A cuenta'.  
Esta modalidad se aplicará en aquellas cobranzas de las que no se tiene información del comprobante abonado y también, para el excedente cobrado de un importe pendiente del vencimiento.  
Si elige la opción 'A cuenta', los recibos generados en forma masiva no tendrán una imputación asignada. Usted podrá utilizar el proceso Imputación de comprobantes para aplicar cada cobranza a los comprobantes respectivos.  
Si elige la opción 'Automático', los recibos se imputarán teniendo en cuenta el criterio de prioridad para la asignación de comprobantes a cobrar.

El criterio de asignación es común para los recibos ingresados desde el proceso Cobranzas y los generados en forma masiva.

Modo de imputación Tango Cobranzas: al igual que el parámetro anterior, permite elegir la modalidad de imputación durante la generación masiva de recibos de aquellos cobros con origen [Tango Cobranzas](?p=12425) que no referencian a ningún comprobante, y también, para el excedente cobrado de un importe pendiente del vencimiento. El valor por defecto es 'A cuenta'. Para definir el valor de esta opción, se sugiere tener en cuenta el uso de la Solicitud de pago electrónico y del Envío de dinero desde [Tango Clientes](?p=12564) en el circuito operativo de su empresa.

Comportamiento habitual para la selección de los comprobantes a cobrar

Selecciona comprobantes en función del importe cobrado: indique el valor de este parámetro teniendo en cuenta su operatoria habitual:

  * Si habitualmente usted ingresa los valores en primer lugar, y siempre cancela los comprobantes según un criterio determinado (por ejemplo, siempre los cancela teniendo cuenta las fechas de vencimiento mas antiguas), seleccione el valor 'Siempre'.
  * En el caso que usted prefiera decidir que comprobantes cancelar, seleccione 'Nunca'.
  * Si depende de cada ocasión en particular, seleccione 'Con confirmación'. En este caso, cada vez que ingrese o modifique un valor en Tesorería el sistema le consultará si desea recalcular los comprobantes a cancelar.



Esta opción está disponible si utiliza el modo imputación automática.

__Nota

Independientemente del valor que seleccione, siempre es posible seleccionar los comprobantes en forma automática, en base a los valores ingresados, utilizando el botón "Selección automática" de la grilla de comprobantes en el proceso _Cobranzas_.

En el caso de utilizar el seleccionador de comprobantes <F3>, si incluye notas de crédito y/o débito, debe decidir a que factura se imputan, antes de confirmar la operación.

Si elige selección automática (en función del importe cobrado) e ingresa en primer lugar los valores, el sistema le propone automáticamente los comprobantes pendientes que pueden ser cancelados por el total del importe ingresado, según la prioridad para la asignar comprobantes a cobrar que haya parametrizado.

(*) Nota para usuarios de versiones anteriores a 9.91.000: este parámetro reemplaza al modo de imputación de comprobantes a cobrar, con sus opciones 'Automática' y 'Por orden de carga'.

La opción 'automática' es reemplazada por la de selección automática en función del importe cobrado utilizando el valor con fechas de vencimiento más antiguas para definir la prioridad para asignar comprobantes a cobrar.

La opción 'por orden' de carga es reemplazada por la de selección manual, contando con las siguientes ventajas por sobre la alternativa anterior:

  * Puede ingresar los comprobantes en cualquier orden, siempre que finalmente defina las imputaciones antes de confirmar la operación.
  * Puede imputar una misma nota de crédito y/o débito a diferentes facturas, siempre que no exceda el importe pendiente del comprobante a imputar.
  * Puede utilizar el seleccionador de comprobantes <F3>.



Muestra todos los comprobantes pendientes: indique si desea que los comprobantes pendientes se presenten automáticamente siempre que ingresa un recibo, o sólo cuando el usuario lo requiera (a pedido). Utilizando esta opción puede prescindir del seleccionador de comprobantes <F3>.  
Esta opción sólo está disponible si trabaja con modalidad 'automática'.

Prioridad para la asignación de comprobantes a cobrar

Criterio: en el caso que utilice la selección automática (en función del importe cobrado), puede optar por el siguiente orden para considerar que comprobantes se cancelan en primer lugar:

  * Con fechas de vencimiento más antiguas.
  * Con fechas de vencimiento más nuevas.
  * Con fechas de vencimiento más nuevas (sólo si están vencidos).
  * Con fechas de emisión más antiguas.
  * Con fechas de emisión más nuevas.
  * Con fechas de vencimiento cercanas a los valores recibidos.



Incluye notas de crédito: tilde este parámetro para que Tango proponga las notas de crédito pendientes, en el momento de seleccionar automáticamente los comprobantes a cobrar. (*)

Incluye notas de débito: tilde este parámetro para que Tango proponga las notas de débito pendientes, en el momento de seleccionar automáticamente los comprobantes a cobrar. (*)

(*) En el caso de considerar las notas de crédito/débito, éstas se imputan a las facturas tomándolas en cuenta según su fecha de emisión y ordenadas según la prioridad para la asignación de comprobantes a cobrar elegida.

__Nota

Tenga en cuenta que aunque el parámetro no esté tildado, puede incluir estos comprobantes como parte de la operación, siempre que los necesite. En el momento de ingresar el recibo, efectúe su ingreso manual o tíldelos desde la lista de comprobantes pendientes propuestos, si activó la carga automática.

Ante igual fecha, se asignan: en el caso de indicar que incluye tanto notas de crédito como de débito, indique el orden en que prefiere que se imputen las facturas correspondientes:

  * Primero las notas de débito.
  * Primero las notas de crédito.
  * Por orden de emisión.



Asignación de cuenta para la corrección de diferencias por redondeo

Código de cuenta: ingrese la cuenta de tesorería donde se imputarán las diferencias por redondeo que podrían generarse al trabajar con clientes con cláusula en moneda extranjera. Este ajuste será realizado en forma automática cuando el sistema detecte que se está intentando cancelar un comprobante en moneda extranjera y no pueda cancelarse en moneda corriente, debido a problemas de redondeo.

__Nota

En el caso de existir cambios en la cotización, los errores de redondeo son absorbidos por los comprobantes de diferencias de cambio a generar.

La diferencia entre el valor numérico real y el valor redondeado que se utiliza al hacer conversiones entre monedas, se conoce como _error de redondeo_. Este depende de la cantidad de decimales con la que usted decida trabajar en cada moneda, y puede provocar que un comprobante, a pesar de estar cancelado en moneda extranjera, no quede cancelado en moneda corriente, debido a pequeñas diferencias surgidas por redondear los importes en las diferentes monedas.

**Ejemplo...  
**Se factura a un cliente con cláusula moneda extranjera, por lo tanto, el importe de referencia a saldar es el de la moneda extranjera, siendo el total en moneda corriente un importe re-expresado a partir del anterior.  
El cliente lo cancela en dos pagos, cobrando en moneda corriente, los importes que se indican en cada caso. Al ser un cliente cláusula debe re expresarse el cobro en moneda corriente, a moneda extranjera, para efectuar el cálculo de los nuevos saldos.  
La cotización utilizada es de $ 4.76, en todos los casos y solo a modo de ejemplo.  
Trabajando con dos decimales en cada moneda:

_Caso 1:_

  1. Se genera una factura de venta por u$s 191.01, con una cotización de $ 4.76 (u$s 191.01* $ 4.76 = $909.23).
  2. El cliente efectúa un primer pago entregando un cheque por $ 500.00. Se calcula el importe a cancelar en moneda extranjera, debido a que es un cliente cláusula ($ 500,00 / $ 4.76 = u$s 105.04). El nuevo saldo de la factura es:  
En moneda extranjera: u$s 191.01 - u$s 105.04 = u$s 85.97  
En moneda corriente: $ 909.23 - $ 500.00 = $ 409.23
  3. Se efectúa un segundo pago, cancelando la factura. El cliente entrega un cheque por $ 409.23, utilizando la misma cotización: ($ 409.23 / $ 4.76 = u$s 85.97).  
El nuevo saldo de la factura es:  
En moneda extranjera: u$s 85.97 - u$s 85.97 = u$s 0.00  
En moneda corriente: $ 409.23 - $ 409.23 = $ 0.00



En este caso, la factura se cancela en ambas monedas, al quedar ambos saldos en 0 y por lo tanto no se produce error de redondeo.

_Caso 2:_

  1. Se genera una factura de venta por u$s 191.01, con una cotización de $ 4.76 (u$s 191.01* $ 4.76 = $909.23).
  2. El cliente efectúa un primer pago entregando un cheque por $ 500.00. Se calcula el importe a cancelar en moneda extranjera, debido a que es un cliente cláusula ($ 500,00 / $ 4.76 =u$s 105.04). El nuevo saldo de la factura es:  
En moneda extranjera: u$s 191.01 - u$s 105.04 = u$s 85.97  
En moneda corriente: $ 909.23 - $ 500.00 = $ 409.23
  3. Se efectúa un segundo pago, cancelando la factura. El cliente entrega un cheque por $ 409.22 (*), utilizando la misma cotización: ($ 409.22 / $ 4.76 = u$s 85.97).  
El nuevo saldo de la factura es:  
En moneda extranjera: u$s 85.97 - u$s 85.97 = u$s 0.00  
En moneda corriente: $ 409.23 - $ 409.22 = $ 0.01  
En este caso, como la factura queda cancelada, en moneda extranjera (que es la que se debe saldar debido a que el cliente es cláusula), asigna la diferencia de $ 0.01 a la cuenta de redondeo.



(*) En el último caso a pesar de ser diferente el importe del saldo en moneda corriente, comparado con el dinero entregado por el cliente, al re-expresarlo a moneda extranjera, el resultado es el mismo. Esto se debe a diferencias de redondeo surgidos por el truncamiento del número calculado.

En el caso 1: u$s 409.23 / $ 4.76 = u$s 85.972689...  
En el caso 2: u$s 409.22 / $ 4.76 = u$s 85.970588...  
En ambos casos, al redondear el resultado a dos decimales, el importe en moneda extranjera, es el mismo: u$s 85.97.  
Debido a este error, es que en cualquiera de los dos casos, el saldo en moneda extranjera queda cancelado, y en moneda corriente sólo se cancelaría en el primer caso.  
Ante esta situación, el sistema realiza el ajuste automático enviando la diferencia pendiente a la cuenta de tesorería definida en el parámetro, generando un movimiento de similar al que se muestra a continuación.

Más información:

Tenga en cuenta que si usted utiliza la funcionalidad <F3> para proponer el importe de la cuenta de tesorería, el sistema calculará $ 409.22, debido a que el importe de referencia en este caso es el del saldo en moneda extranjera (u$s 85.97 * $ 4.76 = $ 409.22). Sin embargo, al interpretar que se está intentando cancelar el comprobante en la cláusula del cliente, también se dejará cancelado en la otra moneda, agregando la cuenta por diferencias de redondeo.

Otros temas:

Sugiere el ingreso de documentos / leyendas: al seleccionar estos parámetros el sistema queda posicionado en las solapas correspondientes, de modo automático antes de grabar el recibo. Tenga en cuenta que, de todos modos, el ingreso de los datos no es obligatorio.

__Nota

Haciendo clic sobre las solapas, puede ingresar documentos o leyendas cuando lo necesite, aún cuando los parámetros no estén chequeados.

Títulos para leyendas: este campo permite modificar el título de cada leyenda a ingresar en el recibo.

##### Intereses por mora

Defina valores por defecto para la generación de notas de débito de interés por mora desde [Gestión de débitos por mora](https://ayudas.axoft.com/24ar/gestiondebitomora_gv) o [Cobranzas](https://ayudas.axoft.com/24ar/ingresocobranza_gv).  
Indique el comportamiento para el ingreso de estos valores en el momento de la generación, asignando permisos de edición para cada uno de ellos.  
Los valores posibles para cada uno de los campos a parametrizar son:

**Valor posible** | **Descripción**  
---|---  
E | El campo se edita en forma normal.  
M | El campo no se edita, muestra el valor por defecto asignado.  
  
Los valores por defecto se utilizan en el caso que alguno de los campos quede sin valor asignado, cuando alguno de los datos de los comprobantes de referencia no coinciden, y se haya definido un control flexible ante control de datos diferentes.

Política de interés: defina la política de cálculo de interés por mora que se considerará a nivel general cuando no exista una definida para la [condición de venta](https://ayudas.axoft.com/24ar/condicionventa_gv) o [cliente](https://ayudas.axoft.com/24ar/clientes_carp_gv) (*).  
La política asignada a nivel general se utiliza también en los casos en que una factura se haya generado sin asignación de política (por ser de una versión anterior o por pertenecer a un cliente que no genera débitos por mora), para realizar la asignación luego de su emisión. En el caso que cuente con permiso de edición, puede optar por elegir otra política en el momento de generar la nota de débito desde [Gestión de débitos por mora](https://ayudas.axoft.com/24ar/gestiondebitomora_gv).

(*) Más información:

La asignación de la política al comprobante se realiza teniendo en cuenta el siguiente orden de prioridades:

  * En primer lugar se utiliza la política del cliente si éste tiene alguna asignada.
  * En segundo lugar se utiliza la política de la condición de venta si ésta tiene alguna asignada.
  * En tercer lugar, se utiliza la política definida a nivel general, en Parámetros de Ventas.



Para más información consulte la [Guía de implementación sobre intereses por mora](?p=27248).

Alícuota de IVA: indique la alícuota de IVA a aplicar a las notas de débito de interés por mora.

__Nota

Tenga en cuenta que si el comprobante original liquidó otros impuestos, estos no se aplican sobre el interés calculado.

Genera mora en la cobranza: indique si desea generar notas de débito de interés por mora desde el proceso [Cobranzas](https://ayudas.axoft.com/24ar/ingresocobranza_gv).  
Valores posibles para este campo:

  * Siempre: en este caso siempre que estén dadas las condiciones para generar mora se emite una o varias notas de débito.
  * Nunca: No se generan notas de débito desde este proceso.
  * Con confirmación: en el caso de que corresponda generar una o varias notas de débito por mora, se consulta si se desea efectuar esta operación.
  * Sólo avisa: en el caso de que corresponda generar una o varias notas de débito por mora, se emite un aviso de esta situación, sin posibilidad de emitir los comprobantes.



En todos los casos en que no se llega a generar la/s nota/s de débito por mora correspondientes, puede hacerlo posteriormente desde [Gestión de débitos por mora](https://ayudas.axoft.com/24ar/gestiondebitomora_gv) utilizando la opción Incluir facturas cobradas con atraso.

Fecha a asignar: este parámetro se habilita cuando Genera mora en la cobranza está configurado como 'Siempre' o 'Con confirmación'.  
Seleccione la fecha que tendrán los comprobantes por intereses por mora generados desde [Cobranzas](?p=21323) y [Cobranzas masivas](?p=21355). Las opciones posibles de selección son: fecha del recibo (opción por defecto) o fecha del día.

##### Fechas de vencimiento

Vencimientos que se registran en días sábado, domingo o feriado

Traslada fecha de vencimiento al siguiente día hábil: al efectuar el cálculo de fechas de vencimiento, es posible que coincidan con un día feriado o fines de semana. Marque este parámetro si desea que sean trasladadas al primer día hábil posible.

**Ejemplo...**  
Factura: con fecha de emisión 08/05/2019.  
Condición de venta: 1 cuota a 20 días de la fecha de factura.  
**Fecha de vencimiento calculada:** Sábado 18/05/2019.  
Si Traslada fecha de vencimiento al siguiente día hábil, la fecha de vencimiento definitiva será 21/05/2019 (lunes).

Comprobantes a generar para recargos y descuentos por cobro en fechas alternativas

Defina valores por defecto para la generación de notas de débito y crédito en concepto de recargos o descuentos por cobros de facturas en fechas alternativas desde Gestión de débitos por mora, Cobranzas o Imputación de comprobantes.  
Indique el comportamiento para el ingreso de estos valores en el momento de la generación, asignando permisos de edición para cada uno de ellos.

Los valores posibles para cada uno de los campos a parametrizar son:

**Valor posible** | **Descripción**  
---|---  
E | El campo se edita en forma normal.  
M | El campo no se edita, muestra el valor por defecto asignado.  
  
Los valores por defecto se utilizan en el caso que alguno de los campos quede sin valor asignado.

Para generar los ajustes antes mencionados, es necesario que la factura cumpla las siguientes condiciones:

  * Contar con una condición de venta asociada que genera fechas alternativas de vencimiento.
  * Que las fechas alternativas tengan asociado un porcentaje de descuento / recargo.
  * Que el cobro de las cuotas se realice entre la fecha de vencimiento real y alguna de sus alternativas



**Ejemplo...**

_Factura:_

Fecha de emisión: 01/04/<%YEAR%>.  
Importe: $300000

_Definición de la condición de venta:_

Cantidad de cuotas: 3  
Vencimiento: los días 5 de cada mes.  
Genera fechas alternativas de vencimiento  
Primer alternativa de vencimiento: se realiza un descuento del 0.5% si se abona la factura hasta 10 días antes del vencimiento.  
Segunda alternativa de vencimiento: se realiza un recargo del 0.5% si se abona la factura luego de su fecha de vencimiento y hasta 10 días después.

_Fechas de vencimiento calculadas:_

**Vencimientos** | **Alternativa 1** | **Alternativa 2**  
---|---|---  
**Cuota** | **Fecha** | **Importe** | **Fecha** | **Importe** | **Fecha** | **Importe**  
1 | 05/04/2019 | 100000 | 26/03/2019 | 99500 | 15/04/2019 | 100500  
2 | 05/05/2019 | 100000 | 25/04/2019 | 99500 | 15/05/2019 | 100500  
3 | 05/06/2019 | 100000 | 26/05/2019 | 99500 | 15/06/2019 | 100500  
  
_Cobro de la primer cuota:_

  * **Opción 1:** se efectúa el cobro el día 05/04/<%YEAR%> por $100000. No se genera ningún comprobante de ajuste.
  * **Opción 2:** se efectúa el cobro el día 26/03/<%YEAR%> por $99500. Se genera una nota de crédito por $5 para ajustar la diferencia por el cobro correspondiente a la primer fecha alternativa.
  * **Opción 3:** se efectúa el cobro el día 10/04/<%YEAR%> por $100500. Se genera una nota de débito por $500 para ajustar la diferencia por el cobro correspondiente a la segunda fecha alternativa.



Si el cobro se efectúa pasada la segunda alternativa de vencimiento, el sistema calculará intereses por mora del modo habitual.

##### Facturas

Integra con Tango Cobranzas para pagos al contado: habilitando esta opción desde el Facturador podrá utilizar como medio de pago 'Tango Cobranzas' para facturas al contado.  
Para esto deber estar integrado a [Tango Cobranzas](?p=12425). Para más información consulte [Guía de implementación sobre Tango Cobranzas](?p=27349).

Enviar por correo electrónico el link de pago de la factura electrónica: habilitando esta opción se enviará el link de pago en el correo de la factura electrónica. Para esto deber estar integrado a [Tango Cobranzas](?p=12425). Para más información consulte [Guía de implementación sobre Tango Cobranzas](?p=27349).

Cuentas de cobro para pagos electrónicos: seleccione las cuentas de Tesorería a la cual serán asignados los cobros por [Tango Cobranzas](?p=12425) (MercadoPago®). Tenga en cuenta que, si habilitó la opción Integra con Tango Cobranzas para pagos al contado, debe contar con al menos un sistema de pago relacionado a una cuenta de Tesorería.

##### Ticket de cambio

Imprime ticket: este parámetro permite imprimir comprobantes no fiscales para el cambio de mercadería, luego de la impresión de una factura.  
Los valores posibles son: 'Nunca', 'Siempre' o 'A pedido'. Sólo será posible utilizar esta opción en facturas que se emitan a través de equipos fiscales. En el proceso de facturación, en la solapa Pagos, mediante tecla de función <F7> llamará a la ventana de impresión de ticket de cambio para modificar la impresión de los artículos que por defecto saldrán impresos en el ticket de cambio. También podrá no imprimir dichos artículos en la factura en curso, o cambiar la modalidad de impresión configurada por defecto.

__Nota

Para que la impresión del ticket de cambio se realice a través de una impresora de comandas no fiscal, deberá seleccionar una en la sección de _Dispositivos_ , dentro de las _Preferencias del Facturador_ y, a su vez, no deberá tener configurado un controlador fiscal en el sistema.

Envía ticket por correo electrónico (Solo Facturador): este parámetro se utiliza en facturas de cualquier tipo y solo utilizado desde el Facturador. Permite generar un archivo con el ticket de cambio y enviarlo por mail, luego de la generación de una factura.

__Nota

Si el parámetro está marcado y el cliente no tiene un correo electrónico definido, podrá agregar esta información al momento de generar la factura. En caso que no se ingrese el correo electrónico, no se enviará el ticket de cambio.

Teniendo en cuenta las preferencias de entrega de ticket de cambio al cliente seleccione la combinación que se ajusta a su negocio:

  1. Si prefiere que se imprima el ticket de cambio y no se envíe por correo electrónico:  
Imprime ticket = 'Siempre'  
Envía ticket por correo electrónico = 'Nunca'
  2. Si prefiere que el ticket siempre se envíe por correo electrónico pero si cliente no tiene correo imprimir el ticket de cambio seleccione:  
Imprime ticket = 'A pedido'  
Envía ticket por correo electrónico = 'Siempre'
  3. Si el cajero selecciona la preferencia de entrega del ticket de cambio al generar el comprobante:  
Imprime ticket = 'A pedido'  
Envía ticket por correo electrónico = 'A pedido'
  4. Si prefiere que el ticket siempre se envíe por correo electrónico pero si cliente no tiene correo no imprimir el ticket de cambio seleccione:  
Imprime ticket = 'Nunca'  
Envía ticket por correo electrónico = 'Siempre'
  5. Si prefiere que el ticket siempre se envíe por correo electrónico y también se imprima el ticket de cambio seleccione:  
Imprime ticket = 'Siempre'  
Envía ticket por correo electrónico = 'Siempre'



Existen también modalidades de impresión de los artículos incluidos en el comprobante para el cambio de mercadería. De acuerdo a su necesidad puede optar por las siguientes opciones:

  * Un ticket de cambio por unidad de artículo: elija esta opción para imprimir un comprobante ticket de cambio por cada unidad vendida del artículo. Se imprimirán tantos tickets de cambio como total de unidades de la factura. En cada comprobante se detallará el artículo y como cantidad "1.00".
  * Un ticket de cambio por renglón de artículo: elija esta opción para imprimir un comprobante ticket de cambio por cada renglón de artículo de la factura. Se imprimirán tantos ticket de cambio como renglones de artículos existan en la factura. En cada comprobante se detallará el artículo y la cantidad vendida.
  * Un ticket de cambio por comprobante: elija esta opción para imprimir un comprobante ticket de cambio por cada factura. Se imprimirá solamente un ticket de cambio donde se detallarán todos los artículos de la factura con su cantidad.
  * Un ticket de cambio solamente para los artículos que descarguen stock: elija esta opción para imprimir solamente un ticket de cambio donde se detallen los artículos que descarguen stock con la factura. Se detallará el artículo y su cantidad.



Texto para el ticket de cambio: puede ingresar texto adicional para ser utilizado como título en el ticket de cambio. Este texto se imprimirá como parte del encabezado.

#### Parámetros para controles

Fecha del comprobante igual a la fecha del día

El objetivo del control de las fechas de comprobantes es el de limitar el ingreso y la actualización de comprobantes con fecha diferente a la del día.  
Para cada uno de los comprobantes que usted genera en el sistema, es posible indicar si controla que la fecha de emisión sea la fecha del día.  
Controles posibles:

  * **Control estricto:** la fecha del comprobante a generar debe coincidir con la fecha del sistema para poder continuar con el proceso.
  * **Control flexible:** si la fecha de emisión no coincide con la del día, se exhibe un mensaje de confirmación para que usted decida si continúa o cancela el proceso.
  * **No controla:** en este caso es posible ingresar un comprobante con cualquier fecha de emisión.



Además del control de la fecha en los comprobantes, usted puede manejar dos fechas de cierre distintas, una para comprobantes de facturación y otra exclusivamente para recibos.  
Estas fechas serán posibles configurarlas desde el proceso Fecha de cierre en el módulo Procesos generales.

Remitos

Valoriza remitos: active este parámetro si desea informar el total neto de impuestos de las mercaderías remitidas.  
Para que la valorización del remito se efectúe en forma obligatoria, seleccione 'Si'.  
En cambio, si necesita valorizar sólo ciertos remitos, puede elegir el valor 'A pedido'. En este caso, no es obligatorio el ingreso de la lista de precios en el momento de generar el comprobante.

Lista de precios: defina el comportamiento para el ingreso de este dato, en el momento de efectuar el remito.  
Los valores entre los que puede optar son:

  * Edita: elija esta opción si desea que el código de la lista de precios pueda ingresarse y/o modificarse en el momento de la generación del comprobante
  * Muestra: el código de la lista no es modificable en el momento del ingreso del remito. Por tal motivo, configure la lista de precios habitual.



Lista de precios habitual: ingrese la lista de precios que se propondrá por defecto al ingresar un remito (cuando el cliente no tiene asignada una lista o el remito se ingresa sin comprobante de referencia).  
Tenga en cuenta que la lista a elegir no debe incluir IVA y sus precios deben estar expresados en moneda corriente.

Importe total del remito: active este parámetro para editar y modificar el total propuesto al valorizar el remito.

__Nota

Tenga en cuenta que el valor de esta opción se aplica únicamente en el momento de la impresión o consulta del comprobante. No será trasladado a los documentos posteriores que hagan referencia al remito.

Descripciones adicionales: defina el comportamiento a aplicar. Los valores posibles para este campo son los siguientes:

  * No: no permite editar las descripciones adicionales ni insertar líneas.
  * Sólo permite agregar líneas: es posible agregar líneas, sin posibilidad de editar el contenido de las descripciones asignadas al artículo.
  * Permite agregar líneas y modificar la descripción del artículo: permite agregar líneas, con la posibilidad de editar el contenido de las descripciones asignadas al artículo.



Emite remitos de traslado: indique si habilita la emisión de este tipo de remitos. Los remitos de traslado no serán facturados.

Identificación de consumidores finales

Tope con pago electrónico y Tope con pago no electrónico: este parámetro es utilizado únicamente por el Facturador. Si los montos facturados exceden estos valores, el sistema no permitirá generar la factura hasta que complete el número de identificación del cliente.  
Se pueden generar facturas a consumidores finales sin necesidad de informar el número de identificación (documento, CUIL, etc.), siempre y cuando tengan un valor inferior a esos valores. Si usa pagos electrónicos es hasta el monto configurado en Tope con pago electrónico, en cambio si utiliza medios de pagos no electrónicos puede facturar hasta el monto configurado en Tope con pago no electrónico.

Otros controles

Codificación del tipo de comprobante: los valores posibles de selección son multipropósito o comprobante.  
Seleccione la opción 'Multipropósito' si utiliza [talonarios](https://ayudas.axoft.com/24ar/talonario_gv) multipropósito y necesita imprimir el código del [tipo de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_gv) con una numeración fija (usando la variable de impresión **@VR**) o el código de barras (usando la variable **@BB**). Con esta parametrización, para todos los comprobantes tipo "A" (facturas, créditos y débitos) se imprimirá el código '01'; para los comprobantes de tipo "B" se imprimirá el código '06' y para los comprobantes de tipo "E", se imprimirá el código '19'.  
Si selecciona la opción 'Por comprobante', el sistema asignará el código de la tabla de la RG 100/98.

Controla vigencia certificado según RG 1817: defina el criterio a aplicar con referencia al control de certificados de sus clientes, según lo establecido por la RG 1817.  
Al activar este parámetro, el sistema validará que la fecha de la factura a emitir esté comprendida en el período de vigencia del certificado presentado por el cliente.  
Los valores posibles son a confirmar y no utiliza.

[/axcond_modulo] 

Modifica la cotización del comprobante a generar: al activar este parámetro, usted podrá cambiar la cotización para aplicarla a un comprobante en particular en el momento de su ingreso.  
De esta manera, cuando invoque el comando [Cotización](https://ayudas.axoft.com/24ar/procesofacturacion_gv) e indique una cotización diferente a la registrada en el sistema, ésta afectará únicamente al comprobante a ingresar. Finalizada la operación, el sistema considerará para el comprobante siguiente, la cotización general. En este caso, para cambiar la cotización general, invoque el proceso Cotizaciones del módulo Procesos generales.  
Este parámetro se tiene en cuenta en el ingreso de comprobantes de cotizaciones, pedidos, facturas, recibos de cobranza, notas de crédito y notas de débito.

Cotización general: si no está instalado el módulo Tesorería y está activo el parámetro Modifica la cotización del comprobante a generar, ingrese el valor de la cotización general del sistema para su aplicación en este módulo.  
Si está instalado el módulo Tesorería y no está activo el parámetro Modifica la cotización del comprobante a generar, actualice la cotización general desde los procesos cotizaciones, pedidos, facturas, notas de crédito y notas de débito.

Asignación obligatoria de perfiles: defina si un usuario que no tiene un perfil asignado, puede ingresar a los procesos que utilizan perfiles en el módulo Ventas.

#### Parámetros para comprobantes de referencia

Remitos

Comprobantes de referencia: permite indicar si en el remito se edita la referencia de comprobantes.

Tipo de comprobante de referencia: indica el tipo de comprobante a utilizar en el ingreso del remito.  
Los valores posibles son: edita, obligatorio y sin referencia. En el caso que elegir el valor 'Obligatorio', sólo podrá seleccionar factura y pedido.

Agrupa artículos iguales: permite determinar el comportamiento a aplicar cuando en el remito se referencien varios pedidos o facturas con artículos repetidos.

Descripciones adicionales / observaciones del renglón: indica el tratamiento a aplicar, con respecto a las descripciones adicionales y a las observaciones del renglón, al agrupar artículos de comprobantes referenciados.  
Si elige la opción 'Mantiene', no se agrupan los artículos y se respetan las descripciones adicionales / observaciones del renglón. Si opta por la opción 'No Mantiene', se omiten las descripciones adicionales / observaciones del renglón y se agrupan los artículos.

Respeta precios de comprobante de referencia: mediante este parámetro defina el tratamiento a aplicar para los precios del comprobante de referencia de los remitos.  
Las opciones disponibles son las siguientes:

  * Respeta precio de referencia.
  * No respeta precio de referencia.
  * Propone precio y edita.



Control de renglones en remitos con referencia a pedidos: este parámetro define la modalidad de control a aplicar en el momento de ingresar los artículos en un remito con referencia a un pedido.  
Valores posibles para este campo:

  * Controla carga: previo a la emisión de un remito con referencia a un pedido, el sistema muestra una ventana para la carga de artículos, los que deben existir en el pedido original. Al finalizar el ingreso de los artículos del pedido a remitir, se visualiza otra ventana con la cantidad total de artículos ingresados, las cantidades originales a remitir del pedido y las cantidades que quedan pendientes por remitir.
  * No controla carga: no se realiza el control de carga de artículos contra los renglones del pedido. Al ingresar remitos con referencia a un pedido, todos los artículos a remitir se cargan directamente en el remito.
  * Confirma control carga: al ingresar un remito con referencia a un pedido, el sistema solicita su confirmación para aplicar el control de carga de artículos. Si no lo confirma, todos los artículos a remitir se cargan directamente en el remito.



__Nota

Tenga en cuenta que al utilizar control de carga, éste se aplica solamente a las unidades disponibles en stock.

Respeta depósitos de comprobantes referenciados: active este parámetro para considerar, para la descarga de stock en el remito, los depósitos de los comprobantes referenciados.

Acepta pedidos con kits sin componentes: tilde este parámetro en el caso que desee completar los kits en el momento de entregar la mercadería. Caso contrario, es necesario completarlos previamente desde los procesos propios de [pedidos](?p=19401) para que se permita referenciar el pedido desde [remitos](https://ayudas.axoft.com/24ar/emisionremito_gv)(*).

(*) Tenga en cuenta que si indica que no acepta pedidos con kits sin componentes, y define que siempre ingresa pedidos con kits sin componentes, no es posible completar el pedido desde ningún proceso.

Facturas, remitos y pedidos con comprobantes de referencia

Ante disminución de cantidades en renglones que agrupen varios comprobantes, distribuye manualmente las cantidades en los comprobantes relacionados: active este parámetro para distribuir en forma manual las cantidades a remitir o a facturar de un artículo, al momento de referenciar varios comprobantes en una factura o remito.  
Caso contrario, al modificar las cantidades propuestas para facturar o remitir, se disminuirá la cantidad de los comprobantes relacionados más antiguos en forma automática.

Permite agregar artículos en facturas y/o remitos: permite definir si se pueden agregar artículos al referenciar comprobantes en una factura o en un remito.

Control de datos diferentes para:

Por medio de esta serie de parámetros es posible controlar si factura o remite referenciando comprobantes (pedidos o remitos) con datos diferentes de los indicados.  
Si configura los controles en forma flexible, al referenciar varios comprobantes, y en éstos difiere algún dato, el sistema permitirá facturarlos tomando ese dato del perfil. Si no existen perfiles, deberá ingresar ese campo en el encabezado de la factura o remito. Este control se aplica a los siguientes datos: vendedores, depósitos, transportes, lista de precios, condición de venta y la bonificación. El comportamiento en estos campos puede ser flexible o control estricto. 

Direcciones de entrega: por medio de este parámetro podrá controlar el ingreso de pedidos, remitos o factura en referencia a varios comprobantes con datos diferentes en las direcciones de entrega asociadas a cada una de ellas.

  * Control flexible:  
Si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega y diferentes configuraciones impositivas, el sistema emitirá el siguiente mensaje de confirmación: "Los comprobantes de referencia tienen distinta configuración impositiva, Confirma?".  
Al confirmar esta validación, desde la ventana de dirección de entrega seleccione la opción deseada de acuerdo al lugar de entrega y al cálculo de impuestos correspondientes.
  * Control estricto:  
Si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje, y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega con configuraciones impositivas diferentes, el sistema emitirá el siguiente mensaje: "Los comprobantes de referencia deben tener la misma configuración impositiva" no permitiendo continuar con la carga del comprobante.



Importante:

Tenga en cuenta que en la ventana de dirección de entrega que despliega el sistema, aparecerán todas las direcciones asociadas al cliente y no sólo las utilizadas en los comprobantes que se están referenciando.

#### Parámetros para clasificación de comprobantes

Utiliza clasificación: active este parámetro si desea utilizar los códigos de clasificación para los comprobantes de ventas.  
Para más información consulte [Clasificación de comprobantes](?p=11840).

Leyenda para clasificación: puede ingresar un nombre descriptivo para todas las clasificaciones.  
El valor de este campo se visualiza en la pantalla de clasificaciones, en los diferentes procesos que la utilicen. También será posible imprimir este valor en los comprobantes.

Comprobantes a clasificar y su clasificación habitual

Usted puede seleccionar aquellos comprobantes que desee clasificar indicando también un código de clasificación habitual para cada tipo de comprobante.

Controles a aplicar

Clasifica comprobantes: usted puede controlar mediante este parámetro cómo clasificar los comprobantes.  
Los controles pueden ser:

  * Siempre: el sistema controla que cada vez que se genere un comprobante, éste sea clasificado antes de grabarlo.
  * A Confirmar: el sistema solicita confirmación para grabar el comprobante sin clasificación.
  * A Pedido: el sistema no realiza ningún control, permitiendo el ingreso de una clasificación para el comprobante.



Permite referenciar comprobantes: usted puede indicar mediante este parámetro cómo controlar los comprobantes que sean referenciados con diferentes clasificaciones, en los diferentes procesos: Emisión de cotizaciones, Ingreso de pedidos, Facturación, Emisión de remitos, Ingreso de nota de débito e Ingreso de nota de crédito.  
Los controles pueden ser:

  * Con diferente clasificación (flexible): active este parámetro para referenciar sin restricciones comprobantes con diferente clasificación (en encabezado y renglones). En caso de coincidir todas las clasificaciones, se propondrá la misma en el comprobante a generar. Caso contrario, se propondrá la clasificación definida como habitual.
  * Sólo cuando tengan la misma clasificación (estricto): active este parámetro para respetar las clasificaciones, tanto de los encabezados como de los renglones de los comprobantes que se referencien. El sistema controlará que todos los encabezados tengan la misma clasificación y respetará las clasificaciones de los artículos, trasladando las mismas en el comprobante a generar. Este parámetro es de utilidad para generar comprobantes con las mismas clasificaciones que los comprobantes referenciados.
  * Respetando clasificación de artículos: active este parámetro para respetar las clasificaciones de los renglones de todos los comprobantes que se referencien. El sistema permitirá referenciar comprobantes con diferentes clasificaciones en el encabezado y trasladando solamente la clasificación de cada artículo. En caso de coincidir las clasificaciones de los encabezados, se propondrá la misma en el comprobante a generar, caso contrario se propondrá la clasificación definida como habitual.



Más información:

Para poder trasladar las clasificaciones de los comprobantes, el sistema validará que las mismas estén habilitadas para el comprobante a generar y que estén vigentes. Si requiere clasificar los recibos de cobranzas y usa [Tango Cobranzas](?p=12425), el sistema también validará que todas las [configuraciones para cobranzas masivas](https://ayudas.axoft.com/24ar/configcobranzamasiva_gv) con dicho origen, tengan definidas una clasificación. Tenga en cuenta que la clasificación de los artículos será una condición más para agrupar los mismos. Para más información, consulte Agrupa los artículos de los remitos o pedidos. 

##### Agrupa los artículos de los remitos o pedidos

Si seleccionó varios remitos o pedidos, es posible indicar a través de un parámetro configurado en Perfiles de facturación, que se acumulen en un mismo renglón todos los ítems que correspondan a igual código de artículo, sumando las cantidades.  
De esta manera se reflejará en la factura, un solo renglón por cada artículo existente en los remitos o pedidos, con la cantidad acumulada.  
La condición para poder agrupar artículos es que tengan igual código, precio, depósito, unidad de medida, bonificación y clasificación.  
Al agrupar los artículos, tenga en cuenta las siguientes consideraciones: 

  * Todos los números de serie o partida ingresados en distintos comprobantes, se asociarán al artículo agrupado respectivo.
  * Puede eliminar de la factura, aquellos artículos que no desea incluir. Utilice para ello, la tecla <F2>.
  * Es posible modificar las cantidades por otras menores a las propuestas.



Al agrupar artículos con descripciones adicionales ingresadas en los comprobantes referenciados, tenga en cuenta lo siguiente:

  * Si en el perfil de facturación configuró agrupar artículos y mantener las descripciones adicionales de cada uno de ellos, no se cargarán en la factura, los artículos agrupados en un mismo renglón. Sino que se cargará cada artículo con su descripción adicional y su cantidad correspondiente.
  * Si en el perfil de facturación configuró agrupar artículos y no mantener las descripciones adicionales de cada uno de ellos, éstas se ignorarán y se cargarán en la factura, los artículos agrupados en un mismo renglón.



Si en el perfil de facturación configura no agrupar los artículos, se exhibirán en pantalla, las líneas asociadas a cada artículo de los comprobantes referenciados (que aún no hayan sido facturadas). Estas líneas podrán modificarse (disminuir cantidades) o eliminarse, pulsando la tecla <F2>.  
Podrá agregar nuevos renglones al comprobante.  
Si factura sobre remitos, los nuevos artículos ingresados no podrán descargar stock, incluso utilizando la tecla de función <Alt + F6>, por lo tanto, la factura quedará pendiente de remitir (por los nuevos artículos ingresados).  
De un mismo comprobante de pedido o remito podrá emitir una o más facturas, es decir, que el sistema controla las cantidades pendientes de facturación y las va actualizando. Por lo tanto, siempre que haga referencia a un comprobante, se exhibirá sólo lo pendiente de facturar.

#### Parámetros para controlador fiscal

Configura datos adicionales: active este parámetro para habilitar la edición de las líneas que serán configuradas con variables de impresión, tanto para facturas como ticket-facturas, en todos los modelos de controladores e impresoras fiscales implementados en el sistema.  
A su vez, las líneas configuradas para el ítem serán impresas en los comprobantes remitos homologados, que emitan por un equipo fiscal desde el proceso [Emisión de remitos](https://ayudas.axoft.com/24ar/emisionremito_gv).  
Para la impresora fiscal EPSON LX-300 existen algunas limitaciones con respecto a la configuración de datos adicionales para el encabezado y pie, que dependen del tamaño de hoja configurado en la memoria fiscal. En los tamaños de hoja de 8 y 8 x 6 pulgadas, podrán configurar solamente las líneas 1 y 2 del encabezado. Para el resto de los tamaños, podrá configurar de la línea 1 a la 3 en el encabezado y de la línea 12 a la 13 en el pie.

__Nota

La configuración de líneas en los ítems es igual para todos los modelos.

Esto posibilitará que, en el momento de facturar, se impriman datos referente a la factura, como vendedor, depósito, etc.  
Tanto para la zona del encabezado, pie o ítems no es obligatorio configurar todas las líneas.  
Se indicará por línea hasta dos variables de impresión y un texto fijo opcional. Este último consta de una leyenda referente a los datos impresos en cada línea.  
En cualquier modelo de controlador fiscal y en la impresora fiscal EPSON LX-300F, el tamaño de cada línea del encabezado y pie será de 40 caracteres. En las impresoras fiscales HASAR 320F, HASAR 321F, HASAR 322F y HASAR 425F es de 50 caracteres. Todo dato que exceda estos tamaños será truncado.  
Se utilizan sólo algunas variables de impresión ya existentes para los .TYP, que se seleccionarán de una lista.  
Las líneas del encabezado y pie que se configuren con variables de impresión, no podrán ser utilizadas para cargar un dato fijo desde el proceso Operación para controladores fiscales debido a que se utiliza el mismo mecanismo para ingresar textos adicionales en el controlador o impresora fiscal.  
Si cumple con el Régimen de Sostenimiento e Inclusión Fiscal para Pequeños Contribuyentes, utilice la variable de impresión **@YM** para incluir la leyenda "Receptor del comprobante - Responsable Monotributo".  
Si se configuran variables de impresión para los ítems, se deshabilitará la tecla de función <F3> para el ingreso datos adicionales. Estos se cargarán en forma automática a través de las variables.  
Consulte en el tópico [Descripciones para los ítems](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv#descripcionitems) la cantidad de caracteres aceptados de acuerdo al modelo utilizado.  
Es aconsejable indicar que, cuantas más líneas se configuren con datos, mayor será el tiempo que lleve un comprobante en generarse, ya que estos datos variables deben ser enviados al inicio de cada comprobante, y borrados después de generarlo para dejar el encabezado y pie sin datos para las siguientes facturas que se generen o para cualquier otro comprobante no fiscal como Cierre X, Z o auditoría.

Imprime formas de pago: active este parámetro para detallar en el pie del comprobante fiscal las diferentes formas de pago que se realicen con la condición de venta utilizada.  
Si no posee el módulo Tesorería, es importante también que mantenga activo este parámetro para que se imprima la condición de venta utilizada como un medio de pago.  
Consulte la cantidad de formas de pago admitida para su modelo en el tópico [Consideraciones especiales para controladores e impresoras fiscales](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv#considespeccontrimpfisc).

Utiliza apertura de cajón: active este parámetro para que después de emitir cada comprobante se envíe un comando para posibilitar la apertura del cajón de dinero.  
Este comando está disponible sólo para algunos modelos de controladores fiscales.

Equipos fiscales para incorporar cajón de dinero:

Los modelos que tienen la posibilidad de incorporar un cajón de dinero son:

  * EPSON TM-300AF+
  * EPSON TM-2000AF+
  * EPSON TM-2002AF+
  * EPSON TM-T285F
  * EPSON TM-U220A
  * EPSON TM-U950F
  * HASAR SMH/P-425F
  * HASAR SMH/P-435F
  * HASAR SMH/P-614F
  * HASAR SMH/P-615F
  * HASAR SMH/P-715F
  * HASAR SMH/P-PR4F
  * HASAR SMH/P-441F
  * NCR 3140
  * SAMSUNG SRP-250DF
  * SAMSUNG SRP-270DF



Activa grabación de auditoría fiscal: la activación de este campo permite registrar las anormalidades en los comprobantes emitidos por equipos fiscales.  
De esta manera, cuando realice el cierre Z correspondiente y consulte las diferencias en los importes facturados entre el equipo fiscal y el sistema, podrá obtener un detalle de los comprobantes no registrados en el sistema y su motivo. Para más información, consulte el proceso Operación de controladores fiscales.

Detalla composición de kits: tilde este parámetro para que se imprima en el ticket el detalle de los artículos que componen el kit.  
Si su controlador o impresora fiscal lo permite, este detalle también se imprime en notas de crédito y remitos.

#### Parámetros para comprobantes electrónicos

##### General

Comprobantes electrónicos (del mercado interno)

Si usted cumple con el régimen especial de emisión y almacenamiento electrónico de comprobantes originales ('A', 'B' o bien, 'C' para Monotributistas), ingrese su Fecha de incorporación.  
Sólo si usted abandona el cumplimiento del régimen indicado deberá ingresar la Fecha de exclusión.

Webservices a utilizar: a continuación, se indican las opciones disponibles.

  * Si usted emite comprobantes electrónicos 'A' y/o 'B', elija la Versión 0 como Webservices a utilizar (vigente a partir del 01 de Julio de 2011). Al seleccionar esta versión será necesario asignar códigos AFIP a las alícuotas, monedas y percepciones definibles antes de facturar.
  * Si usted es Monotributista y cumple con la RG 3067 para la emisión de comprobantes electrónicos 'C', elija la Versión 2 como Webservices a utilizar.
  * Si usted fue notificado por la Administración Federal de Ingresos Públicos respecto de su inclusión en el régimen de emisión de comprobantes electrónicos mediante nota inscripta por el juez administrativo competente, el webservice a utilizar es el correspondiente a la opción 'Notificación Juez'.
  * Si usted cumple con la RG 2557/09 para la emisión de comprobantes electrónicos con aplicación de bonos fiscales electrónicos (según Decreto Nº 2316/08), el webservice a utilizar lo determina el talonario asociado al comprobante electrónico.



Sin embargo, elija un Webservice de referencia, teniendo en cuenta las siguientes consideraciones:

  1. Si usted cumple sólo con la RG 2557/09 para la emisión de comprobantes electrónicos del mercado interno y la utilización de los bonos fiscales electrónicos, elija la opción 'Versión 2'.  
Los comprobantes electrónicos originales que respaldan las operaciones sujetas al régimen de incentivo para las empresas productoras de bienes de capital, sus partes y accesorios, deben emitirse en los términos de la Resolución General Nº 2485 y su modificación.
  2. Si usted también cumple con otro régimen de facturación, elija la opción correspondiente de webservice: 'Versión 2 - Versiones 1, 1.1 y 2 de webservices' o 'Notificación Juez'.  
De esta manera, podrá emitir comprobantes electrónicos bajo los 2 regímenes de facturación.



Más información:

La opción 'Versión 2' del parámetro Webservices a utilizar contempla las versiones 1, 1.1 y 2 de webservices según RG 2485 y también, la versión 1.1 de webservices para bonos fiscales electrónicos (BFE) según RG 2557.  
Usted puede cambiar la versión de webservices a utilizar sólo si no existen comprobantes electrónicos pendientes de obtener CAE, o si utiliza CAEA, si no existen comprobantes pendientes de presentación a AFIP.

Indicador de servicio: usted puede parametrizar la edición del indicador de servicio o bien, ocultar su ingreso en los procesos de facturación (facturas, notas de débito y notas de crédito). Si este dato no se exhibe en pantalla, defina el valor del indicador a tener en cuenta. Las opciones posibles son: productos, servicios o productos y servicios. Si el valor elegido es '2' o '3', el sistema asume que la empresa es prestadora de servicios y deberá ingresar, además, el período del servicio facturado (mes anterior, mes completo o mes siguiente).  
Este dato no es solicitado si usted utiliza bonos fiscales electrónicos (RG 2557/09).

Comprobantes electrónicos (del mercado exterior)

Si usted cumple con el régimen especial de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación, complete los datos que se mencionan a continuación.

Fecha de incorporación: indique la fecha de incorporación al régimen de facturación electrónica para operaciones de exportación.

Fecha de exclusión: complete esta fecha sólo si usted abandona el cumplimiento del régimen indicado.

Idioma del comprobante: elija el idioma en el que se confeccionarán los comprobantes de exportación (facturas, notas de crédito y notas de débito).  
Las opciones posibles son: 'Español', 'Inglés' o 'Portugués'. Por defecto, el sistema considera el español como idioma de todos los comprobantes de exportación.

En comprobantes electrónicos del mercado interno para los que se debe informar el detalle de las operaciones (versión 'Notificación Juez') y en comprobantes del mercado exterior, el sistema solicitará la configuración de los siguientes parámetros:

Detalle del comprobante: elija si la descripción a considerar es la ingresada en cada artículo, o la definida en el sinónimo del artículo.

Por defecto, el sistema considera la descripción ingresada en cada artículo desde el proceso Artículos del módulo Stock.

Incluye comentarios de los artículos: indique si en la descripción del producto a informar a la AFIP se incluyen los comentarios ingresados para cada artículo desde el proceso Artículos del módulo Stock.  
Por defecto, no se incluyen los comentarios de los artículos.

Tenga en cuenta que, si existen comprobantes electrónicos de exportación rechazados en el administrador de comprobantes, estos campos aparecerán deshabilitados.

Prestación de servicios

Si la actividad de su empresa se relaciona con la prestación de servicios, active el parámetro Es empresa prestadora de servicios e indique la modalidad a considerar para el cálculo de las fechas del período a procesar ('Mes anterior', 'Mes completo' o actual, 'Mes siguiente').  
Esta información puede ser modificada desde los procesos de facturación.

Almacenamiento de comprobantes

Directorio: ingrese la ruta en la que desea guardar los archivos generados en la facturación o en el administrador de comprobantes electrónicos.

Subdirectorio: mediante este parámetro podrá seleccionar la estructura de directorios, a partir del directorio establecido anteriormente, en la que se guardarán los comprobantes electrónicos.  
Valores posibles de selección:

  * **CC:** Cliente  
(Ejemplo: UbicaciónEscritaEnElCampoAnteriorCodigoClienteTipoyNroComprobante)
  * **CO:** Comprobante  
(Ejemplo: UbicaciónEscritaEnElCampoAnteriorComprobante)
  * **TA:** Tipo de Archivo  
(Ejemplo: UbicaciónEscritaEnElCampoAnteriorPDF y UbicaciónEscritaEnElCampoAnteriorOtrosComprobante)



El valor por defecto es 'CC'.

##### Otras resoluciones

Resoluciones AFIP - Regímenes específicos - Reemplazo de regímenes específicos

Defina si presenta información adicional requerida por AFIP. Tilde esta opción si alguna de sus actividades se corresponde con alguna de las comprendidas en los alcances de la normativa correspondiente a la RG 3749 o la RG 4004 - E.  
Para más información, consulte la sección Resoluciones AFIP - Reemplazo de regímenes informativos de la [Guía de implementación sobre comprobantes electrónicos](?p=26548).

Valores por defecto

Defina la información predeterminada para Actividad habitual a informar y Tipo de actividad habitual.

RG 3971 - Reintegro de IVA a turistas del extranjero

Genera información RG 3971: tilde esta opción si usted emite comprobantes electrónicos de turismo clase 'T' (según RG 3971).  
Para más información consulte [Generar comprobantes electrónicos T](?p=18616).

Ley 27440 - Factura de crédito electrónica

CBU del emisor: ingrese la CBU requerida por la ley 27440 para generar comprobantes de crédito electrónicos.

Informa opción de transmisión: tilde este parámetro cuando entre en vigencia la Resolución 4919/2021, para informar a AFIP a quién transmitirá cada factura de crédito electrónica (ADC - Agente de Depósito Colectivo o bien, SCA - Sistema de Circulación Abierta).  
Según esta resolución, a partir del 01 de Abril del 2021, en cada factura de crédito electrónica que emita deberá informar la opción de transmisión elegida. **De no hacerlo, el comprobante electrónico será rechazado**.  
Para más información consulte en la [Guía de implementación sobre comprobantes electrónicos](?p=26548) el apartado [Consideraciones para la generación de Factura de crédito electrónica MiPyME (Ley 27440)](?p=26876/#consideraciones-para-la-generacion-de-factura-de-credito-electronica-mipyme-ley-27440).

RG 4480 - Exportación Simplificada

Inscripto en el régimen de Exportación Simplificada: tilde este parámetro si cumple con el Régimen de exportación simplificado o "Exporta Simple" (Resolución 4480/2019), que facilita las operaciones de exportación de pequeñas y medianas empresas, reduciendo los costos de exportación.  
Este parámetro estará habilitado si se cumplen las siguientes condiciones:

  1. La categoría de IVA de la empresa es 'RI' - Responsable Inscripto o 'RS' - Responsable Monotributista.
  2. La empresa emite comprobantes electrónicos del mercado exterior (clase 'E').



Vinculación de comprobantes electrónicos con remitos electrónicos

Informa remitos electrónicos según la RG 5259: tilde esta opción si usted debe informar remitos electrónicos al emitir comprobantes que respalden operaciones de venta de carne y subproductos derivados de la faena de hacienda de las especies bovina/bubalina (según RG 5259).  
Para más información consulte [Guía de implementación RG 5259](?p=14650).

Informa remitos electrónicos según la RG 5264: tilde esta opción si usted debe informar remitos electrónicos al emitir comprobantes que respalden operaciones de venta de harinas y/o subproductos derivados de la molienda de trigo (según RG 5264).  
Para más información consulte [Guía de implementación RG 5264](?p=27065).

##### Puesta a disposición

Dentro de este apartado se desprenden dos solapas que le permiten seleccionar la forma de puesta a disposición de sus comprobantes electrónicos.

Publicación en Tango nexo

Presionando el botón "Publicar en Tango nexo", se abrirá un asistente que le indicará los pasos necesarios para publicar la información de su sistema Tango en la nube.

Envío por correo electrónico

Se encuentran los campos que necesita configurar para el envío de sus comprobantes electrónicos vía e-mail.

Más información:

Tenga en cuenta que, si su empresa usa [Tango Cobranzas](?p=12425), el comprobante tiene una cuota, el cliente no está inhabilitado para Tango Cobranzas y no tiene cláusula moneda extranjera, al final del correo electrónico se podría agregar automáticamente un link de pago. Para más información, consulte la [Guía de implementación sobre Tango Cobranzas](?p=27438).

##### Archivos PDF

En este apartado tiene la posibilidad de definir aspectos relacionados con la generación y el almacenamiento de los comprobantes electrónicos en formato PDF.

Incluir fuentes en el archivo: permite incluir las fuentes usadas dentro del archivo, lo que asegura que el texto se vea con la misma fuente en cualquier dispositivo. Se recomienda habilitar la opción si los archivos serán abiertos en dispositivos móviles. Tenga en cuenta que el tamaño del archivo se verá incrementado.

Guardar el archivo en la base de datos: activando este parámetro se almacenará el archivo PDF generado. A partir de ese momento siempre se leerá dicho archivo, en vez de regenerarlo cada vez que se desee verlo. 

Depurar los archivos almacenados en la base de datos: permite indicar si se desea limpiar la tabla que almacena los comprobantes en formato PDF.

Conservar los archivos por (días): indique la cantidad de días que desee mantener cada archivo en la base de datos. La cantidad mínima permitida es 1.

Guardar archivos depurados en: permite indicar una carpeta dentro del disco duro donde serán copiados los archivos al ser depurados de la base de datos. Deje en blanco este campo si no desea guardar los archivos una vez eliminados de la base de datos.

#### Parámetros para padrones

En esta sección usted debe parametrizar los valores posibles y datos necesarios para el uso de padrones de AGIP y ARBA.

##### Padrones AGIP

Para todos los padrones: defina si actualiza las alícuotas de los clientes de acuerdo a la provincia de la dirección de entrega o por el CUIT del cliente en forma independiente de la provincia.

Solo régimen general: defina los parámetros para el padrón de régimen general de AGIP.

Provincia asociada para padrón régimen general: seleccione la provincia para asociar al padrón régimen general de AGIP.  
La provincia asociada es necesaria en operaciones alcanzadas por el régimen general con contribuyentes pasibles de percepción no incluidos en el archivo del padrón de régimen general de AGIP (RG 421/16).

__Nota

Si usted no selecciona una provincia asociada o la elimina, no se realizará la asignación de alícuota general a clientes no incluidos en el padrón.

Asigna alícuota general a clientes no incluidos en el padrón: defina si actualiza la alícuota general en los clientes no incluidos dentro del padrón de régimen general. Seleccione una opción según los criterios, ya sea direcciones de entrega con igual provincia a la provincia asociada al padrón o en todas las direcciones de entrega independientemente de la provincia asociada.

__Nota

Al eliminar la provincia asociada y luego actualizar las alícuotas en los clientes (en aquellos que ya tuvieran la alícuota general asignada con anterioridad) el proceso de actualización las eliminará dado que no existe una provincia asociada en la empresa.

##### Padrones ARBA

Actualiza alícuotas según: defina si actualiza las alícuotas de los clientes de acuerdo a la provincia de cada dirección de entrega o por el CUIT del cliente en forma independiente de la provincia.

Provincia asociada al padrón: indique la provincia que corresponda con el padrón de ARBA. Este campo es obligatorio si definió que se actualicen alícuotas según la provincia del cliente o dirección de entrega.

Clientes fuera del padrón (solo disponible utilizando el circuito vía Percepciones definibles)  


Asigna alícuota a clientes no incluidos en el padrón: seleccione esta opción si necesita definir una alícuota a incorporar masivamente, a los clientes que estén fuera del padrón de ARBA.

Actualiza alícuotas según: defina si actualiza las alícuotas de los clientes que no están en el padrón, de acuerdo a la provincia de cada dirección de entrega o tomando en cuenta el CUIT del cliente -en forma independiente de la provincia-.

Código de percepción: seleccione del listado la percepción de ingresos brutos de jurisdicción provincial que desea agregar a los clientes que no existan en el padrón de ARBA.

Código alícuota: seleccione del listado la alícuota de percepción que desea agregar a los clientes que no estén incluidos en el padrón de ARBA, es decir, aquella alícuota de percepción que tiene indicado en el campo Padrón la opción 'Sin Padrón', en la solapa Alícuotas del proceso [Percepciones](?p=19407).

#### Observaciones

Esta sección está disponible para el ingreso opcional de un texto o comentario.

##### Contenidos relacionados

  * [Videos sobre parámetros de Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/parametros_gv_vid/)
