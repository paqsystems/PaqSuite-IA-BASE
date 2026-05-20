# Cuentas de Tesorería

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_nexocobr_gv/?p=10235/

## Contenido

# Cuentas de Tesorería

Este proceso permite el ingreso, eliminación y modificación de las cuentas que usted desee imputar y analizar desde el módulo Tesorería.

No pueden eliminarse cuentas que estén utilizadas en movimientos.  
El código de cuenta no es modificable y el tipo de cuenta y sus atributos sólo se pueden modificar si la cuenta no tiene movimientos.

__Nota

Para trabajar en forma integrada con **Ventas** y **Compras** / **Proveedores** es indispensable que estén definidas por lo menos tres cuentas, por ejemplo; _Deudores_ , _Caja_ y _Proveedores_ para poder realizar las imputaciones contables elementales de un movimiento de fondos.

##### Principal

Para dar de alta una cuenta, solo necesita ingresar los datos de identificación:

Código de cuenta: hasta 11 dígitos numéricos. Este código es determinado por usted y es el que se utiliza para la imputación de las cuentas. No es necesario que sean los mismos códigos utilizados en el sistema contable. Este código determina el ordenamiento de las cuentas en los informes que brinda el sistema.

Descripción: nombre de la cuenta.

Tipo de cuenta

Las cuentas se clasifican en cuatro tipos: 'Banco', 'Cartera', 'Tarjeta' y 'Otras'. En base a esta clasificación se determina el comportamiento de la cuenta. Por ello, es importante que esta definición sea correcta y previamente analizada.

