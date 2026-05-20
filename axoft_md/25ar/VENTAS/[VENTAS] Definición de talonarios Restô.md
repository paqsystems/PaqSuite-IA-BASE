# Definición de talonarios Restô

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_rg5762_gv3/?p=25001/

## Contenido

# Definición de talonarios Restô

En la solapa _Principal_ se van a ingresar los datos comunes a todos los tipos de talonario, los mismos se detallan a continuación 

Número de talonario: número que identifica al talonario.

Descripción: este campo es opcional. Puede utilizarlo para describir el talonario definido, o bien, para guardar alguna glosa a imprimir en los comprobantes que se emitan con ese talonario.

Tipo de talonario: defina aquí el tipo de talonario que desea ingresar según las opciones posibles.  
Valores posibles para este campo:

  * **Preimpreso:** el comprobante se emitirá sobre un formulario preimpreso.
  * **Equipo fiscal:** el comprobante será impreso en un equipo fiscal asociado.
  * **Electrónico:** solo tendrá la posibilidad de definir este tipo de talonario si usted cumple con el régimen especial de emisión de comprobantes electrónicos, y desde la solapa Comprobantes electrónicos de Parámetros de Ventas se encuentra definida la fecha de incorporación al régimen especial de emisión y almacenamiento electrónico de comprobantes originales.  
Tenga en cuenta que al seleccionar este tipo de comprobantes se habilitará una solapa adicional con el nombre Documentos electrónicos en donde podrá configurar los datos adicionales para la generación y envío de comprobantes electrónicos a los clientes.
  * **Manual:** utilice esta opción para ingresar al sistema comprobantes que se generan manualmente en un formulario preimpreso.  
Tenga en cuenta que el tipo de talonario manual podrá utilizarse para los tipos de comprobante 'FAC', 'CRE' o 'MULTIPROPÓSITO'.



Tipo de comprobante: este campo indica los tipos de comprobante que puede utilizar cada talonario.  
Los valores posibles son:

**Tipo comprobante** | **Descripción**  
---|---  
FAC | Facturas.  
CRE | Cualquier tipo de nota de crédito definida.  
REC | Recibo de cobranza.  
" " | (Tres blancos o espacios) para formularios multipropósito.  
  
