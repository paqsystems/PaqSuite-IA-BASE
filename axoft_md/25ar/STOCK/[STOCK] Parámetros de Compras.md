# Parámetros de Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_series_st/?p=14676/

## Contenido

# Parámetros de Compras

Mediante este proceso se define una serie de parámetros y valores iniciales, que permiten adaptar el comportamiento del sistema a las necesidades de cada empresa en particular.

Detallamos a continuación, los parámetros de compras a aplicar.

#### Principal

General

Ingreso obligatorio de CUIT: defina si es obligatorio el ingreso de un CUIT válido durante el alta o modificación de proveedores.

Obtiene automáticamente datos del AFIP al ingresar CUIT o identificación en el alta de proveedores: al activar este parámetro se obtienen los datos del proveedor suministrados por AFIP.

Actualiza automáticamente datos del AFIP al modificar proveedores: al activar este parámetro se consultarán los datos suministrados por AFIP para actualizarlos al momento de guardar los cambios. Además, se actualizarán los códigos de retenciones según los padrones (Ciudad de Bs. As.) o el padrón de Rentas (Provincia de Bs. As.).  
Para más información sobre este tema consulte la [guía sobre actualización de alícuotas de IIBB según AGIP Bs.As.](?p=14406)

Verifica CUIT limitadas en el ingreso de comprobantes (RG AFIP 3832/16): mediante este parámetro, usted define al momento de generar una factura de compras necesita que el sistema consulte el estado de la CUIT del proveedor en los servidores de AFIP para detectar automáticamente CUIT limitadas.  
Los valores posibles a ingresar son los siguientes:

  * **Nunca:** no efectúa la consulta contra la AFIP.
  * **Siempre y confirma el ingreso:** efectúa la consulta contra la AFIP y si detecta que la CUIT se encuentra limitada muestra un mensaje permitiéndole decidir si continua con el ingreso del comprobante.
  * **Siempre y limita el ingreso:** efectúa la consulta contra la AFIP y si detecta que la CUIT se encuentra limitada no permite continuar con el ingreso del comprobante.



Depura solicitudes de precios: indique si desea activar el proceso de depuración, solo serán depurados aquellos archivos que estén dentro de la fecha de depuración.

Conserva solicitudes de precios por (meses): este campo permite establecer el número de meses que desea mantener los registros de solicitudes de precios realizados y en función a este valor se determina a partir de qué fecha se aplicará la depuración.

  * Para configurar la tarea de depuración debe hacerlo desde el Administrador | Servicios | Tareas de depuración.
  * Es importante aclarar que, una vez que la información sea depurada no se podrá recuperar.



Proveedores habituales