[Más información (definiciones previas)...](?p=10130/#definiciones-propias-de-tesoreria)

Representa fondos: si la cuenta es de tipo 'Otras', puede indicar si involucra valores de fondos por sí misma. Active este parámetro (tildando este campo) si la cuenta representa disponibilidades, por ejemplo, Caja; Caja en Moneda Extranjera. Para los otros tipos de cuenta, este valor es automático.  
En el caso de cuentas que no representan dinero por si mismas, pero se utilizan como contracuentas de movimientos de tesorería (por ejemplo: Deudores por Ventas, Proveedores, etc.), no active este parámetro.

Para mayor detalle sobre la implicancia de este parámetro, sugerimos consultar la ayuda del proceso [Cierre de caja](?p=10148).  
Esta referencia expresa lo siguiente: "Para las cuentas de tipo 'Otras de fondos' hay un tratamiento especial, por ser las cuentas que representan la caja propiamente dicha. Para estas cuentas, los saldos resultantes en un cierre son almacenados en un archivo al que tiene acceso un usuario autorizado. Estos saldos son tomados como apertura de estas cuentas en el próximo cierre que se realice".

Exportable: indica si la cuenta interviene en la exportación de comprobantes de tesorería para continuar circuitos. Esta configuración se realiza para las cuentas de tipo 'Tarjeta', 'Cheques' u 'Otras de fondos'.

Asocia unidades: active este parámetro para indicar que la cuenta está expresada en una moneda distinta a la corriente.

Conciliable: indica si la cuenta puede usarse en el proceso [Conciliación bancaria](?p=10169). Esta configuración se aplica para las cuentas de tipo 'Otras' o''Banco'.  
Es posible modificar una cuenta, dejándola como no conciliable, siempre y cuando no tenga conciliaciones previas.

Registra facturas de crédito: se solicita para cuentas de tipo 'Otras' de Tesorería. Active este parámetro únicamente si usted trabaja con esa modalidad y posee los módulos Ventas y/o Compras, ya que los procesos Aceptación y Cancelación de facturas de crédito de esos módulos necesitan de una cuenta especial para el tratamiento de estos documentos.

__Nota

Recomendamos leer la implementación de facturas de crédito en **Ventas** y **Compras**.

Código de moneda: indique la moneda de expresión de la cuenta. Si la cuenta no asocia unidades, el sistema asigna la moneda corriente; de lo contrario, propone por defecto la moneda extranjera, permitiendo su modificación por otra moneda. Para mas información sobre las monedas disponibles consulte Monedas.  
Recuerde que el sistema determina cuál es la moneda corriente y extranjera de acuerdo a lo indicado en [Parámetros de Tesorería](?p=10293).  
Los cheques emitidos de una cuenta tipo 'Banco' serán en la moneda definida para esa cuenta; los cheques de terceros se asumen en la moneda de la cartera a la que ingresan y, los cupones son en la moneda de la cuenta de tipo 'Tarjeta' que se imputa al generarlos.

Código de medio de pago según RG 1547: indica el medio de pago asociado a la cuenta en pantalla, según RG 1547.

Código de operación: puede asociar un código de operación a una cuenta según su tipo.

Código de cuenta para transferencia: esta cuenta es de utilidad en la transferencia de valores a caja central desde el facturador y es necesario agrupar el importe a transferir en una sola cuenta y no en la individual por cada caja.

Saldo Inicial

Fecha de saldo: ingrese este campo sólo si desea inicializar la cuenta con un saldo. La inicialización no es obligatoria.

Moneda corriente, Moneda extranjera, Moneda de la cuenta: ingrese el saldo inicial en cada una de las monedas. El saldo inicial en moneda de la cuenta es editable sólo si la moneda de la cuenta no coincide con la moneda corriente o la extranjera.  
Sólo puede ingresar los saldos iniciales si la cuenta no tiene movimientos o todos ellos han pasado a histórico. El sistema los actualiza en forma automática, cada vez que se realice un pasaje a histórico, para dejar reflejado el arrastre de los movimientos depurados.  
Los saldos se podrán modificar solo si el usuario cuenta con permisos para ello. Para mas información consultar [Administrador del sistema](?p=9063).

Datos para facturación al contado

Estos datos solo se solicitaran para cuentas tipo 'Carteras' y 'Otras':

Porcentaje de recargo: indica el porcentaje de recargo a aplicar en facturación para la cuenta, cuando se utiliza un perfil de facturación con modalidad 'Cobro al Contado'.

Porcentaje de bonificación: indica el porcentaje de bonificación a aplicar en facturación para la cuenta correspondiente, cuando se utiliza un perfil de facturación con modalidad 'Cobro al Contado'.

__Nota

Para las cuentas es posible configurar un descuento o un recargo a aplicar, los que se reflejarán en el total del comprobante.

Datos para Tango Cobranzas / Tiendas

Forma de cobro: permite relacionar la cuenta con un sistema de pagos en línea. Esta opción sólo estará editable si la cuenta es de tipo ‘Otra’, representa fondos y usa moneda corriente. Para más información, consulte la [Guía de implementación sobre Tango Cobranzas](?p=27349).

Datos para archivo shopping

Clase de cuenta: si en el proceso [Parámetros de Ventas](?p=19401) usted configuró la modalidad shoppings para el "Grupo Alto Palermo", "Solar de la Abadía", "Nuevo Centro", "Grupo IRSA - Interfaz Fiserv", "Grupo Fortin Maure - Interfaz Solutions Malls" u otro similar a éstos, debe indicar la forma de pago asociada a la cuenta, para informar en el archivo ASCII o en el JSON que se enviará a través del servicio, según la modalidad seleccionada.

Detalle de medios de pago en archivos ASCII

Para el Grupo Alto Palermo los medios de pago a informar en el archivo ASCII son:

**E** | Efectivo  
---|---  
**T** | Tarjeta  
**A** | Alto Check  
**C** | Cheques  
**D** | Dólares  
**K** | Cuenta corriente  
**O** | Otro medio de pago  
  
Para el Solar de la Abadía o Nuevo Centro los medios de pago a informar en el archivo ASCII son:

**1:** | Efectivo  
---|---  
**2:** | Tarjeta  
**3:** | Cheque  
**4:** | Efectivo dólar  
**6:** | Otro medio de pago  
  
Para el Grupo IRSA - Interfaz Fiserv los medios de pago a informar son:

**E** | Dinero (local)  
---|---  
**T** | Tarjeta  
**C** | Cheque  
**D** | Dólares  
**K** | Cuenta  
**Q** | Medio Electrónico/Billetera Digital  
**R  
** | Gift Card  
**O** | Otro medio de pago  
  
Para el Grupo Fortin Maure - Interfaz Solutions Malls los medios de pago a informar son:

**EF** | Pago en efectivo  
---|---  
**DB** | Pago con tarjeta de débito  
**CD** | Pago con tarjeta de crédito  
**TR** | Pago con transferencia bancaria  
**CC** | Venta en cuenta corriente  
**OT** | Otros medios de pago  
  
Códigos de tarjeta a informar

Código de tarjeta Shopping: para el Shopping Solar de la Abadía, Nuevo Centro, Grupo IRSA - Interfaz Fiserv, debe definir además del medio de pago los códigos de tarjeta a informar en el archivo ASCII cuando la cuenta es de tipo 'Tarjeta'.

Para el Solar de la Abadía o Nuevo Centro los códigos de tarjeta son:

**AG** | Argencard  
---|---  
**MC** | Mastercard  
**VI** | Visa  
**DI** | Diners  
**AM** | American Express  
**TS** | Tarjeta Shopping  
**SC** | Tarjeta Shopping Cash  
**TN** | Tarjeta Naranja  
**CA** | Cabal  
**CD** | Cabal 24  
**FR** | Carta Franca  
**CR** | Credencial  
**EL** | Electrón  
**MA** | Maestro  
**LI** | Líder  
**PC** | Provencred  
**IC** | Italcred  
**MI** | Mira  
**TV** | Tarjetas Nevadas  
  
Para el Grupo IRSA - Interfaz Fiserv los códigos de tarjeta son:

**AM** | American Express  
---|---  
**AG** | Argencard  
**TA** | Argenta  
**PL** | C&A Private Label  
**CA** | Cabal  
**CD** | Cabal Débito (24 Horas)  
**CT** | Carta Auto  
**FR** | Carta Franca  
**CS** | Castillo  
**CE** | Cencosud  
**CL** | Clipper  
**CR** | Credencial  
**CI** | Credial  
**CC** | Credicash  
**CI** | Credicred  
**CM** | Credimas  
**TF** | CRM Falabella  
**DT** | Data 2000  
**DI** | Diners  
**EB  
** | Elebar  
**EM** | Empresur  
**FV** | Favacard  
**FE** | Fedil  
**IC  
** | Italcred  
**KD  
** | Kadicard  
**LI  
** | Líder  
**CO  
** | Tarjeta Confiable  
**MA  
** | Maestro  
**SM** | MAS  
**MC** | Mastercard  
**MI  
** | Mira  
**NT  
** | Nativa  
**TV** | Nevada  
**NE** | Nexo  
**NC** | Novacash  
**OG** | Okey Group  
**PR** | Primicia  
**PC** | Provencred  
**SA** | Saltcard  
**SL** | Salto 96  
**SC  
** | Shopping Cash  
**SO** | Sol  
**SR** | Sucredito  
**AZ  
** | Tarjeta Azul  
**TN** | Tarjeta Naranja  
**TN** | Tarjeta Naranja Plan Zeta  
**NO** | Tarjeta Platino  
**TS  
** | Tarjeta Shopping  
**VI  
** | Visa  
**EL** | Visa Débito  
**GC  
** | Giftcard APSA  
**GO  
** | Giftcard Otros  
  
De todas maneras es posible configurar en la cuenta, otro código que no exista en la lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo tarjeta.

Datos adicionales para cuentas de tipo 'Tarjeta':

Código de tarjeta: indique a que código de tarjeta se asocia la cuenta.

Descripción del plan: ingrese la descripción del plan que representa la cuenta.

__Nota

Para asociar la cuenta a una tarjeta que utiliza conexión con POS, la moneda de la cuenta debe ser 'Corriente' (CTE)."] 

Código de plan habitual: si el código de tarjeta ingresado utiliza conexión con POS, indique el código de plan habitual asociado a la terminal POS.  
Caso contrario, es posible ingresar la descripción del plan que representa la cuenta.  
Para más información, consulte el tópico [Operatoria con Terminales POS de tarjetas de crédito y débito](?p=10559/#datos-que-debe-completar-para-emitir-un-cupon).

Cantidad de cuotas: indique la cantidad de cuotas del plan. Este valor será tomado por defecto, pero puede modificarse al confeccionar un cupón.

Cuota redondeo: indique la cuota a la que se le asigna el redondeo si la división no es exacta. Puede ser la primera o la última cuota.

Días para acreditación: indique cuantos días corridos transcurren desde el depósito de los cupones generados con este plan y su cobro.

Porcentaje de comisión: es el descuento o comisión que se retiene al establecimiento.

Tipo de numeración de cupones: puede optar por 'Automática', 'Según POS' o 'Manual'.

  * Manual: elija esta opción si desea ingresar un número de cupón cada vez que se generan. De esta manera, podrá tener asociada a cada transacción el número real de cupón.
  * Automático: utilice esta opción si no le interesa registrar los datos de identificación de un cupón, o si no desea ingresar el número, dejando que el sistema numere automáticamente a partir de un número indicado. En este caso, el número de cupón almacenado no tiene por qué coincidir con el real.
  * Según POS: utilice esta opción si la tarjeta asociada a esta cuenta está configurada para la conexión con POS Ingénico Modelo I5100. En este caso, la numeración de los cupones será administrada por la terminal POS, registrándose en el sistema cada transacción con el número de terminal, lote y número de cupón.



__Nota

Ante la ocurrencia de un error en la conexión con la terminal **POS Ingénico** durante la cobranza, podrá registrar los datos del cupón en forma manual mediante la tecla de función <F7>.

Próximo número de cupón: si optó por la numeración automática, ingrese un número para inicializar el próximo número de cupón a asignar.

##### Cuenta bancaria

Tipo de cuenta bancaria: define el tipo de cuenta como 'Caja de ahorro', 'Cuenta corriente' o 'Cheque diferido'.

Cuenta asociada (cheques diferidos): este dato solo se solicita para cuentas bancarias tipo 'Cheque diferido' e indica cuál es la cuenta corriente bancaria en la que se descontarán esos valores, llegada su fecha de cobro. Por ello, indique un código de cuenta definida como 'Banco' / 'Cuenta Corriente'. La cuenta asociada es modificable si aún no se han emitido cheques diferidos.  
Si la cuenta es de cheques diferidos, los campos: tomarán sus valores directamente de la cuenta asociada.

__Nota

Una cuenta corriente puede estar asociada sólo a una cuenta de cheques diferidos, ya que conceptualmente son la misma cuenta bancaria.  


Banco: ingrese el código de banco asociado a la cuenta.  
Se solicitarán los datos de identificación de la cuenta bancaria: Sucursal, Nro. de cuenta, Digito verificador y el CBU.

Límite de giro en descubierto: este dato solo se solicitara para las cuentas corrientes.

__Nota

**Caja de ahorro / Cuenta corriente / Cheques diferidos** : solamente las cuentas que se definan como cuenta corriente o cheques diferidos estarán habilitadas para emitir cheques.

##### Tarjetas

Estos datos solo se solicitan para cuentas de tipo 'Tarjeta'.

Código de tarjeta: ingrese el código de tarjeta que asociará a la cuenta de tesorería.

Grilla de planes referidos a la tarjeta seleccionada: puede ingresar cada uno de los planes o bien, cargarlos en forma automática mediante el botón "Asignar todos los planes".

**Ejemplo...**

En este caso buscamos y seleccionamos la tarjeta 'Visa'.

**1** | MasterCard  
---|---  
**2** | Visa  
**3** | Visa electrón  
  
Para la tarjeta seleccionada cargamos dos planes.

**1** | Plan 1 pago  
---|---  
**2** | Plan cuotas  
  
Tanto la tarjeta como los planes agregados están asociados a la cuenta que estoy dando de alta.  
Para más información consulte la [Guía de tarjetas de crédito y débito](?p=10559).

##### Datos contables

Cuenta contable: ingrese el código de cuenta contable a la que se imputarán los movimientos de la cuenta.  
Si está habilitada la verificación de las cuentas contables en [Parámetros de Tesorería](?p=10293) se controlará que el código ingresado pertenezca al plan de cuentas definido en el sistema contable y que corresponda a una cuenta imputable. De no realizarse esta verificación, es su responsabilidad asignar correctamente este código. Por defecto, el campo toma el valor del código de cuenta ingresado.  
Se podrá asignar más de una cuenta del módulo Tesorería a la misma cuenta contable. Esto permite tener un análisis detallado en Tesorería y un análisis global en Contabilidad.

**Ejemplo...**

**Código de Cuenta** | **Descripción** | **Código imputación Contable**  
---|---|---  
1 | Caja 1 | 8  
2 | Caja 2 | 8  
7 | Caja 3 | 8  
  
Si en el sistema contable la cuenta 8 equivale a Caja, las tres cuentas se imputarán sobre ella.

Descripción: descripción de la cuenta sobre la que se imputan los movimientos. Su ingreso tiene como objetivo incluir esta descripción en el listado de asientos resumen.

Asigna centros de costo: active este parámetro si los importes de la cuenta se distribuirán en centros de costo.  
Si una cuenta asigna centros de costo, se podrá ingresar su apropiación habitual (detalle de centros de costo a aplicar y el porcentaje respectivo). La suma de los porcentajes en ningún caso, superará el 100% ni se podrán ingresar porcentajes negativos.

__Nota

Agilice las imputaciones utilizando reglas habituales de distribución.

Si el parámetro general Verifica la Existencia de las Cuentas Contables está activo, este campo no se edita; por lo tanto, la cuenta de tesorería se comportará de acuerdo a como esté definida la cuenta en Contabilidad, con respecto a la asignación de costos.

En cambio, si el parámetro general no está activo, este campo se edita, pero una cuenta sólo podrá dejar de asignar centros de costo si no existen movimientos de apropiaciones asociados.

Para mas información consulte Relación Maestro - Sucursales.

##### Clasificación

Código de agrupación: este código permite asignar a cada cuenta un número de agrupación. Las agrupaciones son definidas por usted, de acuerdo a su necesidad de análisis sobre las cuentas.  
Para mas información consultar [Agrupaciones](?p=10135).

__Nota

Este código es modificable, permitiendo generar nuevas agrupaciones.

Clasificador de cuentas: se visualizaran todas las clasificaciones definidas para las distintas cuentas de tesorería.

__Relación Maestro - Sucursal

Si se encuentra trabajando en una empresa definida como casa central, en el momento de crear una cuenta, tendrá la opción de relacionar la cuenta a una o varias sucursales.

La modalidad de relacionar cuenta con sucursales depende de la configuración de [Parámetros de transferencias](?p=9434) del módulo Central, pudiendo ser:

  * Automática: se genera la relación con todas las sucursales en el momento del alta.
  * Manual: luego de procesada el alta, el usuario puede generar la relación con la/las sucursales.



**Adjuntos**

Desde aquí se pueden agregar los diferentes archivos asociados al artículo. Sólo se permiten archivos "txt, md, ini, text, sql, json, html, bak, bkp, exe, msi, zip, rar, 7z, tar, gz, doc, docx, xls, xlsx, ppt, pptx, pdf, bmp, jpg, jpeg, gif, png, avi, mp4, wav, mp3, pfx".

Los archivos podrán descargarse, eliminarse o acceder a una vista previa para ver su contenido, desde esta misma pantalla.

##### Contenidos relacionados

  * [Video sobre automatización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Video sobre conciliación bancaria](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/concilbancaria_sb_vid/)

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre integración con POSNet + QR + PCT](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrposnet-qr-pct_gral_vid/)

  * [Video sobre integración con dispositivos de tarjeta](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrdisptarjeta_gral_vid/)

  * [Video sobre multicaja en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/multicaja_gv_vid/)

  * [Video sobre parámetros de Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/parametros_cp2_vid/)

  * [Video sobre parámetros de Tesorería](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/parametrosb_sb_vid/)

  * [Videos sobre cierres de caja](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/cierrecaja_gral_vid/)

  * [Videos sobre conciliación bancaria automática](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/concilbancautom_sb_vid/)

  * [Videos sobre el Facturador](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/facturador_gv_vid/)

  * [Videos sobre imputaciones contables](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/impcont1_gral_vid/)

  * [Videos sobre integración con Mercado Pago®](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/marcadopago_gral_vid/)

  * [Videos sobre parámetros de Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/parametros_gv_vid/)

  * [Videos sobre transferencia de valores](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfvalor_gral_vid/)
