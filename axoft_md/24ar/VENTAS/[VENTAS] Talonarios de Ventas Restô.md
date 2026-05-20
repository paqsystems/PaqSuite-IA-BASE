# Talonarios de Ventas Restô

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_comprobelectr_gv3/?p=24998/

## Contenido

# Talonarios de Ventas Restô

Mediante este proceso se definen los distintos talonarios a utilizar en los procesos de emisión de comprobantes (facturas, notas de crédito y recibos de cobranza). La asignación de talonarios facilita el control de la impresión y la numeración de los comprobantes.

Al tener configurada la numeración de comprobantes de acuerdo a las disposiciones legales vigentes, los números de comprobante tienen una longitud de catorce caracteres, los que se distribuyen de la siguiente manera: el primer caracter es una letra y representa el tipo de formulario ('A', 'B', 'C', 'E', 'R', 'T' o 'X'), los cinco siguientes indican la sucursal y los ocho restantes, el número de comprobante en sí.  
Todos los procesos de emisión de comprobantes solicitarán el ingreso de un número de talonario. En base a ese talonario, el sistema obtiene el próximo número de comprobante a utilizar.  
Detallamos a continuación cada una de las opciones a parametrizar en las distintas solapas, de acuerdo con el tipo de talonario que desea dar de alta.

##### Principal

Se van a ingresar los datos comunes a todos los tipos de talonario, los mismos se detallan a continuación.

Número de talonario: número que identifica al talonario.

Descripción: es un campo opcional. Puede utilizarlo para describir el talonario definido o bien, para almacenar una leyenda a imprimir en los comprobantes que se emitan con ese talonario.

Tipo de talonario: defina aquí el tipo de talonario que desea ingresar según las opciones posibles.  
Valores posibles para este campo...

  * Preimpreso: el comprobante se emitirá sobre un formulario preimpreso.
  * Equipo fiscal: el comprobante será impreso en un equipo fiscal asociado.
  * Electrónico: solo tendrá la posibilidad de definir este tipo de talonario si usted cumple con el régimen especial de emisión de comprobantes electrónicos, y desde la solapa Documentos electrónicos de la configuración de la terminal de adicionista, se encuentra definida la fecha de incorporación al régimen especial de emisión y almacenamiento electrónico de comprobantes originales.  
Tenga en cuenta que al seleccionar este tipo de comprobantes se habilitará una solapa adicional con el nombre Documentos electrónicos en donde podrá configurar los datos adicionales para la generación y envío de comprobantes electrónicos a los clientes.
  * Manual: utilice esta opción para ingresar al sistema comprobantes que se generan manualmente en un formulario preimpreso.



Tenga en cuenta que el tipo de talonario manual podrá utilizarse para los tipos de comprobante 'FAC', 'CRE' o 'MULTIPROPÓSITO'.

Tipo de Comprobante: este campo indica los tipos de comprobante que puede utilizar cada talonario.  
Los valores posibles son:

**Tipo comprobante** | **Descripción**  
---|---  
FAC | Facturas  
CRE | Cualquier tipo de nota de crédito definida  
REC | Recibo de cobranza  
" " | (Tres blancos o espacios) para formularios multipropósito  
  
Aclaraciones:

