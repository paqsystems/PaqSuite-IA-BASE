# Clientes

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=19444/

## Contenido

# Clientes

Este proceso permite agregar, consultar y modificar clientes, o bien dar de baja a aquellos que no posean saldo en cuenta corriente ni movimientos.

Para simplificar el ingreso de datos comunes a varios clientes, puede utilizar [plantillas](https://ayudas.axoft.com/25ar/valordefectoclientes_gv). Por ejemplo, puede definir una plantilla denominada "Clientes habituales" con los siguientes datos por defecto:

  * Localidad: La Plata
  * Zona: 1 - hasta 30 kms
  * Provincia: Buenos Aires
  * Categoría de IVA: RI - responsable inscripto
  * Detalle de las percepciones a aplicar
  * Tipo de operación para RG 3685 / 4595: Gravada
  * Condición de venta habitual: Contado
  * Clasificación habitual del cliente
  * Y otros datos de acuerdo a sus necesidades



Tenga en cuenta que puede definir y utilizar varias plantillas de acuerdo a su conveniencia. Puede crearlas en base a la condición de IVA, en base al tipo de cliente, a la zona geográfica, etc.  
Para utilizarlas, seleccione la opción "Plantillas" en lugar de "Nuevo"; en base a la plantilla elegida se completarán los datos con la información por defecto para que continúe con el alta del cliente.  
Si necesita actualizar un determinado campo a un grupo de clientes utilice el proceso [Actualización masiva de clientes](https://ayudas.axoft.com/25ar/actualizacionmasivacliente_gv). Por ejemplo, de esta forma puede asignar un grupo de clientes a una clasificación determinada para informes y estadísticas o indicar una nueva configuración impositiva a otro grupo.

__Nota

Usted puede utilizar este método para actualizar información, y además puede hacerlo mediante la exportación / importación de datos desde **Excel**.

##### **Principal**

En la solapa Principal se agrupan los datos básicos de los clientes, los mismos se detallan a continuación.

Código de cliente: identifica en forma unívoca al cliente a ingresar. Estos códigos pueden agruparse desde la solapa Clientes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).  
Está compuesto por: código de familia, código de grupo y código de individuo.  
Los nombres de los códigos de familia y los códigos de grupo se definen desde la solapa Clientes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).

__Nota

El campo _Código de cliente_ puede contener tanto números como letras o cualquier otro caracter. Tenga en cuenta que no es necesario ocupar todos los caracteres disponibles para el código, pero sí debe respetar las ubicaciones de cada agrupación.

__Nota

Las agrupaciones permiten generar informes agrupados por familia o grupo.

Con respecto al código de cliente a asignar, es posible parametrizar si se aplica la codificación automática de clientes.  
Si usted elige esta modalidad, al ingresar un nuevo cliente, se genera automáticamente el código a asignar (de acuerdo a lo ingresado en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) en el campo Próximo Código de cliente).

Próximo código de cliente existente en Clientes.

Cuando se crea un cliente y el sistema detecta que el "próximo código de cliente" ya existe como cliente, se propone como código de cliente al "mayor código de cliente existente" (*) incrementado en una unidad.

Por ejemplo:

  * Próximo código de cliente: 108302 (ya existe como cliente).
  * Mayor código de cliente: 210360.
  * Código de cliente propuesto: 210361.



(*) En caso de que el "mayor código de cliente existente" sea igual al máximo código de cliente posible (por ejemplo, ZZZZZZ), entonces el sistema realiza una búsqueda de códigos menores (vacíos o no utilizados) y se propone como código de cliente el menor código disponible.

Por ejemplo:

  * Próximo código de cliente: 108302 (ya existe como cliente).
  * Mayor código de cliente: ZZZZZZ.
  * Códigos menores no utilizados: 102956,104850 y 107962.
  * Código de cliente propuesto: 102956.



En este caso, el código de cliente generado no es editable.

Ejemplos de codificación automática (Sin prefijo):

A continuación, se detallan unos ejemplos sin uso de prefijo en el código de cliente.

**Ejemplo 1 - Código de cliente numérico** :

  * Próximo código de cliente: 124.
  * En alta de cliente, se propone y graba el código 000124 (autocompleta con ceros a la izquierda).
  * Próximo código de cliente: se graba con 125.



