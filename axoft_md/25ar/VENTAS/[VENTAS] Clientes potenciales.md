# Clientes potenciales

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_alicuotiibbsantafe_gv3/?p=19235/

## Contenido

# Clientes potenciales

Este proceso permite agregar, consultar, modificar y dar de baja clientes potenciales. Llamamos clientes potenciales a aquellos que pueden convertirse en clientes habituales (son los clientes con los que opera con frecuencia) o clientes ocasionales (son clientes que se ingresan al sistema con una información mínima para emitir una cotización, esta información no podrá ser consultada con posterioridad a la emisión del documento) para los que se ingresa información básica que posibilite emitir cotizaciones. Esta información se mantiene en el sistema y puede ser consultada con posterioridad a la emisión de la cotización.  


Este tipo de clientes se utiliza únicamente en los procesos relacionados con [Cotizaciones](https://ayudas.axoft.com/25ar/cotizaciones_carp_gv).  
Los clientes potenciales se transforman en clientes habituales o clientes ocasionales una vez que usted decida registrarlos como tales, al generar un pedido o desde el comando Operaciones opción: Crear habitual.

**< F3> \- Próximo cliente  
**Esta función está disponible sólo si se encuentra habilitado el parámetro Codificación automática de clientes potenciales en la solapa Clientes del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes), y se completa utilizando el valor ingresado en el próximo código de cliente.

Código de cliente: identifica en forma unívoca al cliente potencial.  
Puede contener tanto números como letras o cualquier otro caracter. Tenga en cuenta que no es necesario ocupar todos los caracteres disponibles para el "código".

Codificación automática de clientes potenciales:

Con respecto al código de cliente potencial a asignar, es posible parametrizar si aplica la codificación automática.  
Si elige esta modalidad, al ingresar un nuevo cliente potencial, se genera automáticamente el código a asignar (de acuerdo a lo ingresado en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) en el campo Próximo Nro. de la ventana Clientes Potenciales). En este caso, el código generado no es editable.  
Si opta por no utilizar la codificación automática, al registrar un nuevo cliente potencial, ingrese el código a asignar o bien, al menos un dígito y utilice la funcionalidad Próximo Cliente - <F3>.

Los Códigos de zona y Provincia son obligatorios.

