# Proveedores

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=14686/

## Contenido

# Proveedores

Este proceso le permite agregar nuevos proveedores, consultar y modificar datos de proveedores ya existentes, o bien dar de baja a proveedores que no posean saldo en cuenta corriente ni movimientos vigentes.

Mediante esta opción no es posible modificar saldos de proveedores, ya que éstos son actualizados automáticamente a través de procesos específicos.

##### Principal

En la solapa Principal se agrupan los datos básicos de los proveedores. Los mismos se detallan a continuación.

Código de proveedor: identifica al proveedor. Ingrese el código a asignar o bien, al menos un dígito, y utilice el botón "<+1>" para utilizar la funcionalidad Próximo proveedor.  
Estos códigos pueden agruparse como describimos en el proceso [Longitud de agrupaciones](https://ayudas.axoft.com/24ar/longitudagrupacion_cp2).  
Estará compuesto por: código de familia, código de grupo y código de individuo.  
Los nombres de los códigos de familia y los códigos de grupo se definen en el proceso [Agrupaciones de proveedores](https://ayudas.axoft.com/24ar/agrupacionproveed_cp2).

__Nota

Las agrupaciones le permiten generar informes agrupados por familia / grupo.

**Ejemplo...**  
En el proceso _Longitud de agrupaciones_ se define lo siguiente:  
Longitud de Familia: 1  
Longitud de Grupo: 1  
Automáticamente, y teniendo en cuenta que se asignan 6 dígitos para el código de proveedor, la longitud del individuo será 4, que resulta de: 6 - (1+1).  
En el proceso Agrupaciones de Proveedores se define:

**Código** | **Título**  
---|---  
1 | Metalúrgicas  
11 | Chapa  
12 | Buloneras  
2 | Maquinarias  
21 | Electrónica  
  
Finalmente, en el proceso Proveedores, se definirá:

**Código** | **Razón Social**  
---|---  
110001 | Metalúrgica Argo  
110002 | Ricardo Messina S.A.  
110005 | Aceros Spannaus  
120002 | Bulonera Ramos  
210005 | Electrónica Vega  
  
Los proveedores, entonces, quedarán ordenados de la siguiente manera en el orden jerárquico:

1 | Metalúrgica |  |   
---|---|---|---  
11 |  | Chapa |   
110001 |  |  | Metalúrgica Argo  
110002 |  |  | Ricardo Messina S.A.  
110005 |  |  | Aceros Spannaus  
12 |  | Bulonera |   
120002 |  |  | Bulorena Ramos  
2 | Maquinaria |  |   
21 |  | Electrónica |   
210005 |  |  | Electrónica Vega  
  
El campo Código de proveedor puede contener números, letras o cualquier otro carácter. En el ejemplo, se utilizan números para clarificar el concepto de agrupación.  
Tenga en cuenta que no es necesario ocupar todos los caracteres disponibles para el "código", pero si debe respetar las ubicaciones de cada agrupación.

__Nota

A partir de la versión Tango Delta, si en Parámetros de Compras indicó que utiliza 'Codificación automática' e ingresa en modo 'Nuevo', el código de proveedor se calcula en base al próximo código, en forma secuencial. Si se cancelara esta acción, el código no volverá atrás, consumiendo ese valor.

__Nota

Las altas de proveedores desde API y desde **Excel** no respetan la codificación automática. Se debe indicar siempre el código del nuevo proveedor. Si al completar los datos de alta no se completa el valor del campo _Código_ , se mostrará el siguiente mensaje: "El código es requerido. La codificación automática no está disponible para este tipo de apertura".

CUIT o identificación: se sugiere ingresar correctamente los valores correspondientes a este campo, ya que éstos son utilizados en aquellos procesos que generan información en archivos para otros sistemas (DGI - CITI, SICORE, etc.).  
Tenga en cuenta que el sistema propone el CUIT correspondiente a las personas jurídicas del país al que pertenece el proveedor.  
Esta opción resulta de utilidad cuando el proveedor reside en el extranjero, pues el número de CUIT es único por país.

Si usted parametrizó la aplicación de un control medio de estos valores, ante el ingreso de un número de CUIT repetido, el sistema exhibirá un mensaje solicitando su confirmación. Si, en cambio, usted configuró la aplicación de un control estricto; ante el ingreso de un número de CUIT repetido, el sistema presenta un mensaje de atención para que modifique ese valor (evitando así que dos proveedores tengan el mismo número de CUIT).

Actualizar: esta opción solo se habilita en el caso que el tipo de documento sea '80 - CUIT', '86 - CUIL' y luego de ingresar el número correspondiente.  
Al presionar esta opción se autocompletará los datos del proveedor con los datos suministrados por el AFIP; en el caso que no existan datos se emitirá un mensaje.  
Se actualizarán también los códigos de retenciones según los padrones (Ciudad de Bs. As.) o el padrón de Rentas (Provincia de Bs. As.).  
Para más información sobre este tema consulte [Guía sobre actualización de alícuotas de IIBB según AGIP Bs.As.](?p=14406)  
En el caso que se encuentre activo el [parámetro de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) Obtiene automáticamente datos fiscales al ingresar CUIT o identificación en el alta de proveedores se actualizará automáticamente estos datos sin necesidad de presionar el botón.

Imagen: se puede asociar una imagen al artículo. La misma debe respetar el formato BMP o JPG. En caso de que sea necesario cambiarla, primero se la debe borrar y luego subir la imagen nueva.

Información comercial

Rubro: mediante esta opción puede indicar el rubro comercial al cual pertenece el proveedor. Esta opción es de utilidad para la emisión de informes en Live.

Actividades: consigne la actividad empresaria a la que se dedica su proveedor. Este dato puede ser impreso en los comprobantes de facturación mediante una variable.  
También será posible visualizar, en este apartado, el nombre comercial y domicilio comercial.

Fecha de alta: es posible indicar, de manera opcional, la fecha de alta de los proveedores para ser utilizada en exportaciones.

Fecha de inhabilitación: este campo permite marcar al proveedor como no operativo.  
Un proveedor inhabilitado no puede utilizarse en ningún proceso que genere nuevos movimientos comerciales (incluye órdenes de compra, remitos y comprobantes de compra como facturas, notas de débito y notas de crédito).  
Si la fecha está en blanco, el proveedor se considera habilitado.

Sucursal origen: indica la sucursal que dio de alta al proveedor. Este dato es útil si se está trabajando en una empresa configurada como casa central, la cual recibe el alta de nuevos proveedores que le envían las sucursales, con ese dato casa central puede identificar de qué sucursal proviene ese proveedor.  
Este dato es informativo y no se puede modificar. El sistema lo completa en forma automática.

##### Impuestos

Código de categoría de IVA: seleccione la categoría de IVA del proveedor. Los valores posibles son los siguientes:

  * CF: Consumidor final.
  * EXE: IVA exento operación de exportación.
  * INR: No responsable.
  * PCE: Pequeño contribuyente eventual.
  * PCS: Pequeño contribuyente eventual social.
  * RI: Responsable inscripto.
  * RS: Responsable monotributista.
  * RSS: Monotributista social.



Tipo de inscripción y número de Ingresos brutos: seleccione el tipo de inscripción ('No liquida', 'Local', 'Multilateral' y 'Régimen simplificado') y luego el número de ingresos brutos.

Tenga en cuenta:

Si utiliza el proceso [Generación de archivos para la RG 745](?p=11988/#resolucion-nro-745-agip) debe indicar un valor numérico, compuesto por 3 dígitos de la jurisdicción + 6 dígitos numéricos + 1 dígito verificador (XXX-XXXXXX-X).

Valores para el cálculo de impuestos:

Indique que impuestos deben calcularse cuando se emite un comprobante de facturación al proveedor. Esta información se combina con las tasas de impuestos definidas para los impuestos que se incluyen en el comprobante.

Retenciones

Código de clasificación: permite asociar una clasificación para determinar la base de cálculo de las retenciones del tipo 'Otras'.

Si parametrizó el cálculo automático de retenciones, ingrese los códigos habituales y una leyenda de retención (Ganancias, IVA, Ingresos Brutos y Otras).  
Si el proveedor tuviera una exención en el importe de la retención, puede ingresar el Número de certificado, el porcentaje y las fechas Desde - Hasta de la exención. Estos campos pueden dejarse en blanco si alguna de las retenciones no se calcula para el proveedor ingresado.  
Estos códigos de retención habituales serán sugeridos en el momento del pago, pero pueden ser modificados.  
Además, es posible parametrizar 4 textos, que podrá utilizar en la impresión de la retención.  
Para más información sobre este tema consulte: [Régimen de retención por sujeto (Rentas provincia de Bs. As.)](https://ayudas.axoft.com/24ar/actalicibrentabsas_cp2#regimen)

Textos para comprobantes de Ingresos Brutos:

Es posible configurar para cada uno de los proveedores, líneas de textos adicionales, que se imprimirán en sus correspondientes comprobantes de retención de ingresos brutos.  
Es posible ingresar dos líneas de texto (de 60 caracteres cada una) para el encabezado y otras dos para el pie del comprobante de retención.  
En el momento de generarse el comprobante de retención correspondiente, si el proveedor tiene asociada líneas de texto adicional, éstas se imprimirán en el lugar configurado. Caso contrario, el comprobante de retención no se verá modificado.  
Para eliminar los textos ingresados en cada proveedor, bastará simplemente con borrar el texto asociado.

##### Resoluciones

RG 3685 / 4597 - Régimen Informativo de compras y ventas / Libro de IVA digital

Asigne a su proveedor habitual los valores de Código de tipo operación y Código de comprobante AFIP. Al ingresar comprobantes de su proveedor, estos datos se indicarán como sugerencias.

Genera información: al activar este parámetro, todos los comprobantes que ingrese para el proveedor (facturas, créditos y débitos) serán informados en los archivos de soporte magnético para RG 3685 - Régimen Informativo de compras y ventas / RG 4597 - Libro de IVA digital.

Para más información, consulte la [Guía sobre implementación RG 3685 - Régimen informativo de compras y ventas](?p=11914) o la [Guía de implementación sobre RG 4597 - Libro de IVA digital](?p=27842).

RG 3572 - Sujetos Vinculados

Identifique los proveedores que son empresas vinculadas en la operatoria diaria (según lo establecido por la RG 3572). Para ello, active el parámetro Empresa vinculada e indique el Código de tipo de operación habitual desde el listado de operaciones.

Para más información, consulte la [Guía sobre implementación RG 3572 - Sujetos vinculados](?p=11911).

RG1361 y RG3665

Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) usted indicó que cumple con la RG 1361, debe completar los siguientes datos, que pueden ser modificados durante el ingreso de comprobantes.

Emite comprobantes por controlador fiscal: indique si habitualmente el proveedor le entrega comprobantes emitidos por controlador fiscal.

Tipo de comprobante: en caso que el proveedor emita comprobantes mediante controlador fiscal, indique el tipo de comprobante (tickets o tickets-factura) que recibe en forma habitual.

CAI y Fecha de vencimiento del talonario: si el proveedor es responsable inscripto, puede especificar el CAI y la fecha de vencimiento del talonario que está utilizando actualmente el proveedor.

Más información:

Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) usted indicó que cumple con la RG 3665, debe completar solamente los dos últimos campos.

DGI CITI

Estos campos permiten ingresar valores por defecto a asignar a los comprobantes, relacionados con la información que genera el sistema para la integración con el diskette DGI - CITI.

__Nota

Agilice el ingreso de operaciones indicando el tipo de comprobante que recibe del proveedor.

Clasificación habitual para SIAp: seleccione la clasificación que habitualmente asigna a las operaciones que realiza con este proveedor. Aquellos proveedores a los que no se les haya asignado un código de clasificación particular, serán definidos con 'Considera clasificación de los artículos/conceptos'.  
Por lo tanto, al momento de ingresar el comprobante, siempre tendrá en cuenta la clasificación para SIAP definida para ese proveedor (inclusive la clasificación 'SIN'), independientemente de la clasificación que tuviesen los artículos y/o conceptos involucrados en el mismo.  
En el caso que se deje dicho parámetro en blanco (correspondiente al comportamiento 'Considera clasificación de los artículos/conceptos'), al ingresar el comprobante, la clasificación SIAP será la definida en los artículos/conceptos incluidos en el mismo.

**Ejemplo...**

Caso 1:  
Se define un proveedor con el siguiente parámetro: Clasificación habitual para SIAp: 'C6' (Otros conceptos).  
Luego se ingresa un comprobante para dicho proveedor con un artículo con clasificación habitual para SIAp: 'C9' (Compra como monotributista).  
Al terminar el ingreso, el comprobante tendrá como clasificación para SIAp el valor 'C6', la definida por el proveedor.

Caso 2:  
Se define un proveedor con lo siguiente: Clasificación habitual para SIAp: 'blanco' (Considera clasificación de los artículos).  
Luego se ingresa un comprobante para dicho proveedor con un artículo con clasificación habitual para SIAp: 'C9' (Compra a monotributista).  
Al terminar el registro, el comprobante tendrá como clasificación para SIAp el valor 'C9', la definida en el artículo.

##### Comprobantes

Cupo de crédito: este campo opcional permite indicar un importe de crédito en cuenta corriente asignado por el proveedor. El sistema controlará los importes en los procesos de ingreso de comprobantes, emitiendo un mensaje en caso que exceda el crédito disponible. Si no carga un importe en este campo, no se realizará control de crédito.

Cláusula moneda extranjera: si activa este parámetro, las facturas que se ingresen del proveedor serán canceladas cuando el total en moneda extranjera de la factura coincida con el total en moneda extranjera de los comprobantes que se le imputen, independientemente de la moneda con la que se confeccione cada comprobante. Es decir que las deudas serán expresadas en moneda extranjera contable y, contablemente, la cuenta en moneda corriente se irá ajustando a través de comprobantes por diferencia de cambio. De lo contrario, las deudas con el proveedor serán en moneda corriente y se expresarán en moneda extranjera contable considerando la cotización de origen de cada comprobante que conforma la cuenta, o bien reexpresando la cuenta corriente con una cotización ingresada en el momento de la consulta.

Incluye comprobantes en IVA Compras: al activar este parámetro todos los comprobantes que ingrese para el proveedor (facturas, créditos y débitos) serán informados en el IVA Compras y en los soportes magnéticos (Archivos DGI), a excepción de los créditos y débitos internos (los que solo ajustan la cuenta corriente).

Facturas / Notas de débito / Notas de crédito

Tipo de numeración: active la opción automática si desea que la numeración de los comprobantes a ingresar (facturas, notas de débito y notas de crédito) sea automática, el sistema propondrá un valor, factible a ser modificado. Para formular el próximo número, se considerará el máximo número ya ingresado (considerando la letra asignada al proveedor, sucursal y número), y le adicionará un dígito. Sino, la numeración será manual.

Letra habitual del comprobante: permite ingresar la letra habitual correspondiente a los comprobantes de facturación recibidos del proveedor. Esta letra será sugerida en el ingreso de facturas, notas de crédito y notas de débito del proveedor. Los valores posibles de selección son: 'A', 'B', 'C', 'E', 'M', 'T'. 

Código de condición de compra habitual: indica el código de condición de compra habitual asociado al proveedor. Será el sugerido en el ingreso de comprobantes.

Bonificación: si habitualmente corresponde un porcentaje de descuento, es conveniente ingresarlo para que sea sugerido por el sistema durante el ingreso de comprobantes.

Moneda habitual: indica la moneda en la que se ingresan los comprobantes del proveedor en forma habitual. Será sugerida en el ingreso de comprobantes.

Listas de precios: estos datos son muy importantes porque se utilizan en el ingreso de comprobantes de artículos (facturas, débitos y créditos) y las listas de precios del proveedor.  
Indique si los precios unitarios que se ingresan, incluyen los impuestos (IVA e impuestos internos).  
Si el proveedor no liquida impuestos, no se ingresarán estos campos, ya que por defecto no se los incluirá en los precios.

Comprobantes de referencia

Es posible configurar el circuito a seguir para los comprobantes remito, factura-remito y factura, indicando los comprobantes de referencia para cada uno.

Comprobante de referencia: indique cual va a ser el comportamiento del remito, factura-remito y factura en cuanto al comprobante de referencia.

  * Control estricto: es obligatorio que el el remito, factura-remito, y factura haga referencia al tipo de comprobante configurado.
  * Control flexible: no es obligatorio que el remito, factura-remito y factura haga referencia a otro comprobante.
  * No controla: el remito, factura-remito y factura no hacen referencia a otros comprobantes.



Tipo de comprobante de referencia: indique el tipo de comprobante de referencia cuando se configura que se realiza un control estricto o flexible.

Permite ingresar facturas sin remito asociado: solo para facturas, permite especificar si es obligatorio el ingreso de un remito. Si el parámetro no está activo, debe seleccionar al menos un remito al cargar una factura que no mueva stock.

Información adicional

Asocia a comprobantes de compras en carpeta de importación: indique si habitualmente el proveedor factura conceptos que afectarán los costos de mercadería importada. Cuando se intente asociar un comprobante a una carpeta de importación, el sistema dará aviso si el proveedor no tiene este campo activo. Para el listado de Comprobantes pendientes de asociar a carpetas, se tendrán en cuenta los comprobantes de proveedores que tengan activo este campo.

Exporta comprobantes a otro sistema para su pago: en el caso de exportar comprobantes para cuenta corriente a otro sistema, a través de la opción Transferencias de los módulos Procesos generales / Central, indique para cada proveedor si exporta los comprobantes. Este parámetro es de utilidad para los pagos que se realizan en la casa central y sucursales.

Sucursal destino: informe la sucursal destino a la que se le enviarán los comprobantes para gestionar el pago. Este valor será tomado por defecto para el ingreso de los comprobantes de facturación, el cual luego se utiliza para filtrar la exportación. En la importación también se valida que sea la sucursal correcta. Si al realizar la transferencia no informa la sucursal destino no se aplicará el filtro por sucursal y podrán ser importadas en cualquier sucursal.

##### Pagos

Usted podrá indicar en cada proveedor un medio de pago particular para la generación de ordenes de pago.  
Las cuentas definidas en el proveedor se propondrán como medio de pago defecto en los procesos de [Generación del Pago Masivo](https://ayudas.axoft.com/24ar/pagmasgeneracion_cp2), [Pagos](https://ayudas.axoft.com/24ar/ccorringrpago_cp2) y [Facturas de contado](https://ayudas.axoft.com/24ar/comprobingrfact_cp2#calcret).  
Para los proveedores que no posean definidos medios de pago, se tomarán los valores por defecto de acuerdo al proceso:

  * En Generación de Pagos Masivos: se tomarán de [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2).
  * En Pagos o Facturas de Contado: se tomarán de los [Perfiles para cobranzas y pagos](?p=14679) si los hubiera.



__Nota

Tenga en cuenta que si usted ingresa a los procesos _Pagos_ o _Facturas de Contado_ utilizando un perfil para pagos, debe configurarle las cuentas definidas en los proveedores. Los usuarios que no posean permiso para utilizar una cuenta definida en el proveedor, no podrán realizar el pago utilizando ese perfil.

Código de medio de pago habitual: indique la cuenta habitual, de tipo 'Otras' o 'Banco' (del módulo Tesorería), que utilizará para registrar el egreso del importe del pago. Su ingreso no es obligatorio.

Código de cuenta a debitar: indique la cuenta principal a debitar, de tipo 'Otras' (del módulo Tesorería), donde se registrará el importe de cada orden de pago generada. Su ingreso no es obligatorio. Puede definir la misma cuenta en todos los proveedores o una particular para cada uno.

__Nota

Si define cuentas a debitar diferentes, podrá consultar en **Tesorería** , el saldo de los pagos discriminados por cada cuenta de los proveedores. Pero deberá tener en cuenta que debe configurarles la misma imputación contable, para la exportación a contabilidad.

Emite cheques: si como Medio de pago habitual definió una cuenta de tipo 'Banco', indique el comportamiento habitual con respecto a la emisión de cheques. Tildando este parámetro, al ingresar un pago el sistema le preguntará si desea emitir cheques; caso contrario, sólo podrá registrar un importe (transferencia bancaria).

__Nota

En el caso de haber seleccionado una cuenta bancaria que utiliza cheques diferidos, este campo no será solicitado, debido a que obligatoriamente deberá efectuar el pago con cheques.

Cantidad de días: si emite cheques, indique la cantidad de días a considerar en el cálculo de la fecha de los cheques. En el momento del pago, el sistema calcula la fecha del cheque sumando a la fecha del pago los días indicados en este campo. Si necesita que la fecha del cheque sea igual a la fecha del pago, mantenga este valor en cero, siempre que no haya definido una cuenta bancaria para cheques diferidos.

Clave bancaria única (CBU): es una clave única formada por 22 dígitos numéricos que el banco le asigna al titular de una cuenta bancaria para que pueda realizar transferencias a través de los diferentes medios de transferencia bancarios.  
También es posible ingresar una descripción para cada una de las claves ingresadas.

Orden para la impresión de cheque: este campo se utiliza únicamente para la impresión de cheques, siempre y cuando se encuentre instalado el módulo Tesorería. Por defecto, toma el contenido del campo Razón social, pero puede ser modificado.

Habilitado para pagos masivos: en el caso de que usted tenga habilitado el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2) Usa Pagos Masivos, puede definir que proveedores aplican para intervenir en este proceso.

##### Artículos / Conceptos

Artículos

Mediante esta opción usted puede establecer la relación entre el proveedor y los artículos que habitualmente provee.  
Estos artículos deben existir en el módulo Stock.  
En este caso, se ingresará para cada artículo el Sinónimo de origen o Código de artículo del proveedor. Este código se utilizará para invocar al artículo desde los procesos de ingreso de comprobantes relacionados con proveedores (ordenes de compra, facturas y remitos).  
También puede indicar la unidad de compra a la que se le asignará precios cuando realice la actualización de los mismos, mediante la importación de una planilla de Excel desde el proceso [Administración de precios](https://ayudas.axoft.com/24ar/adminprecios_cp2).  
En el campo Sinónimo de medida, puede indicar el sinónimo de origen con que el proveedor identifica la unidad de medida. (si este valor está informado se utilizará al realizar al proveedor una solicitud de precios).  
La relación proveedor-artículo se utilizará también para la actualización de listas de precios de proveedores.

__Nota

Si desde este proceso, se eliminan artículos de la relación, se eliminarán también los precios que existan para el artículo y el proveedor.

Conceptos

Mediante esta opción usted puede establecer la relación entre el proveedor y los conceptos que habitualmente posee.  
En el caso que desee que el sistema le proponga los conceptos configurados en el proveedor debe configurar el parámetro Valida conceptos por proveedor de [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2), o bien si utiliza perfiles desde [Perfiles de facturas](https://ayudas.axoft.com/24ar/perffacturacp_cp2).

##### Contactos

Desde esta solapa usted administra los contactos asociados al proveedor.  
Es posible configurar los correos electrónicos de los contactos a los que se les enviará archivos PDF de los comprobantes de órdenes de compra y/u órdenes de pago.

##### Observaciones

Comentarios

Este comando permite ingresar un texto asociado al proveedor.  
Al agregar o modificar un proveedor, es posible agregar, modificar o eliminar comentarios referidos a ese proveedor.  
Luego de ingresar el texto deseado, es necesario confirmar el proceso para que se almacenen los datos ingresados.

Relación Maestro - Sucursal:

Si se encuentra trabajando en una empresa definida como Casa Central, en el momento de crear un proveedor nuevo, tendrá la opción de generar la relación Proveedor - Sucursal.  
La modalidad de la creación de la relación Proveedor - Sucursal depende de la configuración de Parámetros generales del módulo Central. Estas pueden ser:

  * Automática: se genera la relación con todas las sucursales en el momento del alta.
  * Manual: luego de procesada el alta, el usuario puede generar la relación con la/las sucursales.



¿Cómo indicar los artículos del proveedor?

Mediante el comando Artículos usted puede establecer la relación entre el proveedor y los artículos que habitualmente provee.  
Estos artículos deben existir en el módulo Stock.  
En este caso, se ingresará para cada artículo el Sinónimo de origen o Código de artículo del proveedor. Este código se utilizará para invocar al artículo desde los procesos de ingreso de comprobantes relacionados con proveedores (ordenes de compra, facturas y remitos).  
También puede indicar la unidad de compra a la que se le asignará precios cuando realice la actualización de los mismos, mediante la importación de una planilla de Excel desde el proceso [Administración de precios](https://ayudas.axoft.com/24ar/adminprecios_cp2).  
La relación proveedor-artículo se utilizará también para la actualización de listas de precios de proveedores.

__Nota

Si desde este proceso, se eliminan artículos de la relación, se eliminarán también los precios que existan para el artículo y el proveedor.

##### Contenidos relacionados

  * [Video sobre Reemplazo Factura 'M' - Retención IVA e IIGG](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/facturam_gv_vid/)

  * [Video sobre ajustes en Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/ajustes_cp2_vid/)

  * [Video sobre centralización cuentas corrientes de Compras](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/cccentral_gral_vid/)

  * [Video sobre diferencia de cambio en Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/diferenciacambio_cp2_vid/)

  * [Video sobre parámetros de Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/parametros_cp2_vid/)

  * [Video sobre remitos de compra desde Tango Colectora](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/colectora_cp2_vid/)

  * [Video sobre solicitudes de precios](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/preciocompra_cp2_vid/)

  * [Videos de importaciones](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/importaciones_cp2_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)

  * [Videos sobre remitos y facturas de compra](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/remitofactura_cp2_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/retencpercep_gral_vid/)

  * [Videos sobre órdenes de pago individual y masivo](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/ordenpago_cp2_vid/)