Como el próximo código de cliente es numérico y es menor al máximo número posible (999999), se incrementa en una unidad numérica (de 124 a 125).

**Ejemplo 2 - Código de cliente llega al máximo número posible:**

  * Próximo código de cliente: 999999.
  * En alta de cliente, se propone y graba el código 999999.
  * Próximo código de cliente: se graba con A.



Cuando se graba el código de cliente con 999999, y al ser igual al máximo número posible, entonces la secuencia pasa a ser alfanumérica comenzando desde la letra A.

**Ejemplo 3 - Código de cliente alfanumérico:**

  * Próximo código de cliente: A.
  * En alta de cliente, se propone y graba el código 00000A (autocompleta con ceros a la izquierda).
  * Próximo código de cliente: se graba con B.



Como el próximo código de cliente tiene al menos 1 carácter alfabético, entonces el autoincremento es alfanumérico (de la letra A pasa a la B).

**Ejemplo 4 - Código de cliente alfanumérico:**

  * Próximo código de cliente: Z.
  * En alta de cliente, se propone y graba el código 00000Z (autocompleta con ceros a la izquierda).
  * Próximo código de cliente: se graba con 1A.



Como el próximo código de cliente tiene al menos 1 carácter alfabético, y por ende, el autoincremento es alfanumérico, el sistema descarta los próximos códigos numéricos (10,11, ... hasta 19 inclusive), y se graba como próximo cliente el 1A.

Ejemplos de codificación automática (Con prefijo):

A continuación, se detallan algunos ejemplos donde se usa el prefijo E, por lo cual, la parte variable del código de cliente que se autoincrementa es de 5 caracteres (código de cliente = prefijo + parte variable):

**Ejemplo 1 - Código de cliente numérico:**

  * Próximo código de cliente: 124.
  * En alta de cliente, se propone y graba el código E00124 (autocompleta con ceros a la izquierda).
  * Próximo código de cliente: se graba con 125.



Como el próximo código de cliente es numérico y es menor al máximo número posible (999999), se incrementa en una unidad numérica (de 124 a 125).

**Ejemplo 2 - Código de cliente llega al máximo número posible:**

  * Próximo código de cliente: 99999.
  * En alta de cliente, se propone y graba el código E99999.
  * Próximo código de cliente: se graba con A.



Cuando se graba el código de cliente con E99999, y la parte variable es igual al máximo número posible (99999), entonces la secuencia pasa a ser alfanumérica comenzando desde la letra A.

**Ejemplo 3 - Código de cliente alfanumérico:**

  * Próximo código de cliente: A.
  * En alta de cliente, se propone y graba el código E0000A (autocompleta con ceros a la izquierda).
  * Próximo código de cliente: se graba con B.



Como el próximo código de cliente tiene al menos 1 carácter alfabético, entonces el autoincremento es alfanumérico (de la letra A pasa a la B).

**Ejemplo 4 - Código de cliente alfanumérico:**

  * Próximo código de cliente: Z.
  * En alta de cliente, se propone y graba el código E0000Z (autocompleta con ceros a la izquierda).
  * Próximo código de cliente: se graba con 1A.



Como el próximo código de cliente tiene al menos 1 carácter alfabético, y por ende, el autoincremento es alfanumérico, el sistema descarta los próximos códigos numéricos (10,11, ... hasta 19 inclusive), y se graba como próximo cliente el 1A.

Si usted opta por no utilizar la codificación automática de clientes, al registrar un nuevo cliente, ingrese el código a asignar o bien, al menos un dígito y utilice la funcionalidad Próximo cliente <F3>.

__Nota

A partir de la versión Tango Delta, si en Parámetros de Ventas indicó que utiliza 'Codificación automática' e ingresa en modo 'Nuevo', el código de cliente se calculará en base al próximo código, en forma secuencial. Si se cancelara esta acción, se mostrará el código siguiente al cancelado previamente.