Condición de venta: este campo es obligatorio. Ingrese el código de [condición de venta](https://ayudas.axoft.com/25ar/condicionventa_gv) asociado al cliente potencial.  
Este código será sugerido posteriormente en el ingreso de cotizaciones, pero es posible modificarlo.

Lista habitual: ingrese, de manera opcional, la lista de precios habitual asociada al cliente potencial.  
Este dato será sugerido en el ingreso de la cotización.

% Bonificación: si habitualmente corresponde un porcentaje de bonificación, es conveniente ingresarlo para que sea sugerido por el sistema durante el ingreso de la cotización.

Correo electrónico: ingrese la dirección de correo electrónico del cliente potencial. De esta manera, podrá generar E-mails a través de Outlook en forma automática.

Página web: ingrese la página Web del cliente potencial.

Rubro comercial: indique el rubro comercial al cual pertenece el cliente. Este dato será de utilidad para la clasificación de clientes y para obtener informes de ventas por rubro comercial en Live.

Luego de ingresar todos los datos requeridos, pulse <F10> para acceder a la ventana donde podrá ingresar la información correspondiente al cálculo de impuestos.

##### Datos adicionales para clientes potenciales

Los siguientes datos están disponibles luego de ingresar o modificar los datos del cliente potencial, al pulsar <F10> tendrá la posibilidad de cargar o modificar los siguientes valores.  
Desde esta ventana podrá parametrizar los valores correspondientes al cálculo de impuestos.

###### Características de Facturación para clientes potenciales

Las características de facturación indican qué impuestos deben calcularse cuando se emite una cotización a un cliente potencial y la forma de exponerlos.  
Esta información se combina con las tasas de impuestos definidas para los artículos que se incluyen en el comprobante.

CUIT: ingrese el tipo y número de documento asociado al cliente.  
El sistema realiza la verificación automática del número de CUIT e informa si no es correcto.

Para personas físicas o jurídicas

Tenga en cuenta que el sistema propone el CUIT correspondiente a las personas jurídicas del país al que pertenece el cliente.  
Esta opción resulta de utilidad cuando el cliente reside en el extranjero, pues el número de CUIT es único por país.  
Pulse la tecla <F7> para utilizar el CUIT correspondiente a personas físicas o <F6> para considerar el CUIT correspondiente a personas jurídicas

Clasificación para percepciones definibles: este campo permite asignar una clasificación especial para ser utilizada en el cálculo de la percepción definible.  
Si se completa este campo la percepción solo se calculará para aquellos clientes y artículos que tengan definida la misma clasificación. 

###### Concepto

Liquida IVA: este campo indica si se calculará el IVA en las cotizaciones, está asociado a la categoría de IVA del cliente potencial.  
Los valores posibles son:

  * **S:** Cliente con categoría 'Responsable Inscripto' o 'Consumidor Final'.
  * **I:** Cliente IVA No Responsable.
  * **E:** Cliente IVA Exento.
  * **M:** Cliente Responsable Monotributo.
  * **C:** Cliente con condición Sujeto No Categorizado.
  * **N:** El cliente no paga IVA ya que es exento en sus compras.
  * **A:** Cliente no alcanzado.



De todos los valores comentados, 'N' (Exento en las compras) es el único que no realiza el cálculo de IVA en las cotizaciones.  
Si el cliente potencial liquida IVA (valor 'S'), indique si discrimina el importe de IVA en las cotizaciones, y si además corresponde liquidar sobretasas (percepciones) o subtasas de IVA.

Porcentaje de exclusión: en caso de liquidar sobretasas de IVA (percepciones), puede indicar un porcentaje por el cual el cliente potencial queda exceptuado en las percepciones del impuesto al valor agregado.  
En ese caso, el sistema realiza la reducción correspondiente en la percepción calculada al cliente potencial en las cotizaciones.

Impuesto interno: indique en este campo si corresponde aplicar impuestos internos al generar cotizaciones, si se discriminan y si se aplican tasas o sobretasas.

IVA liberado: si activa este parámetro, el sistema realiza los cálculos correspondientes al IVA liberado.

Percepción de Ingresos Brutos: indique si calcula la percepción para el cliente potencial.

Ingreso de dos códigos

Es posible ingresar, de manera opcional, hasta dos códigos de alícuota. De existir la alícuota 1, ésta es considerada en las cotizaciones independientemente de la alícuota ingresada para los artículos (salvo en aquellos artículos en los que no active este campo y que en ningún caso calcularán percepción).  
La alícuota adicional permite incluir una segunda percepción, que se calculará sobre todos los artículos de la cotización que generen percepción de Ingresos Brutos.  
Esto permite adaptar el cálculo a distintas normas vigentes para la percepción, según dependa el porcentaje a calcular del artículo o del cliente potencial, y contemplar los casos en los que se calculan dos percepciones por la jurisdicción de la empresa y la del cliente potencial.

<F8> \- Asignación de alícuota de I.B. s/padrón Rentas provincia Bs.As.:

Pulse <F8> \- Asignación de alícuota de I.B. s/padrón Rentas provincia Bs.As. para consultar el padrón de Rentas (provincia de Bs.As.) y asignar en forma automática la alícuota de percepción que se le debe aplicar al cliente.  
Esta tecla de función sólo está habilitada cuando el cliente tiene definido un CUIT y el cursor se encuentra posicionado en alguno de los siguientes campos: Percepción Ing. Brutos o Alícuota fija.  
Para más información sobre este tema consulte: [Régimen de percepción por sujeto (Rentas provincia de Bs.As.)](https://ayudas.axoft.com/25ar/actalicibpadronrentabsas_gv)

<F9> \- Asignación de alícuota de I.B. s/padrón Rentas ciudad Bs.As.:

Pulse <F9> \- Asignación de alícuota de I.B. s/padrón Rentas ciudad Bs.As. para consultar el padrón de Rentas (ciudad de Bs.As.) y asignar en forma automática la alícuota de percepción que se le debe aplicar al cliente.  
Esta tecla de función sólo está habilitada cuando el cliente tiene definido un CUIT y el cursor se encuentra posicionado en alguno de los siguientes campos: Percepción Ing. Brutos o Alícuota fija.  
Para más información sobre este tema consulte [Circuito de actualización de alícuotas de IIBB según AGIP Bs.As.](?p=26538)

Percepción IB Bs.As. 59/98: indica si se calcula el impuesto sobre los ingresos brutos correspondiente a la provincia de Buenos Aires 59/98, que deben aplicar las industrias elaboradoras de cervezas y los agentes de comercialización mayorista de esos bienes.

Particularidades de la Percepción IB Bs.As. 59/98:

Esta percepción se calculará en forma independiente de las anteriores. Si indica una alícuota, ésta es considerada en las cotizaciones independientemente de la alícuota ingresada para los artículos (salvo en aquellos artículos en los que no active este campo y que en ningún caso calcularán la percepción).  
Si usted activa el parámetro pero no ingresa ninguna alícuota, el sistema considera las alícuotas ingresadas en cada uno de los artículos.  
Esta percepción tiene algunas diferencias respecto de las anteriores en cuanto a la base de cálculo. Si el cliente potencial es Responsable Inscripto, se considera sólo el neto gravado como base para aplicar la percepción. En los demás casos se considera el neto gravado más el IVA.

Incluye impuesto interno: en el caso de liquidar el impuesto sobre los ingresos brutos correspondiente a la provincia de Buenos Aires 59/98, puede agregar a la base del cálculo descripta anteriormente para cada cliente potencial, los impuestos internos que se liquiden en la cotización.  
Es importante considerar que para una correcta administración de las percepciones de ingresos brutos, no se deben repetir las alícuotas entre las distintas percepciones, por lo que recomendamos definir rangos de percepciones diferentes para cada caso.

Alícuota percepción no categorizado: este campo es obligatorio para aquellos clientes potenciales que se definan como 'Sujetos no Categorizados'.  
En ese caso, ingrese un código de alícuota de percepción (del 11 al 20). Esta alícuota se aplica sobre el total del comprobante o sobre todos los conceptos gravados más impuestos que figuren en la cotización, pudiéndose discriminar e imprimir a través de una variable de impresión. 

###### Percepciones definibles

Si el cliente liquida percepciones definibles es necesario asociarle un código previamente definido en el proceso [Clasificación percepciones definibles](https://ayudas.axoft.com/25ar/clasifpercepdefin_gv).  
El campo Alícuota no es dato un obligatorio, si no se completa se considerará para liquidar el impuesto, el código que tenga asignado en el artículo.  
Si se completa el código de alícuota, ésta será considerada en los comprobantes, independientemente de la alícuota ingresada para los artículos (salvo en aquellos artículos en los que no se parametrice la percepción definible y que en ningún caso calcularán percepción).  
Si se asigno una clasificación al cliente, para que pueda calcularse la percepción, el artículo debe tener parametrizado la misma percepción-clasificación.

###### Formularios

Indique el formulario (archivo .Typ) a utilizar para la impresión de [Facturas](https://ayudas.axoft.com/25ar/procesofacturacion_gv); [Notas de crédito](https://ayudas.axoft.com/25ar/emisionc_gv) y/o [Notas de débito](https://ayudas.axoft.com/25ar/emisionnd_gv), independientemente que el comprobante sea electrónico o no electrónico, de exportación o de uso en el mercado local.  
El sistema tiene en cuenta por defecto, el formulario 'Habitual', pero usted puede elegir 'Otro'. En este último caso, seleccione el Nombre del TYP a considerar.

###### Parametrización contable

Acceda a informar los parámetros contables si previamente configuró que no integra con Contabilidad en caso contario acceda a parametrización contable de Clientes potenciales.

Cuenta cliente: señala la cuenta contable asociada al cliente para el total del comprobante, para su imputación automática en los asientos.  
Si el campo está en blanco, el asiento tomará la cuenta genérica asignada al valor 'TO' según la definición del tipo de asiento utilizado.

Centro de costo cliente: se utiliza para indicar a qué centro de costo se aplicarán los importes destinados a la cuenta contable del cliente. Se pedirá su ingreso sólo si el campo Cuenta no está en blanco.  
El ingreso del campo Centro de Costo es optativo y pueden presentarse las siguientes situaciones:

  * Si éste queda en blanco, habiéndose ingresado un código de cuenta contable, los importes destinados a la cuenta quedarán sin asignación de centro de costo.
  * Si los campos Cuenta y Centro de Costo quedan en blanco, al realizarse el proceso [Pasaje a Contabilidad](https://ayudas.axoft.com/25ar/pasajecontab_gv), el asiento generado tomará la cuenta genérica asignada según la definición del tipo de asiento utilizado y la distribución en centros de costo definida en el tipo de asiento.



La definición de los campos Cuenta y Centro de costo está relacionada con la definición de tipos de asiento en el módulo Ventas.  
Para mayor información sobre cómo definir el valor 'CL' a fines de generar el asiento contable con el total del comprobante en la cuenta del cliente, consulte el ítem [Tipos de asiento](https://ayudas.axoft.com/25ar/tipoasiento_gv).

##### Comprobantes electrónicos

Tango nexo

Para publicar la información del cliente en Tango nexo complete los siguientes datos:

Publica información: ingrese 'S' en el caso que desee que el cliente publique información en Tango nexo, caso contrario elija la opción 'N'.

Correo electrónico para enviar invitación: en caso que el cliente publique información en Tango nexo, ingrese una dirección de correo electrónico válida a la cual enviarle la invitación para ingresar en la nube para poder visualizar la información publicada.

Envío de comprobantes electrónicos

Si su empresa emite comprobantes electrónicos complete los siguientes datos:

Forma de envío: indique la modalidad de envío a su cliente de los comprobantes electrónicos que usted emita.  
Puede optar por una de las siguientes opciones: 'Siempre' (*), 'Según talonario', 'Sólo publica en Tango nexo', 'E-mail' (**), 'E-mail/Papel' (**) o 'WhatsApp' (***).

**(*):** se muestra cuando no se utiliza el envío de comprobantes por correo electrónico por no tener configurada la solapa _"Comprobantes electrónicos"_ de [Parámetros de correo electrónico](?p=11965).  
**(**):** se muestra cuando se utiliza el envío de comprobantes por correo electrónico por tener configurada la solapa _"Comprobantes electrónicos"_ de [Parámetros de correo electrónico](?p=11965).  
**(***):** se muestra cuando se encuentra habilitado el envío de comprobantes por **WhatsApp** en [Parámetros de WhatsApp](?p=30221).

Según talonario: toma la configuración definida en el talonario.

Solo publica en Tango nexo: el cliente únicamente accederá a sus comprobantes electrónicos a través de Tango nexo.

Comprobantes Electrónicos de Exportación

Si usted emite comprobantes electrónicos de exportación (según R.G. 3066) y necesita definir una parametrización particular para el cliente, complete los datos que se mencionan a continuación.

Identificación tributaria: indique la clave de identificación tributaria del cliente.

Idioma del comprobante: elija el idioma en el que confeccionará los comprobantes de exportación (facturas, notas de crédito y notas de débito) para su cliente. Usted puede optar por el idioma definido como parámetro general o bien, elegir otro diferente.  
Las opciones posibles son: 'P' – Parámetro General, '1' – Español, '2' – Inglés o '3' – Portugués.  
Por defecto, el sistema considera el idioma definido en la solapa Comprobantes electrónicos de [Parámetros de Ventas](?p=19401).

Detalle de los artículos: defina si tiene en cuenta la descripción de los artículos ingresada en cada 'Artículo' o bien, la definida en la relación 'Cliente – Artículo'. Por defecto, el sistema considera lo definido en [Parámetros de Ventas](?p=19401).

Incluye comentarios de los artículos: indique si en la descripción del producto a informar a la AFIP incluye los comentarios ingresados para cada artículo desde el proceso Artículos del módulo Stock. Por defecto, el sistema considera lo definido en el proceso [Parámetros de Ventas](?p=19401).

__Nota

Recuerde que para operar con comprobantes electrónicos, debe parametrizar correctamente los campos respectivos en la solapa _Comprobantes electrónicos_ de [Parámetros de Ventas](?p=19401).
