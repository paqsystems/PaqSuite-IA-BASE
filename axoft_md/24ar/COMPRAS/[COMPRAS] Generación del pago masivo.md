# Generación del pago masivo

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_integrcontabl_cp/?p=15557/

## Contenido

# Generación del pago masivo

Mediante este proceso, usted visualiza en una grilla, todos los pagos masivos que fueron ingresados / autorizados (según la definición del parámetro general Autoriza pagos masivos) y parcialmente pagados.

Cuenta con opciones de filtros que facilitan la búsqueda de la información.  
Si presiona el botón "Actualizar", se cargan en la grilla, todos los pagos masivos que responden al criterio de búsqueda indicado. Éstos se presentan ordenados por número de pago masivo, tomando como inicial, el más antiguo.  
Haga doble clic sobre uno de los pagos masivos de la grilla, para consultar en forma detallada todos los comprobantes que lo conforman.  
Para generar las ordenes de pago a todos los proveedores involucrados en el pago masivo, haga un clic en la columna Pagar (presentada como un hipervínculo). Automáticamente, se mostrará la pantalla de Generación del pago masivo, donde visualizará los datos que fueron cargados en el momento de ingresar el pago masivo (moneda en la que se realizarán las ordenes de pago, cotización estipulada, total del pago expresado en moneda corriente y extranjera contable).  
El sistema generará una orden de pago por cada proveedor incluido en el pago masivo.  
Si posee el módulo Tesorería, puede optar por generar el pago masivo con una misma forma de pago para todo el pago, o utilizando el medio de pago definido para cada proveedor en el proceso [Actualización de proveedores](https://ayudas.axoft.com/24ar/proveedores_cp2). Seleccione Ingresa medio de pago por proveedor para utilizar esta opción.  
En el caso de optar por un único medio de pago para toda la operación, usted deberá indicar los [datos de fondos generales para el pago masivo](https://ayudas.axoft.com/24ar/pagmasgeneracion_cp2#datfongralpagomas).  
En el caso de ingresar medios de pago por proveedor, usted deberá indicar los datos particulares, en la [grilla de datos de fondos por proveedor](https://ayudas.axoft.com/24ar/pagmasgeneracion_cp2#grilladatofondoprov).  
Una vez que confirma la selección, mediante el comando Aceptar se efectúa el pago masivo. Se genera e imprime una orden de pago para cada proveedor y se actualiza la cuenta corriente. Los comprobantes involucrados quedarán 'Cancelados' e 'Imputados' y se generarán los movimientos correspondientes en el módulo Tesorería (si se encuentra instalado).  
Los cheques emitidos deberá imprimirlos desde el proceso [Impresión de cheques](?p=10330) del módulo Tesorería.

Si usted incluyó en el _pago_ comprobantes marcados con diferencias serán cancelados en esta instancia. En caso de que el parámetro general _Elimina Diferencia al Pagar_ se encuentre activo, su estado será cambiado a 'Sin diferencias', como si estas nunca hubieran existido, caso contrario, la diferencia será registrada como 'Resuelta'.  
Si los proveedores seleccionados tienen configuradas retenciones automáticas, éstas serán registradas e impresas junto a las ordenes de pago.

Seleccione un destino de impresión ('Impresora' o 'Archivo') para las órdenes de pago y otro para las retenciones y/o constancias provisionales de retención.

__Nota

Si parametrizó el cálculo automático de retenciones, es necesario que desde los procesos de _Códigos de retención_ defina la _Cuenta de Tesorería_ defecto para cada retención. Caso contrario, se asignará el total del pago masivo a la cuenta configurada como _Medio de pago habitual_.

__Nota

El sistema no tendrá en cuenta en este proceso, los perfiles de Tesorería definidos.

El sistema valida que la fecha de la orden de pago sea posterior a la Fecha de cierre para comprobantes definida en el proceso [Parámetros de Tesorería](?p=10293) y, posterior a la Fecha de cierre para órdenes de pago definida en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) del módulo Compras.

Clasificación: es posible clasificar los pagos, para ello es necesario definir en [Clasificación de comprobantes](?p=11840) las clasificaciones habilitadas para dicho comprobante. Para activar este parámetro se debe ir a [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2).

En caso de integrar con Contabilidad ([Herramientas para integración contable](?p=11936)) al momento de generar el pago, se va a generar el asiento contable si el [tipo de comprobante](?p=10279) y los [parámetros contables](?p=10832) del módulo Tesorería fueron configurados para ello. Para obtener mayor información sobre la generación del asiento contable, acceda a [Imputación contable con Contabilidad](https://ayudas.axoft.com/24ar/comprobimputcontcont_cp2).

Filtros para la generación del pago masivo

Los filtros posibles de aplicar para la selección de pagos masivos a generar, son los siguientes:

  * **Por fecha:** elija el tipo de fecha a considerar (fecha de ingreso, fecha estimada de pago o fecha de pago) e ingrese un rango de fechas.
  * **Por número:** permite ingresar un rango de números de pagos masivos.



Contenido de la grilla para la generación del pago masivo

En la consulta de pagos masivos, el [contenido de la grilla](https://ayudas.axoft.com/24ar/pagmasmodificac_cp2#contenido) tiene iguales características que las mencionadas en el proceso [Modificación de pagos masivos](https://ayudas.axoft.com/24ar/pagmasmodificac_cp2).

Datos de fondos generales para el pago masivo

Utilice esta opción cuando desee utilizar un medio de pago en general para todo el pago masivo.  
Si posee el módulo Tesorería, puede indicar como medio de pago, solamente cuentas de tipo 'Otras' o de tipo 'Banco'.  
Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2), usted indicó que edita datos de tesorería, puede cambiar las cuentas de Tesorería propuestas y los datos del cheque (si paga con una cuenta de tipo 'Banco'). Caso contrario, se considera por defecto, lo definido en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2).

__Nota

Si usted no posee el módulo **Tesorería** , estos datos no se encontrarán habilitados.

En el caso que el Medio de pago habitual elegido sea una cuenta tipo 'Banco', es posible optar por emitir cheques. En ese caso, se solicitarán los datos correspondientes a la chequera a utilizar y desde qué número de cheque se comenzará a emitir.  
Ingrese la cantidad de días, para que el sistema calcule la fecha de vencimiento del cheque, o bien, puede optar por ingresar directamente la fecha, en tal caso el sistema realizará automáticamente el cálculo de los días de plazo.  
El sistema valida que la chequera ingresada esté disponible; que corresponda a la cuenta elegida como Medio de pago habitual y, que tenga cheques en cantidad suficiente como para realizar el pago para todas las órdenes de pago incluidas en el pago masivo. Si usted seleccionó una cuenta bancaria que utiliza cheques diferidos, se validará también, que la fecha de vencimiento de los cheques sea mayor a la fecha de generación del pago.

Grilla de datos de fondos por proveedor

Utilice esta opción cuando desee utilizar los medios de pagos definidos para cada poveedor en el proceso [Actualización de proveedores](https://ayudas.axoft.com/24ar/proveedores_cp2).

__Nota

Si usted no posee el módulo **Tesorería** , estos datos no se encontrarán habilitados.

Al seleccionar la opción Ingresa medio de pago por proveedor, usted visualizará una grilla que cuenta con un renglón para cada proveedor interviniente en el pago masivo.  
Esta grilla muestra los datos de tesorería ingresados para cada proveedor y, en el caso de no estar definidos, toma los datos de tesorería ingresados para Medio de pago habitual en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2).  
Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) usted indicó que Edita datos de Tesorería, puede cambiar las cuentas de Tesorería propuestas para cada proveedor, y los datos del cheque (si paga con una cuenta de tipo 'Banco'). Caso contrario, se considera por defecto, lo definido en el proceso [Actualización de proveedores](https://ayudas.axoft.com/24ar/proveedores_cp2), y estos datos sólo podrán ser visualizados, pero no editados.  
La grilla esta conformada por las siguientes columnas:

Proveedor y Razón social: indican los datos del proveedor para el que se generará la orden de pago. Estos datos surgen de los comprobantes que conforman el pago masivo y no son editables.

Cuenta a debitar: la columna indica la cuenta principal contra la que se ingresarán contracuentas. Este campo toma por defecto la cuenta principal definida para el proveedor, o la definida en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) si es que la primera opción no tuviera valor definido. Es posible cambiar la cuenta propuesta por otra cuenta de tipo 'Otros'.

Medio de pago: esta columna muestra el medio de pago habitual ingresado en el proceso [Actualización de proveedores](https://ayudas.axoft.com/24ar/proveedores_cp2), o el definido en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) en el caso de que el proveedor no lo tenga definido. Es posible cambiar la cuenta propuesta por otra cuenta de tesorería.

Con cheque: si usted seleccionó una cuenta de tipo "bancos" puede indicar si el pago se realizará con cheque, o solo registrará un movimiento de egreso bancario. En el caso de cuentas bancarias que utilizan cheques diferidos, el pago 'Con cheque' será obligatorio.

Chequera: en el caso de haber seleccionado pago 'Con cheque' el sistema le propondrá por defecto la primer chequera disponible para la cuenta de bancos elegida.  
Podrá seleccionar otra chequera disponible, siempre que tenga el sistema configurado como para editar los datos de tesorería.

Importante:

El sistema generará el pago utilizando siempre el primer cheque disponible en la chequera seleccionada. En el caso de que usted precise especificar un número de cheque puntual, puede ingresarlo seleccionando la opción _Ingresa Nº de cheque por proveedor_.  
Podrá seleccionar cualquier número de cheque, siempre y cuando esté disponible, y no se haya utilizado este número, en el mismo pago, para otro proveedor.

Días / Fecha: ingrese la cantidad de días, para que el sistema calcule la fecha de vencimiento del cheque, o bien, puede optar por ingresar directamente la fecha, en tal caso el sistema realizará automáticamente el cálculo de los días de plazo.  
Si usted seleccionó una cuenta bancaria que utiliza cheques diferidos, se validará también, que la fecha de vencimiento de los cheques sea mayor a la fecha de generación del pago.

Total pago / Pago en unidades: estas columnas le informan el total de la orden de compra que se generará al proveedor.

Confirme los medios de pagos por proveedor seleccionados, pulsando <F10> o "Aceptar".

Clasificación de comprobantes: seleccione la clasificación que desea para el proveedor.

Movimientos de Tesorería en la generación de pagos masivos

En este momento, el sistema activa directamente el módulo Tesorería para registrar tantos Ingresos de comprobantes de clase 2 (Pagos) como ordenes de pago estén incluidas en el pago masivo.  
El sistema permite registrar la forma de pago en cualquier moneda, independientemente de la moneda en la que se haya emitido la factura. En este caso, todas las órdenes de pago se registrarán en la moneda indicada en el pago masivo.  
Recuerde que cada cuenta tiene asociada una moneda de expresión, cuya cotización se toma directamente de Tesorería (a excepción de la moneda extranjera que se toma de la orden de pago y no es modificable durante el ingreso de cuentas).  
El sistema verifica que se cancele el total del comprobante en su moneda de expresión, siendo la otra moneda una mera reexpresión.  
Por ejemplo, si ingresa un pago masivo en moneda corriente, el sistema verificará que se cancele el total de la orden de pago en esa moneda. En caso de existir diferencia de redondeo en la otra moneda, el sistema se encargará de ajustarla durante la grabación del comprobante.

Impresión de Órdenes de Pago y Retenciones

Una vez confirmado el ingreso de datos, el sistema da opción a imprimir la orden de pago, según el formato definido por usted y guardado en el archivo PROV.TYP.  
Se proponen como destinos de impresión, las opciones 'Pantalla' o 'Archivo'. Si se calcularon retenciones y/o constancias provisionales de retención, se imprimirán los certificados correspondientes. 

Impresión de cheques

Para imprimir los cheques asignados a un pago masivo, seleccione el proceso [Impresión de cheques](?p=10330) del módulo Tesorería y, desde el comando Listar, elija la opción 'Por pago masivo'.  
Se solicita el ingreso de un número de pago masivo.  
Se emitirán, en forma automática, todos los cheques propios relacionados con el número de pago masivo indicado.

Anulación de una orden de pago

Para anular una orden de pago relacionada a un pago masivo, primero deberá eliminar la imputación de la orden de pago con los comprobantes afectados (desde el proceso [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputacomprobante_cp2)) y luego, proceder a su anulación.  
El pago masivo relacionado a la orden de pago no cambiará su estado de 'Pagado'. Podrá generar una nueva orden de pago a cuenta desde el proceso [Pagos](https://ayudas.axoft.com/24ar/ccorringrpago_cp2) y realizar la imputación desde el proceso [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputacomprobante_cp2).  
En caso de integrar con Contabilidad ([Herramientas para integración contable](?p=11936)) al anular el pago, se va a revertir el asiento contable siempre que el comprobante de pago que se esté anulando haya generado asiento, y el comprobante de reversión del módulo Tesorería esté configurado para que genere asiento.

##### Imputación contable con Contabilidad

Los datos del asiento se exhiben en formato grilla, podrán existir más o menos líneas de acuerdo a la definición del modelo de asiento y de los artículos o conceptos ingresados en el comprobante.

Al pie de la grilla, se exhibe la suma de los importes en la columna "Debe", la suma de los importes en la columna "Haber" y la diferencia entre ambas.  
Cada renglón se compone de los siguientes datos:

Número: es el número de renglón del asiento. Este dato no es editable.

Código de cuenta: ingrese o seleccione el código de [cuenta contable](?p=11850). Este dato es de ingreso obligatorio. En caso de poder editar la cuenta o de agregar más renglones, puede seleccionar una cuenta contable habilitada para el módulo en el que se encuentra.

Descripción de cuenta: este dato se completa automáticamente al completar la columna "Código de cuenta".

Debe / Haber: por defecto el importe se completará automáticamente de acuerdo al comprobante. Usted puede editar el importe. El sistema realiza los siguientes controles: el asiento debe tener dos líneas como mínimo, el asiento debe balancear, no se permite ingresar importes negativos, ni dejar renglones con importe en cero, los importes del asiento deben coincidir con los valores ingresados en el comprobante.  
El ingreso de este dato es obligatorio.  
Si ingresa el importe en la columna "Debe", se deshabilita la edición de la columna "Haber" y viceversa.  
Haga clic en el botón "..." para abrir la calculadora.

Auxiliares: el valor de este campo depende de la definición del parámetro Usa auxiliares contables en la [cuenta contable](?p=11850) y de los tipos de auxiliares asociados a la cuenta contable desde el proceso [Actualización individual de auxiliares contables](?p=11827).  
Para ingresar o consultar las imputaciones a auxiliares y subauxiliares contables de la [cuenta contable](?p=11850) en la que está posicionado, ubique el cursor sobre esta columna y haga clic o presione la tecla <Enter>. Las imputaciones pueden ser manuales o bien, basadas en reglas de apropiación automáticas asociadas a la cuenta - tipo de auxiliar.  
Es posible ingresar el porcentaje y que se calcule en forma automática el importe, o viceversa. Si la imputación a auxiliares contables queda pendiente por el total del importe de la línea o renglón del asiento, el porcentaje será igual a 100% para el auxiliar 'Sin Asignar'.  
Usted puede seleccionar una regla de apropiación, puede elegir una regla que esté habilitada para el módulo en el cual se encuentra.  
Usted puede definir una regla por defecto y si el tipo de auxiliar es del tipo 'Manual' y no usa apertura en Subauxiliares, puede asociar un grupo de auxiliares para relación cuenta - tipo auxiliar. Esto permite habilitar sólo algunos auxiliares de todos los auxiliares creados para el tipo de auxiliar y actúa como un filtro.  
Es prioritario aplicar la regla de apropiación por defecto (ya sea del módulo o definida en Procesos generales sobre un grupo de auxiliares asociado) en el asiento. Una vez aplicada la regla, presione el botón "Ver todos los auxiliares" para reemplazar los auxiliares de la regla defecto, por los auxiliares del grupo asociado. Esto significa que el asiento:

  * O es excluyente.
  * O aplica la regla.
  * O apropia uno o más de los auxiliares del grupo de auxiliares asociados.



Si no posee un grupo de auxiliares asociados, cuando presione el botón "Ver todos los auxiliares" se agregarán todos los auxiliares sin aplicar ningún filtro o grupo.  
Para más información consulte el ítem [Actualización individual de auxiliares contables](?p=11827).

Leyenda: el sistema exhibe la leyenda definida en el modelo de asiento, será posible modificarla.

Diferencia: corresponde al total del debe menos el total del haber. No es posible grabar un asiento con diferencia distinta a cero.

Asignar diferencia <F9>: permite asignar al renglón actual la diferencia entre el total del debe y del haber.

##### Contenidos relacionados

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre órdenes de pago individual y masivo](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/ordenpago_cp2_vid/)