El comportamiento es entonces, el siguiente:

  1. Al dar de alta un cliente, al cancelar esta acción y reingresar a la opción "Nuevo", se mostrará el código siguiente al que se canceló previamente.
  2. Al presionar <F5> para refrescar, se mostrará el número de cliente que se estaba por dar de alta.
  3. Al abrir varios ABMs, en la carga de datos se mostrará el mismo número de cliente en todas las ventanas; pero al momento de grabar y si el código que se muestra ya fue grabado previamente, se exhibirá el mensaje de confirmación: "El código de cliente utilizado ya existe. Se modificará por xxxxxx. ¿Confirma?". Donde xxxxxx es el nuevo código de cliente.



Tenga en cuenta que al eliminar un cliente, ese código no se recupera. Se visualizará el próximo código (y no el código eliminado).  
Si utiliza prefijo para codificación, el código de cliente mostrará el prefijo junto con la numeración correspondiente.

__Nota

Las altas de clientes desde API y desde **Excel** no respetan la codificación automática. Debe indicar siempre el código del nuevo cliente. Si al completar los datos de alta no ingresa el valor del campo _Código_ , se mostrará el siguiente mensaje: "El código es requerido. La codificación automática no está disponible para este tipo de apertura".

Codificación de clientes usando familias y grupos

En el proceso [Longitud de Agrupaciones](https://ayudas.axoft.com/25ar/longagrupacion_gv) se define lo siguiente:

  * Longitud de Familia:1
  * Longitud de Grupo:1



Automáticamente, y teniendo en cuenta que se asignan 6 dígitos para el código de cliente, la longitud del individuo será 4, que resulta de: 6 - (1+1).  
En el proceso [Agrupaciones de Clientes](https://ayudas.axoft.com/25ar/agrupacioncliente_gv) se define:

**Código** | **Título**  
---|---  
1 | Casas de Artículos del hogar  
11 | Mayoristas  
12 | Minoristas  
  
Finalmente, en el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv) ingresamos:

**Código** | **Razón Social**  
---|---  
110025 | Distribuidora Mayorista Roca  
110026 | El mundo de las heladeras  
120049 | Guillermo Rodríguez  
120050 | Ricardo Vázquez  
  
Los clientes, entonces, quedan ordenados en orden jerárquico de la siguiente manera:

1 | Casa de Artículos del Hogar |  |   
---|---|---|---  
11 |  | Mayoristas |   
110025 |  |  | Distribuidora Mayorista Roca  
110026 |  |  | El Mundo de las Heladeras  
12 |  | Minoristas |   
120049 |  |  | Guillermo Rodríguez  
120050 |  |  | Ricardo Vázquez  
  
El campo Código de Cliente puede contener tanto números como letras o cualquier otro carácter. En el ejemplo, se utilizan números para clarificar el concepto de agrupación.  
Tenga en cuenta que no es necesario ocupar todos los caracteres disponibles para el "código", pero sí debe respetar las ubicaciones de cada agrupación.

CUIT o identificación: sugerimos ingresar correctamente los valores correspondientes a estos campos, ya que son utilizados en aquellos procesos que generan información en archivos para otros sistemas (IVA Ventas, SICORE, etc.).  
El sistema realiza la verificación automática del número de CUIT.

Si en [Parámetros de Ventas](?p=19401) habilita la opción Actualiza información con AFIP podrá completar datos del cliente automáticamente según la información brindada por el organismo.  
Se actualizarán también los códigos de percepciones según los padrones (Ciudad de Bs. As.) o el padrón de Rentas (Provincia de Bs. As.).  
Para más información sobre este tema, consulte la [guía sobre actualización de alícuotas de IIBB según AGIP Bs. As. (Rentas Ciudad de Bs. As.)](?p=26538) y la [guía sobre actualización de alícuotas definibles de IIBB según ARBA](?p=26537).

Datos de contacto

Correo electrónico: ingrese la dirección de correo electrónico del cliente. Permitirá generar e-mails a través de su cliente de correo en forma automática para el envío del resumen de cuenta.

Página Web: ingrese la URL del sitio web del cliente. Este dato puede ser impreso en los comprobantes mediante una variable.

Los Códigos de vendedor y Transporte no son obligatorios. Si habitualmente corresponden a un código específico, es conveniente ingresarlos para que sean sugeridos por el sistema durante el ingreso de comprobantes. 

Información comercial

Rubro comercial: indique el rubro comercial al cual pertenece el cliente. Este será de utilidad para la clasificación de clientes y para obtener informes de ventas por rubro comercial en Live.

Grupo empresario: indique el grupo empresario al que pertenece el cliente. Puede administrar la cuenta corriente de todo el grupo empresario o la de cada cliente en forma individual.

Fecha de alta: es posible indicar, de manera opcional, la fecha de alta de los clientes, para ser utilizada luego en exportaciones, multidimensionales e informes.

Fecha de inhabilitación: esta fecha sirve como referencia del día de la inhabilitación del cliente. Si la fecha está en blanco significa que el cliente está habilitado. El tratamiento en el sistema de los clientes inhabilitados dependerá de lo configurado en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv) para cada uno de los parámetros del ítem Clientes Inhabilitados.

