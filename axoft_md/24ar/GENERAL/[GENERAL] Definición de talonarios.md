# Definición de talonarios

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=19579/

## Contenido

# Definición de talonarios

Mediante este proceso se definen los distintos talonarios a utilizar en los procesos de emisión de comprobantes (cotizaciones, pedidos, facturas, notas de débito, notas de crédito, remitos y recibos de cobranza).

##### Principal

En la solapa Principal se van a ingresar los datos comunes a todos los tipos de talonario, los mismos se detallan a continuación.

Número de talonario: número que identifica al talonario.

Descripción: es un campo opcional. Puede utilizarlo para describir el talonario definido o bien, para almacenar una leyenda a imprimir en los comprobantes que se emitan con ese talonario.

Tipo de talonario: defina aquí el tipo de talonario que desea ingresar según las opciones posibles.  
Valores posibles para este campo:

  * Preimpreso: el comprobante se emitirá sobre un formulario preimpreso.
  * Equipo fiscal: el comprobante será impreso en un equipo fiscal asociado.
  * Electrónico: solo tendrá la posibilidad de definir este tipo de talonario si usted cumple con el régimen especial de emisión de comprobantes electrónicos, y desde la solapa Comprobantes Electrónicos de Parámetros de Ventas se encuentra definida la fecha de incorporación al régimen especial de emisión y almacenamiento electrónico de comprobantes originales.  
Tenga en cuenta que al seleccionar este tipo de comprobantes se habilitará una solapa adicional con el nombre Documentos electrónicos en donde podrá configurar los datos adicionales para la generación y envío de comprobantes electrónicos a los clientes.
  * Manual: utilice esta opción para ingresar al sistema comprobantes que se generan manualmente en un formulario preimpreso.  
Tenga en cuenta que el tipo de talonario manual podrá utilizarse para los tipos de comprobante 'FAC', 'CRE', 'DEB' o 'Multipropósito'.



Comprobante

Tipo de comprobante: este campo indica los tipos de comprobante que puede utilizar cada talonario.  
Los valores posibles son: 

**Tipo Comprobante** | **Descripción**  
---|---  
FAC | Facturas  
CRE | Cualquier tipo de nota de crédito definida  
DEB | Cualquier tipo de nota de débito definida  
" " | (Tres blancos o espacios) para formularios multipropósito  
PED | Pedidos  
REC | Recibo de cobranza  
DEV | Devolución de remitos  
REM | Remitos de stock  
COT | Cotizaciones  
PED | Pedidos  
  
