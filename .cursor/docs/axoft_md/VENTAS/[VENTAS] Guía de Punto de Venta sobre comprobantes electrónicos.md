# Guía de Punto de Venta sobre comprobantes electrónicos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv2/guia_comprobelectr_gv2/

## Contenido

# Guía de Punto de Venta sobre comprobantes electrónicos

**Comprobantes electrónicos del mercado interno  
**La AFIP ha establecido un régimen especial para la emisión y almacenamiento electrónico de comprobantes originales, respaldatorios de las operaciones de compraventa de cosas muebles, locaciones y prestaciones de servicios, locaciones de cosas y obras y las señas o anticipos que congelen precios.  
Le recomendamos visitar la página web <http://www.afip.gov.ar/fe/> para obtener información sobre quienes están obligados a emitir facturas electrónicas, las características de la misma, qué es el Código de Autorización Electrónico "CAE", etc.

Más información:

Puede consultar la web de la AFIP para obtener más información referida a la factura electrónica, desde [ABC Consultas y Respuestas Frecuentes sobre Normativa, Aplicativos y Sistemas](http://www.afip.gov.ar/genericos/guiavirtual/directorio_subcategoria.aspx?id_nivel1=562&id_nivel2=603).

**Comprobantes electrónicos de exportación  
**La RG 3066/10 de la AFIP, sus Modificatorias y Complementarias establecen un régimen especial para la emisión y almacenamiento de comprobantes originales que respalden operaciones de exportación.  
Para conocer las características de este régimen, haga clic aquí: <http://www.afip.gov.ar/fe/#comp>

La RG 4480/19 de la AFIP establece el Régimen de Exportación Simplificada "Exporta Simple" con el objeto de facilitar las operaciones de exportación de menor cuantía con fines comerciales, a través de determinados Operadores Logísticos (OLES). Este régimen busca potenciar el incremento de la actividad exportadora y posibilitar la operatoria para nuevos exportadores.  
Estas operaciones de exportación simplificada solo pueden ser realizadas por Responsables Inscriptos y/o Monotributistas y siempre que las mismas no superen los U$S 1.5000 o bien la suma de dichas operaciones en un año no superen U$S 600.000.  
Previo a la generación de la factura de exportaciones se tiene que tramitar el DES (Documento de Exportación Simplificada), donde se informan todos los datos de la exportación que corresponden a bienes y que debe ser autorizado por AFIP.  
Para conocer las características de este régimen, haga clic aquí: <http://www.afip.gob.ar/exportaSimple>, o consulte la [guía de implementación respectiva](?p=6175).

Más información:

Puede consultar la web de la AFIP para obtener más información referida a la factura electrónica, desde [este link accederá a la sección ABC Consultas y Respuestas Frecuentes sobre Normativa, Aplicativos y Sistemas](http://www.afip.gov.ar/genericos/guiavirtual/directorio_subcategoria_nivel3.aspx?id_nivel1=562id_nivel2=603&id_nivel3=1527).

**Diferencias entre la factura tradicional y la factura electrónica  
**_Factura tradicional:_

  * Para solicitar la impresión de sus comprobantes fiscales, el contribuyente (la empresa emisora) se presenta en una imprenta habilitada por la AFIP para tal fin.
  * La imprenta efectúa el pedido de impresión de comprobantes a la AFIP.
  * La AFIP controla el cumplimento de los requisitos y autoriza la impresión de los comprobantes.
  * La imprenta entrega al contribuyente el talonario autorizado con "CAI" (Código de Autorización de Impresión).



De esa manera, cuando llega la hora de entregar un comprobante al cliente, el emisor le entrega un comprobante autorizado.

_Facturación electrónica:_

  * Para solicitar la impresión de sus comprobantes electrónicos, el contribuyente (empresa emisora) debe solicitar a la AFIP una clave fiscal (contraseña para poder realizar trámites desde Internet) de nivel 3. Para más información acerca de la clave fiscal, consulte la página <http://www.afip.gov.ar/claveFiscal/>
  * Además, la empresa emisora debe obtener el certificado digital generado por la AFIP (*). Para más información, acerca de su generación, consulte el ítem [Pedido de Certificado Digital](?p=26870).  
Si usted cumple con más de un régimen de facturación electrónica, puede usar el mismo certificado digital. Para ello, debe relacionarlo con los webservices correspondientes.
  * Si prefiere seguir imprimiendo, la empresa emisora debe generar nuevos formularios preimpresos. Los nuevos formularios no deben estar numerados (no incluir el número de CAI ni su fecha de vencimiento).
  * Si prefiere no imprimir el comprobante, puede enviarlo por correo electrónico.



  * El mismo contribuyente, y no la imprenta, es el que solicita autorización ante la AFIP, obteniendo el CAE que debe detallar junto al comprobante. Ello se realiza por cada uno de los comprobantes emitidos.



**(*) Ejemplos...**

  1. Usted ya opera con Factura Electrónica (para el mercado interno) y a partir del 1º de Julio del 2010 debe emitir Facturas Electrónicas de Exportación. En este caso, debe agregar la relación de su certificado digital con el webservice de factura electrónica de exportación (WSFEX).
  2. Usted ya opera con Factura Electrónica (para el mercado interno) y a partir del 1º de Enero del 2011 debe emitir Facturas Electrónicas para percibir un bono fiscal y aplicarlo al pago de impuestos nacionales. En este caso, debe agregar la relación de su certificado digital con el webservice de bonos fiscales electrónicos (wsbfev1).



Le recomendamos visitar la página web <http://www.afip.gov.ar/fe/> para obtener más información.

**Características de una factura electrónica:**

  1. Posee efectos fiscales frente a terceros si contiene el Código de Autorización Electrónico "CAE", asignado por la AFIP.
  2. Está identificada con un punto de venta específico, distinto a los utilizados para la emisión de comprobantes manuales o a través de controlador fiscal. El punto de venta debe estar comprendido entre los valores 00001 y 99998.
  3. Tiene una fecha de vencimiento específica para su remisión (10 días).
  4. Los aspectos generales de una factura electrónica de exportación son los siguientes: 
     1. Posibilidad de paginación de los comprobantes y de transporte.
     2. Los títulos / encabezados de los comprobantes podrán emitirse en idiomas distintos al español.
     3. Se cuenta con campos opcionales para la incorporación de textos libres.
     4. Confección de la factura en forma previa o con posterioridad a la oficialización de la destinación aduanera.



Más información:

No existe el concepto de talonario "multipropósito" para los comprobantes electrónicos.  
La numeración de facturas, notas de crédito y notas de débito se maneja en forma separada, aunque queda a su criterio la utilización de un formulario particular para cada tipo de comprobante, o la utilización de un único formulario para todos los comprobantes imprimiendo la palabra "FACTURA", "NOTA DE CRÉDITO" o "NOTA DE DÉBITO" según el comprobante que se emita.

##### Procedimiento de emisión de factura electrónica

Para que las facturas electrónicas sean consideradas documento con valor fiscal, en el momento de la transacción o luego de la misma, la empresa emisora debe enviarle a la AFIP los siguientes datos:

  * **En el caso de una factura electrónica del mercado interno:** el monto total de la operación, el origen (empresa emisora), datos del emisor y del receptor (el cliente).  
Si usted utiliza la versión 2 de Webservices –comprobantes 'A' y 'B' (según RG 2485) o bien, comprobantes 'C' para Monotributistas (según RG 3067), se informa además, el detalle de los comprobantes relacionados; alícuotas de IVA y otros tributos del comprobante a autorizar.  
Si usted utiliza la versión J de Webservices porque fue notificado por la Administración Federal de Ingresos Públicos respecto de su inclusión en el régimen de emisión de comprobantes electrónicos del mercado interno, mediante nota inscripta por el juez administrativo competente (según RG 2904 - Art. 4º), se informa también el detalle de cada operación (ítems del comprobante electrónico generado).
  * **Si utiliza Bonos Fiscales Electrónicos (según RG 2557/09)** , se informan los datos del comprobante incluyendo el detalle de sus ítems y el número identificatorio de proyecto asociado –si el comprobante corresponde a una actividad alcanzada por el beneficio de Promoción Industrial.
  * **Si usted opera bajo alguna de las actividades que requieren informar datos adicionales** , durante el proceso de facturación, notas de débito y notas de crédito, podrá completar dicha información.
  * **En el caso de una factura electrónica de exportación:** el origen (empresa emisora), el cliente o receptor, el detalle de los ítems, el monto total de la operación, el detalle de los documentos aduaneros (si corresponde).



La AFIP devolverá para cada comprobante un Código de Autorización Electrónico (CAE), que hace referencia a la factura que lo originó.  
Incorporando el CAE a la factura, con todos los detalles de precio, cantidades, unidades de medida, etc. y en el formato deseado, la empresa emisora genera la Factura Electrónica.  
El receptor debe recibir la factura electrónica dentro de los 10 días corridos desde la asignación del "CAE", ya sea remitida por correo electrónico o en su versión impresa.

##### Contenidos relacionados

No se ha encontrado ninguno

#### Puesta en marcha

Para implementar el circuito de comprobantes electrónicos debe seguir el procedimiento detallado a continuación.

**Pasos previos que todo cliente debe realizar ante la AFIP:**

  1. **Gestione la clave fiscal de nivel 3**. (En [www.afip.gob.ar/clavefiscal](https://www.afip.gob.ar/claveFiscal/), conozca cómo obtener la clave fiscal. Este es un trámite personal a cargo del dueño o apoderado de la empresa.)
  2. **Obtenga el certificado digital** (*). Recomendamos utilizar el programa [Pedido de certificado digital](https://ayudas.axoft.com/24ar/guia_pm1_comprobelectr_gv2) (AxCertSetup.exe) para generar la información necesaria para gestionar el certificado digital ante la AFIP. El mencionado programa se encuentra en el directorio de instalación del sistema. Este programa fue desarrollado para facilitar esta operación, no obstante puede realizar este trámite siguiendo las instrucciones de la AFIP.  
Si usted cumple con más de un régimen de facturación electrónica, puede usar el mismo certificado digital. Para ello, debe relacionarlo con los webservices correspondientes.
  3. **Realice los pasos de configuración desde la página de AFIP**.



(*) **Ejemplos...**

  1. Usted ya opera con Factura Electrónica (para el mercado interno) y a partir del 1º de Julio del 2010 debe emitir Facturas Electrónicas de Exportación. En este caso, debe agregar la relación de su certificado digital con el webservice de factura electrónica de exportación (WSFEX).
  2. Usted ya opera con Factura Electrónica (para el mercado interno) y a partir del 1º de Enero del 2011 debe emitir Facturas Electrónicas para percibir un bono fiscal y aplicarlo al pago de impuestos nacionales. En este caso, debe agregar la relación de su certificado digital con el webservice de bonos fiscales electrónicos (wsbfev1).



Le recomendamos visitar la página web <http://www.afip.gov.ar/fe/> para obtener más información.

##### Pedido de Certificado Digital

Para generar el pedido de certificado debe seguir los pasos que indica la AFIP Ya que este procedimiento tienen cierto grado de complejidad, Axoft Argentina S.A. ha desarrollado un Asistente que lo guiará en la obtención del mismo.

Para acceder a este asistente, seleccione Programas | Tango Gestión | Pedido de certificado digital y siga los pasos que se le indican en pantalla.

El asistente genera 3 archivos. Al conectarse a la web de la AFIP para entregar el pedido de certificado digital, indique como nombre de archivo aquél que tenga extensión *.req (Request) para su validación por parte del AFIP.

Tenga en cuenta que AFIP puede devolver el mensaje de error: 'El Request enviado es inválido. Por favor revíselo', en las siguientes situaciones:

  * El archivo seleccionado no es el pedido por AFIP.
  * El archivo está dañado.
  * El archivo no está correctamente generado.



En ese caso, sugerimos realizar los siguientes pasos:

  1. Reinstale Openssl.
  2. Verifique que no existan espacios en nombre y alias ingresados.
  3. Regenere archivo .req (Request).



##### Configuración en AFIP

Desde el sitio web de AFIP, apartado Contribuyentes, realice los siguientes pasos:

  1. Registre el punto de venta correspondiente ante la AFIP: desde la opción 'A / B / M de Puntos de Venta', elija 'Alta' y luego, seleccione 'RECE para aplicativo y web services' como sistema de facturación asociado.
  2. Habilite el uso de la modalidad 'Comprobantes en línea': desde la opción 'Administración de Certificados Digitales', elija 'Nueva Relación'; haga clic en "Buscar" para seleccionar el Servicio y elija 'Comprobantes en Línea'. Por último, haga clic en "Buscar" para seleccionar el representante y confirme la operación.
  3. Asocie el certificado digital obtenido a un webservice: desde la opción 'Administrador de Relaciones de Clave Fiscal', elija 'Nueva Relación'; haga clic en "Buscar" para seleccionar el Webservice a utilizar (ejemplo: WS Factura electrónica). Si utiliza más de un webservice (ejemplo: para Facturación Electrónica del mercado interno y para Facturación de Exportación), asocie el certificado a los servicios requeridos.



##### Cambio de versión de Webservices

El webservice vigente hasta el 30 de Junio del 2011 para la solicitud y autorización de emisión de comprobantes electrónicos originales del mercado interno, es el correspondiente a la Versión 0.

A partir del 01 de Julio del 2011 y, si usted emite comprobantes electrónicos 'A' y/o 'B' (según la RG 2485), elija la Versión 2.

Si usted cumple con el régimen especial de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación, con la entrada en vigencia de la RG 3066 (que modifica la RG 2758), cambia el webservice para el envío a la AFIP de estos comprobantes. Al actualizar su sistema, el webservice a considerar será WSFEXV1. Este cambio no se configura a través de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2).

Si usted debe cumplir con la Resolución General 2904 - Art. 4º (comprobantes electrónicos del mercado interno con detalle de operaciones), el webservice a utilizar será el correspondiente a la Versión J.

Si usted es Monotributista y cumple con la RG 3067 para la emisión de comprobantes electrónicos 'C', elija la Versión 2 como Webservices a utilizar.

Si usted cumple con la RG 2557/09 para la emisión de comprobantes electrónicos con aplicación de Bonos Fiscales Electrónicos (según Decreto Nº 2316/08), el webservice a utilizar lo determina el talonario asociado al comprobante electrónico.

Sin embargo, elija un Webservice de referencia, teniendo en cuenta las siguientes consideraciones:

  1. Si usted cumple sólo con la RG 2557/09 para la emisión de comprobantes electrónicos del mercado interno y la utilización de los Bonos Fiscales Electrónicos, elija la opción 'Versión 2'.  
Los comprobantes electrónicos originales que respaldan las operaciones sujetas al régimen de incentivo para las empresas productoras de bienes de capital, sus partes y accesorios, deben emitirse en los términos de la Resolución General Nº 2485 y su modificación.
  2. Si usted también cumple con otro régimen de facturación, elija la opción correspondiente de webservice: '2 - versiones 1, 1.1 y 2 de webservices' o 'J - Notificación Juez'.  
De esta manera, podrá emitir comprobantes electrónicos bajo los 2 regímenes de facturación.



Al cambiar a la versión 2 de webservices es necesario que asigne el código AFIP a las [alícuotas,](https://ayudas.axoft.com/24ar/alicuota_gv2) [monedas](?p=11955) y [percepciones definibles](https://ayudas.axoft.com/24ar/percepcdefin_gv2) antes de facturar.

La opción 'Versión 2' del parámetro Webservices a utilizar contempla las versiones 1, 1.1 y 2 de webservices según RG 2485 y también, la versión 1.1 de webservices para Bonos Fiscales Electrónicos (BFE) según RG 2557.

**Pasos a realizar por el cambio de versión de webservices**

Tenga en cuenta las siguientes indicaciones al cambiar de versión 0 a versión 2 de webservice:

  1. Invoque el proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2) para registrar la versión de webservices a utilizar.  
Para poder realizar el cambio de versión de webservices, el sistema valida que no existan comprobantes electrónicos pendientes de obtener CAE.  
Si existen comprobantes electrónicos sin CAE, ejecute el proceso [Administración de Comprobantes Electrónicos](https://ayudas.axoft.com/24ar/admincomprelectr_gv2) y obtenga el CAE de los comprobantes electrónicos pendientes / rechazados.  
Una vez obtenido el CAE de todos los comprobantes, cambie de versión de webservice desde la solapa Comprobantes electrónicos de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2).
  2. Desde el proceso [Alícuotas](https://ayudas.axoft.com/24ar/alicuota_gv2) indique, para cada una de las alícuotas, el código de tributo definido por AFIP.
  3. Si usted aplica [Percepciones definibles](https://ayudas.axoft.com/24ar/percepcdefin_gv2) defina para cada una de ellas, el código habilitado por AFIP.



##### Pasos previos a la generación de un comprobante electrónico

A continuación enumeramos los pasos necesarios para poner en marcha el circuito de Comprobantes Electrónicos:

  1. Definición de los datos de la empresa
  2. Definición de los parámetros del Administrador de Comprobantes Electrónicos
  3. Definición de las provincias
  4. Definición de los países (sólo para Comprobantes Electrónicos de Exportación)
  5. Definición de las monedas (sólo para Comprobantes Electrónicos de Exportación)
  6. Alta de talonarios
  7. Codificación de artículos (sólo para versión 'Notificación Juez' de Webservices)
  8. Clasificación de artículos
  9. Clasificación de los clientes (sólo para Comprobantes Electrónicos de Exportación)
  10. Codificación de alícuotas
  11. Codificación de percepciones definibles
  12. Resoluciones AFIP - Regímenes específicos - Reemplazo de regímenes informativos (información de datos adicionales)



_**1\. Definición de los datos de la empresa**_

Ingrese a la solapa Empresa del proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2) y complete y/o verifique los datos particulares de su empresa (razón social, domicilio, fecha de inicio de actividades y número de inscripción en Ingresos Brutos).  
Luego, ingrese a la solapa [Comprobantes electrónicos](https://ayudas.axoft.com/24ar/modifcomprobelectr_gv2) del proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2) y complete los siguientes datos:

Para comprobantes electrónicos del mercado interno:

  * Si usted cumple con la RG 2485 (sus Modificatorias y Complementarias).
  * Si usted cumple con la RG 2904 - Art. 4º (notificación juez).
  * Si usted cumple con la RG 3067 (comprobantes clase 'C' emitidos por Monotributistas).
  * Si usted cumple con la RG 2557/09 (con la utilización de Bonos Fiscales Electrónicos).
  * Si usted cumple con la RG 3749 (comprobantes clase 'M' y/o reemplazo de regímenes informativos).
  * Si usted cumple con la RG 4004 (comprobantes clase 'B' o 'C' de locación de inmuebles con destino casa habitación).



Complete los siguientes datos:

  * Ingrese la Fecha de Incorporación al régimen especial de emisión y almacenamiento electrónico de comprobantes originales.
  * No ingrese Fecha de Exclusión, ya que el sistema considerará que usted abandonó el régimen de comprobantes electrónicos.
  * Seleccione el Webservices a utilizar: 
    * Para comprobantes electrónicos 'A' y/o 'B' (según RG 2485), elija la Versión 0 - Mercado interno (vigente hasta el 30 de Junio del 2011).
    * Para comprobantes electrónicos 'A' y/o 'B' (según RG 2485), a partir del 01 de Julio del 2011 o para comprobantes electrónicos 'M' (según RG 3749) elija la Versión 2 - Incluye versiones 1, 1.1 y 2.
    * Si usted es Monotributista y cumple con la RG 3067 para la emisión de comprobantes electrónicos 'C', elija la Versión 2 - Incluye versiones 1, 1.1 y 2.
    * Si usted factura actividades alcanzadas por el reemplazo de regímenes informativos indicados en la RG 3749 o RG 4004 E, elija la Versión 2 - Incluye versiones 1, 1.1 y 2.
    * Si usted fue notificado por la Administración Federal de Ingresos Públicos respecto de su inclusión en el régimen de emisión de comprobantes electrónicos mediante nota inscripta por el juez administrativo competente (según RG 2904), elija la Versión J - Notificación Juez.
    * Si usted cumple con la RG 2557/09 para la emisión de comprobantes electrónicos con aplicación de Bonos Fiscales Electrónicos (según Decreto Nº 2316/08), el webservice a utilizar lo determina el [talonario](https://ayudas.axoft.com/24ar/talonario_gv2) asociado al comprobante electrónico.
    * Sin embargo, elija un Webservice de referencia, teniendo en cuenta las siguientes consideraciones: 
      * Si usted cumple sólo con la RG 2557/09 para la emisión de comprobantes electrónicos del mercado interno y la utilización de los Bonos Fiscales Electrónicos, elija la opción ‘Versión 2’.  
Los comprobantes electrónicos originales que respaldan las operaciones sujetas al régimen de incentivo para las empresas productoras de bienes de capital, sus partes y accesorios, deben emitirse en los términos de la Resolución General Nº 2485 y su modificación.
      * Si usted también cumple con otro régimen de facturación, elija la opción correspondiente de webservice: 'Versión 2 - versiones 1, 1.1 y 2 de webservices' o 'J - Notificación Juez'.  
De esta manera, podrá emitir comprobantes electrónicos bajo los 2 regímenes de facturación (*).
  * Configure el Indicador de servicio y Valor del Indicador: si utiliza el webservice 2 - Incluye versiones 1, 1.1 y 2, puede parametrizar la edición del Indicador de Servicio.  
Usted puede editar este dato o bien, ocultar su ingreso en los procesos de facturación (facturas, notas de débito y notas de crédito).  
Si este dato se oculta, defina el valor del indicador a tener en cuenta. Las opciones posibles son: 1 - Productos, 2 - Bienes o 3 - Productos y Servicios.  
Si el valor elegido es '2' o '3', el sistema asume que la Empresa es Prestadora de Servicios y deberá ingresar además, el período del Servicio Facturado (Mes Anterior, Mes Completo o Mes Siguiente).  
Este dato no es solicitado si usted utiliza Bonos Fiscales Electrónicos (RG 2557/09).



Para comprobantes electrónicos del mercado exterior:  
Si cumple con la RG 3066 (sus Modificatorias y Complementarias), indique la fecha de incorporación al régimen especial de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación.

  * Complete los siguientes datos: 
    * Ingrese la Fecha de Incorporación al régimen especial de emisión y almacenamiento electrónico de comprobantes originales.
    * No ingrese Fecha de Exclusión, ya que el sistema considerará que usted abandonó el régimen de comprobantes electrónicos.
    * Seleccione el Idioma habitual de los comprobantes (español, inglés o portugués).



Para comprobantes del mercado interno con codificación de las operaciones (según RG2904 - art. 4º) y comprobantes electrónicos del mercado exterior (según RG 3066):

  * Indique cuál será el Detalle del comprobante (descripción del artículo o sinónimo del cliente)
  * Indique si incluye comentarios de los artículos como parte de la descripción de los productos.



Más información:

La opción 'Versión 2' del parámetro Webservices a utilizar contempla las versiones 1, 1.1 y 2 de webservices según RG 2485 y también, la versión 1.1 de webservices para Bonos Fiscales Electrónicos (BFE) según RG 2557.

__Nota

Usted puede cambiar la versión de webservices a utilizar sólo si no existen comprobantes electrónicos pendientes de obtener CAE.

Si necesita aplicar una parametrización especial a uno o más clientes, defina esta configuración en la ficha de cada cliente. Para más información, consulte el ítem [Clasificación de los clientes](https://ayudas.axoft.com/24ar/modifcomprobelectr_gv2).

Si emite comprobantes electrónicos y la actividad de su empresa se relaciona con la Prestación de Servicios:

  * Active el parámetro Es empresa prestadora de servicios.
  * Indique la modalidad para el cálculo de las fechas del servicio facturado ('Mes anterior', 'Mes completo o actual', 'Mes siguiente'). Esta información puede ser modificada desde los procesos de facturación.  
Por ejemplo, seleccione 'Mes Anterior' si su empresa factura el primer día de cada mes, los servicios brindados el mes anterior.
  * Active el parámetro Empresa Prestadora de Servicios.
  * Si esta alcanzado por RG 3749 o RG 4004 E (reemplazo de regímenes informativos): 
    * Ingrese a la solapa Otras resoluciones ubicada en [Comprobantes electrónicos](https://ayudas.axoft.com/24ar/modifcomprobelectr_gv2) de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2) (dicha opción estará habilitada únicamente si el web service seleccionado es 'Versión 2').
    * Tilde el campo Presenta información adicional requerida por AFIP.
    * Indique el valor por defecto para el campo Actividad habitual a informar. Seleccione la actividad con que opera con mayor frecuencia, siendo sus posibilidades las siguientes (si su actividad más frecuente no está en las opciones deje el campo en blanco): 
      * Educación pública de gestión privada.
      * Locación de inmuebles rurales.
      * Locación de inmuebles turísticos.
      * Locación de inmuebles.
    * En Tipo de actividad habitual seleccione alguna de las opciones considerando la actividad que desarrolla y lo especificado en las normativas vigentes. El campo puede quedar en blanco.



Para el envío del comprobante electrónico a su cliente a través de correo electrónico:

  * Ingrese a la solapa Envío por correo electrónico.
  * Complete los datos referidos al servidor de correo electrónico, usuario (nombre de la cuenta de mail), clave (contraseña del usuario), remitente, asunto y cuerpo. Este paso no es obligatorio y puede realizarse con posterioridad.



Para el resguardo del comprobante electrónico:

  * Ingrese la ubicación en el disco donde se guardarán los archivos (en formato PDF) generados en cada facturación.



_**2\. Definición de los parámetros del Administrador de Comprobantes Electrónicos**_

Por cada computadora que emita comprobantes electrónicos, realice los siguientes pasos para poder enviar comprobantes electrónicos a la AFIP.  
En la pantalla de [Administración de Comprobantes Electrónicos](https://ayudas.axoft.com/24ar/admincomprelectr_gv2), ingrese a Parámetros y coloque los datos de conexión.

  1. Ingrese el certificado extendido por la AFIP (indique ubicación y nombre del archivo).
  2. Indique la ubicación del archivo que contiene la clave privada (utilizada para solicitar el certificado digital).
  3. Ingrese la identificación de origen (utilizada para solicitar el certificado digital).



La clave privada y la identificación de origen las puede obtener del asistente mencionado en el ítem [Pedido de Certificado Digital](https://ayudas.axoft.com/24ar/guia_pm1_comprobelectr_gv2). Tenga en cuenta que en Identificación de origen debe ingresar el contenido del archivo con extensión *.txt (no su ubicación).

__Nota

Recuerde que esta configuración debe ser efectuada en cada una de las terminales que emitan comprobantes electrónicos.

_**3\. Definición de las provincias**_

Ingrese al proceso [Provincias](https://ayudas.axoft.com/24ar/provincia_gv2) y controle que la codificación asignada en Clasificación AFIP sea la correcta para cada una de las provincias definidas.  
Este dato es requerido por la AFIP para la preparación de los archivos de comprobantes electrónicos correspondientes a la RG 2485 (sus Modificatorias y Complementarias), la RG 2557/09 (Bonos Fiscales Electrónicos) y a la RG 1361.

_**4\. Definición de los países (sólo para Comprobantes Electrónicos de Exportación)**_

Si usted genera comprobantes electrónicos de exportación (RG 3066), invoque el proceso [Países](https://ayudas.axoft.com/24ar/pais_gv2) del módulo Ventas y complete la clasificación AFIP con el código que este organismo asigna a cada país.

_**5\. Definición de las monedas (sólo para Comprobantes Electrónicos de Exportación)**_

Si usted genera comprobantes electrónicos para el mercado interno y/o de exportación, invoque el proceso [Monedas](?p=11955) del módulo Procesos generales y complete el Código moneda Comp Elec. con la clasificación que la AFIP asigna a cada unidad monetaria.

_**6\. Alta de talonarios**_

Ingrese al proceso [Talonarios](https://ayudas.axoft.com/24ar/talonariocomprobelectr_gv2) y defina los talonarios (nuevos puntos de venta solicitados en AFIP) a utilizar durante la generación de comprobantes electrónicos.  
En cada uno de esos talonarios, active el parámetro Genera Comprobante Electrónico.  
Al definir un talonario de comprobantes electrónicos, tenga en cuenta las siguientes consideraciones:

  * No es posible aplicar la modalidad 'Multipropósito', por lo que deberá dar de alta talonarios para Facturas, N/D y N/C en forma independiente.
  * Para imprimir comprobantes electrónicos, ingrese el destino de impresión en el talonario.
  * El primer número habilitado del talonario debe ser 1 (uno).
  * Defina el Tipo de Conexión a utilizar para su comunicación con la AFIP ('En Línea' o bien, 'Diferido'). 
    * En Línea: indica que en el momento de emitir el comprobante electrónico, Tango se comunicará con el servidor de la AFIP para solicitar el CAE. correspondiente. Para más información consulte [Modalidad en Línea](?p=26603#enlinea).
    * Diferido: indica que la obtención del CAE será posterior a la confección del comprobante electrónico. Tenga en cuenta que un comprobante electrónico sin CAE no tiene validez legal, y por lo tanto no puede ser entregada al cliente. Para más información consulte [Modalidad Diferida](?p=26603#diferida).
  * Si usted cumple con la RG 2557/09 para la emisión de comprobantes electrónicos del mercado interno y la utilización de los Bonos Fiscales Electrónicos, defina los talonarios con tipo asociado 'A' y/o 'B' para la generación de comprobantes electrónicos. Para cada talonario, tilde el parámetro Utiliza Bono Fiscal Electrónico. De esta forma, los diferenciará de los talonarios electrónicos con letra 'A' y/o 'B' que utilicen otro webservice.
  * Si usted cumple con la RG 3749 y necesita emitir comprobantes electrónicos tipo Recibo (Facturas - Recibo) debe tildar el campo Recibo-factura para que al generar el comprobante electrónico este sea informado a AFIP con el código correspondiente. Si necesita emitir comprobantes 'M' debe crear un talonario electrónico del tipo 'M'.
  * Indique si imprime el comprobante electrónico una vez obtenido el CAE.
  * Indique si envía el comprobante generado a su cliente por correo electrónico.
  * Ingrese la ubicación (directorio o carpeta) y el nombre de la imagen escaneada del formulario preimpreso a incluir en los comprobantes que se envíen por correo electrónico. Sugerimos escanear el formulario preimpreso grabando la imagen sin márgenes adicionales. Es posible que deba efectuar algunas pruebas hasta que la visualización del archivo pdf sea correcta. Tenga en cuenta que a diferencia de los comprobantes no electrónicos, los comprobantes electrónicos pueden imprimirse o enviarse por correo electrónico cuantas veces lo desee.
  * Acceda a la opción Formularios, invoque la función Dibujar <F6> para agregar las variables de reemplazo para comprobantes electrónicos (CAE, Fecha de Vencimiento, etc.). Tenga en cuenta que también es necesario agregar las variables de reemplazo para Tipo de comprobante y Número de Comprobante.
  * Si cumple con la RG 3066, diseñe sus formularios incluyendo las [palabras de control para comprobantes electrónicos de exportación](https://ayudas.axoft.com/24ar/var_palabcontrol_gv2) y las [palabras de reemplazo para comprobantes electrónicos de exportación](https://ayudas.axoft.com/24ar/variables_gv2).
  * Si necesita emitir comprobantes 'A' con CBU Informado, recuerde diseñar el formulario correspondiente incluyendo la leyenda "Pago en CBU informado". Ubique dicha leyenda según lo indicado en la normativa vigente.



**¿Cuántos talonarios debo definir?  
**Si usted genera en forma electrónica, comprobantes de facturas, notas de débito y notas de crédito de tipo 'A' y 'B', sugerimos definir por punto de venta, un talonario electrónico para cada tipo de comprobante / tipo asociado / número de sucursal. Es decir, no debería tener definidos más de 3 talonarios electrónicos de clase 'A' (FAC, DEB, CRE) ni más de 3 talonarios electrónicos de clase 'B' (FAC, DEB, CRE) por punto de venta.  
Si usted genera en forma electrónica, comprobantes de facturas, notas de débito y notas de crédito de tipo 'C' (para Monotributistas), sugerimos definir por punto de venta, un talonario electrónico para cada Tipo de comprobante / Tipo asociado / Número de sucursal. Es decir, no debería tener definidos más de 3 talonarios electrónicos de clase 'C' (FAC, DEB, CRE) por punto de venta.  
Si usted genera en forma electrónica, comprobantes de exportación (facturas, notas de débito y notas de crédito de tipo 'E'), sugerimos definir por punto de venta, un talonario electrónico para cada Tipo de comprobante / Tipo asociado / Número de sucursal. Es decir, no debería tener definidos más de 3 talonarios electrónicos de clase 'E' (FAC, DEB, CRE) por punto de venta.  
Si usted genera en forma electrónica, comprobantes de facturas, notas de débito y notas de crédito de tipo 'A' y 'B' (según RG 2557/09), sugerimos definir por punto de venta, un talonario electrónico para cada Tipo de comprobante / Tipo asociado / Número de sucursal. Es decir, no debería tener definidos más de 3 talonarios electrónicos de clase 'A' (FAC, DEB, CRE) ni más de 3 talonarios electrónicos de clase 'B' (FAC, DEB, CRE) por punto de venta.  
Si usted genera en forma electrónica comprobantes del mercado interno según la RG 2485 y/o según la RG 2557/09 (Bonos Fiscales Electrónicos), defina un juego de talonarios para cada resolución general.  
Es decir, 3 talonarios electrónicos de clase 'A' ('FAC', 'DEB', 'CRE') y 3 talonarios electrónicos de clase 'B' ('FAC', 'DEB', 'CRE') por punto de venta si emite comprobantes electrónicos para el mercado interno según RG 2485; y además, 3 talonarios electrónicos de clase 'A' ('FAC', 'DEB', 'CRE') que utilicen BFE y 3 talonarios electrónicos de clase 'B' ('FAC', 'DEB', 'CRE') que utilicen BFE por punto de venta, si emite comprobantes electrónicos asociados a Bonos Fiscales Electrónicos.

_**7\. Codificación de artículos (sólo para versión 'Notificación Juez' de Webservices)**_

Ingrese al proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) del módulo Stock y en la solapa Principal complete el código de barras de cada artículo.  
Este dato es requerido por la AFIP para la preparación de los archivos de comprobantes electrónicos correspondientes a la RG 2904 (Régimen especial de emisión y almacenamiento electrónico de comprobantes originales. Codificación de las operaciones efectuadas).

_**8\. Clasificación de artículos**_

Ingrese al proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) del módulo Stock y complete los siguientes datos en la solapa Datos legales:

**Para Comprobantes Electrónicos (del mercado interno)  
**Indique el Código de Unidad de Medida de Stock (definido por AFIP) y su Equivalencia.  
Seleccione el Código de Unidad de Medida para la presentación de Ventas (definido por AFIP) y el valor de su Equivalencia.  
Estos datos son requeridos por la AFIP para el envío de información de los comprobantes electrónicos.  
Si usted emite comprobantes electrónicos clase 'A', 'B' y utiliza Bonos Fiscales Electrónicos (según RG 2557/09), asigne a sus artículos, el Código de producto (N.C.M.) -según el Nomenclador Común del Mercosur.

**Para Comprobantes de Exportación Electrónicos  
**Ingrese la clasificación según AFIP para la Unidad de Medida de Stock y para la presentación de Ventas.  
Estos datos son requeridos por la AFIP para el envío de información de los comprobantes de facturación electrónicos correspondientes a operaciones de exportación.

**Para comprobantes electrónicos del mercado interno y para comprobantes electrónicos de exportación  
**Tenga en cuenta que:

  * Usted puede actualizar los datos de los artículos en forma masiva, utilizando el proceso [Actualización Global de Códigos de AFIP](?p=17025) del módulo Stock.
  * Puede invocar el comando Listar para obtener información de los artículos que han sido configurados y también, aquellos no configurados para la generación de comprobantes electrónicos.
  * Usted puede actualizar el Código de producto (N.C.M.) desde el proceso [Actualización Masiva de Artículos](?p=17026) del módulo Stock.



_**9\. Clasificación de los clientes (sólo para Comprobantes Electrónicos de Exportación)**_

Para el Envío de Comprobantes Electrónicos:  
Si su empresa emite comprobantes electrónicos (del mercado interno y/o de exportación), defina para cada uno de sus clientes, los siguientes datos:

Forma de Envío: indique la modalidad de envío a su cliente de los comprobantes electrónicos que usted emita. Puede optar por una de las siguientes opciones: e-mail, e-mail / papel o tener en cuenta la definición del talonario.

Mail Envío: es la dirección de e-mail para el envío de los comprobantes electrónicos. Por defecto, se propone la dirección ingresada en el campo Correo electrónico del cliente.

Para Comprobantes Electrónicos con Codificación de las Operaciones  
Si cumple con la RG 2904 - Art. 4º (Webservice: 'Notificación Juez') para la emisión de comprobantes electrónicos del mercado interno con el detalle de la codificación de las operaciones, y necesita aplicar una configuración particular a uno o más clientes, defina los siguientes parámetros:

Detalle de los artículos: indique si considera el definido en el 'Artículo' o el definido para el 'Artículo - Cliente'.

Incluye Comentarios de los artículos como parte de la descripción de los productos.  
Por defecto, el sistema considera lo definido en la solapa Comprobantes electrónicos del proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2).

Para Comprobantes de Exportación Electrónicos:  
Si cumple con la RG 3066 (sus Modificatorias y Complementarias) para la emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación, ingrese la Identificación Tributaria de cada uno de los clientes a los que emite comprobantes de tipo 'E'.  
En el caso de no completar este dato, el sistema informará a la AFIP, el CUIT del país destino del comprobante electrónico de exportación.  
Si necesita aplicar una configuración particular a uno o más clientes, defina los siguientes parámetros para comprobantes electrónicos de exportación:

  * Idioma del comprobante (español, inglés o portugués).
  * Detalle de los artículos: indique si considera el definido en el 'Artículo' o el definido para el 'Artículo - Cliente'.
  * Incluye Comentarios de los artículos como parte de la descripción de los productos.



Por defecto, el sistema considera lo definido en la solapa Comprobantes electrónicos del proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2).

_**10\. Codificación de alícuotas**_

Para cada [alícuota](https://ayudas.axoft.com/24ar/alicuota_gv2) ingresada en el sistema, indique cuál es el código definido por AFIP.  
Realice este paso si emite comprobantes electrónicos del mercado interno.

_**11\. Codificación de percepciones definibles**_

Para cada [percepción definible](https://ayudas.axoft.com/24ar/percepcdefin_gv2), seleccione el código definido por AFIP.  
Realice este paso si emite comprobantes electrónicos del mercado interno.

__Nota

Tenga en cuenta que podrá configurar percepciones definibles para clientes y artículos, las cuales se utilizarán sólo en Facturador.

_**12\. Resoluciones AFIP - Regímenes específicos - Reemplazo de regímenes informativos (información de datos adicionales)**_

Si usted está alcanzado por la RG 3749 o la RG 4004 - E (*) y alguna de sus actividades requiere informar datos adicionales debe parametrizar el sistema para informarlos.  
Recuerde que esto aplica para los comprobantes electrónicos que sean emitidos mediante web service 2 y en talonarios que no utilicen bonos fiscales.

(*) La información adicional requerida por la RG 4004 solo se podrá informar a AFIP utilizando el Facturador.

Para ello, debe realizar los siguientes pasos:

**1\. Configurar en Parámetros de venta - Comprobantes electrónicos - Solapa Otras resoluciones  
**En la solapa Otras resoluciones de [Comprobantes electrónicos](?p=19401/#parametros-para-comprobantes-electronicos) encontrará los siguientes campos:

Resoluciones AFIP - Regímenes específicos - Reemplazo de regímenes informativos: tilde esta opción si alguna de sus actividades se corresponde con alguna de las comprendidas en los alcances de la citada normativa.

En ese caso, complete los siguientes campos.

Actividad habitual a informar: seleccione la actividad más recurrente.

  * Educación pública de gestión privada.
  * Locación de inmuebles rurales.
  * Locación de inmuebles turísticos.
  * Locación de inmuebles.



Si su actividad más frecuente no se encuentra entre esas opciones, deje el campo en blanco.

Tipo de actividad habitual: seleccione el tipo habitual de sus comprobantes, pudiendo ser:

  * **Para RG 3749:**
    * Comprendida.
    * No comprendida.
  * **Para RG 4004 - E:**
    * Propietario directo.
    * A través de intermediario.



En las resoluciones indicadas, rectificativas y complementarias se determinan las condiciones que hacen que los comprobantes correspondan a un tipo u otro. El campo puede ser dejado en blanco y ser completado, en caso de corresponder, al momento de emitir el comprobante.

**2\. Definir los perfiles que necesite para su operación  
**_Perfiles de facturación  
_En la pantalla de perfiles de facturación configure los siguientes campos:

Estos campos determinan el comportamiento de los ítems Actividad a informar y Tipo de actividad en los procesos de [Facturación](https://ayudas.axoft.com/24ar/facturas_gv2) y [Pedidos](https://ayudas.axoft.com/24ar/ingresopedido_gv2).

Actividad a informar y Tipo de actividad: se aplican únicamente en la emisión de comprobantes electrónicos que utilicen web service 2 y no utilicen talonario de bonos fiscales.  
Opciones de comportamiento:

  * O - Obligatorio: los comprobantes no podrán ser generados sin indicar en ellos la actividad y tipo de actividad a informar. Esta opción de comportamiento únicamente se aplica durante el ingreso de comprobantes de facturación (no afecta al ingreso de pedidos).
  * N - No obligatorio: el sistema no obligará a indicar la actividad y tipo de actividad a informar en sus comprobantes. Esta es la opción recomendada si usted posee varias actividades y algunas de ellas no deben informar datos adicionales según RG 3749.



Utilice estas opciones junto a 'Edita', 'Muestra' u 'Oculta' para conseguir el comportamiento deseado durante el ingreso de los comprobantes.

Valores por defecto: indique en estos campos la actividad y tipo de actividad que desea informar al utilizar este perfil. Estos campos pueden quedar en blanco y completar los valores en el ingreso del comprobante.

__Nota

Tenga en cuenta que si la factura se genera en referencia a un pedido, la actividad a informar será la parametrizada en el mismo.

_Perfiles de notas de crédito_

En la pantalla perfiles de notas de crédito configure los siguientes campos:

Estos campos controlan el comportamiento de los campos Actividad a informar y Tipo de actividad en los procesos de [emisión de notas de crédito](https://ayudas.axoft.com/24ar/emisionc_gv2).

Actividad a informar y Tipo de actividad: se aplican únicamente en la emisión de comprobantes electrónicos que utilicen el web service 2 y no utilicen talonario de bonos fiscales.  
Opciones de comportamiento:

  * O - Obligatorio: las notas de crédito no podrán ser generadas sin indicar la actividad a informar.
  * N - No obligatorio: el sistema no obligará a indicar la actividad a informar en sus notas de crédito. Esta es la opción le permitira modificar los datos en el ingreso de los comprobantes o bien dejarla en blanco.



Utilice estas opciones junto a 'Edita', 'Muestra' u 'Oculta' para conseguir el comportamiento deseado durante el ingreso de los comprobantes.

Valores por defecto: indique en estos campos la actividad y tipo de actividad que desea informar al utilizar este perfil. Estos campos pueden quedar en blanco y completar los valores en el ingreso del comprobante.

**3\. Definir los contactos responsables del pago  
**Si su actividad corresponde a "Educación pública de gestión privada" debe informar el tipo y número de documento del responsable del pago. Para ello, en la pantalla Contactos el cliente encontrará los siguientes campos.

Responsable de pagos: tilde el contacto que sea responsable del pago de sus facturas. Sólo uno de los contactos del cliente podrá ser el responsable del pago.

Tipo de documento y Número de documento: correspondiente al documento del contacto. Estos campos son obligatorios para el contacto responsable del pago.

**4\. Emisión de facturas / notas de crédito / notas de débito y pedidos  
**

Al ingresar un comprobante de factura, nota de débito, nota de crédito o pedido, se presentará una pantalla para indicar los datos que serán informados a la AFIP en el comprobante electrónico correspondiente. Esta pantalla se presentará automáticamente luego de ingresar los datos de cabecera. También puede acceder a esta pantalla pulsando <Ctrl + I>.

Actividad a informar: en este campo ingrese la actividad a informar según corresponda al comprobante que está emitiendo, puede quedar en blanco.

Tipo de actividad: seleccione alguna de las opciones considerando la actividad que desarrolla y lo especificado en las normativas vigentes. El campo puede quedar en blanco.

Pedidos: los valores por defecto para la actividad y el tipo de actividad a informar se tomarán del perfil seleccionado. Si no utiliza perfiles, el sistema tomará los valores indicados en Parámetros de Ventas.

Facturación: los valores por defecto para la actividad y el tipo de actividad a informar se tomarán de los pedidos referenciados. Si no se emite el comprobante en relación a pedidos, el sistema tomará los valores por defecto indicados en el perfil que esté utilizando. Si no utiliza perfiles el sistema tomará los valores indicados en Parámetros de Ventas.

Notas de crédito: los valores por defecto para la actividad a informar y el tipo de actividad se tomarán del comprobante de referencia. Si el comprobante de referencia no fuera electrónico, o si no emite la nota de crédito en relación a un comprobante de referencia, los obtendrá del perfil que se esté utilizando. Si no se utilizan perfiles, los obtendrá de Parámetros de Ventas.

Notas de débito: los valores por defecto para la actividad a informar y el tipo de actividad se tomarán del comprobante de referencia Si el comprobante de referencia no fuera electrónico, o si no emite la nota de débito en relación a un comprobante de referencia, los obtendrá de Parámetros de Ventas.

Responsable del pago: si la actividad que usted informa en el comprobante corresponde con "Educación pública de gestión privada", complete los datos del responsable del pago.

Tipo de documento: indique en este campo el tipo de documento (CUIT - CUIL o DNI) del responsable del pago.

Número de documento: registre en este campo el número de documento del responsable del pago. Si el tipo de documento ingresado es un CUIT o un CUIL el sistema verifica que el número sea correcto.

__Nota

Tenga en cuenta que AFIP valida el tipo y número de documento ingresado contra el padrón general, por lo cual es importante ingresar datos correctos para evitar rechazos en los comprobantes.

__Nota

Los valores por defecto para el tipo y número de documento del responsable del pago se tomarán del contacto del cliente que este definido como tal, o bien del comprobante de referencia. Si no hay un contacto parametrizado como responsable del pago o se genera una factura a un cliente ocasional, se utilizará el tipo y número de documento del cliente.

##### Consideraciones adicionales para comprobantes 'E' a clientes de Tierra del Fuego

Si usted emite comprobantes electrónicos de exportación (clase 'E') a clientes de Tierra del Fuego, tenga en cuenta las siguientes indicaciones:

  * **Países:**
    * VERIFIQUE que exista un país con el nombre TIERRA DEL FUEGO.
    * VERIFIQUE que en Clasificación AFIP tenga asignado el código 250 (Tierra del Fuego - (AAE)) -que es el código asignado por este organismo.
  * **Provincias:**
    * VERIFIQUE que exista la provincia correspondiente a TIERRA DEL FUEGO.
    * VERIFIQUE que la codificación asignada en Clasificación AFIP sea la correcta para esta provincia (24).
  * **Clientes:**
    * VERIFIQUE que sus clientes tengan asignados el País y la Provincia correctas.
    * TENGA EN CUENTA que para clientes de Tierra del Fuego sólo se permite que liquiden percepciones de Ingresos Brutos.



##### Consideraciones adicionales para la generación de comprobantes T

A continuación, enumeramos los pasos necesarios para poner en marcha el circuito de comprobantes electrónicos T (de turismo):

  * **Parámetros de ventas:** ingresando a [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2), dentro de la solapa [Comprobantes electrónicos](https://ayudas.axoft.com/24ar/paramgrales_gv2/#parametros-para-comprobantes-electronicos), sub-solapa Resoluciones, habilite la opción Genera información RG 3971.
  * **Definición de talonarios:** ingrese a [Talonarios](https://ayudas.axoft.com/24ar/talonario_gv2) y defina los talonarios electrónicos tipo 'T' a utilizar durante la generación de comprobantes indicando el nuevo punto de venta asignado por AFIP.  
Para más información sobre consideraciones generales consulte [Alta de talonarios](?p=26876/#6).
  * **Definición del TYP de impresión:** ingrese desde el módulo Procesos generales a Formularios | Ventas para definir el dibujo del TYP a utilizar según lo solicitado por la RG 3971.  
Para la definición del TYP, usted posee nuevas variables específicas: **@JT:** forma de pago seleccionada, **@NJ:** número de tarjeta, **@SW:** código SWIFT, **@NW:** número de cuenta.
  * **Codificación de alícuotas:** para la generación del reintegro de IVA, defina una alícuota de IVA (con código de alícuota del 1 al 10), con Porcentaje: 21% y con Código AFIP: 10 - 21% Aplica reintegro.  
Por otra parte, verifique la existencia de la alícuota con código 91 - IVA Liberado.
  * **Codificación de artículos:** ingrese al proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) del módulo Stock y, para los artículos que se incluyen en los comprobantes electrónicos tipo 'T', complete dentro de la solapa Datos legales (en la sección Comprobantes de turismo electrónico) los datos correspondientes a: 
    * Tipo de ítem según la codificación de AFIP: 
      * 00 - Ítem general
      * 91 - Ajuste de IVA
      * 97 - Anticipo
      * 99 - Descuento General.
    * Tipo de ítem según la codificación de AFIP: 
      * 0001 - Servicio de alojamiento sin desayuno
      * 0002 - Servicio de alojamiento con desayuno
      * 0005 - Excedente
      * 0020 - Modificación de Información de los huéspedes sin modificación del importe
      * 0021 - Modificación de la fecha de ingreso sin modificación de importe.
    * Tipo de unidad (*): 
      * 0001 - Persona
      * 0002 - Carpa
      * 0003 - Bungalow
      * 0004 - Cabaña
      * 0005 - Departamento
      * 0010 - Single
      * 0011 - Doble
      * 0012 - Triple
      * 0013 - Cuádruple
      * 0014 - Plaza (para hostel).
  * **Generación de comprobantes T:** genere los comprobantes electrónicos T desde el Facturador. Para más información consulte [Generar comprobantes electrónicos T](https://ayudas.axoft.com/24ar/genercomprobelectt_posgv).



(*) Los artículos a los que podrá definir estas características e incluir en comprobantes electrónicos T, son aquellos de tipo simple, que no usan escala, no llevan series ni partidas y no facturan por importe.

Generación de notas de débito T:

En la versión actual no se encuentra disponible la generación de notas de débito T. Momentáneamente deberá registrarlo como una factura.

##### Consideraciones para la generación de Factura de crédito electrónica MiPyME (Ley 27440)

En base Ley de Financiamiento Productivo Nº 27440, La RG N° 4367/2018 de la AFIP, sus Modificatorias y Complementarias establecen un régimen especial para la emisión y almacenamiento de comprobantes originales que respalden facturas de crédito electrónicas.

Para conocer las características de este régimen, haga clic aquí: <https://www.afip.gob.ar/facturadecreditoelectronica/default.asp>.

**Pasos previos a la generación de un comprobante de crédito electrónico**

Luego de completar los [pasos previos que todo cliente debe realizar ante la AFIP](?p=26876) y los de la generación de un Comprobante de Crédito electrónico, utilice los procesos indicados para poner en marcha el circuito de comprobante de créditos electrónicos:

  * **Parámetros de ventas:** ingrese a [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2), dentro de la solapa Comprobantes electrónicos, sub-solapa Otras resoluciones, defina el CBU del emisor (dato obligatorio para la generación de este tipo de comprobantes).
  * **Talonarios:** ingrese al proceso [Talonarios](https://ayudas.axoft.com/24ar/talonariocomprobelectr_gv2) y defina los talonarios (nuevos puntos de venta solicitados en AFIP) a utilizar durante la generación de comprobantes de crédito electrónicos.  
En cada uno de esos talonarios, active, además de las consideraciones propias para factura electrónica, el parámetro Comprobante de crédito electrónico.



**Generación de comprobantes de crédito electrónicos MiPyme**

Para generar un comprobante de crédito electrónico:

  * Seleccione un [talonario](https://ayudas.axoft.com/24ar/talonariocomprobelectr_gv2) que tenga activado el parámetro Comprobante de crédito electrónico.
  * Seleccione una [condición de venta](https://ayudas.axoft.com/24ar/condicionventa_gv2) de contado, o con una cuota.



Para más información consulte [Generar comprobantes de crédito electrónicos](?p=19327).

##### Contenidos relacionados

No se ha encontrado ninguno

#### Detalle del circuito

Una vez terminada la etapa de puesta en marcha opere con los siguientes procesos para generar comprobantes electrónicos: [Facturas](?p=19327), [Facturas punto de venta](?p=19302), [Notas de crédito](?p=19289) y [Notas de débito](?p=19290), más los procesos relacionados con la [facturación de pedidos](?p=72911/#facturacion-de-pedidos).  
Además, usted puede consultar y operar con la información específica de los comprobantes electrónicos desde los siguientes procesos:

  * Desde [Administración de comprobantes electrónicos](?p=19186) podrá solicitar a la AFIP la autorización de emisión de aquellos comprobantes electrónicos pendientes o rechazados por AFIP. Desde esta opción también podrá visualizar, imprimir o enviar por correo electrónico los comprobantes ya autorizados por la AFIP.
  * Desde [Modificación de comprobantes](?p=20552) podrá consultar y modificar los datos de sus comprobantes electrónicos del mercado interno y de sus comprobantes electrónicos de exportación.
  * Si desea anular un comprobante electrónico, el sistema le avisará que no será posible. El procedimiento adecuado es ingresar un comprobante (ya sea nota de crédito o una nota de débito) para registrar la anulación.



Desde el proceso [IVA Ventas](?p=21546), podrá listar los comprobantes con su respectivo CAE y aquellos que aún están pendientes de obtenerlo.  
Desde el proceso [Generación del archivo 1361](?p=21480/#generacion-de-archivo-rg-1361) podrá obtener los archivos de duplicados electrónicos, archivo de percepciones, el código de seguridad y el archivo de registraciones de operaciones de ventas para cumplir con dicha resolución.

##### Generación de comprobantes electrónicos

Existen dos modalidades con las que puede comunicarse con AFIP para solicitar el CAE.  
Al definir cada [talonario](?p=26876/#6), usted decide el tipo de conexión con AFIP, las que explicamos a continuación:

  * Modalidad "En línea"
  * Modalidad "Diferida"



Más información:

Es posible solicitar el código de autorización "CAE" en el mismo momento de la venta (modalidad "En línea") o posteriormente (modalidad "Diferida"). Para esta última modalidad, desde el [Administrador de comprobantes electrónicos](?p=19186) solicite el CAE pendiente. Esta opción también resulta de utilidad cuando algún comprobante fue rechazado por la AFIP.

Tenga en cuenta que, en caso de tener un talonario definido como de conexión "En línea" y si durante el proceso de facturación no se puedan realizar comprobantes electrónicos, el sistema preguntará si se desea modificar el tipo de conexión a "Diferido" para poder guardar el comprobante.

**Modalidad 'En línea'**

La modalidad "en línea" es un proceso automático mediante el cual se obtiene el código de autorización (desde el mismo proceso [Facturación](?p=18441)) en forma automática, vía Internet.  
Para ejemplificar el proceso de facturación electrónica, tomamos el caso de una empresa que emite facturas electrónicas (Emisor) en base a la modalidad de obtención del CAE "en línea". En la figura inferior podemos observar que un cliente realiza un pedido. El emisor envía los datos referidos a la operación a la AFIP. solicitando el código de autorización "CAE".

Realice los siguientes pasos para generar comprobantes electrónicos en esta modalidad:

  1. Inicie el proceso de emisión de comprobantes correspondiente ([Facturas](?p=19327), [Notas de crédito](?p=19289) y [Notas de débito](?p=19290)).
  2. Seleccione un talonario de comprobantes electrónicos que tenga configurada esta modalidad (al seleccionar el formulario, la modalidad de conexión se podrá observar en la parte superior, a la derecha del _Tipo de Comprobante_).
  3. Ingrese los datos del comprobante.
  4. Pulse <F10> para aceptar el comprobante.
  5. De manera automática, el sistema se conecta vía web con la AFIP para obtener el código de autorización electrónico (CAE) correspondiente al comprobante ingresado.
  6. Si el comprobante fue autorizado por la AFIP: 
     1. Se exhibe el número de comprobante y el número de CAE obtenido.
     2. Si activó el parámetro Imprime comprobante, se emite el comprobante con CAE y fecha de vencimiento del CAE.
     3. Si activó el parámetro Envía comprobante por correo electrónico, el comprobante autorizado se envía al cliente. Si cumple con la RG 2485, se remite también el archivo correspondiente al Anexo V de la mencionada resolución.
  7. Si el comprobante no fue autorizado por la AFIP: 
     1. Se exhibe el número de comprobante y el motivo de su rechazo. (*)



**(*)** Si el comprobante fue rechazado por la AFIP:

  1. Usted puede seguir operando 'En línea' pero tenga en cuenta que los comprobantes posteriores serán también rechazados dado que la AFIP verifica la correlatividad de los comprobantes para el otorgamiento del CAE.
  2. Usted puede cambiar el tipo de conexión a 'Diferido'. Este cambio puede realizarse luego de seleccionar el medio de pago, en ese momento, de haber algún comprobante rechazado o pendiente, el sistema consultará si desean cambiar la conexión para poder guardar el comprobante. De esa forma, evita seguir enviando comprobantes que serán rechazados por AFIP. Esto se deberá repetir en cada comprobante que se quiera generar luego de que uno sea rechazado y hasta que dejen de haber comprobantes pendientes o rechazados.
  3. Usted puede consultar el problema que originó el rechazo del comprobante desde el proceso [Administración de comprobantes electrónicos](?p=19186). Una vez solucionado el problema puede obtener el CAE desde este proceso.



**Modalidad 'Diferida'**

En este caso, el emisor tramita el pedido del CAE en un momento posterior a la confección de la factura, pudiendo realizar una solicitud de varios comprobantes a la vez.

Al recibir las autorizaciones, el emisor podrá generar los comprobantes pendientes.

Más información:

Si usted elige, como tipo de conexión con AFIP, la modalidad 'Diferida', tenga en cuenta que la solicitud de autorización de comprobantes a la AFIP no puede exceder los 5 (cinco) días corridos de la fecha de los comprobantes. De tratarse de prestaciones de servicios, dicha transferencia podrá efectuarse dentro de los 10 días corridos anteriores o posteriores a la fecha consignada en el comprobante.

Realice los siguientes pasos para generar comprobantes electrónicos en esta modalidad:

  1. Ingrese al proceso de emisión de comprobantes correspondiente ([Facturas](?p=19327), [Notas de crédito](?p=19289) y [Notas de débito](?p=19290)).
  2. Seleccione un talonario de comprobantes electrónicos que tenga configurada esta modalidad (al seleccionar el talonario, la modalidad de conexión se podrá observar en la parte superior, a la derecha del _Tipo de Comprobante_).
  3. Ingrese los datos del comprobante.
  4. Pulse <F10> para aceptar el comprobante.
  5. El sistema informa el número de comprobante generado y le avisa que queda pendiente la autorización del comprobante por parte de la AFIP (obtención del CAE).
  6. Para obtener el CAE de los comprobantes generados en esta modalidad, ejecute el proceso [Administración de comprobantes electrónicos](?p=19186).



##### Consideraciones generales

  * Tenga en cuenta que un comprobante electrónico no tiene efectos fiscales frente a terceros hasta que la Administración Federal de Ingresos Públicos (AFIP) otorgue el Código de Autorización Electrónico (CAE). Es decir, no son considerados en los procesos que generan información para los distintos aplicativos.
  * Un comprobante puede tener CAE y haber sido 'Observado' por AFIP En ese caso, usted puede consultar el motivo de la observación desde los siguientes procesos (*): 
    * [Administrador de comprobantes electrónicos](https://ayudas.axoft.com/24ar/admindocelectr_gv2), solapa Comprobantes autorizados, pulsando en la columna "Observación AFIP".
    * Consulta Live de Facturación de Ventas, habiendo elegido un determinado comprobante.
  * Si genera un comprobante electrónico para un cliente ocasional es necesario que ingrese los datos de su cliente para que su comprobante pueda ser autorizado por la AFIP.
  * Desde los procesos de emisión de comprobantes es posible cambiar el tipo de conexión con AFIP, haciendo clic en el comando Comprobante electrónico. De esta manera, usted pasa a la modalidad 'En Línea', 'Diferido' o 'Según Talonario'.
  * El sistema aplica validaciones particulares en el ingreso de comprobantes electrónicos.
  * Si emite el remito junto con la factura, se solicita el destino de impresión del remito (según la definición de su formulario o .Typ) y se informa el número de remito generado.
  * Si la actividad de su empresa se relaciona con la prestación de servicios y emite comprobantes electrónicos 'A' o 'B' (para el mercado interno), en procesos de facturación es posible modificar el rango de fechas del servicio facturado.
  * Sólo es posible anular un comprobante electrónico 'Aceptado' mediante otro comprobante electrónico. Ejemplo: una factura electrónica sólo puede anularse mediante una nota de crédito electrónica.
  * El sistema permite eliminar todos los comprobantes electrónicos 'Rechazados' por AFIP.  
Esta opción se encuentra en el [Administrador de comprobantes electrónicos](https://ayudas.axoft.com/24ar/admindocelectr_gv2) y estará disponible según el rol asignado al usuario.  
El número de comprobante eliminado será reutilizado en la generación de un nuevo comprobante electrónico del mismo talonario.
  * Si optó por eliminar sólo algunos comprobantes electrónicos rechazados, tenga en cuenta que deberá verificar el Próximo número a emitir del talonario asociado, previo a continuar con la facturación.
  * Para registrar ajustes, devoluciones, recargos, etc., en donde el comprobante a generar NO tiene igual clase (letra) que la factura que dio origen a la operación, ingrese un comprobante de débito o de crédito -es posible indicar el comprobante de referencia (Tipo y Número de comprobante) y el Período asociado.  
El Período asociado (desde fecha - hasta fecha) se informará en el xml del comprobante a enviar a AFIP. Este dato es de ingreso obligatorio.  
Al informar un comprobante de referencia, quedará registrada en el sistema, la imputación del comprobante (de débito o de crédito).  
En los procesos de generación automática o masiva de comprobantes de débito o crédito, quedan registradas las imputaciones en el sistema y se informará automáticamente el período asociado en el XML del comprobante a enviar a AFIP. Por defecto, se informa la fecha de emisión del comprobante de ajuste, como rango fechas de este período.  
De esta manera, evitará que su comprobante electrónico sea rechazado por AFIP (al ser de distinta clase o tener letra diferente a la del comprobante de origen).
  * Si usted emite comprobantes electrónicos para el mercado interno y utiliza la versión 'Notificación Juez' de webservices (según R.G. 2904 - Art. 4º) y obtiene el rechazo de una nota de débito o nota de crédito electrónica, en la que indicó un Período de referencia, verifique si el emisor del comprobante o el cliente indicados están inscriptos en el régimen de Factura Electrónica de Crédito. En ese caso, debe informar un comprobante de referencia y NO un período. Elimine el comprobante rechazado y reingréselo informando un comprobante de referencia.
  * Si usted emite comprobantes electrónicos para el mercado interno, utiliza la versión 'Notificación Juez' de webservices (según RG 2904 – Art. 4º) y registra la devolución de uno o más artículos en una factura electrónica, la devolución de ese/esos artículos se informará a AFIP con el código 95 – ANULACION / DEVOLUCION (como Unidad de Medida).



(*) Tenga en cuenta que el ejemplar impreso del comprobante electrónico debe incluir los códigos y leyendas de cada una de las observaciones de AFIP.  
Para ello, agregue las variables de reemplazo para comprobantes electrónicos: **@OK** para el código de la observación y **@HK** para su descripción en el diseño de sus comprobantes (archivos TYP).  
Contemple la posibilidad de imprimir más de una observación en un mismo comprobante.