Sucursal origen: indica la sucursal que dio de alta al cliente. Este dato es útil si se está trabajando en una empresa configurada como Casa Central, la cual recibe el alta de nuevos clientes que le envían las sucursales, con ese dato Casa Central puede identificar de qué sucursal proviene ese cliente. Este dato es informativo y no se puede modificar. El sistema lo completa en forma automática.

Relación Maestro - Sucursal:

Si se encuentra trabajando en una empresa definida como casa central, en el momento de dar de alta un cliente, usted tendrá la opción de relacionarlo con sucursales.

La relación cliente - sucursal depende de la configuración de [Parámetros de transferencias](?p=9434) del módulo Central, pudiendo ser:

  * **Automática:** se genera la relación con todas las sucursales en el momento del alta.
  * **Manual:** luego de procesada el alta, puede seleccionar las sucursales asociadas al cliente.



Al exportar clientes se incluirán únicamente aquellos asociados a la sucursal a la que se envía información.

##### **Facturación**

Configuración impositiva

Código de categoría de IVA: seleccione la categoría de IVA del cliente. Los valores posibles son los siguientes:

  * CF: consumidor final.
  * EX: exento.
  * EXE: IVA exento operación de exportación.
  * **INA:** IVA no alcanzado.
  * INR: no responsable.
  * PCE: pequeño contribuyente eventual.
  * PCS: pequeño contribuyente eventual social.
  * RI: responsable inscripto.
  * RS: responsable monotributista.
  * RSS: monotributista social.
  * SNC: sujeto no categorizado.



Las características de facturación indican qué impuestos deben calcularse cuando se emite un comprobante de facturación al cliente y la forma de exponerlos. Esta información se combina con las tasas de impuestos definidas para los artículos que se incluyen en el comprobante.  
De acuerdo a lo establecido por la Ley 27.618, para discriminar el IVA en comprobantes clase 'B' emitidos a clientes 'Monotributistas' (categoría de IVA 'RS' - Responsable monotributista), modifique el archivo TYP e incluya las siguientes variables de reemplazo: **@TY** (total de IVA), **@YI** (descripción de la alícuota), **@YP** (porcentaje de la alícuota), **@YT** (importe de la alícuota).

Código de alícuota no categorizado: este campo es obligatorio para aquellos clientes que defina como 'Sujetos no Categorizados'. En ese caso, deberá ingresar un código de alícuota de percepción (del 11 al 20).  
Esta alícuota se aplicará sobre el total del comprobante o sobre todos los conceptos gravados más impuestos que figuren en el comprobante, pudiéndose discriminar e imprimir a través de una variable de impresión.

Porcentaje de exclusión: en caso de liquidar sobretasas de IVA, se podrá indicar un porcentaje de exclusión, por el cual el cliente queda exceptuado en las percepciones del impuesto al valor agregado.  
Si indica un porcentaje distinto a cero, el sistema realizará la reducción correspondiente en la percepción calculada al cliente en los comprobantes de facturación.

Código de clasificación para percepciones: este campo permite asignar una clasificación especial para ser utilizada en el cálculo de la percepción definible.  
Si se completa este campo la percepción solo se calculará para aquellos clientes y artículos que tengan definida la misma clasificación.

RG 1817