Cabe aclarar que un talonario definido como multipropósito podrá ser utilizado sólo para facturas y notas de crédito en versiones sin controlador o impresora fiscal. Los recibos llevan una numeración independiente.  
En versiones para controlador fiscal, no podrán utilizarse talonarios multiprópositos para facturas y créditos, ya que los controladores e impresoras fiscales cuentan con contadores independientes: uno para las facturas 'A', uno para las facturas 'B' y uno para notas de crédito.  
Para más información, consulte en el ítem [Consideraciones especiales para equipos fiscales](?p=19769), el título [Numeración de comprobantes en equipos fiscales](?p=19769/#consideraciones-especiales-para-controladores-e-impresoras-fiscales).

Recibo-Factura: permite indicar que el comprobante emitido actuará simultáneamente como factura y recibo, unificando ambos documentos en una misma emisión. Este campo se aplica cuando se utiliza el Web Services 2, el tipo de comprobante es factura con letras 'A', 'B' o 'C', y el tipo de talonario no es 'Equipo fiscal'. Esta opción es excluyente con los campos Aplica RG 5762/25 y Comprobante de crédito electrónico (Ley 27.440). Si alguno de ellos se encuentra tildado, el campo Recibo - Factura permanecerá deshabilitado. 

Letra/Clase: corresponde a la letra del comprobante, y representa el tipo de formulario asociado al documento. Puede ser 'A', 'B', 'C', ‘'T'’, 'U', 'V', 'W', 'Y', 'Z' o un 'blanco', recomendamos utilizar las siguientes letras para una correcta identificación de los documentos a generar.

**Letra** | **Tipo de Documento**  
---|---  
A, B, C | Para los ticket-factura y facturas fiscales.  
B, C, M | Para los documentos correspondientes a boletas de ventas.  
T | Para ser utilizado por aquellas empresas autorizadas a emitir tickets a través de sistemas computarizados según la RG 3419 de DGI.  
U, V, W, Y, Z | Representan un ticket como comprobante, y se identificarán en el subdiario de IVA con la letra 'T'.  
Blanco | Multipropósito.  
  
  * Si el talonario hace referencia a un controlador fiscal para tickets, el tipo asociado podrá elegirse entre las letras 'T' a 'Z', excluyendo las letras 'X'.
  * Para los recibos en las impresoras fiscales HASAR podrá seleccionar los tipos de letras 'A', 'B', 'C' o 'blanco' y para las impresoras fiscales EPSON, la letra 'X' y 'blanco'.
  * Consulte en el ítem [Comprobantes emitidos por equipo fiscal](?p=19769), los tipos de comprobante que permite emitir cada modelo de equipo fiscal y el tratamiento de cada uno de ellos.



__Nota

Los comprobantes 'M' dejan de tener vigencia a partir del 01/12/2025 según RG 5762/2025. Consulte la [Guía de implementación RG 5762/25 - Factura A con retención (Reemplazo de Factura M)](?p=10543).  


Aplica RG 5762/25: permite identificar a los talonarios alcanzados por la Resolución General 5762/2025 de ARCA, que entra en vigencia a partir del 01/12/2025, reemplazando los comprobantes 'M'. Consule la [Guía de implementación RG 5762/25 - Factura A con retención (Reemplazo de Factura M)](?p=10543). Al tildar este campo, el sistema asociará automáticamente el comprobante a la modalidad 'Operación sujeta a retención'. Este campo aplica únicamente a los talonarios con letra 'A' y que no corresponden a equipos fiscales. Esta opción es excluyente con los campos Recibo - Factura y Comprobante de crédito electrónico (Ley 27.440). Si alguno de ellos se encuentra tildado, el campo Aplica RG 5762/25 permanecerá deshabilitado.

Punto de venta: indique en este campo el número de sucursal. Si el tipo de edición definido corresponde a la legislación argentina, el sistema completará el número ingresado con ceros a la izquierda, por ejemplo, 00001.  
El sistema permite habilitar distintos talonarios por cada sucursal o puestos de facturación, para que cada uno lleve su numeración independiente.  
En el caso de estar dando de alta un talonario para uso fiscal, es importante que se registre correctamente este campo con el número de punto de venta del equipo fiscal que configurará en el talonario.  
En el caso de estar dando de alta un talonario para uso fiscal, es importante que se registre correctamente este campo con el número de punto de venta del equipo fiscal que configurará en el talonario.

__Importante

Tenga en cuenta que para dar de alta un talonario fiscal manual, es necesario tildar la opción Ingreso manual de comprobantes ya registrados en el equipo fiscal desde la solapa _Equipos fiscales_.

Rango de números habilitados: estos campos indican el primer y último número habilitado de cada talonario.  
Se utilizan para controlar, desde los procesos de emisión de comprobantes, su correcta numeración.

Próximo número a emitir: indica el número a utilizar por el sistema en el próximo comprobante emitido con el talonario.  
Los comprobantes 'FAC' y 'CRE' asociados a un equipo fiscal mantienen su propio control en la numeración. Por lo tanto, este campo lo actualizará el equipo fiscal y debe ser respetado.  
Para más información, consulte en el ítem [Consideraciones especiales para equipos fiscales](?p=19769), el título [Numeración de comprobantes en equipos fiscales](?p=19769/#consideraciones-especiales-para-controladores-e-impresoras-fiscales).

Edita numeración durante el ingreso de comprobantes: tilde este parámetro para editar el número del comprobante en el momento de ingresarlo al sistema.  
Aplicable a talonarios de pedidos y facturas que no se encuentren configurados para la emisión de comprobantes fiscales y electrónicos.

Fecha de vencimiento: a partir de la RG 100/98 es posible ingresar una fecha de vencimiento para los talonarios de los tipos de comprobantes 'FAC’ y 'CRE' , y para el tipo asociado 'A', 'B' y 'C'. El sistema validará que no se generen comprobantes con fecha posterior a la definida en este campo.  
Para los talonarios asociados a equipos fiscales, esta fecha de vencimiento no tiene validez pero continúa utilizándose para restringir el uso del talonario.

Admite duplicidad de comprobantes según RG 100/98: este parámetro únicamente se editará para los tipos de comprobantes 'FAC' y 'CRE', y para el tipo asociado 'A', 'B', 'C' y 'M', y se utilizará para diferenciar los nuevos comprobantes generados por el sistema a partir de la entrada en vigencia de esta resolución.

__Nota

Tenga en cuenta que esta opción nunca se encontrará disponible en talonarios habilitados para la emisión de comprobantes electrónicos o fiscales.

Solución para el cruzamiento de números de comprobantes:

##### Impresión

Código de Autorización de Impresión (CAI): en versiones sin equipo fiscal, este código será suministrado por la AFIP en el momento en el que se solicita la impresión de los formularios. En estos casos, este código podrá ser impreso en los comprobantes a través de su variable de impresión.  
Para versiones de controlador o impresora fiscal, este código lo imprimen únicamente y en forma automática, los equipos fiscales en los comprobantes tipo 'A'. Los equipos fiscales no lo imprimen, ni es necesario enviar este código de autorización de impresión.

Destino de impresión: si el talonario no está asociado a un equipo fiscal, el uso de este campo es optativo.  
Puede indicar la impresora por defecto en la que se imprimirán los comprobantes. Si no ingresa una impresora, deberá indicar el destino de impresión en el momento de emitir el comprobante.  
Usted puede indicar:

  * Un "destino" si utiliza un puerto de impresión (LPT1, LPT2, LPT3).
  * Una "ruta" en caso de utilizar impresoras de red.



En este último caso, es importante que la impresora se encuentre compartida y que se ingrese el nombre completo de la ruta (por ejemplo, ServerPHP).

__Nota

En el momento de emitir el comprobante, el sistema valida que exista la impresora indicada. Si existe, imprimirá directamente en la impresora correspondiente al talonario. Si la impresora no existe, informará el inconveniente y permitirá seleccionar la impresora a utilizar, sugiriendo la impresora por defecto de **Windows**.

Si utiliza impresoras de red para la emisión de comprobantes, es muy importante que todos los usuarios utilicen el mismo nombre, para identificar a cada impresora.

__Importante

Tenga en cuenta que al dar de alta un talonario de tipo "Manual", no es posible indicar un destino de impresión dado que este tipo de comprobantes no se imprimen.

##### Formularios

En esta grilla usted puede indicar el formulario a utilizar para los diferentes tipos de comprobantes, definiendo de esta manera el formato de impresión de cada uno. Es posible elegir un formulario como habitual para ser utilizado por defecto en el momento de emitir el comprobante.  
El sistema habilita los tipos de comprobante de acuerdo al campo Tipo de comprobante ingresado en la solapa Principal del talonario.  
En el caso de no completar la grilla para asociar los formularios en cada talonario, se utilizarán como habituales los formularios que el sistema provee por defecto.  
Para emitir un comprobante con un dibujo diferente, realice los siguientes pasos:

  1. Desde el módulo Procesos Generales acceda a Formulario de Ventas para configurar los formularios para los tipos de comprobantes de Ventas utilizando las variables de control e impresión disponibles para cada tipo en particular.
  2. Luego seleccione en la grilla el nombre del formulario correspondiente al dibujo a aplicar.
  3. Ingrese el tipo de comprobante.
  4. Por último, defina este formulario como habitual.



Dibujar: seleccione este comando para abrir el formulario asociado y acceder al formato de impresión, desde allí le será posible realizar los cambios que necesite en el diseño del comprobante.

__Importante

En el proceso de emisión de comprobantes correspondiente, presione las teclas de función _< Ctrl+F4>_ para invocar _Otros Formularios_ desde donde podrá seleccionar el nuevo formulario a considerar.

Más información:

  * La grilla no está habilitada para aquellos talonarios asociados a un equipo fiscal.
  * Para más información sobre la confección de los distintos formularios, consulte el ítem [Modelos de impresión de comprobantes en Ventas Restô](?p=25361).



##### Equipos fiscales

Ingreso manual de comprobantes ya registrados en el equipo fiscal: esta opción se utiliza para reemplazar los talonarios para equipo fiscal, en ocasiones en las que es necesario registrar comprobantes que fueron impresos y quedaron registrados en la memoria fiscal, que por algún motivo no se registraron en el sistema (ya sea por la existencia de algún inconveniente con el equipo fiscal, falla del equipo, facturación superior a 5000, ajustes de cuentas corrientes, etc.).  
Le permite registrar en el sistema comprobantes fiscales 'A', 'B', 'C', 'T' (facturas y/o notas de dédito) y comprobantes de exportación 'E'. Por tal motivo, se solicita que ingrese el código del equipo fiscal que reemplazará. Para más información, consulte el ítem [Consideraciones especiales para equipos fiscales](?p=19769).

Equipo fiscal asociado: indique el modelo de equipo fiscal por el que se emitirán los comprobantes cuando se utilice este talonario desde los procesos de facturación.  
Únicamente se mostrarán los modelos de equipos fiscales disponibles, de acuerdo al tipo de comprobante seleccionado en la solapa Principal.

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
DEB | A,B,C  
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
CRE | A,B,C  
DEB | A,B,C  
REM | X,R BLANCOS  
REC | A,B,C, BLANCOS  
11 | Epson TM-2002AF+ / NCR 3140 / Samsung SRP-270DF | FAC | A,B,C,T,U,V,W,Y,Z  
CRE | A,B,C  
13 | Samsung SRP-250DF | FAC | A,B,C,T,U,V,W,Y,Z  
14 | Hasar SMH/P-715F / SMH/P 441F | FAC | A,B,C,T,U,V,W,Y,Z  
DEB | A,B,C  
CRE | A,B,C  
15 | Epson TM-U220A / TM-U220AFII | FAC | A,B,C,T,U,V,W,Y,Z  
CRE | A,B,C  
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

Consulte en el ítem [Equipos habilitados para emitir comprobantes fiscales](?p=19252/#modelos-habilitados-y-tipos-de-comprobantes-emitidos) los tipos de comprobantes que permite emitir cada modelo de equipo fiscal y el tratamiento de cada uno de ellos.

Número de serie del equipo fiscal: para los talonarios asociados a un equipo fiscal, usted puede ingresar el código y número de serie de su equipo en el talonario.  
De esta manera, es posible controlar que cada puesto de facturación utilice solamente el equipo fiscal indicado en el talonario. Si no desea realizar este control, deje este campo en blanco. Para los talonarios definidos como 'Talonario Manual' de tipo 'Fiscal' (utilizados para ingresar un comprobante que no fue registrado en el sistema pero sí fue emitido en el equipo fiscal), es necesario que complete también el código del equipo fiscal.  
Configure el código del equipo fiscal en el talonario, una vez que su equipo se encuentre inicializado, ya que no será posible realizar el control con los equipos en modo de prueba.

Destino de impresión: indique la impresora por defecto en la que desea imprimir los comprobantes, para los talonarios asociados a un equipo fiscal, el ingreso del destino de impresión es obligatorio, siendo sus valores posibles los que van desde el 'COM1' al 'COM256'.  
Si el talonario no está asociado a un equipo fiscal el uso de este campo es optativo.

Copias Comprobante (Imp. Fiscal Hasar): indica la cantidad de comprobantes fiscales (facturas y débitos) y no fiscales homologados (créditos, recibos y remitos) a emitir para cada talonario.  
Está disponible únicamente para la impresora fiscal modelo HASAR 320F / 321F / 322F / 330F / 425F / 435F como impresora de facturas. Los valores posibles de ingresar son '0', '2', '3' y '4'.

Valores para Copias Comprobante (Imp. Fiscal Hasar):  
Los valores '0', '2', '3' y '4' indican lo siguiente:

  1. **Valor '0':** se utiliza para los modelos con copia carbónica. El equipo fiscal imprime una sola vez el comprobante, con la leyenda: "ORIGINAL BLANCO/ COPIA COLOR" en su encabezado.
  2. **Valor '2':** se utiliza para los modelos sin copia carbónica. El equipo fiscal imprime dos veces el comprobante. En el primer comprobante se imprime automáticamente la leyenda: "ORIGINAL" y para la copia, la leyenda "DUPLICADO".
  3. **Valor '3':** se utiliza para los modelos sin copia carbónica. El equipo fiscal imprime tres veces el comprobante. En el primer comprobante se imprime automáticamente la leyenda: "ORIGINAL"; para la primer copia, la leyenda "DUPLICADO" y para la segunda copia, la leyenda "TRIPLICADO".
  4. **Valor '4':** se utiliza para los modelos sin copia carbónica. El equipo fiscal imprime cuatro veces el comprobante. En el primer comprobante se imprime automáticamente la leyenda: "ORIGINAL"; para la primer copia, la leyenda "DUPLICADO"; para la segunda copia, la leyenda "TRIPLICADO" y para la tercer copia, la leyenda "CUADRUPLICADO".



Formato de impresión: sólo para versiones del sistema que utilicen el modelo HASAR SMH/P-425F o 435F, seleccione la opción 'Tickets' si su controlador opera como impresora de tickets o la opción 'Formulario' si opera como impresora de facturas.  
Si selecciona la opción 'Tickets' no podrá emitir facturas, notas de débito y notas de crédito en formato ticket.

##### Talonarios para comprobantes electrónicos

En esta sección se explica la definición de talonarios para la emisión y almacenamiento de comprobantes electrónicos originales del mercado interno.

  * Si usted cumple con el régimen especial de emisión y almacenamiento electrónico de comprobantes originales del mercado interno (RG 2485, sus Modificatorias y Complementarias), defina los talonarios con tipo asociado 'A' y/o 'B' para la generación de comprobantes electrónicos.
  * Si usted está adherido al Régimen Simplificado para Pequeños Contribuyentes (RS) y cumple con el régimen especial de emisión y almacenamiento electrónico de comprobantes originales (RG 3067), defina los talonarios con tipo asociado 'C' para la generación de comprobantes electrónicos.
  * Si usted opto por adherir al Régimen de Facturas de Crédito Electrónicas MiPyMEs (Ley 27440), defina los talonarios con tipo asociado 'A', 'B' o 'C' para la generación de comprobantes electrónicos. Para cada talonario a utilizar para la generación de estos comprobantes, tilde el parámetro Comprobante de crédito electrónico.
  * Si usted optó por utilizar CAEA indíquelo en las opciones de Tipo de autorización para cada talonario a utilizar con esta modalidad. Esta opción es válida cuando utiliza webservice Versión 2, no utiliza Bonos y no es un talonario para generar comprobantes de exportación.
  * Si usted optó por utilizar CAEA puede indicar en los talonarios con tipo de autorización CAE el talonario CAEA automático a utilizar en el Facturador cuando se encuentra en esta modalidad seleccionándolo en la opción Talonario CAEA asociado.



El tipo de conexión puede ser diferida o en línea. Los talonarios con tipo de autorización CAE, pueden tener tipo de conexión en línea o diferido, mientras que los talonarios con tipo de autorización CAEA tiene ya definido como tipo de conexión "diferido".  
Se puede indicar si el talonario imprime o no el comprobante, así como, si al momento de imprimir, se deberá utilizar la configuración de la impresora para comprobantes electrónicos.  
También se podrá definir una imagen para el talonario preimpreso.

Al definir un talonario de comprobantes electrónicos, tenga en cuenta las siguientes consideraciones:

  * No es posible aplicar la modalidad 'Multipropósito'.
  * El Punto de Venta debe estar comprendido entre los valores 00001 y 99998 y/o de exportación, sugerimos definir por punto de venta, un talonario electrónico para cada Tipo de comprobante / Tipo asociado / Número de sucursal.  
Es decir, no debería tener en uso más de 3 talonarios electrónicos de clase 'A' ('FAC', 'CRE') ni más de 3 talonarios electrónicos de clase 'B' ('FAC', 'CRE') por punto de venta -si emite comprobantes electrónicos para el mercado interno.



##### Contenido dependiente

  * [Definición de talonarios Restô](https://ayudas.axoft.com/24ar/ayudas/gv3/archivo_carp_gv3/cargainicial_gv3/talonario_carp_gv3/talonariodefinic_gv3/)
  * [Imágenes](https://ayudas.axoft.com/24ar/ayudas/gv3/archivo_carp_gv3/cargainicial_gv3/talonario_carp_gv3/talonarioimagen_gv3/)