Consulte en el ítem [Modelos habilitados y tipos de comprobante emitidos](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv#modeloshabilit) los tipos de comprobantes que permite emitir cada modelo de equipo fiscal.

Aclaraciones:

Cabe aclarar que un talonario definido como multipropósito podrá ser utilizado sólo para facturas, notas de crédito y notas de débito en versiones sin controlador o impresora fiscal. Los remitos y los recibos llevan una numeración independiente.  
En versiones para controlador fiscal, no podrán utilizarse talonarios multiprópositos para facturas, débitos y créditos, ya que los controladores e impresoras fiscales cuentan con contadores independientes: uno para las facturas 'A', uno para las facturas 'B', uno para notas de crédito y otro para remitos.  
Para más información, consulte en el ítem [Consideraciones especiales para equipos fiscales](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv#considerespec), el título [Numeración de comprobantes en equipos fiscales](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv#numcompimprfisc).  
Los talonarios para remitos se utilizan para emitir facturas y remitos en forma independiente, o cuando se generan remitos a clientes por el proceso [Emisión de remitos](https://ayudas.axoft.com/24ar/emisionremito_gv).

Recibo-Factura: permite indicar que el comprobante emitido actuará simultáneamente como factura y recibo, unificando ambos documentos en una misma emisión. Este campo se aplica cuando se utiliza el Web Services 2, el tipo de comprobante es 'Factura' con letras 'A', 'B' o 'C', y el tipo de talonario no es 'Equipo fiscal'.  
Esta opción es excluyente con los campos Aplica RG 5762/25 y Comprobante de crédito electrónico (Ley 27.440). Si alguno de ellos se encuentra tildado, el campo Recibo-Factura permanecerá deshabilitado.

Letra/Clase: corresponde a la letra del comprobante, y representa el tipo de formulario asociado al documento. Puede ser 'A', 'B', 'C', 'E', 'M', 'R', 'T', 'X', 'U', 'V', 'W', 'Y', 'Z' o un 'blanco', recomendamos utilizar las siguientes letras para una correcta identificación de los documentos a generar.

**Letra** | **Tipo de Documento**  
---|---  
A, B, C | Para los ticket-factura y facturas fiscales.  
B, C, M | Para los documentos correspondientes a boletas de ventas.  
T | Para ser utilizado por aquellas empresas autorizadas a emitir tickets a través de sistemas computarizados según la RG 3419 de DGI.  
U, V, W, Y, Z | Representan un ticket como comprobante, y se identificarán en el subdiario de IVA con la letra 'T'.  
R, X | Para remitos.  
E | Para los documentos correspondientes a facturas de exportación.  
Blanco | Multipropósito.  
  
  * Si el talonario hace referencia a un controlador fiscal para tickets, el tipo asociado podrá elegirse entre las letras 'T' a 'Z', excluyendo las letras 'X' y 'R' de remitos.
  * Para los remitos en las impresoras fiscales HASAR y EPSON podrá seleccionar los tipos de letras 'X', 'R' o 'blanco'.
  * Para los recibos en las impresoras fiscales HASAR podrá seleccionar los tipos de letras 'A', 'B', 'C' o 'blanco' y para las impresoras fiscales EPSON, la letra 'X' y 'blanco'.
  * Consulte en el ítem [Comprobantes emitidos por equipo fiscal](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv), los tipos de comprobante que permite emitir cada modelo de equipo fiscal y el tratamiento de cada uno de ellos.



__Nota

Los comprobantes 'M' dejan de tener vigencia a partir del 01/12/2025 según RG 5762/2025. Consulte la [guía de implementación sobre RG 5762/25 - Factura A con retención (Reemplazo de Factura M)](?p=11887).  


Aplica RG 5762/25: permite identificar a los talonarios alcanzados por la Resolución General 5762/2025 de ARCA, que entra en vigencia a partir del 01/12/2025, reemplazando los comprobantes 'M'. Consule la [guía de implementación sobre RG 5762/25 - Factura A con retención (Reemplazo de Factura M)](?p=11887). Al tildar este campo, el sistema asociará automáticamente el comprobante a la modalidad 'Operación sujeta a retención'. Este campo aplica únicamente a los talonarios con letra 'A' y que no corresponden a equipos fiscales.  
Esta opción es excluyente con los campos Recibo-Factura y Comprobante de crédito electrónico (Ley 27.440).  
Si alguno de ellos se encuentra tildado, el campo Aplica RG 5762/25 permanecerá deshabilitado.

Numeración

Punto de venta: indique en este campo el número de sucursal. Si el tipo de edición definido corresponde a la legislación argentina, el sistema completará el número ingresado con ceros a la izquierda, por ejemplo 00001.  
El sistema permite habilitar distintos talonarios por cada sucursal o puestos de facturación, para que cada uno lleve su numeración independiente.  
En el caso de estar dando de alta un talonario para uso fiscal, es importante que se registre correctamente este campo con el número de punto de venta del equipo fiscal que configurará en el talonario.  
En el caso de estar dando de alta un talonario para uso fiscal, es importante que se registre correctamente este campo con el número de punto de venta del equipo fiscal que configurará en el talonario

Importante:

Tenga en cuenta que para dar de alta un talonario fiscal manual, es necesario tildar la opción Ingreso manual de comprobantes ya registrados en el equipo fiscal desde la solapa Equipos fiscales.

Rango de números habilitados: estos campos indican el primer y último número habilitado de cada talonario.  
Se utilizan para controlar, desde los procesos de emisión de comprobantes, su correcta numeración.

Próximo número a emitir: indica el número a utilizar por el sistema en el próximo comprobante emitido con el talonario.  
Los comprobantes 'FAC', 'DEB', 'CRE' y 'REM' asociados a un equipo fiscal mantienen su propio control en la numeración. Por lo tanto, este campo lo actualizará el equipo fiscal y debe ser respetado.  
Consulte en el ítem [Comprobantes emitidos por equipo fiscal](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv) el título [Numeración de comprobantes en equipos fiscales](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv#numcompimprfisc).

Edita numeración durante el ingreso de comprobantes: tilde este parámetro para editar el número del comprobante en el momento de ingresarlo al sistema.  
Aplicable a talonarios de pedidos yfacturas que no se encuentren configurados para la emisión de comprobantes fiscales y electrónicos.

Fecha de vencimiento: a partir de la RG 100/98, es posible ingresar una fecha de vencimiento para los talonarios de los tipos de comprobantes 'FAC', 'CRE' y 'DEB' y de tipo asociado 'A', 'B', 'C' y 'E'.  
El sistema validará que no se generen comprobantes con fecha posterior a la definida en este campo.  
Para los talonarios asociados a equipos fiscales, esta fecha de vencimiento no tiene validez, pero continúa utilizándose para restringir el uso del talonario.

Admite duplicidad de comprobantes según RG 100/98: este parámetro únicamente se editará para los tipos de comprobantes 'FAC', 'DEB', 'CRE', y para el tipo asociado 'A', 'B', 'C', 'M' y 'E', y se utilizará para diferenciar los nuevos comprobantes generados por el sistema a partir de la entrada en vigencia de esta resolución.

Importante:

Tenga en cuenta que esta opción nunca se encontrará disponible en talonarios habilitados para la emisión de comprobantes electrónicos o fiscales.

Solución para el cruzamiento de números de comprobantes:

Si existieran comprobantes anteriores o se produjera cruzamiento de números de comprobantes (entre la numeración anterior a la RG 100/98 y la numeración actual), será necesario activar la opción Admite duplicidad de comprobantes según RG 100/98. Sugerimos conservar el parámetro no activado hasta que se produzcan las situaciones antes descriptas.  
La RG 100/98 establece que la numeración de los comprobantes preimpresos de tipo 'FAC', 'CRE' y 'DEB'; y de tipo asociado 'A', 'B', 'C' y 'E' debe comenzar a partir de 00000001. Puede darse el caso que usted ya haya generado un comprobante con la misma letra, sucursal y número, y que éste se encuentre todavía activo en el sistema.  
Para subsanar este inconveniente debe agregar un nuevo talonario y utilizar el parámetro mencionado. Los nuevos comprobantes se grabarán en el sistema con una letra minúscula. Téngalo en cuenta en los procesos donde es necesario el ingreso del número del comprobante, como en el [ingreso de cobranzas](https://ayudas.axoft.com/24ar/ingresocobranza_gv) o la [emisión de remitos](https://ayudas.axoft.com/24ar/emisionremito_gv).

Exportación de registros

Exporta para gestión central: aplicable a talonarios de pedidos y remitos. Tilde este parámetro para activar la exportación de estos comprobantes (desde los procesos de Exportación para gestión central de Ventas).

Sucursal destino: si activa el parámetro anterior, indique el número de sucursal que recibirá los pedidos generados con este talonario. Este dato se utiliza por defecto en el ingreso del comprobante, la cual luego se utiliza como filtro en el proceso Exportación de pedidos para gestión central y Exportación de remitos de Ventas.

Método de exportación de pedidos: indique mediante este parámetro el circuito que desea utilizar con los pedidos que transfiere a otras sucursales. Las opciones son las siguientes:

  * **No controla:** los pedidos que se exportan podrán ser remitidos y facturados en la empresa origen como en el destino, pero en la empresa origen se mostrará un mensaje de advertencia indicando que ha sido transferido a otra sucursal.
  * **Remite y factura en destino:** los pedidos que se transfieran bajo este método serán remitidos y facturados solamente en la empresa destino.
  * **Remite en sucursal origen y factura en destino:** en este caso los pedidos transferidos serán facturados en la sucursal destino, pero el remito se realizará en la sucursal origen.
  * **Factura en sucursal origen y remite en destino:** los pedidos transferidos que utilizarán este método serán facturados en la sucursal origen y remitidos en la sucursal destino.



##### Impresión

Código de Autorización de Impresión (CAI): en versiones sin equipo fiscal, este código será suministrado por la AFIP en el momento en el que se solicita la impresión de los formularios. En estos casos, este código podrá ser impreso en los comprobantes a través de su variable de impresión.  
Para versiones de controlador o impresora fiscal, este código lo imprimen únicamente y en forma automática, los equipos fiscales en los comprobantes tipo 'A'. Los equipos fiscales no lo imprimen, ni es necesario enviar este código de autorización de impresión.

Destino de impresión

_Sólo para comprobantes preimpresos o manuales:_

Si el talonario no está asociado a un equipo fiscal, el uso de este campo es optativo.  
Puede indicar la impresora por defecto en la que se imprimirán los comprobantes. Si no ingresa una impresora, deberá indicar el destino de impresión en el momento de emitir el comprobante.  
Usted puede indicar:

  * Un "destino" si utiliza un puerto de impresión (LPT1, LPT2, LPT3).
  * Una "ruta" en caso de utilizar impresoras de red.



En este último caso, es importante que la impresora se encuentre compartida y que se ingrese el nombre completo de la ruta (por ejemplo, ServerPHP).

__Nota

En el momento de emitir el comprobante, el sistema valida que exista la impresora indicada. Si existe, imprimirá directamente en la impresora correspondiente al talonario. Si la impresora no existe, informará el inconveniente y permitirá seleccionar la impresora a utilizar, sugiriendo la impresora por defecto de **Windows**.

Si utiliza impresoras de red para la emisión de comprobantes, es muy importante que todos los usuarios utilicen el mismo nombre, para identificar a cada impresora.

Importante:

Tenga en cuenta que al dar de alta un talonario de tipo "Manual", no es posible indicar un destino de impresión dado que este tipo de comprobantes no se imprimen.

Utiliza configuración de destino de impresión para generación de PDF: active este parámetro para generar el PDF utilizando la configuración de impresión (tamaño de papel, orientación y fuente) de la impresora definida como destino.

__Importante

Este parámetro se habilita cuando el tipo de comprobante del talonario es 'Recibo' y se define una impresora de destino.

_Sólo para comprobantes electrónicos:_

Si la impresión es en papel, defina como predeterminada una impresora de este tipo. Indique la impresora a utilizar como destino de impresión en el talonario, así el sistema podrá direccionar el comprobante para que sea impreso.  
Si la impresión es en formato PDF, defina como puerto habitual o destino de impresión esa impresora PDF. En este caso, se generará la copia en PDF del comprobante, en el directorio definido en Parámetros de Ventas. Es posible consultar e imprimir el PDF generado desde el proceso [Administración de comprobantes electrónicos](https://ayudas.axoft.com/24ar/procesofacturacion_gv).

Cantidad máxima de renglones durante el ingreso de comprobantes: indique la cantidad máxima de renglones que puede tener un comprobante.  
Es de utilidad para definir la cantidad máxima de artículos que puede contener un comprobante por su tamaño y diseño. Si el comprobante se imprime en un único formulario, esta cantidad será igual a la cantidad de iteraciones indicada en la definición del formulario.  
Si la cantidad máxima de iteraciones es mayor a la indicada en la definición del formulario, el sistema realizará el transporte en forma automática, utilizando más de una hoja para el mismo comprobante.

Consideraciones sobre las iteraciones:

La cantidad a ingresar en este campo será menor o igual a 1000. Los talonarios asociados a cualquier modelo de equipo fiscal, tomarán 1000 como máximo de iteraciones para los comprobantes 'FAC', 'DEB' y 'CRE'.  
Aunque se cargue un límite de artículos de 1000, los equipos fiscales realizan en forma automática el transporte a otra hoja cuando detectan que no entran más artículos en la hoja actual. En el caso de los tickets y tickets-factura no hay problema por el transporte ya que no les corresponde, por lo tanto este campo únicamente servirá para limitar la carga de artículos en el comprobante asociado al talonario.  
Los remitos emitidos por el equipo fiscal EPSON tienen como valor máximo de 12 iteraciones y no realizan transporte. El valor máximo de iteraciones es debido al formato de hoja de 10 o 12 pulgadas que se debe configurar para Tango. Consulte el ítem [Configuración](https://ayudas.axoft.com/24ar/configequipfiscal_gv) en el proceso [Operación de controladores fiscales](https://ayudas.axoft.com/24ar/operacequipfiscal_gv).  
Para los recibos emitidos por el equipo fiscal HASAR el máximo de iteraciones será de 9, ya que este modelo posee una restricción en cuanto a la cantidad de iteraciones a imprimir en los recibos.  
Consulte el tratamiento de estos comprobantes en el ítem [Comprobantes emitidos por equipo fiscal](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv).  
Este valor también es aplicable a los pedidos.  
Para el resto de los casos ('REC', 'DEV', 'REM'), la cantidad a ingresar será menor o igual a 100.

Información sobre impresión de comprobantes:

Si usted está autorizado a imprimir sus números de comprobante, es posible que utilice transporte (por ejemplo, un remito puede ocupar más de una hoja). En este caso, no importa si la cantidad máxima de renglones coincide con la cantidad de iteraciones indicada en la definición del formulario. Por el contrario, si no desea que se realice transporte, entonces haga coincidir ambas cantidades.  
Si posee formularios preimpresos con numeración correlativa, es indispensable que coincidan estas definiciones, de lo contrario dará lugar a inconvenientes en el uso del formulario preimpreso.

Imprime comprobantes: indique el comportamiento de impresión del talonario de tipo 'Recibo' o tipo 'Pedido'. Las opciones son: 'Siempre' (valor por defecto en el alta o copia de talonario), 'Nunca' o 'Con confirmación'.

Utiliza formulario gráfico: si el talonario corresponde al tipo de comprobante 'Pedido', se habilita este parámetro. Indique si utiliza formulario gráfico en la generación de PDF. Por defecto estará desactivado.

Formularios

En esta grilla usted puede indicar el [formulario](https://ayudas.axoft.com/24ar/formularios_gv) a utilizar para los diferentes tipos de comprobantes, definiendo de esta manera el formato de impresión de cada uno. Es posible elegir un formulario como habitual para ser utilizado por defecto en el momento de emitir el comprobante.  
El sistema habilita los tipos de comprobante de acuerdo al campo Tipo de comprobante ingresado en la [solapa Principal](https://ayudas.axoft.com/24ar/principaltalonario_gv) del talonario.  
En el caso de no completar la grilla para asociar los formularios en cada talonario, se utilizarán como habituales los formularios que el sistema provee por defecto.  
Para emitir un comprobante con un dibujo diferente, realice los siguientes pasos:

  1. Desde el módulo Procesos generales acceda a Formulario de Ventas para configurar los formularios para los tipos de comprobantes de Ventas utilizando las variables de control e impresión disponibles para cada tipo en particular.
  2. Luego seleccione en la grilla el nombre del formulario correspondiente al dibujo a aplicar.
  3. Ingrese el tipo de comprobante.
  4. Por último, defina este formulario como habitual.



Formularios gráficos: si el tipo de comprobante del talonario corresponde a 'Pedido' y si utiliza formularios gráficos entonces se habilita esta grilla. Indique el [formulario gráfico](?p=9218) a utilizar al momento de 'Compartir' un pedido. Además, debe indicar si ese formulario gráfico es el habitual para ser utilizado por defecto al momento de generar el PDF desde [Pedidos](?p=19344).  
Para crear un nuevo formulario gráfico, realice los siguientes pasos:

  * Desde el módulo Procesos generales acceda a [Formulario gráficos de Ventas](?p=9218) para configurar un nuevo formulario gráfico para pedidos.
  * Luego seleccione en la grilla el nombre del formulario gráfico correspondiente, configurado en el paso anterior.
  * Por último, defina este formulario como habitual.



Dibujar: seleccione este comando para abrir el formulario asociado y acceder al formato de impresión, desde allí le será posible realizar los cambios que necesite en el diseño del comprobante.

Importante:

En el proceso de emisión de comprobantes correspondiente, presione las teclas de función <Ctrl+F4> para invocar Otros Formularios desde donde podrá seleccionar el nuevo formulario a considerar.

  * Si el comprobante es 'DEV' (devolución) no se habilitará el comando, ya que este tipo de comprobante no tiene impresión asociada.
  * La grilla no está habilitada para aquellos talonarios asociados a un equipo fiscal.
  * Para más información sobre formularios, consulte el ítem [Asistente de formularios](?p=12150).



Equipos fiscales

Ingreso manual de comprobantes ya registrados en el equipo fiscal: esta opción se utiliza para reemplazar los talonarios para equipo fiscal, en ocasiones en las que es necesario registrar comprobantes que fueron impresos y quedaron registrados en la memoria fiscal, que por algún motivo no se registraron en el sistema (ya sea por la existencia de algún inconveniente con el equipo fiscal, falla del equipo, facturación superior a 5000, ajustes de cuentas corrientes, etc.).  
Le permite registrar en el sistema comprobantes fiscales 'A', 'B', 'C', 'T' (facturas y/o notas de débito) y comprobantes de exportación 'E'. Por tal motivo, se solicita que ingrese el Código del equipo fiscal que reemplazará. Para más información, consulte el ítem [Consideraciones especiales para equipos fiscales](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv#considerespec).

Equipo fiscal asociado: indique el modelo de equipo fiscal por el que se emitirán los comprobantes cuando se utilice este talonario desde los [procesos de facturación](https://ayudas.axoft.com/24ar/procesofacturacion_gv).  
Únicamente se mostrarán los modelos de equipos fiscales disponibles, de acuerdo al tipo de comprobante seleccionado en la [solapa Principal](https://ayudas.axoft.com/24ar/principaltalonario_gv).  
En este caso las opciones son:

**Número** | **Descripción** | **Comprobantes** | **Tipo**  
---|---|---|---  
0 | Sin controlador | FAC | A,B,C,E,M,T,U,V,W,Y,Z,BLANCOS  
REC | A,B,C,M,BLANCOS  
CRE | A,B,C,E,M,T,U,V,W,Y,Z,BLANCOS  
DEB | A,B,C,E,M,T,U,V,W,Y,Z,BLANCOS  
DEV | A,B,C,E,M,R,BLANCOS  
REM | X,R  
COT | A,B,C,E,M,R,BLANCOS  
PED | A,B,C,E,M,T,U,V,W,Y,Z,BLANCOS  
MULTIPROPÓSITO | A,B,C,E,M,T,U,V,W,Y,Z,BLANCOS  
1 | Hasar SMH/P-614F | FAC | T,U,V,W,Y,Z  
2 | Epson TM-300A/F | FAC | T,U,V,W,Y,Z  
3 | Hasar SMH/P-615F o PR4F | FAC | A,B,C,T,U,V,W,Y,Z  
4 | Epson TM-2000AF+ / 300AF+ / U950F | FAC | A,B,C,T,U,V,W,Y,Z  
5 | Hasar 320F | FAC | A,B,C  
CRE | A,B,C  
DEB | A,B,C  
REM | X,R BLANCOS  
REC | A,B,C, BLANCOS  
6 | Epson LX-300F | FAC | A,B,C  
|  | DEB | A,B,C  
7 | Epson TM-T285F | FAC | T,U,V,W,Y,Z  
8 | Epson LX-300F+ / FX-880F | FAC | A,B,C  
DEB | A,B,C  
CRE | A,B,C  
REC | X, BLANCOS  
REM | X,R BLANCOS  
9 | Hasar SMH/P-425F | FAC | A,B,C  
CRE | A,B,C  
DEB | A,B,C  
REM | X,R BLANCOS  
REC | A,B,C, BLANCOS  
10 | Hasar 321F / 322F | FAC | A,B,C  
|  | CRE | A,B,C  
|  | DEB | A,B,C  
|  | REM | X,R BLANCOS  
|  | REC | A,B,C, BLANCOS  
11 | Epson TM-2002AF+ / NCR 3140 / Samsung SRP-270DF | FAC | A,B,C,T,U,V,W,Y,Z  
|  | CRE | A,B,C  
13 | Samsung SRP-250DF | FAC | A,B,C,T,U,V,W,Y,Z  
14 | Hasar SMH/P-715F / SMH/P 441F | FAC | A,B,C,T,U,V,W,Y,Z  
|  | DEB | A,B,C  
|  | CRE | A,B,C  
15 | Epson TM-U220A / TM-U220AFII | FAC | A,B,C,T,U,V,W,Y,Z  
|  | CRE | A,B,C  
16 | Hasar SMH/P-330F / SMH/P 1120F | FAC | A,B,C  
CRE | A,B,C  
DEB | A,B,C  
REM | X,R BLANCOS  
REC | A,B,C, BLANCOS  
17 | Hasar SMH/P-435F | FAC | A,B,C  
CRE | A,B,C  
DEB | A,B,C  
REM | X,R BLANCOS  
REC | A,B,C, BLANCOS  
99 | TALONARIO MANUAL | FAC | A,B,C,E,M,T,U,V,W,Y,Z  
CRE | A,B,C,E,M,T,U,V,W,Y,Z  
DEB | A,B,C,E,M,T,U,V,W,Y,Z  
BLANCO | A,B,C,E,M,T,U,V,W,Y,Z  
  
* 12: Número reservado para el sistema.

Consulte en el ítem [Equipos habilitados para emitir comprobantes fiscales](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv#modeloshabilit) los tipos de comprobantes que permite emitir cada modelo de equipo fiscal y el tratamiento de cada uno de ellos.

Número de serie del equipo fiscal: para los talonarios asociados a un equipo fiscal, usted puede ingresar el código y número de serie de su equipo en el talonario.  
De esta manera, es posible controlar que cada puesto de facturación utilice solamente el equipo fiscal indicado en el talonario. Si no desea realizar este control, deje este campo en blanco. Para los talonarios definidos como 'Talonario Manual' de tipo 'Fiscal' (utilizados para ingresar un comprobante que no fue registrado en el sistema pero sí fue emitido en el equipo fiscal), es necesario que complete también el código del equipo fiscal.  
Configure el código del equipo fiscal en el talonario, una vez que su equipo se encuentre inicializado, ya que no será posible realizar el control con los equipos en modo de prueba.

Destino de impresión: indique la impresora por defecto en la que desea imprimir los comprobantes, para los talonarios asociados a un equipo fiscal, el ingreso del destino de impresión es obligatorio, siendo sus valores posibles los que van desde el 'COM1' al 'COM256'.  
Si el talonario no está asociado a un equipo fiscal el uso de este campo es optativo.

Copias comprobante (Imp. Fiscal Hasar): indica la cantidad de comprobantes fiscales (facturas y débitos) y no fiscales homologados (créditos, recibos y remitos) a emitir para cada talonario.  
Está disponible únicamente para la impresora fiscal modelo HASAR 320F / 321F / 322F / 330F / 425F / 435F como impresora de facturas. Los valores posibles de ingresar son '0', '2', '3' y '4'.

Valores para Copias Comprobante (Imp. Fiscal Hasar):

Los valores '0', '2', '3' y '4' indican lo siguiente:

  1. **Valor "0":** se utiliza para los modelos con copia carbónica. El equipo fiscal imprime una sola vez el comprobante, con la leyenda: "ORIGINAL BLANCO/ COPIA COLOR" en su encabezado.
  2. **Valor "2":** se utiliza para los modelos sin copia carbónica. El equipo fiscal imprime dos veces el comprobante. En el primer comprobante se imprime automáticamente la leyenda: "ORIGINAL" y para la copia, la leyenda "DUPLICADO".
  3. **Valor "3":** se utiliza para los modelos sin copia carbónica. El equipo fiscal imprime tres veces el comprobante. En el primer comprobante se imprime automáticamente la leyenda: "ORIGINAL"; para la primer copia, la leyenda "DUPLICADO" y para la segunda copia, la leyenda "TRIPLICADO".
  4. **Valor "4":** se utiliza para los modelos sin copia carbónica. El equipo fiscal imprime cuatro veces el comprobante. En el primer comprobante se imprime automáticamente la leyenda: "ORIGINAL"; para la primer copia, la leyenda "DUPLICADO"; para la segunda copia, la leyenda "TRIPLICADO" y para la tercer copia, la leyenda "CUADRUPLICADO".



Formato de impresión: sólo para versiones del sistema que utilicen el modelo HASAR SMH/P-425F o 435F, seleccione la opción 'Tickets' si su controlador opera como impresora de tickets o la opción 'Formulario' si opera como impresora de facturas.  
Si selecciona la opción 'Tickets' no podrá emitir facturas, notas de débito y notas de crédito en formato ticket.

##### Comprobantes en PDF

Para talonarios asociados a cotizaciones, recibos y remitos, puede completar opcionalmente los parámetros para [Generación/envío de comprobantes en formato PDF](?p=11896).

Ingrese el directorio y la imagen de fondo (*.bmp, *.jpg) del PDF: defina una ruta válida con la imagen que utilizará como fondo en la generación del archivo en formato PDF. El campo admite 255 caracteres como máximo. Puede seleccionar archivos .bmp y .jpg.

Copia del archivo PDF

Guarda copia: active este parámetro para guardar una copia de todos los comprobantes emitidos en formato PDF. Este parámetro permite mantener una copia de todos los comprobantes emitidos con el talonario, independientemente del destino de impresión que seleccione al emitirlos.

Directorio: ingrese una ruta válida para el almacenamiento en el disco o en un servidor de los archivos. Si utiliza un directorio compartido, todos los usuarios que generen comprobantes deben tener acceso a dicho directorio.

Subdirectorio: seleccione una clasificación para el almacenamiento en el disco de los archivos en formato PDF. Serán ordenados por código de proveedor o por comprobantes.

__Nota

Esta opción muestra como ejemplo la ruta seleccionada por el usuario para el almacenamiento. Está conformada por el directorio válido y el subdirectorio seleccionado.

Talonarios para comprobantes electrónicos

En esta sección se explica la definición de talonarios para la emisión y almacenamiento de comprobantes electrónicos originales del mercado interno; de comprobantes electrónicos de exportación y de comprobantes electrónicos de turismo.

  * Si usted cumple con el régimen especial de emisión y almacenamiento electrónico de comprobantes originales del mercado interno (RG 2485, sus Modificatorias y Complementarias), defina los talonarios con tipo asociado 'A' y/o 'B' para la generación de comprobantes electrónicos.
  * Si usted está adherido al Régimen Simplificado para Pequeños Contribuyentes (RS) y cumple con el régimen especial de emisión y almacenamiento electrónico de comprobantes originales (RG 3067), defina los talonarios con tipo asociado 'C' para la generación de comprobantes electrónicos.
  * Si usted fue notificado por la Administración Federal de Ingresos Públicos respecto de su inclusión en el régimen de emisión de comprobantes electrónicos mediante nota inscripta por el juez administrativo competente (RG 2904), defina los talonarios con tipo asociado 'A' y/o 'B' para la generación de comprobantes electrónicos.
  * Si usted cumple con la RG 2557/09 para la emisión de comprobantes electrónicos del mercado interno y la utilización de los Bonos Fiscales Electrónicos, defina los talonarios con tipo asociado 'A' y/o 'B' para la generación de comprobantes electrónicos. Para cada talonario, tilde el parámetro Utiliza Bono Fiscal Electrónico. De esta forma, los diferenciará de los talonarios electrónicos con letra 'A' y/o 'B' que utilicen otro webservice.
  * Si usted cumple con la RG 3971, defina los talonarios con tipo asociado 'T' para la generación de comprobantes electrónicos de turismo.
  * Si usted cumple con el régimen especial de emisión y almacenamiento electrónico de comprobantes originales que respaldan operaciones de exportación (RG 3066, sus Modificatorias y Complementarias), defina los talonarios con tipo asociado 'E' para la generación de facturas, notas de crédito y notas de débito de exportación electrónicas.
  * Si usted opto por adherir al Régimen de Facturas de Crédito Electrónicas MiPyMEs (Ley 27440), defina los talonarios con tipo asociado 'A', 'B' o 'C' para la generación de comprobantes electrónicos. Para cada talonario a utilizar para la generación de estos comprobantes, tilde el parámetro Comprobante de crédito electrónico.
  * Si usted optó por utilizar CAEA indíquelo en las opciones de tipo de autorización para cada talonario a utilizar con esta modalidad. Esta opción es válida cuando utiliza webservice Versión 2, no utiliza bonos y no es un talonario para generar comprobantes de exportación.
  * Si usted optó por utilizar CAEA puede indicar, en los talonarios con tipo de autorización CAE, el talonario CAEA automático a utilizar en el Facturador cuando se encuentra en esta modalidad seleccionándolo en la opción 'Talonario CAEA asociado'.



Al definir un talonario de comprobantes electrónicos, tenga en cuenta las siguientes consideraciones:

  * No es posible aplicar la modalidad 'Multipropósito'.
  * El Punto de Venta debe estar comprendido entre los valores 00001 y 99998.
  * Para imprimir comprobantes electrónicos, ingrese el destino de impresión en el talonario.
  * Active el parámetro Genera Comprobante Electrónico.
  * El primer número habilitado del talonario debe ser '1' (uno).
  * Defina el tipo de conexión a utilizar para su comunicación con la AFIP ('En Línea' o bien, 'Diferido'). Elija la modalidad 'Diferido', por ejemplo, no tiene acceso a Internet desde un puesto de trabajo. Opte por la modalidad 'En Línea' para obtener el CAE en forma instantánea. Si al momento de confeccionar el comprobante no estuviera disponible la conexión a Internet el mismo será registrado con estado 'rechazado' y usted podrá obtener el CAE con posterioridad utilizando el proceso [Administración de comprobantes electrónicos](https://ayudas.axoft.com/24ar/procesofacturacion_gv).
  * Indique si imprime el comprobante electrónico una vez obtenido el CAE.
  * Indique si publica comprobantes en Tango Tiendas para que el cliente pueda visualizarlo la tienda de origen. ( **MercadoLibre Argentina®** , **Tienda nube Argentina®, API**)
  * Indique si envía el comprobante generado a su cliente por correo electrónico o por Whatsapp.
  * Ingrese la ubicación (directorio o carpeta) y el nombre de la imagen escaneada (archivo de tipo .bmp o .jpg) del formulario preimpreso a incluir en los comprobantes que se envíen por correo electrónico o por Whatsapp. Sugerimos escanear el formulario preimpreso grabando la imagen sin márgenes adicionales. Es posible que deba efectuar algunas pruebas hasta que la visualización del archivo pdf sea correcta. Tenga en cuenta que a diferencia de los comprobantes no electrónicos, pueden imprimirse o enviarse por correo electrónico o por Whatsapp cuantas veces lo desee.
  * Acceda a la opción Formularios, invoque la función Dibujar <F6> para agregar las variables de reemplazo para comprobantes electrónicos (CAE, Fecha de Vencimiento, etc.). Tenga en cuenta que también es necesario agregar las [variables de reemplazo](https://ayudas.axoft.com/24ar/modelimpr_carp_gv) para Tipo de comprobante y Número de Comprobante.



¿Cuántos talonarios puedo definir?

Si usted genera en forma electrónica comprobantes del mercado interno y/o de exportación, sugerimos definir por punto de venta, un talonario electrónico para cada Tipo de comprobante / Tipo asociado / Número de sucursal.  
Es decir, no debería tener en uso más de 3 talonarios electrónicos de clase 'A' ('FAC', 'DEB', 'CRE') ni más de 3 talonarios electrónicos de clase 'B' ('FAC', 'DEB', 'CRE') por punto de venta -si emite comprobantes electrónicos para el mercado interno ; y no más de 3 talonarios electrónicos de clase 'E' ('FAC', 'DEB', 'CRE') por punto de venta, si emite comprobantes electrónicos de exportación.  
Si usted genera, en forma electrónica, comprobantes del mercado interno según la RG 2485; según la RG 2557/09 (Bonos Fiscales Electrónicos) y/o según la RG 3971 (Reintegro de IVA a turistas del extranjero), defina un juego de talonarios para cada resolución general.  
Es decir, 3 talonarios electrónicos de clase 'A' ('FAC', 'DEB', 'CRE') y 3 talonarios electrónicos de clase 'B' ('FAC', 'DEB', 'CRE') por punto de venta si emite comprobantes electrónicos para el mercado interno según RG 2485; 3 talonarios electrónicos de clase 'A' ('FAC', 'DEB', 'CRE') que utilicen BFE y 3 talonarios electrónicos de clase 'B' ('FAC', 'DEB', 'CRE') que utilicen BFE por punto de venta, si emite comprobantes electrónicos asociados a Bonos Fiscales Electrónicos; y además, 3 talonarios electrónicos de clase 'T' ('FAC', 'DEB', 'CRE') por punto de venta, si emite comprobantes electrónicos de turismo (según RG 3971).  
Para más información acerca de la generación de comprobantes electrónicos, consulte el [Circuito de comprobantes electrónicos](?p=26548).

##### Contenidos relacionados

  * [Guía sobre comprobantes electrónicos](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_comprobelectr_gv/)

  * [Video sobre Reemplazo Factura 'M' - Retención IVA e IIGG](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/facturam_gv_vid/)

  * [Video sobre cotizaciones](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cotizaciones_gv_vid/)

  * [Video sobre emisión de facturas "A" a monotributistas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factamonotrib_gv_vid/)

  * [Video sobre formularios gráficos en pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/formgrafpedido_gv_vid/)

  * [Video sobre integración con WhatsApp](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/whatsapp_gral_vid/)

  * [Video sobre notas de crédito](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/nc_gral_vid/)

  * [Video sobre regímenes de facturación](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/regfact_gral_vid/)

  * [Video sobre remitos de ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/reciboremito_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ventamixta_gv_vid/)

  * [Videos sobre emisión de comprobantes con CAEA](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/caea_gv_vid/)

  * [Videos sobre factura de crédito electrónica](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/fce_gral_vid/)

  * [Videos sobre parámetros de Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/parametros_gv_vid/)