Vencimiento y N° de certificado: con relación a lo establecido por la RG 1817 y si está activo el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-controles) Controla vigencia certificado según RG 1817, ingrese la fecha de vencimiento y el número de certificado presentado por el cliente.  
Para conocer las fechas de vencimiento de los certificados de sus clientes, utilice el proceso Nómina de clientes, emitiendo el informe con destino Excel.

RG 3572

Parámetros disponibles en caso de estar activo el parámetro general RG 3572 - Sujetos vinculados. Para más información, consulte la Guía de implementación sobre [RG 3572 - Sujetos vinculados](?p=11911).

RG 3685 / 4597

Para más información, consulte la [Guía de implementación sobre RG 3685 - Régimen informativo de compras y ventas](?p=11914).

Facturación

Actividades: consigne la actividad empresaria a la que se dedica su cliente. Este dato puede ser impreso en los comprobantes de facturación mediante una variable.

Condición de venta habitual: este campo es obligatorio. Ingrese el código de condición de venta habitual asociado al cliente. Este código será sugerido posteriormente en el ingreso de comprobantes y podrá ser modificado.

Lista de precios habitual: permite ingresar, opcionalmente, la lista de precios habitual asociada al cliente, que será sugerida en los procesos de facturación, emisión de remitos valorizados y pedidos.

