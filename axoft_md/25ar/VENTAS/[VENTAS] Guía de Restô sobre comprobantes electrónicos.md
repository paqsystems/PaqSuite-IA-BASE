# Guía de Restô sobre comprobantes electrónicos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_comprobelectr_gv3/

## Contenido

# Guía de Restô sobre comprobantes electrónicos

La AFIP ha establecido un régimen especial para la emisión y almacenamiento electrónico de comprobantes originales, respaldatorios de las operaciones de compraventa de cosas muebles, locaciones y prestaciones de servicios, locaciones de cosas y obras y las señas o anticipos que congelen precios.

Le recomendamos visitar la página web <http://www.afip.gov.ar/fe/> para obtener información sobre quienes están obligados a emitir facturas electrónicas, las características de la misma, qué es el Código de Autorización Electrónico "CAE", etc.

Más información:

Puede consultar la web de la AFIP para obtener más información referida a la factura electrónica, desde [este link a la sección ABC Consultas y Respuestas Frecuentes sobre Normativa, Aplicativos y Sistemas](http://www.afip.gov.ar/genericos/guiavirtual/directorio_subcategoria.aspx?id_nivel1=562&id_nivel2=603).

##### Diferencias entre la factura tradicional y la factura electrónica

**Factura tradicional:**

  * Para solicitar la impresión de sus comprobantes fiscales, el contribuyente (la empresa emisora) se presenta en una imprenta habilitada por la AFIP para tal fin.
  * La imprenta efectúa el pedido de impresión de comprobantes a la AFIP.
  * La AFIP controla el cumplimento de los requisitos y autoriza la impresión de los comprobantes.
  * La imprenta entrega al contribuyente el talonario autorizado con "CAI" (Código de Autorización de Impresión), de esa manera, cuando llega la hora de entregar un comprobante al cliente, el emisor le entrega un comprobante autorizado.



**Facturación electrónica:**

  * Para solicitar la impresión de sus comprobantes electrónicos, el contribuyente (empresa emisora) debe solicitar a la AFIP una clave fiscal (contraseña para poder realizar trámites desde Internet) de nivel 3. Para más información acerca de la clave fiscal, consulte la página [http://www.afip.gov.ar/claveFiscal/ ](http://www.afip.gov.ar/claveFiscal/)
  * Además, la empresa emisora debe obtener el certificado digital generado por la AFIP. Para más información acerca de su generación, consulte el ítem [Pedido de Certificado Digital](?p=26870).
  * Si prefiere seguir imprimiendo, la empresa emisora debe generar nuevos formularios preimpresos. Los nuevos formularios no deben estar numerados (no incluir el número de CAI ni su fecha de vencimiento).
  * Si prefiere no imprimir el comprobante, puede enviarlo por correo electrónico.



##### Características de una factura electrónica:

  1. Posee efectos fiscales frente a terceros si contiene el Código de Autorización Electrónico "CAE", asignado por la AFIP.
  2. Está identificada con un punto de venta específico, distinto a los utilizados para la emisión de comprobantes manuales o a través de controlador fiscal. El punto de venta debe estar comprendido entre los valores 00001 y 99998.
  3. Tiene una fecha de vencimiento específica para su remisión (10 días).
  4. Los aspectos generales de una factura electrónica de exportación son los siguientes: 
     1. Posibilidad de paginación de los comprobantes y de transporte.
     2. Los títulos / encabezados de los comprobantes podrán emitirse en idiomas distintos al español.
     3. Se cuenta con campos opcionales para la incorporación de textos libres.
     4. Confección de la factura en forma previa o con posterioridad a la oficialización de la destinación aduanera.



Más información:

No existe el concepto de talonario "multipropósito" para los comprobantes electrónicos. La numeración de facturas y notas de crédito se maneja en forma separada, aunque queda a su criterio la utilización de un formulario particular para cada tipo de comprobante, o la utilización de un único formulario para todos los comprobantes imprimiendo la palabra "FACTURA" o "NOTA DE CRÉDITO" según el comprobante que se emita.

##### Procedimiento de emisión de factura electrónica

Para que las facturas electrónicas sean consideradas documento con valor fiscal, en el momento de la transacción o luego de la misma, la empresa emisora debe enviarle a la AFIP los siguientes datos (factura electrónica del mercado interno): el monto total de la operación, el origen (empresa emisora), datos del emisor y del receptor (el cliente).  
La AFIP devolverá para cada comprobante un Código de Autorización Electrónico (CAE), que hace referencia a la factura que lo originó.  
Incorporando el CAE a la factura, con todos los detalles de precio, cantidades, unidades de medida, etc. y en el formato deseado, la empresa emisora genera la Factura Electrónica.  
El receptor debe recibir la factura electrónica dentro de los 10 días corridos desde la asignación del "CAE", ya sea remitida por correo electrónico o en su versión impresa.

##### Puesta en marcha

Para implementar el circuito de Comprobantes Electrónicos debe seguir el procedimiento detallado a continuación:

**Pasos previos que todo cliente debe realizar ante la AFIP:**

  1. Gestione la clave fiscal de nivel 3. En [www.afip.gov.ar/clavefiscal](http://www.afip.gov.ar/clavefiscal), conozca cómo obtener la clave fiscal. Este es un trámite personal a cargo del dueño o apoderado de la empresa.
  2. Obtenga el certificado digital. Recomendamos utilizar el programa Pedido de certificado digital(AxCertSetup.exe) para generar la información necesaria para gestionar el certificado digital ante la AFIP. El mencionado programa se encuentra en el directorio de instalación del sistema. Este programa fue desarrollado para facilitar esta operación, no obstante puede realizar este trámite siguiendo las instrucciones de la AFIP.
  3. Realice los pasos de configuración desde la página de AFIP.



Más información:

Le recomendamos visitar la página web <http://www.afip.gov.ar/fe/> para obtener más información.

###### Pedido de certificado digital

Para generar el pedido de certificado debe seguir los pasos que indica la AFIP. Ya que este procedimiento tiene cierto grado de complejidad, Axoft Argentina S.A. ha desarrollado un Asistente que lo guiará en la obtención del mismo.  
Para acceder a este asistente, seleccione Programas | Tango Restó | Pedido de certificado digital y siga los pasos que se le indican.  
Una vez completado los datos que le solicta el formualio, haga clic en el botón “Siguiente”.  
El asistente genera 3 archivos. Al conectarse a la web de la AFIP para entregar el pedido de certificado digital, indique como nombre de archivo aquel que tenga extensión *.req (Request) para su validación por parte del AFIP.  
Tenga en cuenta que AFIP puede devolver el mensaje de error: 'El Request enviado es inválido. Por favor revíselo', para los siguientes casos:

  * El archivo seleccionado no es el pedido por AFIP.
  * El archivo está dañado.
  * El archivo no está correctamente generado.



Para solucionar, , sugerimos realizar los siguientes pasos:

  1. Reinstale Openssl.
  2. Verifique que no existan espacios en nombre y alias ingresados.
  3. Regenere archivo .req (Request).



###### Configuración en AFIP

Desde el sitio web de AFIP, apartado Contribuyentes, realice los siguientes pasos:

  1. **Registre el punto de venta correspondiente ante la AFIP:** desde la opción 'A / B / M de Puntos de Venta', elija 'Alta' y luego, seleccione 'RECE para aplicativo y web services' como sistema de facturación asociado.
  2. **Habilite el uso de la modalidad 'Comprobantes en línea':** desde la opción 'Administración de Certificados Digitales', elija 'Nueva Relación'; haga clic en "Buscar" para seleccionar el Servicio y elija 'Comprobantes en Línea'. Por último, haga clic en "Buscar" para seleccionar el representante y confirme la operación.
  3. **Asocie el certificado digital obtenido a un webservice:** desde la opción 'Administrador de Relaciones de Clave Fiscal', elija 'Nueva Relación'; haga clic en "Buscar" para seleccionar el Webservice a utilizar (ejemplo: WS Factura electrónica).



###### Pasos previos a la generación de un Comprobante Electrónico

A continuación, enumeramos los pasos necesarios para poner en marcha el circuito de Comprobantes Electrónicos.

**1\. Definición de los datos de la empresa  
**En la configuración de la terminal del módulo adicionista, se encuentra la solapa Documentos electrónicos, en ella podrá visualizar las solapas Empresa, Puesta a disposición y Archivo PDF.  
En la solapa Empresa deberá completar o verificar la siguiente información:

  * CUIT de su empresa.
  * Fecha de Incorporación al régimen especial de emisión y almacenamiento electrónico de comprobantes originales.



__Nota

No ingrese _Fecha de Exclusión_ , ya que el sistema considerará que usted abandonó el régimen de comprobantes electrónicos.  


El Webservices a utilizar será versión 2.  
El Indicador de servicio por defecto es oculto y las opciones posibles del Valor del Indicador serán: '1 – Productos', '2 – Bienes' o '3 – Productos y Servicios'.  
Almacenamiento de comprobantes: De igual manera se debe definir el destino donde serán almacenados los documentos electrónicos generados y el criterio sobre el cual serán ordenados (Cliente, comprobante o tipo de archivo).  
En la solapa Puesta a disposición se podrán configurar los datos del servidor de correo electrónico del remitente para el envío del comprobante electrónico.  
En la solapa Archivo PDF permite configurar el sistema para la depuración de la base de datos de los archivos generados, indicando el directorio destino a donde serán movidos los archivos y a partir de cuantos días transcurrido según la fecha de emisión de los mismos.

**2\. Definición de los parámetros del Administrador de Comprobantes Electrónicos (Hacer llamado al punto 2 que se encuentra más abajo)  
**Por cada computadora que emita comprobantes electrónicos, realice los siguientes pasos para poder enviar comprobantes electrónicos a la AFIP.  
En la pantalla de [Administración de Comprobantes Electrónicos](?p=30232/#administracion-de-comprobantes-electronicos), ingrese a Parámetros y coloque los datos de conexión.

  1. Ingrese el certificado extendido por la AFIP (indique ubicación y nombre del archivo).
  2. Indique la ubicación del archivo que contiene la clave privada (utilizada para solicitar el certificado digital).
  3. Ingrese la identificación de origen (utilizada para solicitar el certificado digital).



La clave privada y la identificación de origen las puede obtener del asistente mencionado en el ítem [Pedido de Certificado Digital](?p=26870). Tenga en cuenta que en identificación de origen debe ingresar el contenido del archivo con extensión *.txt (no su ubicación).

__Nota

Recuerde que esta configuración debe ser efectuada en cada una de las terminales que emitan comprobantes electrónicos.  


**3\. Definición de las monedas  
**Si usted genera comprobantes electrónicos para el mercado interno y/o de exportación, invoque el proceso [Monedas](?p=11955) del módulo Procesos generales y complete el Código moneda AFIP. con la clasificación que la AFIP asigna a cada unidad monetaria.

**4\. Alta de talonarios  
**Ingrese al proceso [Talonarios](?p=24998) y defina los talonarios (nuevos puntos de venta solicitados en AFIP) a utilizar durante la generación de comprobantes electrónicos.  
En cada uno de esos talonarios, active (tilde) el parámetro Genera Comprobante Electrónico.  
Al definir un talonario de comprobantes electrónicos, tenga en cuenta las siguientes consideraciones:

  * No es posible aplicar la modalidad 'Multipropósito', por lo que deberá dar de alta talonarios para Facturas, N/D y N/C en forma independiente.
  * Para imprimir comprobantes electrónicos, ingrese el destino de impresión en el talonario.
  * El primer número habilitado del talonario debe ser 1 (uno).
  * Defina el Tipo de Conexión a utilizar para su comunicación con la AFIP ('En Línea' o bien, 'Diferido'). 
    * **En Línea:** indica que, en el momento de emitir el comprobante electrónico, el sistema se comunicará con el servidor de la AFIP para solicitar el CAE correspondiente. Para más información consulte [Modalidad en línea](?p=30232/#detalle-del-circuito).
    * **Diferido:** indica que la obtención del CAE será posterior a la confección del comprobante electrónico. Tenga en cuenta que un comprobante electrónico sin CAE no tiene validez legal, y por lo tanto no puede ser entregada al cliente. Para más información consulte [Modalidad diferida](?p=30232/#detalle-del-circuito).
  * Indique si imprime el comprobante electrónico una vez obtenido el CAE.
  * Indique si envía el comprobante generado a su cliente por correo electrónico.
  * Ingrese la ubicación (directorio o carpeta) y el nombre de la imagen escaneada del formulario preimpreso a incluir en los comprobantes que se envíen por correo electrónico. Sugerimos escanear el formulario preimpreso grabando la imagen sin márgenes adicionales. Es posible que deba efectuar algunas pruebas hasta que la visualización del archivo pdf sea correcta. Tenga en cuenta que a diferencia de los comprobantes no electrónicos, los comprobantes electrónicos pueden imprimirse o enviarse por correo electrónico cuantas veces lo desee.
  * Acceda a la opción Formularios, invoque la función Dibujar para agregar las variables de reemplazo para comprobantes electrónicos (CAE, fecha de vencimiento, etc.). Tenga en cuenta que también es necesario agregar las variables de reemplazo para Tipo de comprobante y Número de comprobante.



¿Cuántos talonarios debo definir?

Si usted genera en forma electrónica, comprobantes de facturas, notas de débito y notas de crédito de tipo 'A' y 'B', sugerimos definir por punto de venta, un talonario electrónico para cada tipo de comprobante / tipo asociado / número de sucursal. Es decir, no debería tener definidos más de 3 talonarios electrónicos de clase 'A' (FAC, DEB, CRE) ni más de 3 talonarios electrónicos de clase 'B' (FAC, DEB, CRE) por punto de venta.  
Si usted genera en forma electrónica, comprobantes de facturas, notas de débito y notas de crédito de tipo 'C' (para Monotributistas), sugerimos definir por punto de venta, un talonario electrónico para cada tipo de comprobante / tipo asociado / número de sucursal. Es decir, no debería tener definidos más de 3 talonarios electrónicos de clase 'C' (FAC, DEB, CRE) por punto de venta.

**5\. Clasificación de los clientes  
**Para el envío de comprobantes electrónicos, si su empresa emite comprobantes electrónicos (del mercado interno), defina para cada uno de sus clientes, los siguientes datos:

Forma de Envío: indique la modalidad de envío a su cliente de los comprobantes electrónicos que usted emita. Puede optar por una de las siguientes opciones: e-mail, e-mail / papel o tener en cuenta la definición del talonario.

Mail Envío: es la dirección de e-mail para el envío de los comprobantes electrónicos. Por defecto, se propone la dirección ingresada en el campo Correo electrónico del cliente.

**6\. Codificación de alícuotas  
**Para cada alícuota ingresada en el sistema, indique cuál es el código definido por AFIP.  
Realice este paso si emite comprobantes electrónicos del mercado interno.

##### Detalle del circuito

Una vez terminada la etapa de puesta en marcha opere con los siguientes procesos para generar comprobantes electrónicos: Adicionista, Mostrador, Delivery, Factura mesa, Factura cliente.  
Además, usted puede consultar y operar con la información específica de los comprobantes electrónicos desde los siguientes procesos:

  * Desde [Administración de Comprobantes Electrónicos](?p=30232/#administracion-de-comprobantes-electronicos) podrá solicitar a la AFIP la autorización de emisión de aquellos comprobantes electrónicos pendientes o rechazados por AFIP. Desde esta opción también podrá visualizar, imprimir o enviar por correo electrónico los comprobantes ya autorizados por la AFIP.
  * Si desea anular un comprobante electrónico, el sistema le avisará que no será posible. El procedimiento adecuado es ingresar un comprobante (nota de crédito) para registrar la anulación.



###### Generación de comprobantes electrónicos

Existen dos modalidades con las que puede comunicarse con AFIP para solicitar el CAE.  
Al definir cada talonario, usted decide el tipo de conexión con AFIP.

  * Modalidad "En línea"
  * Modalidad "Diferida"



Más información:

Es posible solicitar el código de autorización "CAE" en el mismo momento de la venta (modalidad "En línea") o posteriormente (modalidad "Diferida"). Para esta última modalidad, desde el Administrador de Comprobantes Electrónicos solicite el CAE pendiente. Esta opción también resulta de utilidad cuando algún comprobante fue rechazado por la AFIP.

**Modalidad 'En línea'  
**La modalidad "en línea" es un proceso automático mediante el cual se obtiene el código de autorización (desde el mismo proceso de Facturación) en forma automática, vía Internet.  
Para ejemplificar el proceso de facturación electrónica, tomamos el caso de una empresa que emite facturas electrónicas (Emisor) en base a la modalidad de obtención del CAE "en línea".  
Realice los siguientes pasos para generar comprobantes electrónicos en esta modalidad:

  1. Ingrese al proceso de emisión de comprobantes correspondiente desde adicionista, mostrador, delivery, factura mesa o factura cliente.
  2. Seleccione un talonario de comprobantes electrónicos que tenga configurada esta modalidad, o defina como talonarios habituales en el puesto de caja, los talonarios electrónicos a utilizar.
  3. Ingrese los datos del comprobante.
  4. Haga clic en el botón “Facturar” (+)
  5. De manera automática, el sistema se conecta vía web con la AFIP para obtener el código de autorización electrónico (CAE) correspondiente al comprobante ingresado.
  6. Si el comprobante fue autorizado por la AFIP: 
     1. Se exhibe el número de comprobante y el número de CAE obtenido.
     2. Si activó el parámetro Imprime comprobante, se emite el comprobante con CAE y fecha de vencimiento del CAE.
     3. Si activó el parámetro Envía comprobante por correo electrónico, el comprobante autorizado se envía al cliente.
  7. Si el comprobante no fue autorizado por la AFIP: 
     1. Se exhibe el número de comprobante y el motivo de su rechazo. (*)



(*) Si el comprobante fue rechazado por la AFIP:

  1. Usted puede seguir operando 'En línea' pero tenga en cuenta que los comprobantes posteriores serán también rechazados dado que la AFIP verifica la correlatividad de los comprobantes para el otorgamiento del CAE.
  2. Usted puede consultar el problema que originó el rechazo del comprobante desde el proceso [Administración de Comprobantes Electrónicos](?p=30232/#administracion-de-comprobantes-electronicos). Una vez solucionado el problema puede obtener el CAE desde este proceso.



**Modalidad 'Diferida'  
**En este caso, el emisor tramita el pedido del CAE en un momento posterior a la confección de la factura, pudiendo realizar una solicitud de varios comprobantes a la vez.  
Al recibir las autorizaciones, el emisor podrá generar los comprobantes pendientes.

Más información:

Si usted elige como tipo de conexión con AFIP, la modalidad 'Diferida', tenga en cuenta que la solicitud de autorización de comprobantes a la AFIP no puede exceder los 5 (cinco) días corridos de la fecha de los comprobantes. De tratarse de prestaciones de servicios, dicha transferencia podrá efectuarse dentro de los 10 días corridos anteriores o posteriores a la fecha consignada en el comprobante.

Realice los siguientes pasos para generar comprobantes electrónicos en esta modalidad:

  1. Ingrese al proceso de emisión de comprobantes correspondiente desde adicionista, mostrador, delivery, factura mesa o factura cliente.
  2. Seleccione un talonario de comprobantes electrónicos que tenga configurada esta modalidad, o defina como talonarios habituales en el puesto de caja, los talonarios electrónicos a utilizar.
  3. Ingrese los datos del comprobante.
  4. Haga clic en el botón "Facturar" (+).
  5. El sistema informa el número de comprobante generado y le avisa que queda pendiente la autorización del comprobante por parte de la AFIP (obtención del CAE).
  6. Para obtener el CAE de los comprobantes generados en esta modalidad, ejecute el proceso [Administración de Comprobantes Electrónicos](?p=30232/#administracion-de-comprobantes-electronicos).



###### Consideraciones generales

  * Tenga en cuenta que un comprobante electrónico no tiene efectos fiscales frente a terceros hasta que la Administración Federal de Ingresos Públicos (AFIP) otorgue el Código de Autorización Electrónico (CAE). Es decir, no son considerados en los procesos que generan información para los distintos aplicativos.
  * Un comprobante puede tener CAE y haber sido 'Observado' por AFIP En ese caso, usted puede consultar el motivo de la observación desde los siguientes procesos: 
    * Administrador de comprobantes electrónicos, solapa Comprobantes autorizados, pulsando en la columna 'Observación AFIP'.  
Tenga en cuenta que el ejemplar impreso del comprobante electrónico debe incluir los códigos y leyendas de cada una de las observaciones de AFIP.  
Para ello, agregue las variables de reemplazo para comprobantes electrónicos: **@OK** para el código de la observación y**@HK** para su descripción en el diseño de sus comprobantes (archivos TYP).  
Contemple la posibilidad de imprimir más de una observación en un mismo comprobante.
  * Si genera un comprobante electrónico para un cliente ocasional es necesario que ingrese los datos de su cliente para que su comprobante pueda ser autorizado por la AFIP.
  * Sólo es posible anular un comprobante electrónico 'Aceptado' mediante otro comprobante electrónico. Ejemplo: una factura electrónica sólo puede anularse mediante una nota de crédito electrónica.
  * El sistema permite eliminar todos los comprobantes electrónicos 'Rechazados' por AFIP.  
Esta opción se encuentra en el Administrador de comprobantes electrónicos y estará disponible según el rol asignado al usuario.  
El número de comprobante eliminado será reutilizado en la generación de un nuevo comprobante electrónico del mismo talonario.
  * Si optó por eliminar sólo algunos comprobantes electrónicos rechazados, tenga en cuenta que deberá verificar el próximo número a emitir del talonario asociado – previo a continuar con la facturación.



###### Administración de comprobantes electrónicos

Usted podrá administrar los comprobantes electrónicos generados por la empresa, obtener los CAE para los comprobantes pendientes o rechazados y enviar los comprobantes electrónicos a los clientes por correo electrónico o generar una copia impresa.

__Nota

El circuito de comprobantes electrónicos está disponible sólo si su licencia está habilitada. Para más información, consulte con su proveedor de **Tango**.

Utilice esta herramienta para la gestión de sus comprobantes electrónicos del mercado interno.  
En la [primer solapa](https://ayudas.axoft.com/25ar/comprobantespendientesrechados_gv) es posible visualizar los comprobantes electrónicos que todavía no poseen CAE o cuyo pedido fue rechazado debido a algún tipo de inconsistencia detectada por la AFIP, y solicitar el CAE para cada comprobante.  
La [segunda solapa](https://ayudas.axoft.com/25ar/comprobantesautorizados_gv) detalla los comprobantes ya autorizados por la AFIP permitiendo consultarlos en PDF y XML, imprimirlos o enviarlos por correo electrónico.

**Opciones de la barra de herramientas  
**

Las opciones disponibles en la barra de herramientas le permiten realizar consultas y configuraciones vinculadas con los comprobantes electrónicos, así como también eliminar los comprobantes rechazados por AFIP.

**Parámetros:**  
Utilice esta opción para ingresar los parámetros necesarios para poder enviar comprobantes electrónicos a la AFIP.

__Nota

Recomendamos utilizar el programa _Pedido de certificado digital (AxCertSetup.exe)_ para generar la información necesaria para gestionar el certificado digital ante la AFIP. En mencionado programa se encuentra en el directorio de instalación de **Tango**.

Certificado: indique la ubicación del archivo que contiene el certificado digital generado por la AFIP.

Clave privada: indique la ubicación del archivo que contiene la clave privada utilizada para solicitar el certificado digital.

Identificación de origen: ingrese la identificación de origen (source) utilizada para solicitar el certificado digital. Si utilizó el programa Pedido de certificado digital, ingrese el contenido del archivo *.txt generado por dicho programa.

Máximo tiempo de espera: representa la cantidad de segundos que el Administrador de comprobantes electrónicos esperará como máximo para lograr una conexión exitosa con AFIP. Superado ese tiempo, el sistema exhibirá un mensaje de atención (por time-out). El tiempo de espera, por defecto, es de 30 segundos. Usted puede modificar este parámetro, ingresando un valor comprendido en el rango de 1 a 999 segundos.

__Nota

Utilice el botón "Probar conexión" para verificar que los datos ingresados son válidos para establecer una conexión con el servidor de la AFIP.

Últimos comprobantes autorizados: esta opción le permite conocer el último número de comprobante autorizado para cada punto de venta y tipo de comprobante.

__Nota

Tenga en cuenta que la autorización de la AFIP es secuencial por lo que no autorizará un nuevo comprobante si el inmediato anterior no fue autorizado.

Estado de los servidores AFIP: pulse este botón para verificar si los servidores de la AFIP están funcionando correctamente.

Tenga en cuenta que AFIP opera con webservices diferentes, según la Resolución General que se aplique para la generación de comprobantes electrónicos.

Eliminar rechazados: pulse este botón para solucionar los rechazos de comprobantes electrónicos enviados a AFIP.

Para más información, consulte el ítem Eliminación de comprobantes electrónicos rechazados en la solapa Comprobantes pendientes / rechazados.

Obtener CAEA: pulse este botón para solicitar o consultar CAEA.

Ingresando el periodo y quincena puede obtener CAEA mediante la conexión con los webservice de AFIP o ingresarlo manualmente cuando no posee conexión.

Recuerde que puede solicitar CAEA 5 días corridos inmediatos anteriores al inicio de cada período o dentro del mismo.

El valor de CAEA obtenido será utilizado para los comprobantes que utilizan un talonario cuyo tipo de autorización corresponde a CAEA.

**Permisos y roles  
**El Administrador "en línea" no requiere que el usuario tenga permiso de acceso a ese proceso.  
Las columnas de "Importes", "Unidades" y "Cotización" estarán visibles según el rol asignado por usuario. De igual manera, la acción "Eliminar rechazados" estará disponible según el rol asignado por usuario.  
Para más información, consulte el proceso Administrador de Roles.

**Comprobantes autorizados  
**Ingrese a esta solapa cuando desee visualizar, imprimir o enviar por correo electrónico los comprobantes ya autorizados por la AFIP.  
Mediante la utilización de filtros, usted puede consultar los comprobantes electrónicos aplicando un criterio de selección particular (cliente, vendedor, talonario, comprobante, fecha de emisión).  
Por defecto, el criterio de búsqueda es Fecha de emisión, considerando la fecha del día como rango de fechas a aplicar.  
Desde la grilla resultante será posible visualizar el comprobante en PDF y XML, y seleccionar cualquiera de ellos para imprimirlos o enviarlos por correo electrónico.  
Para cada uno de los comprobantes se detalla el CAE obtenido y su respectiva fecha de vencimiento, la cantidad de impresiones y/o envíos por correo electrónico realizados.  
Un comprobante puede tener CAE y haber sido 'Observado' por AFIP. Para más información, consulte el ítem [Comprobantes observados](https://ayudas.axoft.com/25ar/comprobanteobservado_gv).  
Para visualizar los comprobantes, indique el criterio de búsqueda deseado y pulse el botón "Obtener comprobantes".  
Seleccione el o los comprobantes y pulse el botón "Enviar a". Desde la ventana con el título Emitir comprobantes, seleccione la operación a realizar: imprimir, enviar por correo y/o generar a directorio.

**Código QR  
**

AFIP dispuso la implementación obligatoria de un código de respuesta rápida "QR" en los comprobantes electrónicos.

Esta medida alcanza a todos los contribuyentes que emitan comprobantes electrónicos según lo establecido por la Resolución General N° 4.291 (operan con el wsfev1 para la emisión de comprobantes electrónicos del mercado interno 'A', 'B' y 'C').

El código "QR" podrá ser escaneado por una cámara estándar de un dispositivo celular, tablet o similar con acceso a internet y brindará información sobre el comprobante y el emisor del mismo.

Este código brindará la siguiente información del comprobante:

  * Fecha de emisión
  * CUIT del emisor
  * Punto de venta
  * Tipo de Comprobantes
  * Número de Comprobante
  * Importe total
  * Moneda
  * Cotización
  * Tipo Documento Receptor (de corresponder)
  * Número de Documento de Receptor (de corresponder)
  * Código del Tipo de Autorización
  * Código de Autorización



No olvide incluir la variable de reemplazo **@QR** en el archivo TYP asociado a los talonarios electrónicos.

Para más información acerca de las especificaciones técnicas del código QR, consulte el link: <https://www.afip.gob.ar/fe/qr/especificaciones.asp>.

**Comprobantes pendientes / rechazados  
**Desde esta solapa solicite a la AFIP el código de autorización de emisión (CAE).  
En la misma pantalla se visualizan los comprobantes pendientes de autorización y aquellos que fueron rechazados (por habérseles detectado algún tipo de inconsistencia).  
En este último caso, pulse sobre la columna "Motivo rechazo" para conocer la causa del rechazo. Para más información, consulte el ítem Rechazo de comprobantes electrónicos.  
Pulse el botón "Obtener CAE" para solicitar el código de autorización correspondiente a cada comprobante. En forma simultánea, puede proceder a la emisión del comprobante electrónico. Para ello, tilde para cada talonario la columna "Imprimir" y / o "Enviar correo" según corresponda, dependiendo de la licencia de su llave.

__Nota

Tenga en cuenta que la emisión del comprobante (impresión y/o envío por correo electrónico) puede ser realizada en forma diferida a la obtención del CAE. Dicha opción está disponible en la solapa _Comprobantes autorizados_.

**Rechazo de comprobantes electrónicos**

  * AFIP rechazará la solicitud de autorización de un comprobante electrónico cuando se detecten inconsistencias en los datos vinculados al emisor.  
En este caso, el emisor del comprobante puede emitir un comprobante a través del "Controlador Fiscal" o en forma manual, o solicitar nuevamente la autorización de emisión electrónica, una vez subsanado el inconveniente.
  * Si la fecha del comprobante electrónico está fuera del rango permitido por AFIP (+/- 5 días o bien, +/- 10 días, según el tipo de operación), se rechazará la solicitud de autorización. En este caso, corrija la fecha del comprobante desde el proceso Modificación de comprobantes.
  * Ante cualquier otro de caso de rechazo de un comprobante electrónico, comuníquese con el Departamento de Servicios.



Más información:

Tenga en cuenta que no es posible anular mediante el proceso [Anulación de comprobantes](?p=21138), un comprobante electrónico ya generado o bien, la numeración de un talonario que genere comprobantes electrónicos. Ante el rechazo de un comprobante electrónico, utilice la opción Eliminar rechazados de la barra de herramientas.

**Eliminación de comprobantes electrónicos rechazados  
**La opción Eliminar rechazados de la barra de herramientas permite realizar la eliminación o borrado de los comprobantes electrónicos rechazados por AFIP.  
De esta manera, no se verá afectado el circuito de facturación electrónica.  
El sistema exhirá en una nueva ventana, los comprobantes electrónicos con estado 'Rechazado', agrupados por Talonario.  
Por defecto, el sistema propone la eliminación de todos los comprobantes rechazados; pero es posible cambiar esta selección -por ejemplo, para elegir sólo el primer comprobante rechazado de un talonario.

__Nota

Tenga en cuenta que, si optó por eliminar sólo algunos comprobantes electrónicos rechazados, deberá verificar el próximo número a emitir del talonario asociado - previo a continuar con la facturación.

El sistema realizará, por cada comprobante seleccionado, las siguientes acciones:

  1. La anulación del comprobante seleccionado. Se aplican validaciones y controles similares a los del proceso [Anulación de comprobantes](?p=21138) (para la opción 'Comprobante generado').
  2. La eliminación o borrado del comprobante de las tablas del sistema.
  3. La actualización del Próximo número a emitir en el talonario del comprobante.



__Nota

El proceso puede demorar unos minutos dependiendo de la cantidad de comprobantes a eliminar y las tablas o archivos a actualizar.

##### Comprobantes observados

Si durante el proceso de autorización de comprobantes clase 'A', AFIP detecta inconsistencias en los datos del receptor, autorizará el comprobante electrónico asignándole un "CAE" junto con el detalle de las irregularidades encontradas.  
Ejemplos de situaciones posibles de observación: CUIT inválida del cliente receptor del comprobante electrónico; el receptor no se encuentra categorizado como Responsable Inscripto en el Impuesto al Valor Agregado, etc.  
Para conocer el detalle de las observaciones, pulse sobre la columna 'Observación AFIP' en la grilla de comprobantes autorizados.

__Importante

El impuesto discriminado en tales comprobantes no podrá computarse como crédito fiscal del Impuesto al Valor Agregado.  


Tenga en cuenta que el ejemplar impreso del comprobante electrónico debe incluir los códigos y leyendas de cada una de las observaciones de AFIP.  
Para ello, agregue las variables de reemplazo para comprobantes electrónicos: @OK para el código de la observación y @HK para su descripción en el diseño de sus comprobantes (archivos TYP).  
Contemple la posibilidad de imprimir más de una observación en un mismo comprobante.