Consulte en el ítem [Modelos habilitados y tipos de comprobante emitidos](?p=19252/#modeloshabilit) los tipos de comprobantes que permite emitir cada modelo de equipo fiscal.

Aclaraciones:

Cabe aclarar que un talonario definido como multipropósito podrá ser utilizado sólo para facturas y notas de crédito en versiones sin controlador o impresora fiscal. Los recibos llevan una numeración independiente.  
En versiones para controlador fiscal, no podrán utilizarse talonarios multiprópositos para facturas y créditos, ya que los controladores e impresoras fiscales cuentan con contadores independientes: uno para las facturas 'A', uno para las facturas 'B' y uno para notas de crédito.  
Para más información, consulte en el ítem [Numeración de comprobantes en equipos fiscales](?p=19252/#numcompimprfisc).

Letra/Clase: corresponde a la letra del comprobante, y representa el tipo de formulario asociado al documento Puede ser 'A', 'B', 'C', 'E', 'R', 'T', 'X', 'U', 'V', 'W', 'Y', 'Z' o un 'blanco', recomendamos utilizar las siguientes letras para una correcta identificación de los documentos a generar.  
Recomendamos utilizar las siguientes letras para una correcta identificación de los comprobantes a generar.

**Letra** | **Tipo de documento**  
---|---  
A, B, C | Para los ticket-factura y facturas fiscales.  
B, C, M | Para los documentos correspondientes a boletas de ventas.  
T | Para ser utilizado por aquellas empresas autorizadas a emitir tickets a través de sistemas computarizados según la RG 3419 de DGI.  
U, V, W, Y, Z | Representan un ticket como comprobante, y se identificarán en el subdiario de IVA con la letra 'T'.  
Blanco | Multipropósito  
  
  * Si el talonario hace referencia a un controlador fiscal para tickets, el tipo asociado podrá elegirse entre las letras 'T' a 'Z', excluyendo las letras 'X'.
  * Para los recibos en las impresoras fiscales HASAR podrá seleccionar los tipos de letras 'A', 'B', 'C' o 'blanco' y para las impresoras fiscales EPSON, la letra 'X' y 'blanco'.  
• Consulte en el ítem Comprobantes emitidos por equipo fiscal, los tipos de comprobante que permite emitir cada modelo de equipo fiscal y el tratamiento de cada uno de ellos.



Uso exclusivo / Puesto de caja: indique si el talonario va a ser excluido para un puesto de caja en particular.

Punto de venta: indique en este campo el número de sucursal. Si el tipo de edición definido corresponde a la legislación argentina, el sistema completará el número ingresado con ceros a la izquierda, por ejemplo '00001'.  
El sistema permite habilitar distintos talonarios por cada sucursal o puestos de facturación, para que cada uno lleve su numeración independiente.  
En el caso de estar dando de alta un talonario para uso fiscal, es importante que se registre correctamente este campo con el número de punto de venta del equipo fiscal que configurará en el talonario.

__Importante

Tenga en cuenta que, para dar de alta un talonario fiscal manual, es necesario tildar la opción Ingreso manual de comprobantes ya registrados en el equipo fiscal desde la solapa _Equipos fiscales_.

Rango de números habilitados: estos campos indican el primer y último número habilitado de cada talonario.  
Se utilizan para controlar, desde los procesos de emisión de comprobantes, su correcta numeración.

Próximo número a emitir: indica el número a utilizar por el sistema en el próximo comprobante emitido con el talonario.  
Los comprobantes 'FAC' y 'CRE' asociados a un equipo fiscal mantienen su propio control en la numeración. Por lo tanto, este campo lo actualizará el equipo fiscal y debe ser respetado.  
Consulte en el ítem [Numeración de comprobantes en equipos fiscales](?p=19252/#numcompimprfisc).

Edita numeración durante el ingreso de comprobantes: tilde este parámetro para editar el número del comprobante en el momento de ingresarlo al sistema.  
Aplicable a talonarios de pedidos y facturas que no se encuentren configurados para la emisión de comprobantes fiscales y electrónicos.

Fecha de vencimiento: a partir de la RG 100/98, es posible ingresar una fecha de vencimiento para los talonarios de los tipos de comprobantes 'FAC' y 'CRE' y, de tipo asociado 'A', 'B' y 'C'. El sistema validará que no se generen comprobantes con fecha posterior a la definida en este campo. Para los talonarios asociados a equipos fiscales, esta fecha de vencimiento no tiene validez, pero continúa utilizándose para restringir el uso del talonario.

Admite duplicidad de comprobantes según RG 100/98: este parámetro únicamente se editará para los tipos de comprobantes 'FAC' y 'CRE' y, para el tipo asociado 'A', 'B' y 'C, y se utilizará para diferenciar los nuevos comprobantes generados por el sistema a partir de la entrada en vigencia de esta resolución.

__Importante

Tenga en cuenta que esta opción nunca se encontrará disponible en talonarios habilitados para la emisión de comprobantes electrónicos o fiscales.  
Solución para el cruzamiento de números de comprobantes:  
Si existieran comprobantes anteriores o se produjera cruzamiento de números de comprobantes (entre la numeración anterior a la RG 100/98 y la numeración actual), será necesario activar la opción _Admite duplicidad de comprobantes según RG 100/98_. Sugerimos conservar el parámetro no activado hasta que se produzcan las situaciones antes descriptas.

##### Impresión

Código de autorización de impresión (CAI): en versiones sin equipo fiscal, este código será suministrado por la AFIP en el momento en el que se solicita la impresión de los formularios. En estos casos, este código podrá ser impreso en los comprobantes a través de su variable de impresión.  
Para versiones de controlador o impresora fiscal, este código lo imprimen únicamente y en forma automática, los equipos fiscales en los comprobantes tipo 'A'. Los equipos fiscales no lo imprimen, ni es necesario enviar este código de autorización de impresión.

Destino de impresión: si el talonario no está asociado a un equipo fiscal, el uso de este campo es optativo.  
Puede indicar la impresora por defecto en la que se imprimirán los comprobantes. Si no ingresa una impresora, deberá indicar el destino de impresión en el momento de emitir el comprobante.  
Usted puede indicar:

  * Un "destino" si utiliza un puerto de impresión (LPT1, LPT2, LPT3).
  * Una "ruta" en caso de utilizar impresoras de red.



En este último caso, es importante que la impresora se encuentre compartida y que se ingrese el nombre completo de la ruta (por ejemplo, ServerPHP).

__Nota

En el momento de emitir el comprobante, el sistema valida que exista la impresora indicada. Si existe, imprimirá directamente en la impresora correspondiente al talonario. Si la impresora no existe, informará el inconveniente y permitirá seleccionar la impresora a utilizar, sugiriendo la impresora por defecto de Windows.

Si utiliza impresoras de red para la emisión de comprobantes, es muy importante que todos los usuarios utilicen el mismo nombre, para identificar a cada impresora.

__Importante

Tenga en cuenta que al dar de alta un talonario de tipo "Manual", no es posible indicar un destino de impresión dado que este tipo de comprobantes no se imprimen.

##### Formularios

En esta grilla usted puede indicar el [formulario](?p=25361) a utilizar para los diferentes tipos de comprobantes, definiendo de esta manera el formato de impresión de cada uno. Es posible elegir un formulario como habitual para ser utilizado por defecto en el momento de emitir el comprobante.  
El sistema habilita los tipos de comprobante de acuerdo al campo Tipo de comprobante ingresado en la [solapa Principal del talonario](?p=25001).  
En el caso de no completar la grilla para asociar los formularios en cada talonario, se utilizarán como habituales los formularios que el sistema provee por defecto.  
Para emitir un comprobante con un dibujo diferente, realice los siguientes pasos:

  1. Desde el módulo Procesos generales acceda a Formulario de Ventas para configurar los formularios para los tipos de comprobantes de ventas utilizando las variables de control e impresión disponibles para cada tipo en particular.
  2. Luego seleccione en la grilla el nombre del formulario correspondiente al dibujo a aplicar.
  3. Ingrese el tipo de comprobante.
  4. Por último, defina este formulario como habitual.