Cupo de crédito: este campo permite indicar un importe de crédito en cuenta corriente para el cliente.  
El sistema controla los importes en los procesos de ingreso de comprobantes y si se excede el crédito disponible, emite un mensaje o bien no permite el ingreso, según la parametrización del perfil. Para más información, consulte el proceso [Perfiles de facturación](https://ayudas.axoft.com/25ar/perfilfacturacion_gv).

% de bonificación: si habitualmente corresponde un porcentaje de descuento, es conveniente ingresarlo para que sea sugerido por el sistema durante el ingreso de comprobantes.

Cláusula moneda extranjera: si activa este parámetro, las facturas que se generen para ese cliente estarán canceladas cuando el total en moneda extranjera de la factura coincida con el total en moneda extranjera de los comprobantes que se le imputen, independientemente de la moneda con la que se confeccione cada comprobante.  
Es decir que sus deudas serán expresadas en moneda extranjera y, contablemente, la cuenta en moneda corriente se irá ajustando a través de comprobantes por diferencia de cambio. De lo contrario, las deudas del cliente serán en moneda corriente y podrán expresarse en moneda extranjera considerando la cotización de origen de cada comprobante que conforma la cuenta, o bien reexpresando la cuenta corriente con una cotización ingresada en el momento de la consulta.  
Los clientes que integren grupos empresarios deben respetar la cláusula moneda extranjera del grupo.  
Si se modifica el campo "CLAUSULA", deberá ejecutar los procesos Recomposición de saldos y Reconstrucción de estados.

Integración con otras sucursales

Exporta comprobantes para gestión central: tilde esta opción para permitir que los comprobantes emitidos al cliente puedan continuar el circuito en otra sucursal. Entre los circuitos que puede continuar están:

  * Envío de facturas para cobrarlas en casa central.
  * Envío de pedidos para ser remitidos / facturados por otra sucursal.
  * Envío de remitos para facturase en otra sucursal.
  * Envío de facturas para ser remitidos por otra sucursal.



Envío de facturas que afectan stock para el traslado de la mercadería

Sucursal destino para cobranza (cta. cte): informe la sucursal destino a la que serán enviados los comprobantes para la gestión de la cobranza.

Sucursal destino para movimientos de stock (traslado): informe la sucursal destino a la que será enviada la mercadería de las facturas remito.

Para más información sobre este tema consulte la [guía de implementación sobre gestión central](?p=11925).

##### **Ingresos brutos**

Tipo de inscripción y Número de Ingresos brutos: seleccione el tipo de inscripción ('No liquida', 'Local', 'Multilateral' y 'Régimen simplificado') y luego el número de ingresos brutos.

Más información:

Tenga en cuenta que si utiliza el proceso [Generación de archivos para la RG 745](?p=11988/#resolucion-nro-745-agip) debe indicar un valor numérico, compuesto por 3 dígitos de la jurisdicción + 6 dígitos numéricos + 1 dígito verificador (XXX-XXXXXX-X).  


  * **Fecha de vigencia para los coeficientes:** si el cliente liquida IIBB y su tipo de inscripción es "Convenio multilateral", indique una fecha de vigencia de los coeficientes de cada jurisdicción. Si el cliente realiza una operación en esas jurisdicciones y está dentro de la vigencia indicada, se validará el coeficiente mínimo para la jurisdicción al aplicar percepciones, y en caso de no superarlo no se aplicará la retención.
  * **Jurisdicciones para convenio multilateral:** si el cliente está inscripto en convenio multilateral, debe indicar el índice de participación de sus operaciones en las diferentes jurisdicciones (información disponible en el formulario denominado CM05 del contribuyente). Si desea controlar que el coeficiente mínimo supere un valor indicado por la entidad recaudadora, por ejemplo, el 0.01, complete los valores informados por el cliente en la grilla. Al calcularse una percepción de IIBB, si el coeficiente no supera el mínimo indicado en la percepción, no se aplicará el impuesto.



##### Cobranzas

N° de pago electrónico: es el valor que identifica al cliente para las cobranzas en entidades recaudadoras (Pagomiscuentas, Pago Fácil o Rapipago).  
Este dato es de ingreso obligatorio si existen [configuraciones para cobranzas masivas](https://ayudas.axoft.com/25ar/configcobranzamasiva_gv) para las entidades recaudadoras (Pagomiscuentas, Pago Fácil o Rapipago).  
El sistema valida que se ingresen sólo números y que el valor sea mayor a cero y sin decimales. Asimismo, el número de pago electrónico debe ser único para cada cliente. De no cumplirse las condiciones indicadas, se exhibe un mensaje de confirmación.

Nómina de clientes:

En la consulta Live Nómina de Clientes, usted puede activar la columna "Pago electrónico" para incluir este dato en el detalle.

Genera notas de débitos por mora: defina si se debe calcular interés por mora sobre los comprobantes impagos vencidos del cliente. En el caso de que el parámetro esté inhabilitado, los comprobantes del cliente no generarán interés, aun cuando se cobren vencidos.  
En el caso de haber generado facturas sin política asociada, posteriormente puede asignarles una política y comenzar a generar mora sobre los comprobantes que así lo requieran, utilizando el proceso [Gestión de débitos por mora](https://ayudas.axoft.com/25ar/gestiondebitomora_gv).  
A la inversa, si generó facturas con política asignada y luego decide que no deben devengar interés, es posible mediante el mismo proceso, efectuar esta operación.

Código de política de cálculo de interés por mora: indique la política de cálculo de interés por mora que debe aplicarse sobre los comprobantes del cliente. Este campo no es obligatorio. En el caso de no haber asignado un valor, se considera la política asignada a la [condición de ventas](https://ayudas.axoft.com/25ar/condicionventa_gv) o la asignada a nivel general en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).  


La asignación de la política al comprobante se realiza teniendo en cuenta el siguiente orden de prioridades:

  * En primer lugar se utiliza la política del cliente si éste tiene alguna asignada.
  * En segundo lugar se utiliza la política de la condición de venta si ésta tiene alguna asignada.
  * En tercer lugar, se utiliza la política definida a nivel general, en Parámetros de Ventas.



Para más información consulte la [Guía de implementación sobre intereses por mora](?p=27248).

##### Direcciones

Usted cuenta con la posibilidad de asociar a un cliente múltiples direcciones de entrega. La dirección habitual será usada para la emisión de comprobantes. Cada una de las direcciones asociadas al cliente podrá tener una configuración impositiva distinta, dependiendo de los impuestos que necesite calcular para cada una de las sucursales. En el momento de la emisión de los comprobantes, el sistema realizará el cálculo de impuestos según la dirección seleccionada.  
Por ejemplo, si el cliente posee su casa central en Capital Federal y sus sucursales están en distintas provincias del país, usted puede definir la casa central como dirección principal. A cada una de las sucursales le puede difinir una dirección de entrega y asociarle el código de alícuota de IIBB que se calcule en esa provincia en particular.

**1) Impuestos calculados para la casa central, con dirección en Capital Federal:**

  * IVA: 21 %
  * Percepción definible ARCIBA: 1,5 %



**2) Impuestos calculados para la sucursal con dirección en Provincia de Buenos Aires:**

  * IVA: 21 %
  * Percepción IIBB ARBA: 2,5 %



Dependiendo de lo configurado en los [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes), en el ingreso de comprobantes podrá seleccionar una de las direcciones de entrega cargadas, para que el sistema realice el cálculo de impuestos correspondiente, teniendo en cuenta la configuración impositiva de la dirección seleccionada.

Código: ingrese un código para identificar a cada dirección de entrega.

Habitual: indique si la dirección de entrega ingresada será la habitual para el cliente. Tenga en cuenta que únicamente podrá identificar una dirección de entrega habitual, la misma será utilizada por defecto en la emisión de comprobantes.  
Una vez definido el código y modalidad (si es 'habitual' o 'no habitual') de una dirección de entrega, podrá ingresar todos los datos referentes al domicilio y la su configuración impositiva.

Toma la configuración de impuestos de la dirección habitual: tilde esta opción para utilizar la misma configuración impositiva definida en la dirección de entrega habitual. Caso contrario, usted debe definir la configuración de impuestos en forma manual.  
De esta forma puede definir los impuestos manualmente, o indicar si se deben tomar los asociados a la dirección de entrega habitual.

Liquida IVA liberado: seleccione esta opción en caso de que el cliente requiera realizar facturas por compras que necesiten devolución de IVA.

% de liberación:  defina en que porcentaje se encontrará el IVA liberado.

__Nota

Recuerde que sólo se podrán generar facturas si el valor de porcentaje de liberación de IVA no está entre el 0.01% y 99.9%

Liquida percepción Ingresos Brutos: cuando esta opción está tildada se puede definir una alícuota fija y una alícuota adicional para la percepción de Ingresos Brutos.

Incluye imp. de IVA en la base de cálculo: defina la base imponible para las percepciones de ingresos brutos cuando se usan alícuotas. Cuando esta opción está tildada la base imponible para la percepción de ingresos brutos corresponde a 'Neto Gravado + IVA', de lo contrario la base imponible es 'Neto Gravado'. Está destildado por defecto.

Actualizar según padrones

Pulse <F9> para consultar los padrones (Ciudad de Bs. As.) o el padrón de Rentas (Provincia de Bs. As.) y asignar en forma automática los códigos de percepciones que se le debe aplicar al cliente.

__Nota

Esta acción se encuentra habilitada cuando el tipo de documento del cliente es CUIT (80) y el número de documento tiene 11 caracteres de longitud (sin incluir guiones).  


Para más información sobre este tema consulte [Actualización de alícuotas de I.I.B.B. según AGIP Bs. As. (Rentas Ciudad de Bs. As.)](?p=26538) y [Guía de Implementación sobre actualización de Alícuotas Definibles de IIBB según ARBA](?p=26537).

Copiar dirección legal: al tildar la opción o pulsar <ALT + G> se asigna el domicilio cargado en la solapa principal.

**Más información sobre alícuotas de Ingresos Brutos…**

Con respecto a las alícuotas de ingresos brutos, es posible definir un cliente que liquide percepción de Ingresos Brutos sin especificar una alícuota en particular, en este caso se utilizará en la facturación aquella definida como [percepción de Ingresos Brutos en el artículo](https://ayudas.axoft.com/25ar/articulo_carp_st). De la misma forma está situación se aplica en percepciones definibles.  
Existe una única excepción en la cual la definición de la alícuota es obligatoria. Esta es cuando se cargan percepciones definibles de AGIP o ARBA.

##### Puesta a disposición

Tango nexo

Para publicar la información del cliente en Tango nexo complete los siguientes datos:

Publica información: ingrese 'S' en el caso que desee que el cliente publique información en Tango nexo, caso contrario elija la opción 'N'.

Correo electrónico para enviar invitación: en caso que el cliente publique información en Tango nexo, ingrese una dirección de correo electrónico válida a la cual enviarle la invitación para ingresar en la nube para poder visualizar la información publicada.  
Para más información sobre Tango nexo [ingrese aquí](?p=12429).

Envío de comprobantes electrónicos

Si su empresa emite comprobantes electrónicos complete los siguientes datos:

Imprime: indique la modalidad de envío a su cliente de los comprobantes electrónicos que usted emita.  
Puede optar por una de las siguientes opciones: 'Siempre' (*), 'Sólo publica en Tango nexo', 'Según talonario', 'E-mail' (**), 'E-mail/Papel' (**), 'WhatsApp' (***).

Según talonario: toma la configuración definida en el [talonario](https://ayudas.axoft.com/25ar/talonario_gv).

Solo publica en Tango nexo: el cliente únicamente accederá a sus comprobantes electrónicos a través de Tango nexo.

Correo electrónico para los envíos (**): se indica el o los correos electrónicos (separados por punto y coma) a utilizar para el envío de los comprobantes electrónicos.

Móvil para los envíos por WhatsApp (***): se indica el o los números de celular (separados por punto y coma) a utilizar para enviar los comprobantes electrónicos por WhatsApp.

**(*):** se muestra cuando no se utiliza el envío de comprobantes por correo electrónico por no tener configurada la solapa _"Comprobantes electrónicos"_ de [Parámetros de correo electrónico](?p=11965).  
**(**):** se muestra cuando se utiliza el envío de comprobantes por correo electrónico por tener configurada la solapa _"Comprobantes electrónicos"_ de [Parámetros de correo electrónico](?p=11965).  
**(***):** se muestra cuando se encuentra habilitado el envío de comprobantes por **WhatsApp** en [Parámetros de WhatsApp](?p=30221).

Comprobantes electrónicos de exportación

Si usted emite comprobantes electrónicos de exportación (según RG 3066) y necesita definir una parametrización particular para el cliente, complete los datos que se mencionan a continuación.

Identificación tributaria: indique la clave de identificación tributaria del cliente.

Idioma del comprobante: elija el idioma en el que confeccionará los comprobantes de exportación (facturas, notas de crédito y notas de débito) para su cliente. Usted puede optar por el idioma definido como parámetro general o bien, elegir otro diferente.  
Las opciones posibles son: 'P' - Parámetro General, '1' - Español, '2' - Inglés o '3' - Portugués.  
Por defecto, el sistema considera el idioma definido en la solapa Comprobantes electrónicos del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).

Detalle de los artículos: defina si tiene en cuenta la descripción de los artículos ingresada en cada 'Artículo' o bien, la definida en la relación 'Cliente - Artículo'. Por defecto, el sistema considera lo definido en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).

Incluye comentarios de los artículos: indique si en la descripción del producto a informar a la AFIP incluye los comentarios ingresados para cada artículo desde el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st) del módulo Stock. Por defecto, el sistema considera lo definido en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).

Importante:

Recuerde que para operar con comprobantes electrónicos, parametrice correctamente los campos respectivos en la solapa Comprobantes electrónicos de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).