Código de proveedor: identifica en forma unívoca al proveedor a ingresar. Estos códigos pueden agruparse, como se describe en el proceso [Longitud de agrupaciones](https://ayudas.axoft.com/25ar/longitudagrupacion_cp2). Está compuesto por: código de familia, código de grupo y código de individuo. Los nombres de los códigos de familia y los códigos de grupo se definen en el proceso [Agrupaciones de proveedores](https://ayudas.axoft.com/25ar/agrupacionproveed_cp2). 

__Nota

El campo _Código_ de proveedor puede contener tanto números como letras o cualquier otro caracter. Tenga en cuenta que no es necesario ocupar todos los caracteres disponibles para el _código_ , pero sí debe respetar las ubicaciones de cada agrupación.

__Nota

Las agrupaciones permiten generar informes agrupados por familia / grupo.

Más información sobre codificación automática de proveedores...  
Con respecto al código de proveedor a asignar, es posible parametrizar si se aplica la codificación automática de proveedores.  
Si usted elige esta modalidad, al ingresar un nuevo proveedor, se genera automáticamente el código a asignar (de acuerdo a lo ingresado en el proceso Parámetros de Compras en el campo Próximo código de proveedor). En este caso, el código de proveedor generado no es editable.  
Si usted opta por no utilizar la codificación automática de proveedor, al registrar un nuevo proveedor, ingrese el código a asignar o bien, al menos un dígito y utilice la funcionalidad Próximo proveedor <F3>.

__Nota

Tenga en cuenta que para las altas de proveedores por API o **Excel** el funcionamiento es diferente. Para más información consulte el ítem [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp2).

Codificación de proveedores usando familias y grupos  
En el proceso [Agrupaciones de proveedores](https://ayudas.axoft.com/25ar/agrupacionproveed_cp2) se define lo siguiente:

  * Longitud de familia:1
  * Longitud de grupo:1



Automáticamente, y teniendo en cuenta que se asignan 6 dígitos para el código de proveedor, la longitud del individuo será 4, que resulta de: 6 - (1+1).  
En el proceso [Agrupaciones de proveedores](https://ayudas.axoft.com/25ar/agrupacionproveed_cp2) se define:

**Código** | **Título**  
---|---  
1 | Casas de artículos del hogar  
11 | Mayoristas  
12 | Minoristas  
  
Finalmente, en el proceso [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp2) ingresamos:

**Código** | **Razón Social**  
---|---  
110025 | Distribuidora Mayorista Roca  
110026 | El mundo de las heladeras  
120049 | Guillermo Rodríguez  
120050 | Ricardo Vázquez  
  
Los proveedores, entonces, quedan ordenados en orden jerárquico de la siguiente manera:

**1** | Casa de Artículos del Hogar |  |   
---|---|---|---  
**11** |  | **Mayoristas** |   
110025 |  |  | Distribuidora Mayorista Roca  
110026 |  |  | El Mundo de las Heladeras  
**12** |  | **Minoristas** |   
120049 |  |  | Guillermo Rodríguez  
120050 |  |  | Ricardo Vázquez  
  
El campo Código de proveedor puede contener tanto números como letras o cualquier otro carácter. En el ejemplo, se utilizan números para clarificar el concepto de agrupación.  
Tenga en cuenta que no es necesario ocupar todos los caracteres disponibles para el "código", pero sí debe respetar las ubicaciones de cada agrupación.

Permite alta de proveedores desde procesos: usted puede dar de alta nuevos proveedores desde los procesos de ingreso de comprobantes (órdenes de compras, facturas, créditos, débitos, remitos, pagos, composición inicial)  
Si no desea hacer uso de esta facilidad, con el fin de permitir las altas solo a los usuarios habilitados, no active este parámetro.

Clasifica proveedores en altas: si activa este parámetro, al dar de alta un proveedor en el sistema, el sistema solicitará su confirmación para clasificarlo en ese momento. Si confirma esta acción, se abre automáticamente el [clasificador de proveedores](https://ayudas.axoft.com/25ar/clasificadorproveedor_cp2).

Duplicación del tipo y Número de documento: mediante este parámetro configure el tipo de validación a aplicar en el caso de números repetidos para la combinación de tipo y número de documento.  
De esta manera, usted define si aplica un control flexible (habilita el ingreso de números repetidos, de utilidad para aquellas empresas que operan con proveedores con sucursales), un control estricto con el que no se permiten valores repetidos para la combinación de ambos campos; o bien, un control estricto (Solo CUIT) para estos campos solamente cuando el tipo de documento es 'CUIT'. Por defecto, se propone la opción 'Control flexible'.  
En el caso de clientes del exterior (si tienen asignado como Tipo y Número de documento, el CUIT de su país), no se aplica el control de duplicidad.  
Cabe aclarar que este control no se tiene en cuenta en proveedores ocasionales (con código '000000').

Escenarios de aplicación...  
El sistema tendrá en cuenta este parámetro al dar de alta un proveedor, en las siguientes situaciones:

  1. Desde el proceso [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp2).
  2. Mediante la tecla <F6> \- Alta de Proveedores desde otros procesos, tales como [Facturas](https://ayudas.axoft.com/25ar/comprobfactura_cp2).
  3. Al importar proveedores desde [Transferencias / Tablas generales / Proveedores](?p=11992) de los módulos Procesos generales o Central.
  4. Al importar [órdenes de compra](?p=9415), [remitos](?p=9418) y/o [comprobantes de facturación para la Gestión Central](?p=9412) del módulo Central.



Y también, al modificar o copiar los datos de un proveedor desde el proceso [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp2).  
Cabe aclarar que este control no se tiene en cuenta en proveedores ocasionales (con código '000000').

Proveedores habituales / ocasionales

Tipo de documento habitual: es el tipo de documento habitual a considerar para el proveedor (habitual u ocasional).

Provincia habitual: es la provincia a considerar por defecto para el proveedor (habitual y ocasional).

Soporte magnético 

DGI - CITI para proveedores ocasionales: para la generación del archivo DGI - CITI.  
Los comprobantes de proveedores tienen asignado un Tipo de operación habitual y una Clasificación de compra habitual. Estos valores pueden asignarse por proveedor. En este proceso, se indicarán los valores por defecto a sugerir para el caso de proveedores ocasionales.

RG 3685 / 4597 para proveedores ocasionales: necesario para generar los archivos informativos de Compras, que requiere la resolución general 3685 y la resolución general 4597 de AFIP.  
Los comprobantes de proveedores ocasionales requieren la asignación de un tipo de operación y un código de comprobante AFIP. Usted puede asignar los valores en este proceso. Al momento de ingresar el comprobante de un proveedor ocasional se indicarán estos datos como sugerencias.  
Para más información, consulte la [Guía sobre implementación RG 3685 - Régimen informativo de compras y ventas](?p=11914) o la [Guía de implementación sobre RG 4597 - Libro de IVA digital](?p=27842).

Genera información RG 1361, RG 1547 y RG 3665: si usted debe cumplir con estas resoluciones active este parámetro.  
Además podrá completar información adicional en la ficha del proveedor y durante el ingreso y modificación de comprobantes.

Genera información RG 3572 - Sujetos vinculados: si usted debe cumplir con el Régimen informativo de operaciones en el mercado interno - Sujetos Vinculados, active este parámetro.  
Para más información, consulte la [Guía sobre implementación RG 3572 - Sujetos vinculados](?p=11911).

Clasificar IVA en el ingreso de comprobantes: si usted desea clasificar las alicuotas de IVA en el ingreso de comprobantes, puede parametrizarlo con los siguientes valores para cada tipo de comprobante:

  * **Siempre:** al finalizar la carga de totales, el sistema pedirá que se ingresen las clasificaciones.
  * **Pregunta:** al finalizar la carga de totales, el sistema le consultará si desea clasificar las alicuotas
  * **Oculta:** el sistema no muestra la ventana de clasificación.



Siglas y Leyendas

Sigla para el Listado de IVA, sigla para la identificación tributaria, leyenda para moneda corriente, leyenda para moneda extranjera contable: el sistema prevé la posibilidad de parametrizar ciertos nombres que son propios del país donde se esté trabajando.

Longitud de agrupaciones del Proveedor

Los códigos de proveedor pueden ser divididos en tres agrupaciones: familia, grupo e individuo.  
Mediante este proceso, se definirá la longitud dentro del código que será asignada a la familia, al grupo y al individuo. En el caso de proveedor es de 6 dígitos. De esta manera, definiendo la cantidad de dígitos que se van a utilizar para la familia y para el grupo, automáticamente quedará definida la longitud del individuo.

Definición de longitud de agrupaciones:

Si se define:

  * Longitud de Familia: 1
  * Longitud de Grupo: 1



Automáticamente, la longitud del individuo será 4, que resulta de: 6 - (1 + 1).

Si usted no desea agrupar en familias y grupos, defina las longitudes respectivas en 0 (cero).

#### Impuestos

En esta sección usted debe parametrizar los valores posibles y datos necesarios para el cálculo de impuestos.

Impuestos para fletes e intereses: indica las tasas a utilizar en el cálculo del impuesto para estos conceptos. Por defecto, se propone la 'Tasa general'.

Valores por defecto para el cálculo de impuestos en el alta de proveedores: los valores ingresados en esta pantalla serán sugeridos en el alta de proveedores, siendo posible su modificación.  
Recomendamos ingresar los valores habituales, es decir, aquellos que más se repetirán en varios proveedores.  
Indique para cada uno de los impuestos, si se calcularán y si se discriminarán en los comprobantes. En la explicación del proceso [Proveedores](?p=14686) detallamos el uso de estos campos.  
Cabe recordar que el cálculo de impuestos en los comprobantes surgirá siempre de la combinación de las alícuotas ingresadas en los artículos con los parámetros del proveedor.

Títulos para leyendas en comprobantes de retenciones

Estos títulos se visualizan en la pantalla de retenciones del proceso [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp2).

#### Comprobantes

##### Generales

Utiliza solicitudes de compra: active este parámetro si desea utilizar los procesos correspondientes a solicitudes de compra.

Utiliza órdenes de compra: active este parámetro si desea utilizar los procesos correspondientes a órdenes de compra. Si su empresa no utiliza órdenes de compra, es conveniente no activar este parámetro.

Condiciones para la modificación: es posible activar este parámetro sin ningún inconveniente. Si desea desactivarlo, deberá cerrar todas las órdenes pendientes y realizar la depuración correspondiente.

__Nota

Usted puede administrar carpetas de importación en forma independiente a este parámetro.

Utiliza pagos masivos: active este parámetro para generar pagos masivos de comprobantes.

Utiliza textos predeterminados para la impresión de solicitudes, órdenes de compra y carpeta de importación: este parámetro indica si se utilizan los textos predeterminados para solicitudes de compra, órdenes de compra y carpetas de importación que se generan por el proceso [Textos para Comprobantes de Compra](https://ayudas.axoft.com/25ar/textocomprobcp_cp2).

Solicita sector en el ingreso de comprobantes: los sectores se asocian a los comprobantes de proveedores y permiten obtener informes agrupados. En este parámetro se indica si se desea asociar sectores en el momento de ingresar los comprobantes.

Facturas / notas de débito / notas de crédito

Encabezado

Edita número interno (minuta): el sistema asigna una numeración interna única para todos los comprobantes de proveedores (facturas, notas de crédito y débito). Este número de comprobante interno o minuta puede ser generado en forma automática (indicando que no se edita) o sugerido para ser modificado por el operador al ingresar el comprobante.

Próximo número: si no está activo el parámetro anterior, ingrese el número a partir del cual se asignará en forma automática a los comprobantes de proveedores como numeración interna.

Permite indicar si el comprobante se debe incluir en IVA compras: si parámetro esta activo permite que se edite en el ingreso de comprobantes el campo Incluye en Subdiario de IVA Compras. Además, puede configurar los valores predeterminados que serán utilizados en el ingreso de comprobantes de los siguientes datos:

  * Condición de compra: indique el tipo de edición del campo y el valor por defecto. Los valores posibles son 'Edita', 'Muestra' y 'Oculta'.
  * Vencimientos: indique el tipo de edición para la lista de vencimientos (cuotas) de los comprobantes. Los valores posibles son 'Edita', 'Muestra' y 'Oculta'.
  * Tipo de asiento: indique los valores por defecto para cada uno de los diferentes tipos de comprobantes (Facturas, Débitos y Créditos).  
Si este parámetro se encuentra en blanco, el sistema tomará los valores definidos en el proceso [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp2), en el [Tipo de Comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_cp2) o en [Tipo de Gasto](https://ayudas.axoft.com/25ar/tipogasto_cp2).  
Para más información sobre este tema, consulte Asignación de Tipo de Asiento.



Dependiendo su configuración podrán ser editados, consultados u ocultados desde la pantalla de ingreso de comprobantes.

Más información:

Se puede definir el tipo de asiento asociado a los comprobantes desde los distintos procesos:

  1. Actualización de Proveedores.
  2. Actualización de Tipos de Comprobante.
  3. Actualización de Tipos de Gasto.
  4. Actualización de Parámetros de Compras.



Al momento de ingresar un comprobante el campo Tipo de asiento se asignará en base a la detalle anterior.  
Por ejemplo, si el proveedor tiene un tipo de asiento asociado el sistema siempre propondrá el tipo de asiento asociado al proveedor, de lo contrario asignará el tipo de asiento asociado al comprobante y así sucesivamente

Cuerpo

Valida conceptos por proveedor: en los comprobantes en los que se ingresan renglones de conceptos, el sistema permite acceder a una lista de conceptos asociados al proveedor. Caso contrario, se accede a todos los conceptos ingresados en el sistema.  
Es importante tener en cuenta que si activa este parámetro e ingresa un código de concepto que no existe en la relación, el sistema emitirá un mensaje pero permitirá ingresar el concepto en el comprobante luego de su confirmación.

Valida artículos por proveedor: en los comprobantes en los que se ingresan renglones de artículos, el sistema permite acceder a una lista del archivo correspondiente.  
Si se utiliza la relación proveedor - artículo (asociación entre el código de proveedor y los artículos que provee), es posible realizar la consulta desde esta relación activando este parámetro. Si el parámetro no está activado, siempre se realizará la consulta sobre toda la lista de artículos.  
Si se ingresaron los artículos relacionados para cada proveedor, será conveniente que active este parámetro, para facilitar las búsquedas y realizar un mejor control de los códigos ingresados.  
Es importante tener en cuenta que si activa este parámetro e ingresa un código de artículo que no existe en la relación, el sistema emitirá un mensaje pero permitirá ingresar el artículo en el comprobante luego de su confirmación.

Permite alta de valores de escala desde procesos: active este parámetro para generar el alta de artículos con escala.  
Esta funcionalidad se encuentra disponible para el ingreso de factura, notas de débito, notas de crédito y remitos.

Actualiza precios de última compra: desde esta opción define si el sistema guarda para cada artículo el precio de última compra. Si la fecha contable del comprobante es menor a la última fecha registrada, el valor no será actualizado.

Actualiza precios de reposición: tilde este parámetro para que, al guardar los comprobantes, el precio de reposición de cada artículo presente en los mismos, sea actualizado.

Admite reingreso de series: tilde este parámetro para controlar que los series ingresados no hayan tenido movimientos en el sistema. Este parámetro es de utilidad cuando quiera evitar la generación de series "mellizos" o duplicados.

__Nota

Recuerde que por más que no active este parámetro, el sistema seguirá validando que el número de serie ingresado no exista en stock.

Si activa los parámetros que actualizan el precio de reposición y/o el precio de última compra durante el ingreso de comprobantes, también se guardará una auditoría de esa actualización que podrá ser consultada desde la consulta Live de Evolución de costos que se encuentra en el módulo Stock en la sección Valorización | Costos.  
La tabla de auditoría de precios para costos se podrá depurar desde el proceso Cierre e histórico que se encuentra en Procesos periódicos lel módulo Stock. Luego de realizar esta depuración la información de auditoría no estará disponible.

Asocia datos adjuntos: tilde este parámetro para asociar datos adjuntos en el ingreso de comprobantes.

Muestra comprobantes AFIP pendientes de registrar: active este parámetro para habilitar la consulta de Comprobantes de AFIP pendiente de registrar en el ingreso de facturas, notas de débito, y notas de crédito (quedando excluidas las facturas de importación y despachos). Cuando esta opción está activada permite visualizar la información de comprobantes registrados en la AFIP que se encuentren pendientes de registrar en el módulo Compras. Los comprobantes registrados en la AFIP deberán ser previamente ingresados desde el proceso Compras | Procesos periódicos | Mis comprobantes AFIP.  
Si utiliza perfiles para la registración de facturas de compras, adicionalmente debe habilitar el parámetro equivalente en los perfiles que considere necesarios para puedan acceder a la opción de menú.

Etiquetas para artículos

Defina los valores habituales correspondientes a la generación de etiquetas.

Modelo de impresión: defina la etiqueta que se utilizará para los artículos.

Lista de precios: defina la lista a utilizar para imprimir etiquetas del artículo, cuando desee incluir precios en la impresión.

Remitos

Valor habitual para la cantidad de artículos: mediante este parámetro usted puede indicar una cantidad de artículos por defecto a tener en cuenta en el proceso de [Ingreso de Remitos](https://ayudas.axoft.com/25ar/ingresoremito_cp2).

Imprime etiquetas: en este parámetro usted puede indicar si desea imprimir etiquetas desde el proceso [Remito](https://ayudas.axoft.com/25ar/ingresoremito_cp2).

##### Solicitudes de compra

Para utilizar el [circuito de solicitudes de compra](?p=14476), configure los siguientes parámetros, que serán considerados en el momento de ingresar una solicitud de compra y en su gestión posterior. Para más información, consulte el ítem [Circuito de solicitudes de compra](?p=14476).

Utiliza solicitudes de compra: active este parámetro en el caso de utilizar los procesos correspondientes a solicitudes de compra. Si desea desactivarlo, cierre todas las solicitudes pendientes y realice la depuración correspondiente.

Requiere Autorización: existen dos alternativas para la generación de una solicitud de compra, dependiendo de si utiliza el mecanismo de autorización antes de la emisión del comprobante. Si se activa este parámetro, luego de generar una solicitud de compra se procederá a autorizarla y finalmente a emitirla. Si no se activa, el proceso [Ingreso De Solicitudes de Compra](https://ayudas.axoft.com/25ar/solicitudcp_cp2) realiza en forma automática la autorización y emisión del comprobante. Este parámetro es modificable.

Talonario para solicitud: permite configurar el comportamiento y el talonario por defecto para el ingreso de una solicitud de compra.

Descripción para clasificación 1 y Descripción para clasificación 2: indica el texto descriptivo para las clasificaciones adicionales de una solicitud de compra. El valor de este campo se presenta en los diferentes procesos que utilizan las clasificaciones adicionales como referencia. Si el campo esta vacío, se desactiva el uso de la clasificación adicional en los procesos de [Solicitudes de compra](https://ayudas.axoft.com/25ar/solicp_cp2).

Sustituye artículos genéricos: para configurar la modalidad de reemplazo de un artículo genérico ingresado en una solicitud de compra, en el momento de cambiarlo por un artículo definitivo cuando se realiza la orden de compra. Si usted selecciona la opción 'Por Artículos Relacionados' solo podrá cambiar un artículo genérico por algún artículo contemplado en sus relaciones, caso contrario, podrá cambiarlo por cualquier artículo contenido en el archivo maestro.

Permite reemplazo de artículos: permite definir si un artículo pedido en una solicitud de compra puede ser reemplazado por otro artículo en el momento de generar la orden de compra.

Controla entrega de artículos sin stock: active este parámetro si desea que el sistema controle la existencia en stock de aquellos artículos destinados a cumplir con la solicitud de compras, en este caso se exhibe un mensaje de aviso y se solicita su confirmación; caso contrario no será posible entregar una cantidad mayor a la existente en stock.

Talonario para orden de compra: permite configurar el comportamiento y el talonario por defecto para la generación de ordenes de compra desde el proceso [Gestión de solicitudes](https://ayudas.axoft.com/25ar/solicpgestion_cp2).

Referencia solicitudes en orden de compra: este parámetro se utiliza para generar ordenes de compra en base a solicitudes de compra.

Agrupa artículos en orden de compra: permite determinar el comportamiento a aplicar cuando en la orden de compra se referencien varias solicitudes con artículos repetidos. Los artículos a agrupar serán aquellos que hayan sido ingresados con un mismo tipo de artículo, código, unidad de medida y precio sugerido.

Distribuye manualmente las cantidades en los comprobantes relacionados: si activa este parámetro, al referenciar varios comprobantes en una orden de compra, al agrupar artículos en el comprobante podrá distribuir en forma manual las cantidades a comprar o a ingresar de un artículo. Caso contrario, al modificar las cantidades propuestas para comprar o ingresar, se disminuirá la cantidad de los comprobantes relacionados más antiguos en forma automática.

Modalidad de traslado y agrupamiento de datos en gestión de solicitudes

Modalidad de agrupamiento en Gestión de solicitudes

Agrupa artículos iguales: el proceso [Gestión de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpgestion_cp2) fue concebido pensando en la necesidad de las empresas de consolidar los artículos solicitados por todos los sectores, a los efectos de poder agruparlos y realizar compras en forma conjunta, mas allá del origen del pedido interno.  
De este modo, si un mismo artículo fue solicitado en varias solicitudes distintas, usted podrá ver en el proceso de Gestión, un solo renglón para tal artículo, agrupando todas las solicitudes donde se lo pidió.  
En el caso de que el modo de agrupamiento no sea lo mas conveniente para sus necesidades, defina que 'No Agrupa artículos iguales'. Esta opción le permitirá ver en renglones separados lo que se pidió en cada solicitud.  
En el caso de optar por agruparlos, es posible que éstos provengan de solicitudes de compras que difieran en alguno de sus datos. Indique el comportamiento que tendrá el sistema cuando encuentre datos diferentes en las solicitudes que se consolidarán en el renglón.  
Es posible definir tal comportamiento, cuando las solicitudes difieran en el solicitante, el comprador, la sucursal, el primer proveedor sugerido, el sector o la clasificación.

**Ejemplo...**

Se ingresan tres solicitudes de compras:

**Tal y Nº de Solicitud** | **Tipo y código de artículo** | **Cantidad solicitada** | **Solicitante** | **Sector**  
---|---|---|---|---  
20 0001-00001528 | N 0200200328 | 8 | Andrea Diez | Administración  
20 0001-00001530 | N 0200200328 | 6 | Teresa Rofo | Administración  
20 0001-00001535 | N 0200200328 | 9 | Teresa Rofo | Atención al cliente  
  
En el caso de no agrupar artículos iguales, la visualización en _Gestión de solicitudes_ será la siguiente:

**Tipo y código de artículo** | **Cantidad a comprar**  
---|---  
N 0200200328 | 8  
N 0200200328 | 6  
N 0200200328 | 9  
  
Este ejemplo indica que se generarán tres renglones de detalle de ordenes de compra, brindando así la posibilidad de asignar cada renglón a un proveedor distinto, para generar distintas ordenes de compra, o a diferentes depósitos, dentro de una misma orden de compra, si esto fuera necesario.  
En el caso de agrupar artículos iguales, y definir que agrupa los renglones aún cuando difieran sus datos, la visualización será:

**Tipo y código de artículo** | **Cantidad a comprar**  
---|---  
N 0200200328 | 23  
  
En el caso de agrupar artículos iguales, y definir que no agrupa los renglones cuando difiera el solicitante, la visualización será:

**Tipo y código de artículo** | **Cantidad a comprar**  
---|---  
N 0200200328 | 8  
N 0200200328 | 15  
  
En este ejemplo, ud visualiza las 8 unidades solicitadas por Andrea Diez en un renglón, y las 15 unidades solicitadas por Teresa Rofo en el otro, independientemente del sector para el que se pidió la compra.  
En el caso de agrupar artículos iguales, y definir que no agrupa los renglones cuando difiera el sector, la visualización será:

**Tipo y código de artículo** | **Cantidad a comprar**  
---|---  
N 020020032 | 14  
N 0200200328 | 9  
  
En este ejemplo, usted visualiza las 14 unidades solicitadas para Administración y las 9 solicitadas para Atención al cliente, en renglón aparte. Podría generar una O/C para Administración y otra para Atención al cliente, si utliliza este desglose para información de centros de costos.

Traslado de datos a la orden de compra

Por medio de esta serie de parámetros es posible definir si algunos de los datos cargados en la solicitud de compra serán trasladados a la orden de compra al referenciarla. Este control se aplica a los siguientes datos: Plan de Entrega, Textos, Leyendas y Observaciones del Artículo, Comprador y Primer proveedor sugerido.  
Indique en Precio del artículo cual es el precio que desea trasladar hacia la orden de compra: si el precio sugerido por el solicitante, o el precio cotizado que se encuentre en primer lugar (el del primer proveedor sugerido)

__Nota

En el caso de seleccionar la modalidad 'Todas las solicitudes posibles', sólo serán incluidas en la orden de compra las leyendass, textos y observaciones que cuenten con lugar para ser agregadas, comenzando por la primer solicitud referenciada.

Importante:

En el caso de que usted haya configurado que agrupa los artículos aun cuando difieran el comprador o el primer proveedor sugerido, y su configuración indique que estos datos deben ser trasladados hacia la orden de compra, tenga presente que el dato al generar la orden de compra quedará en blanco si un mismo renglón incluye datos diferentes.  
Estos datos son obligatorios para la generación de una orden de compra, por lo que deberá indicar en el momento de generarlas un valor para ambos. Es posible definir un valor por defecto para los casos en que el dato haya quedado en blanco por valores diferentes, utilizando los [Perfiles para solicitud de compras](https://ayudas.axoft.com/25ar/perfsolicitudcp_cp2).

##### Órdenes de compra

Modifica órdenes de compra en estado autorizada o emitida: es posible activar este parámetro para realizar modificaciones en ordenes de compra que se encuentran autorizadas o que ya fueron emitidas. En caso de realizar modificaciones sobre órdenes de compras autorizadas, al confirmar la modificación pasan a estado generadas para que se vuelvan a autorizar.

Modifica el precio de órdenes de compra parcialmente facturadas: al activar este parámetro se permitirá modificar el precio de un ítem de una orden de compra, siempre que no haya sido totalmente facturada, aunque la orden se encuentre en estado 'Emitida', 'Emitida y Cerrada' o 'Cumplida'.

Emite al ingresar la orden de compra: al activar este parámetro y si no está activo el parámetro Utiliza el circuito de autorización, el proceso [Ingreso y modificación de órdenes de compra ](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2) realiza en forma automática la emisión del comprobante.

Permite imprimir desde modificación de órdenes de compra: la activación del parámetro permite la impresión de órdenes de compra, sin importar el estado en el que se encuentren.

Cantidad de copias sin valorizar al imprimir: en la impresión de órdenes de compra, es posible seleccionar la emisión de una o más copias sin importes, ingresando la cantidad en este campo.  
El sistema controlará este valor con el indicado en @COPIAS dentro del formulario de impresión, para determinar qué copias se emiten valorizadas y cuáles no.

**Ejemplo:**

@COPIAS=3  
Copias sin Valorizar = 1  
En este caso se emitirán valorizadas las 2 primeras copias y sin importes la última.

Utiliza el circuito de autorización: existen dos alternativas para la generación de órdenes de compra, dependiendo si desea utilizar un mecanismo de autorización antes de la emisión del comprobante. Si se activa este parámetro, luego de generar una orden de compra se procederá a autorizarla y finalmente emitirla. Si no se activa, el proceso [Ingreso y modificación de órdenes de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2) realiza en forma automática la autorización y emisión del comprobante, siempre que el parámetro Emite al generar la orden de compra se encuentra activo.

Importe a partir del cual requiere autorización: defina un importe mínimo que requiere ser aurorizado.

Ítems de la orden de compra que puede autorizar: podrá informar los ítems si previamente indicó que el modo de autorización de la orden de compra es por ítems.  
Desde el proceso [Ítems de autorización de orden de compra](https://ayudas.axoft.com/25ar/autorizordencp_cp2) ingrese cada ítem que conformará la lista de conceptos disponibles para ser autorizados.

**Ejemplo...  
**Se configura $5.000.000 como importe mínimo que requiere autorización.  
Se ingresan dos ítems que requieren autorización:

  * Importe total de la orden de compra cuando supera el importe mínimo.
  * Cantidad de artículos requiere autorización siempre.



Caso 1:  
Se ingresa una orden de compra por $10.000.000. La orden de compra queda en estado 'Ingresada'.  
Requiere autorización por Importe total, por haber superado el importe mínimo configurado.  
Pero también requiere autorización por Cantidad, porque se configuró que siempre requiere ser autorizada por cantidad.

Caso 2:  
Se ingresa una orden de compra por $3.000.000. La orden de compra queda en estado 'Ingresada'.  
No requiere autorización por el ítem Importe total, porque el total es menor al importe mínimo de autorización.  
Pero se debe autorizar por Cantidad, porque se configuró que siempre requiere ser autorizada por cantidad.

Otros temas

Sugiere el ingreso de textos / leyendas: al seleccionar estos parámetros el sistema queda posicionado en las solapas correspondientes de modo automático antes de grabar la orden de compra. Tenga en cuenta que, de todos modos, el ingreso de los datos no es obligatorio.  
Haciendo clic sobre las solapas, puede ingresar textos o leyendas cuando lo necesite, aún cuando los parámetros no estén chequeados.

##### Pagos

Permite reimprimir órdenes de pago: activando este parámetro, será posible reimprimir una orden de pago desde el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp2) con la tecla de función <Alt + F11>. Sólo será posible reimprimir las órdenes de pago generadas a partir de la versión 9.30.000 en adelante.

Utiliza distinto talonario para aceptación de facturas de crédito: el objetivo de este parámetro es el de permitir utilizar, para los comprobantes correspondientes a la aceptación de facturas de crédito, una numeración distinta a la usada en órdenes de pago.

Talonario habitual: seleccione el talonario por defecto para los comprobantes que corresponden a aceptación de facturas de crédito, en caso que no desee utilizar el mismo talonario de emisión de orden de pago.

Autorización de comprobantes para el pago

Requiere autorización: indique si los comprobantes (facturas, notas de débito y notas de crédito) de sus proveedores requieren autorización previa a su pago. Active al menos un tipo de comprobante a autorizar.  
Indique el [tipo de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_cp2) sujeto a autorización (facturas, notas de débito, notas de crédito) y el importe mínimo a autorizar para cada tipo de comprobante.

Modalidad: si está activo el parámetro anterior, elija la modalidad a aplicar en la autorización de los comprobantes. Es posible autorizar o desautorizar por comprobante o por cuota.

Comprobantes a autorizar: indique el [tipo de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_cp2) sujeto a autorización (facturas, notas de débito, notas de crédito) y el importe mínimo a autorizar para cada tipo de comprobante.  
Si cambia la Moneda de expresión importe mínimo y existen [perfiles de autorización de comprobantes de compras](?p=14679), se modificarán los importes máximos de los perfiles existentes. El sistema solicita su confirmación para realizar este cambio.

Orden de carga de datos

Orden de carga de datos: elija el orden de ingreso de datos más adecuado a su modo de operar. En el caso que prefiera ingresar en primer lugar los valores, marque Movimiento de tesorería / Comprobantes.

Método de imputación del comprobante

Modalidad: elija la modalidad de imputación de sus comprobantes al realizar el pago a sus proveedores. indique si el ingreso de los comprobantes a pagar se realiza de modo automático o manual (por orden de carga).  
Si elige la modalidad de imputación por orden de carga, usted debe ingresar los comprobantes a cancelar en el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp2), detallando individualmente el tipo y número de comprobante.  
Utilizando esta opción, los comprobantes se imputarán en el orden en que son ingresados. Se controla que el importe a imputar sea mayor a cero. En este caso, se aplica la siguiente validación: el importe del comprobante de crédito no debe superar el importe a pagar de la factura precedente. Si se realizara una imputación parcial, el importe pendiente puede imputarse a otra factura o puede dejarlo a cuenta para ser imputado posteriormente.  
Si configura la imputación automática y desde el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp2) activa la opción Carga automática, Tango le propondrá automáticamente los comprobantes pendientes.

Mostrar todos los comprobantes vencidos y los que vencerán dentro de: este parámetro propone un filtro para la carga automática de todos los comprobantes vencidos y los que vencerán dentro de un período de días determinado, por ejemplo; 7 días. Es posible modificar la cantidad de días propuesta desde una opción en el proceso Pagos.

Criterio para la asignación de comprobantes a pagar: en el caso que utilice la modalidad automática (en función del importe pagado) puede optar por el siguiente orden para considerar qué comprobantes se cancelan en primer lugar:

  * Con fechas de vencimiento más antiguas.
  * Con fechas de vencimiento más nuevas.
  * Con fechas de emisión más antiguas.
  * Con fechas de emisión más nuevas.



Incluye notas de crédito: tilde este parámetro para que Tango proponga las notas de crédito pendientes, en el momento de seleccionar automáticamente los comprobantes a pagar. (*)

Incluye notas de débito: tilde este parámetro para que Tango proponga las notas de débito pendientes, en el momento de seleccionar automáticamente los comprobantes a pagar. (*)

(*) En el caso de considerar las notas de crédito/débito, éstas se imputan a las facturas tomándolas en cuenta según su fecha de emisión y ordenadas según la prioridad para la asignación de comprobantes a pagar elegida.

Ante igual fecha, se asignan: en el caso de indicar que incluye tanto notas de crédito como de débito, indique el orden en que prefiere que se imputen las facturas correspondientes:

  * Primero las notas de débito.
  * Primero las notas de crédito.
  * Por orden de emisión.



Asignación de cuenta para la corrección de diferencias por redondeo

Código de cuenta: ingrese la cuenta de Tesorería donde se imputarán las diferencias por redondeo que podrían generarse al trabajar con proveedores con cláusula en moneda extranjera. Este ajuste será realizado en forma automática cuando el sistema detecte que se está intentando cancelar un comprobante en moneda extranjera y no pueda cancelarse en moneda corriente, debido a problemas de redondeo.

__Nota

En el caso de existir cambios en la cotización, los errores de redondeo son absorbidos por los comprobantes de diferencias de cambio a generar.

Otros temas

Sugiere leyendas: al seleccionar este parámetro Tango queda posicionado en la solapa correspondiente, de modo automático antes de grabar la orden de pago. Tenga en cuenta que, de todos modos, el ingreso de los datos no es obligatorio.

__Nota

Haciendo clic sobre la solapa, leyendas cuando lo necesite, incluso cuando los parámetros no estén chequeados.

Títulos para leyendas: este campo permite modificar el título de cada leyenda a ingresar en la orden de pago.

##### Pagos masivos

Requiere autorización: active este campo si necesita tener la instancia de aprobación de los pagos masivos ingresados, antes de efectivizar su pago. En este caso, los pagos masivos ingresados nacerán con el estado 'Ingresado', para que sean autorizados desde el proceso [Autorización de pagos masivos](https://ayudas.axoft.com/25ar/pagmasautoriz_cp2).

Tipo de numeración: seleccione la opción (manual o automática) para la numeración de los pagos que se realicen desde el proceso [Generación de pagos masivos](https://ayudas.axoft.com/25ar/pagmasgeneracion_cp2).

Próximo número: si utiliza numeración automática, ingrese el número desde el que se registrarán los pagos masivos. En el caso de numeración manual, este campo no es editable ya que el número del pago masivo será solicitado en el momento de su ingreso.

Medio de pago

Cuenta a debitar: indique la cuenta principal a debitar de tipo 'Otras' (del módulo Tesorería), donde se registrará el importe de cada orden de pago generada.

Medio de pago habitual: indique la cuenta habitual, de tipo 'Otras' o 'Banco' (del módulo Tesorería), que utilizará para registrar el egreso del importe del pago.

__Nota

Si parametrizó el cálculo automático de retenciones, es necesario que desde el proceso Códigos de retención defina la Cuenta de Tesorería defecto para cada retención. Caso contrario, se asignará el total del pago masivo a la cuenta configurada como Medio de pago habitual.

Emite cheques: si como Medio de Pago Habitual definió una cuenta de tipo 'Banco', indique si emitirá cheques o registrará solamente el importe (transferencia bancaria).

Cantidad de días: si emite cheques, indique la cantidad de días a considerar en el cálculo de la fecha de los cheques. En el momento del pago, el sistema obtiene la fecha del cheque sumando los días indicados en este campo a la fecha del pago. Si necesita que la fecha del cheque sea igual a la fecha del pago, ingrese cero como valor de este parámetro. Este dato puede ser modificado siempre que parametrice Edita datos de Tesorería = Sí.

Edita datos de Tesorería: active este parámetro si necesita modificar en el proceso [Generación del pago masivo](https://ayudas.axoft.com/25ar/pagmasgeneracion_cp2), las cuentas de Tesorería propuestas y los datos del cheque (si paga con una cuenta de tipo 'Banco').  
Tenga en cuenta que los datos que usted defina, serán tenidos en cuenta en el momento de generar el pago masivo, en dos situaciones:

  * En el caso que usted indique que va a generar el pago con un medio de pago general para todos los proveedores. El sistema propondrá lo ingresado en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) como un defecto, que podrá ser modificado si usted cuenta con permiso de edición.
  * En el caso que usted indique que va a generar el pago ingresando medios de pago específicos para cada proveedor, y cuente con algún proveedor que no los tenga definidos. El sistema propondrá, para quienes tengan los datos de fondo en blanco, lo ingresado en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) como un defecto.



Comprobantes con diferencias

Permite pagar comprobantes con diferencias: active este campo si necesita poder realizar pagos a comprobantes aun cuando los mismos presenten diferencias por cantidades recibidas o en los precios registrados entre su lista y la del proveedor. En este caso, se avisará mediante un mensaje que la diferencia existe, pero se permitirá incluir el comprobante para su pago.

Elimina diferencias al pagar: active este campo si desea que la diferencia de los comprobantes que ud está pagando, sea eliminada al momento de efectivizar el pago. Caso contrario, la diferencia quedara 'Resuelta', sin perder el historial.

##### Importaciones

Actualiza precios de última compra y reposición al generar costos: indique si el proceso de generación de costos de partidas importadas actualiza los precios de última compra y reposición.

Edita número de embarque: indique si es posible modificar el número de embarque propuesto por el sistema durante su ingreso.

Próximo número: indica cuál será el próximo número de embarque a registrar en el sistema.

Agrupa artículos iguales en embarque al referenciar carpetas: indique si al generar un embarque en referencia a varias carpetas se consolidan los artículos iguales en un mismo renglón.

##### Comprobantes de ajuste

En esta solapa usted podrá configurar los tipos de comprobantes que serán utilizados para generar comprobantes de ajustes internos desde el proceso [Generación de comprobantes de ajustes](https://ayudas.axoft.com/25ar/genercomprobajuste_cp2).  
Además será posible indicar si éstos generan asiento y su correspondiente modelo de asiento.

Tipos de comprobante: indique los tipos de comprobante a utilizar para la generación de débito y crédito en la cancelación de saldos y diferencia de cambio.

Genera asiento: indique si genera asiento. Por defecto, muestra lo configurado en la parametrización contable del tipo de comprobante.

Modelo de asiento: este parámetro se habilita si se encuentra activo el parámetro Genera asiento y permite seleccionar un modelo de asiento para ese tipo de comprobante.

#### Parámetros para datos contables

Acceda a configurar los siguientes parámetros contables si previamente configuró que integra con Contabilidad desde [Herramientas para integración contable](?p=11936).

  * Parametrización contable para proveedores ocasionales.
  * Modifica imputaciones contables en el ingreso de comprobantes.
  * Activa la impresión de imputaciones contables.
  * Verifica la existencia de las cuentas contables.
  * Respeta definición de tipos de asientos



Parametrización contable para proveedores ocasionales: si indica una Cuenta proveedor ocasional y Centro de costo proveedor ocasional, estos valores se considerarán por defecto cuando se ingresen datos de proveedores ocasionales.  
Al momento de ingresar el proveedor ocasional, si estos campos quedan sin especificarse, el asiento tomará la cuenta genérica asignada al valor 'TO' según la definición del tipo de asiento utilizado.

Modifica imputaciones contables en el ingreso de comprobantes: si activa este parámetro, el sistema permitirá modificar el asiento asociado a un comprobante de facturación (facturas, notas de crédito y notas de débito) en el momento de su ingreso. El asiento sugerido será el que corresponda al Tipo de Asiento indicado para el comprobante. Si no activa este parámetro, no será posible modificar el asiento en los procesos de ingreso, pero sí en el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modificomprob_cp2). Para más información, consulte el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_cp2) Respeta la definición de tipos de asiento.

Activa la impresión de imputaciones contables: active este parámetro si desea imprimir en los procesos de ingreso de comprobantes, las imputaciones contables y las apropiaciones por centros de costo asociadas.

Verifica la existencia de las cuentas contables: permite indicar si se validan las cuentas contables con el plan de cuentas de Tango Contabilidad en todos los procesos en los que se hace referencia a ellas. Si el parámetro no se activa, no se controlará la existencia de las cuentas contables, pudiéndose ingresar cualquier código, que será aceptado o rechazado en el momento de realizar el transporte de asientos desde el sistema contable.

Respeta la definición de tipos de asiento: este parámetro afecta los comprobantes que generan asiento contable. Indica si se respeta la configuración del tipo de asiento, tal cual como fue definida desde el proceso [Tipos de asiento](https://ayudas.axoft.com/25ar/tiposasiento_cp2).  
Si activa este parámetro, en el ingreso o en la modificación de comprobantes:

  * No se permitirá agregar líneas al asiento contable.
  * No será posible eliminar líneas del asiento contable.
  * No se podrá modificar los importes del asiento contable.
  * Se permitirá cambiar una cuenta por otra.
  * Se permitirá realizar la distribución de las cuentas por centro de costo.



Si no activa este parámetro pero está activo el parámetro Modifica Imputaciones Contables en el Ingreso de comprobantes, en el ingreso o en la modificación de comprobantes:

  * Se permitirá modificar el asiento contable en su totalidad.



Los parámetros Modifica imputaciones contables en el ingreso de comprobantes y Respeta la definición de tipos de asiento operan en forma conjunta. El primero indica si es posible modificar las imputaciones contables; en tanto que el segundo determina qué acción es posible realizar.

#### Controles

Asignación obligatoria de perfiles: defina si un usuario que no tiene un perfil asignado, puede ingresar a los procesos que utilizan perfiles en el módulo Compras.

Ingreso de comprobantes

Fecha de emisión y Fecha contable: puede indicar el comportamiento de ingreso para validar la edición de ambas fechas. El control se realiza en el caso de ingresar una fecha futura. Los valores posibles son: 'Control estricto' (no permite ingresarla), 'Control flexible' (permite ingresarla, pero exhibe un mensaje de confirmación) y 'No utiliza' (permite ingresarla), y sólo para Fecha contable es posible utilizar el valor Control estricto mes en curso', que sólo permite ingresar fechas comprendidas entre el primer y último día del mes en curso.  
El control de la Fecha de emisión además de ser aplicado a facturas, notas de débito y notas de crédito, se aplica también a los remitos de proveedores.

Asigna período de validez para el IVA: si activa este parámetro podrá controlar el ingreso de comprobantes con IVA en un determinado período.

Cantidad de meses: si asigna período de validez para IVA, ingrese el número de meses a considerar en la validación de los comprobantes con IVA.

Los parámetros anteriores actúan de la siguiente manera: al ingresar un comprobante, el sistema controla que el mes de la fecha contable del comprobante no exceda al valor que resulta de sumar el mes de la fecha de emisión del comprobante y el número indicado en el parámetro Cantidad de meses. En ese caso, se exhibe un mensaje de aviso y se solicita su confirmación.

__Nota

En la validación de comprobantes con IVA sólo se analiza el mes de cada una de las fechas.

**Ejemplo...**

En el proceso Parámetros de Compras, usted define:

  * Asigna período de validez para IVA: Sí
  * Cantidad de meses: 2



Al ingresar un comprobante con Fecha: 02/03/2026 y Fecha contable: 02/06/2026, el sistema exhibirá el mensaje: "La fecha contable excede el plazo máximo de validez de impuestos. ¿Confirma?". En este caso, el mes de la fecha contable (06) supera el valor 05, que surge de sumar 3 (mes de la fecha de emisión) + 2 (cantidad de meses).  
Si como fecha contable, usted indica una fecha comprendida en el rango 02/03/2026 al 31/05/2026, el sistema permitirá el ingreso del comprobante.

Admite números duplicados de comprobantes (RG 100/98 - 241/98): esta resolución establece que la numeración de los comprobantes preimpresos de tipo FAC, CRE y DEB y de tipo asociado A, B y E comenzará a partir del 00000001.  
Puede darse el caso que usted ya haya recibido un comprobante de un proveedor con la misma letra, sucursal y número; y que éste se encuentre aún en el sistema.  
Activando este parámetro, el sistema detectará la duplicidad y pedirá confirmación para ingresar el comprobante. Confirmando la opción se podrá ingresar el comprobante en el sistema, y será almacenado con una letra minúscula.  
Recuerde la existencia de letras minúsculas en los casos donde es necesario el ingreso del número de comprobante: [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp2), [Actualización de Facturas de Crédito](https://ayudas.axoft.com/25ar/factcredactualiza_cp2) y [Actualización de Retenciones](https://ayudas.axoft.com/25ar/actualretencion_cp2).

Solicita reingreso de número de comprobante y total en factura, notas de crédito y notas de débito y solicita reingreso de número de comprobante y total en remitos: estos parámetros permiten efectuar un control del ingreso de datos. Si activa los parámetros, al finalizar la carga de un comprobante (una vez confirmada la pantalla de totales), se solicita el reingreso del Número de Comprobante y el Total. De esta manera, no podrá continuar con la registración del comprobante hasta completar estos datos.

Inhabilita edición de subtotales: si activa este parámetro, se bloquea la edición de los importes de subtotales y netos de la pantalla de totales del comprobante. De esta manera no será posible modificar los importes calculados por el sistema. Cabe aclarar que son editables los importes relacionados con Fletes, Bonificación e Intereses.

#### Importación por AI

##### Carpeta de red

Habilita importación desde carpeta de red: habilite esta opción para recibir comprobantes desde la carpeta de red que configure.

Mover archivos ya procesados: habilite esta opción si desea mover los archivos ya procesados por la IA a otra carpeta.

##### Origen correo electrónico

Importar comprobantes desde correo electrónico: habilite este campo si desea seleccionar el correo electrónico como uno de los origines a recibir comprobantes de proveedores.

Mover comprobantes procesados a subcarpeta de correo electrónico: habilite esta opción para mover los comprobantes procesados que ingresan mediante correo.

Carpeta del buzón de correo: se habilitará al habilitar el campo anterior.

#### Comprobantes con diferencia

Controla comprobantes con diferencias: indique si realiza este control de los comprobantes. Usted puede optar por aplicar un 'Control estricto', 'Control flexible' o bien, no utilizarlo ('No controla').  
Defina para cada comprobante el tipo de diferencia a controlar: Factura / Factura de Importación o Factura - Remito, Remito de proveedores.  
Los tipos de diferencias posibles de controlar son los siguientes:

  * Diferencia por cantidad: es la diferencia que se genera por haber recibido una factura de un proveedor por una cantidad mayor a la cantidad recepcionada.
  * Diferencia por precio: esta diferencia se genera por dos motivos: 
    * por haber recibido una factura o remito en la que el precio de uno o más artículos es mayor al precio definido en la lista de precios utilizada en el comprobante.
    * por haber recibido una factura o remito en la que la bonificación de uno o mas artículos es menor a la bonificación definida en la lista de precios utilizada en el comprobante



En la siguiente tabla se resume para cada comprobante, el tipo de diferencia posible de controlar:

**Tipo de comprobante** | **A controlar**  
---|---  
Factura | Diferencias por precio  
Factura - remito | Diferencias por precio  
Factura - remito | Diferencias por cantidad  
Factura de Importación | Diferencias por precio  
Remito | Diferencia por cantidad  
  
Verifica desvíos de precios: defina si efectúa el control en la modificación de precios, teniendo en cuenta un desvío. Es posible llevar un control estricto, flexible o directamente no utilizarlo. Este parámetro se aplica en los comprobantes de factura - remito, factura sobre remito y factura de importación.  
Si Verifica desvío de precios, para el cálculo de la diferencia por precio se considerará el desvío configurado en la lista de precio.

Remite cantidades mayores a las facturadas: active este parámetro para que el sistema permita ingresar cantidades remitidas mayores a la facturada.  
Este control se puede configurar como 'Control estricto' (no se permite cantidades remitidas mayores a la facturada), 'Control flexible' (emite mensaje de advertencia) o 'No controla', y se aplica a los comprobantes de Factura - Remito y Remitos de proveedores.

Asume cantidad remitida igual a la facturada: si utiliza el control de diferencias en comprobantes, mediante este parámetro puede indicar el valor por defecto para la cantidad recibida en el ingreso de Facturas - Remito y Remitos de proveedores. Si activa este parámetro, la Cantidad recibida se completa con el valor ingresado en la columna cantidad del renglón de la factura, y en el caso del Remito la cantidad a facturar se completa con el valor ingresado en la cantidad del remito. Caso contrario, el valor propuesto para la cantidad recibida es cero.

##### Órdenes de pago / pagos masivos

Fecha igual a la del día: el comportamiento de este control es el de limitar el ingreso y la modificación de la fecha de emisión con respecto a la fecha del día.  
Controles posibles:

  * Control estricto: la fecha de emisión debe coincidir con la fecha del sistema para poder continuar con el proceso.
  * Control flexible: si la fecha de emisión no coincide con la del día, se exhibe un mensaje de confirmación para que usted decida si continúa o cancela el proceso.
  * No controla: en este caso es posible registrar el pago con cualquier fecha de emisión.



Además de este control existen otros controles aplicables a la fecha de órdenes de pago y pagos masivos. Estas son: fecha de cierre configurable desde el proceso [Fechas de cierre](?p=11865) en el módulo Procesos Generales y el control de fechas futuras desde el proceso [Parámetros de Tesorería](?p=10293) en el módulo de Tesorería.

#### Parámetros para comprobantes de referencia

Órdenes de compras

Permite referenciar solicitudes de compra: active esta opción para indicar si permite referenciar solicitudes de compras al ingresar una orden de compra.

Compra cantidad mayor a la solicitada: indique si permite comprar más de lo solicitado.

Agrupa artículos iguales: active esta opción para indicar si agrupa artículos iguales al referenciar varias solicitudes de compra.

Traslado de datos al referenciar solicitudes de compra: esta sección le permite controlar el traslado de los datos cargados en la solicitud hacia la orden de compra.

Ante disminución de cantidades en renglones que agrupen varios comprobantes, distribuye manualmente las cantidades en los comprobantes relacionados.

##### Factura - Remito y Remito

Configure el circuito a seguir para los comprobantes de remito, factura-remito y factura, indicando los comprobantes de referencia para cada uno. Esta configuración puede efectuarse a nivel general o particularmente para cada proveedor.

Comprobante de referencia (remito): indique cual va a ser el comportamiento del remito en cuanto al comprobante de referencia-.

  * Control estricto: es obligatorio que el remito haga referencia a una orden de compra o a una factura.
  * Control flexible: el remito puede hacer referencia a una factura, a una orden de compra o no tener referencia.
  * No controla: el remito no hace referencia a otros comprobantes.



Comprobante de referencia (factura - remito): indique cual va a ser el comportamiento de la factura-remito en cuanto al comprobante de referencia.

  * Control estricto: es obligatorio que la factura-remito haga referencia a una orden de compra.
  * Control flexible: la factura-remito puede hacer referencia a una orden de compra o no tener referencia.
  * No controla: la factura-remito no hace referencia a otros comprobantes.



Tipo de comprobante de referencia: tanto para remito como para factura-remito indique el tipo de comprobante de referencia cuando se configura que se realiza un control estricto o flexible sobre el comprobante de referencia.

__Nota

Tenga en cuenta que estos parámetros no define el comportamiento del circuito, sino que sólo es utilizado como un valor por defecto a asignar a cada proveedor. El comportamiento estará dado por el valor que en definitiva se asigne a cada proveedor en particular o el definido en el perfil de factura.

Permite recepcionar cantidades mayores a las pendientes: en los procesos de recepción de mercadería sobre órdenes de compra, el sistema realizará el control entre la cantidad recibida y la pendiente. Si se activa este parámetro se permitirá recibir cantidades mayores a las pendientes; en caso contrario no se permitirá el ingreso, lo que brinda un mayor control sobre las cantidades a recepcionar.

Recuerde que, en el caso que se agrupe en un renglón varias solicitudes no será posible recepcionar una cantidad mayor a la pendiente.

__Nota

Este parámetro no es aplicable a órdenes de importación.

##### Facturas

Permite el ingreso de facturas pendientes de remitir: existen dos procesos para el ingreso de facturas de proveedores. Uno por el que se ingresan comprobantes que actualizan Stock (factura - remito) y otro de facturas, en el que no existe movimiento de Stock (ya que éste se produce con el ingreso del remito).  
Si activa este parámetro, se permitirá el ingreso de facturas pendientes de remitir, las que podrán ser asociadas posteriormente por el proceso [Imputación de remitos](https://ayudas.axoft.com/25ar/factrefocremit_cp2).  
Si no utiliza esta modalidad (ingreso de la factura y luego del remito), no active el parámetro. En ese caso, la imputación de al menos un remito será obligatoria en el proceso [Ingreso de facturas](https://ayudas.axoft.com/25ar/factura1_carp_cp2).

Comprobante de referencia (factura): indique cual va a ser el comportamiento de la factura en cuanto al comprobante de referencia.

  * Control estricto: es obligatorio que la factura haga referencia a una orden de compra o a un remito.
  * Control flexible: la factura puede hacer referencia a una orden de compra, a un remito o no tener referencia.
  * No controla: la factura no hace referencia a otros comprobantes.



Tipo de comprobante de referencia: para factura indique el tipo de comprobante de referencia cuando se configura que se realiza un control estricto o flexible sobre el comprobante de referencia.

Traslado de datos al referenciar órdenes de compra: esta sección le permite controlar el traslado de los datos cargados en la orden de compra cuando se realice el ingreso de una factura o factura-remito.

Traslado de datos a la orden de compra: por medio de estos parámetros es posible definir si los datos cargados y referenciados en la orden de compra serán trasladados en las referencias del ingreso de facturas o factura-remito.  
Este control se aplica a los siguientes datos:

  * **Condición de compra:** indica si trasladada la condición de compra de la orden de compra, a la factura o factura-remito;
  * **Bonificación:** indica si trasladada la bonificación del encabezado de la orden de compra a la factura o factura-remito;
  * **Lista de precios:** indica si traslada la lista de precios de la orden de compra a la factura o factura-remito;
  * **Observaciones:** indica si traslada las observaciones de la orden de compra a la factura o factura-remito.



__Nota

Al ingresar una factura o factura-remito, se trasladarán los datos de referencia del encabezado de más de una orden de compra siempre y cuando los datos de las órdenes de compra coincidan entre sí. Sin embargo, si los datos de referencia del encabezado son distintos no trasladará ninguno.

__Nota

Tenga en cuenta que estos parámetros que indican la referencia del comprobante de factura no define su comportamiento, sino que sólo es utilizado como un valor por defecto a asignar a cada proveedor. El comportamiento estará dado por el valor que en definitiva se asigne a cada proveedor en particular o el definido en el perfil de factura.

Propone artículos recibidos al referenciar remitos: utilice este parámetro para definir el comportamiento que tendrá el sistema en el momento de ingresar una factura de compras, cuando se hace referencia a uno o varios remitos respecto a la modalidad de ingreso de los artículos.  
Los valores posibles son:

  * Si: asigne este valor para que el sistema sugiera los artículos ingresados en el o los remitos referenciados en el momento del ingresar del comprobante.
  * No: asigne este valor para que el sistema no le sugiera los artículos ingresados en el o los remitos referenciados en el momento del ingresar del comprobante. En este caso, usted debe ingresar el código de artículo, y el sistema validará que dicho código exista en los comprobantes referenciados.
  * A confirmar: al utilizar esta opción, toda vez que ingrese facturas en referencia a remitos, el sistema le consultará si desea que se propongan los artículos del comprobante referenciado.



Para mas detalle sobre su comportamiento, consulte [Ingreso de facturas](https://ayudas.axoft.com/25ar/factrefocremit_cp2).

Agrupa artículos de facturas en referencia a remitos: active esta opción para indicar si agrupa artículos iguales al referenciar varios remitos.

Ante una disminución de cantidades en renglones que agrupen varios comprobantes, distribuye manualmente las cantidades en los comprobantes relacionados: indique el comportamiento que va a tener la factura cuando se disminuya la cantidad a facturar al hacer referencia a varios remitos u órdenes de compra.

#### Comprobantes de referencia

Agrega artículos al referenciar órdenes de compra: en los procesos de recepción de mercaderías y facturas sobre órdenes de compra, el sistema realizará el control de los renglones. Si está activo este parámetro, el sistema permitirá agregar renglones a los ya definidos en la orden de compra.

Ingresa artículos manualmente al referenciar órdenes de compra (sólo factura-remito y factura): active este parámetro si desea que en el momento de ingresar una factura - remito o una factura en referencia a una orden de compra, el sistema no le sugiera los artículos ingresados en el comprobante referenciado, para que usted los tipee manualmente.

[/axcond_modulo] 

#### Parámetros para importación de comprobantes por AI

En esta sección defina los siguientes campos:

Adjunta documento original al comprobante: marque esta opción para adjuntar el documento original (PDF, JPG o PNG) al comprobante registrado. Luego podrá consultar estos datos adjuntos desde la ficha Live de facturas, créditos y débitos.

Descartar nuevos comprobantes si se encuentran registrados en Tango: marque esta opción para descartar automáticamente documentos que luego de ser procesados por la AI (y se obtenga el tipo, número y CUIT del proveedor) se descarten automáticamente en caso de ya encontrarse registrados en el sistema.

Carpeta de red

Habilita importación desde carpeta de red: marque esta opción para importar documentos de una carpeta de red para ser analizados con AI.

Carpeta de red para importar archivos: indique la carpeta a monitorear para buscar nuevos comprobantes. Tenga en cuenta que esta carpeta debe estar disponible para ser accedida desde el servidor, y por todos los usuarios a los que quiera permitirle subir nuevos documentos.

Nombre de la subcarpeta para archivos procesados: indique el nombre de la subcarpeta donde se ubicarán los documentos que ya hayan sido procesados.

Correo electrónico

Importar comprobantes desde correo electrónico: marque esta opción para importar documentos de una casilla de correo electrónico. Para que esta opción tenga efecto, usted debe configurar una casilla de Recepción de correos en el proceso [Parámetros de correo electrónico](?p=11965), en Procesos generales.

#### Parámetros para clasificación de comprobantes

Utiliza clasificación: active este parámetro si desea utilizar los códigos de clasificación para los comprobantes de ventas. Para más información consulte [Clasificación de comprobantes](?p=11840).

Leyenda para clasificación: puede ingresar un nombre descriptivo para todas las clasificaciones. El valor de este campo se visualiza en la pantalla de clasificaciones, en los diferentes procesos que la utilicen. También será posible imprimir este valor en los comprobantes.

Comprobantes a clasificar y su clasificación habitual: usted puede seleccionar aquellos comprobantes que desee clasificar indicando también un código de clasificación habitual para cada tipo de comprobante.

Clasifica comprobantes: usted puede controlar mediante este parámetro cómo clasificar los comprobantes.  
Los controles pueden ser:

  * Siempre: el sistema controla que cada vez que se genere un comprobante, éste sea clasificado antes de grabarlo.
  * A confirmar: el sistema solicita confirmación para grabar el comprobante sin clasificación.
  * A pedido: el sistema no realiza ningún control, permitiendo el ingreso de una clasificación para el comprobante.



Permite referenciar comprobantes: usted puede indicar mediante este parámetro cómo controlar los comprobantes que sean referenciados con diferentes clasificaciones, en los diferentes procesos (Ingreso de solicitudes, Órdenes de compra, Facturación, Notas de crédito, Notas de débito, Remitos).  
Los controles pueden ser:

  * Con diferente clasificación (Flexible): active este parámetro para referenciar sin restricciones comprobantes con diferente clasificación (en encabezado y renglones). En caso de coincidir todas las clasificaciones, se propondrá la misma en el comprobante a generar. Caso contrario, se propondrá la clasificación definida como habitual.
  * Sólo cuando tengan la misma clasificación (Estricto): active este parámetro para respetar las clasificaciones, tanto de los encabezados como de los renglones de los comprobantes que se referencien. El sistema controlará que todos los encabezados tengan la misma clasificación y respetará las clasificaciones de los artículos, trasladando las mismas en el comprobante a generar. Este parámetro es de utilidad para generar comprobantes con las mismas clasificaciones que los comprobantes referenciados.
  * Respetando clasificación de artículos: active este parámetro para respetar las clasificaciones de los renglones de todos los comprobantes que se referencien. El sistema permite referenciar comprobantes con diferentes clasificaciones en el encabezado y trasladando solamente la clasificación de cada artículo. En caso de coincidir las clasificaciones de los encabezados, se propondrá la misma en el comprobante a generar, caso contrario se propondrá la clasificación definida como habitual.



Para poder trasladar las clasificaciones de los comprobantes, el sistema validará que las mismas estén habilitadas para el comprobante a generar y que sean vigentes.

Tenga en cuenta que las clasificaciones de los artículos será una condición más para agrupar los mismos.  
Para más información consulte el tópico [Agrupa los artículos en Orden de Compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2). Si se referencia una o más solicitudes que contienen el mismo código de artículo con diferente clasificación, se mostrará un mensaje advirtiendo esta situación. Esto solo corresponde para el caso en que el ingreso de órdenes de compras esté configurado para que referencie comprobantes con diferente clasificación ('Flexible') o cuando tengan la misma clasificación ('Estricto').

#### Parámetros para retenciones

Cálculo Longitud de agrupaciones del Proveedor

IVA: indica si se utiliza el cálculo automático de retenciones de IVA (RG 3125 DGI).

Ganancias: indica si se utiliza el cálculo automático de retenciones de Impuesto a las Ganancias.

Calcula otras retenciones: si activa este parámetro, el sistema permite ingresar -en el momento del pago- un importe en forma manual o calcularlo en forma automática para cada uno de los códigos de retención definidos. Este importe podrá ser discriminado en el comprobante de pago e imputado contablemente en el módulo Tesorería.

Calcula retenciones de Ingresos Brutos: indica si se utiliza el cálculo automático de retenciones correspondientes a Ingresos Brutos en el momento del pago de los comprobantes.

Edita tipo de retención (CPR/RET): una vez que se confirmaron los medios de cancelación, muestra la ventana en la cual se detalla el tipo de comprobantes que se generarán (RET/CPR).

Permisos  


Códigos de retención: indica si el sistema permite modificar el código de una retención en el ingreso de un pago.

Edita importes: indica si el sistema permite modificar el importe de una retención en el ingreso de un pago.

Distribuye pago a cuenta: indica si permite distribuir el importe de un pago a cuenta entre las distintas bases de cálculo durante el ingreso de un pago. Por ejemplo: si realiza un pago a cuenta de $121.00 y tiene activo este parámetro, el sistema le permitirá descontar el importe de IVA según la alícuota especificada, de modo que la base para el cálculo de las retenciones sea de $100.00; de lo contrario, la base de cálculo siempre será igual al importe total del pago a cuenta.

Alíc. de IVA para pago a cuenta: al indicar que permite editar importes en un pago a cuenta, usted puede ingresar el porcentaje de IVA para la distribución de ese pago a cuenta.

Calcula retenciones a proveedores ocasionales: indica si permite calcular retenciones a proveedores ocasionales. En el caso de retenciones con acumulados, el proceso acumulará por tipo y numero de CUIT/CUIL.

Clasificación por defecto en el alta de proveedores habituales y ocasionales: permite definir la clasificación de retención que se asignará automáticamente al dar de alta nuevos proveedores, ya sean habituales u ocasionales.  
Este valor se asigna como predeterminado cuando el proveedor tiene habilitada la opción Aplica retenciones en los pagos, pudiendo ser modificado manualmente en cada caso.  
Dicha clasificación determina la base de cálculo a utilizar en retenciones de tipo 'Otras'. Para más información consulte la[ guía de implementación sobre bases de cálculo para retenciones tipo Otras](?p=16557).

Datos comprobantes de retención

Corresponde a una serie de campos a imprimir en los comprobantes de retención. Los datos a ingresar son los siguientes: Razón Social de la Empresa, Domicilio, Localidad, CUIT, Número de Ingresos Brutos, Apellido y Nombre Firmante de comprobantes de retenciones, Cargo.

Jurisdicciones de ingresos brutos

Se configuran las numeraciones, en forma independiente por jurisdicción, para los comprobantes de retención de ingresos brutos que se generen (conforme a la Resolución N° 533- SH y F-2000 de la Dirección General de Rentas de la ciudad de Buenos Aires).  
Si indica el talonario para cada jurisdicción, en el momento de generar el comprobante no se tendrá en cuenta la numeración del talonario definido. El sistema tomará de esta tabla, de acuerdo a la Provincia asignada al proveedor, el talonario y su Próximo Número a Emitir.

Jurisdicción: indica cada una de las provincias o jurisdicciones que intervendrán en la generación de comprobantes de retención con numeraciones independientes.

__Nota

En caso de aplicar esta resolución, ingrese todas las jurisdicciones de los proveedores a los que se les practica retención de IB.

Nro. de agente de retención: este campo es de ingreso obligatorio si se desea imprimir en el comprobante de retención, el número de agente de retención para la Provincia indicada en el proveedor.

Talonario: ingrese el talonario a utilizar en la emisión del comprobante de retención para la Provincia indicada en el proveedor. Para mantener una única numeración en los comprobantes de retención de Ingresos Brutos o si no necesita aplicar la resolución mencionada, la tabla anterior debe permanecer sin datos.

##### Retenciones ARBA A122R

Esta solapa permite configurar los parámetros necesarios para operar como Agente de Retención de Ingresos Brutos ARBA bajo el régimen A-122R, incluyendo la definición de actividades y la conexión con el servicio web de ARBA.  
Este régimen implica la generación y presentación de comprobantes de retención y declaraciones juradas mediante los servicios de ARBA.

RN 22/2025 - Agente de retención IIBB ARBA A122R: indica que la empresa actúa como agente de retención bajo este régimen. Al activarlo se habilitan las funcionalidades asociadas a A122R.

Actividades para clasificación A122R: permite definir las actividades utilizadas en la generación de retenciones.  
Se utilizan en:

  * Declaraciones juradas.
  * Generación de retenciones.
  * Procesos en línea con ARBA.
  * Generación de Archivo – ARBA A-122R – Retenciones por lote



La actividad marcada como habitual se utiliza por defecto.

Servicio ARBA en línea

Permite configurar la conexión con ARBA.

  * **Activar servicio:** habilita la integración con ARBA.
  * **Método de conexión:**
    * **En línea:** procesa las retenciones mediante el servicio de ARBA en el proceso que genera la retención.
    * **Diferido:** permite procesar las retenciones posteriormente desde Compras e Importaciones | Cuentas Corrientes | Administrador de retenciones ARBA.
  * **CUIT:** correspondiente al agente.
  * **Clave CIT:** clave de acceso a la página de ARBA.
  * **Verificar conexión:** valida los datos ingresados.



Consideraciones:

  * Es necesario activar el régimen para operar con A122R.
  * Si el servicio no está activado, las retenciones podrán procesarse por lote utilizando las actividades definidas.
  * Se considerarán las retenciones de Ingresos Brutos con padrón ARBA para su procesamiento bajo el régimen A122R.



##### Padrón Santa Fe

En esta solapa se configuran los parámetros para asignar retenciones a proveedores según el padrón de Santa Fe.

Asigna retención para proveedores de Sante Fe no incluidos en el padrón: seleccione esta opción si necesita definir una alícuota a incorporar masivamente, a los proveedores que estén fuera del padrón de Santa Fe.

Código de provincia asociada al padrón: indique la provincia que corresponda con el padrón de Santa Fe. Este campo es obligatorio si definió que se asigna retención para proveedores de Santa Fe no incluidos en el padrón.

Código de retención: seleccione del listado la retención de ingresos brutos de jurisdicción provincial que desea agregar a los proveedores que no existan en el padrón de Santa Fe. Esta retención no debe tener asignado ningún padrón.

Consideraciones: la retención seleccionada no debe tener padrón asignado y la provincia configurada debe coincidir con el código de provincia asociada al padrón.

#### Observaciones

Esta sección está disponible para el ingreso opcional de un texto o comentario.

##### Contenidos relacionados

  * [Video sobre integración contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/integrcontable_gral_vid/)

  * [Video sobre parámetros de Compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/parametros_cp2_vid/)