##### Comentarios

Este comando permite ingresar un texto asociado al cliente.  
Al agregar o modificar un cliente, es posible agregar, modificar o eliminar comentarios referidos a ese cliente.  
Luego de ingresar el texto deseado, es necesario confirmar el proceso para que se almacenen los datos ingresados.

##### Contenidos relacionados

  * [Video sobre Ley 27618 de monotributo](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/leymonotributo_gral_vid/)

  * [Video sobre control de crédito de clientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/controlcredito_gv_vid/)

  * [Video sobre diferencia de cambio en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/diferenciacambio_gv_vid/)

  * [Video sobre direcciones de entrega](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/direntrega_gv_vid/)

  * [Video sobre facturación masiva de pedidos](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/factmasivpedido_gv_vid/)

  * [Video sobre facturación sin controlador fiscal](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/factsincf_gv_vid/)

  * [Video sobre grupos empresarios](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/grupoempresario_gv_vid/)

  * [Video sobre integración con WhatsApp](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/whatsapp_gral_vid/)

  * [Video sobre interés por mora](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/interesmora_gv_vid/)

  * [Video sobre transferencia de facturas para remitir](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfact_gral_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/ventamixta_gv_vid/)

  * [Videos sobre configuración impositiva](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/configimpositiva_gral_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)

  * [Videos sobre parámetros de Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/parametros_gv_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/retencpercep_gral_vid/)

  * [Videos sobre transferencia de mercadería](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfstock_gral_vid/)
