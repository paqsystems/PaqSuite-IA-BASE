# Información impositiva en Ventas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=21480/

## Contenido

# Información impositiva en Ventas

Estos procesos permiten generar los distintos soportes magnéticos correspondientes a normas legales, que se deben entregar a la DGI o a otros organismos oficiales.

##### Información para F2002 - IVA por actividad

Este proceso permite generar la información del débito fiscal, detallado por la actividad asignada a los artículos facturados. Permite generar el archivo para ser incorporado en el formulario F2002 Iva por actividad liquidación retenciones sufridas.

Entre las funcionalidades disponibles para la generación, usted podrá:

  1. Filtrar la información por talonarios.
  2. Filtrar la información por puntos de ventas.



Entre las validaciones del proceso, tenga presente que:

  * Sólo se tendrán en cuenta los comprobantes que intervengan en el IVA ventas.
  * Para los comprobantes electrónicos solo se consideraran aquellos que hayan obtenido CAE.
  * En caso que el comprobante contenga fletes o intereses; el importe correspondiente a estos conceptos se asignará a la actividad económica de los artículos del comprobante.



La información correspondiente a crédito fiscal se detallará en forma separada.  
Se solicitará el mes-año a procesar, el directorio donde guardará el archivo y la confirmación para detallar la información generada.  
El formato del archivo para la importación de las retenciones es el siguiente:

**Concepto** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
Código de régimen de retención. | 1 | 3 | 3  
CUIT del agente de retención. | 4 | 14 | 11  
Fecha de la retención. | 15 | 24 | 10  
Nº Certificado / Cód. Operación. | 25 | 40 | 16  
Monto de la retención | 41 | 58 | 18  
  
Incluir línea en blanco al final del archivo: permite incluir una línea en blanco al final del archivo .TXT generado por el proceso.

##### Información para SIAp - IVA

Este proceso permite obtener un papel de trabajo donde se detallan los acumulados de cada una de las clasificaciones para SIAp - IVA desglosados por alícuota. Esta información le será de utilidad para completar los datos requeridos por el aplicativo IVA.

Si usted emite comprobantes electrónicos, tenga en cuenta que no se procesan los comprobantes electrónicos sin CAE asignado.  
Se solicita el ingreso del rango de fechas a considerar.  
Opcionalmente, es posible incluir en el listado, el detalle de los comprobantes 'Sin clasificar'.  
Si elige como destino de impresión Excel o Access y activa el parámetro Imprime comprobantes sin clasificar, sólo se enviarán al destino seleccionado los comprobantes pendientes de clasificación.  
Puede completar la clasificación de los comprobantes utilizando el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modifcomprobante_gv).

**Exportación de retenciones  
**Esta opción le permite generar un archivo de texto detallando las retenciones de IVA recibidas durante el período seleccionado.  
Este proceso genera el archivo GVSIAPIV.TXT en el directorio que usted seleccione.  
No se incluirán aquellos clientes con número de CUIT inválidos. En este caso, el sistema emitirá un informe de aquellos clientes que tengan ingresado un tipo y número de documento inválidos (para los que no se generaron registros). Realice las correcciones correspondientes y genere nuevamente el archivo.

Formato de archivo

**Concepto** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
Código de régimen de retención. | 1 | 3 | 3  
CUIT del agente de retención. | 4 | 16 | 13  
Fecha de la retención. | 17 | 26 | 10  
Nº Certificado / Cód. Operación. | 27 | 51 | 25  
Monto de la retención | 52 | 67 | 16  
  
##### Generación de archivo SIAp - SICORE

Este proceso es de utilidad si usted practica percepción de IVA en facturación.

**Generar percepciones**

Permite generar un archivo para ser importado en el aplicativo SIAp-SICORE 9.0 Release 9 para la liquidación y presentación de retenciones y percepciones. El mismo generará el archivo GVSICORE.TXT en el directorio que usted seleccione.  
Si usted emite comprobantes electrónicos, tenga en cuenta que no se procesan los comprobantes electrónicos sin CAE asignado.  
Los comprobantes se generan asociados a un número de CUIT y no a un código de cliente. Si un cliente se encuentra ingresado en el sistema con dos códigos de cliente distintos e igual número de CUIT, se acumularán sus comprobantes al mismo CUIT.  
No se incluirán aquellos clientes con tipo de documento '99' (consumidor final) ni los que no tengan ingresado un valor correcto en el campo Número de CUIT.  
En este caso, el sistema emitirá un informe de aquellos clientes que tengan ingresado un tipo y número de documento inválidos (para los que no se generaron registros). Realice las correcciones correspondientes y genere nuevamente el archivo.  
Se informará el Código de alícuota correspondiente a percepción de IVA (entre 11 y 20) y el Código de Régimen de percepción. El sistema sugerirá por defecto '493', que es el que corresponde a percepciones de grandes contribuyentes según la RG 3125 de DGI.  
Al finalizar el proceso, el sistema informará la cantidad de registros grabados como control.  
Es posible emitir en forma opcional un informe con los importes por percepciones generados.

**Generar datos de clientes  
**Permite generar un archivo ASCII con los datos de los clientes habituales y/o ocasionales, que posteriormente podrá ser incorporado al aplicativo SIAp - SICORE versión 9.0 Release 9.  
Se incluirán en la generación, los datos de aquellos clientes parametrizados con sobretasas / subtasas de IVA.  
Este proceso generará el archivo CLIENTES.TXT en el directorio que usted seleccione.

**Trabajando en el sistema SIAp - SICORE  
**Una vez creado el archivo, importe dentro del sistema SIAp - SICORE los datos generados.

**Formato de importación  
**El formato SIAp - SICORE para la importación de retenciones es el siguiente:

**Descripción** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
Código de Comprobante | 1 | 2 | 2  
Fecha de emisión del comprobante (DD/MM/YYYY) | 3 | 12 | 10  
Número del comprobante | 13 | 28 | 16  
Importe del comprobante | 29 | 44 | 16  
Código de impuesto | 45 | 48 | 4  
Código de régimen | 49 | 51 | 3  
Código de operación | 52 | 52 | 1  
Base de cálculo | 53 | 66 | 14  
Fecha de emisión de la retención | 67 | 76 | 10  
Código de condición | 77 | 78 | 2  
Retención practicada a sujetos suspendidos según: | 79 | 79 | 1  
Importe de la retención | 80 | 93 | 14  
Porcentaje de exclusión | 94 | 99 | 6  
Fecha de emisión del boletín | 100 | 109 | 10  
Tipo de documento del retenido | 110 | 111 | 2  
Número de documento del retenido | 112 | 131 | 20  
Número certificado original | 132 | 145 | 14  
Denominación del ordenante | 146 | 175 | 30  
Acrecentamiento | 176 | 176 | 1  
CUIT del país del retenido | 177 | 187 | 11  
CUIT del ordenante | 188 | 198 | 11  
  
Formato de archivo de sujetos percibidos:

**Concepto** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
Número de documento de sujeto percibido | 1 | 11 | 11  
Razón Social | 12 | 31 | 20  
Domicilio Fiscal | 31 | 51 | 20  
Localidad | 52 | 71 | 20  
Provincia | 72 | 73 | 2  
  
**Importación de datos  
**Desde el aplicativo SIAp - SICORE se procederá importar el archivo generado por el sistema.  
Tenga presente que si se realizó previamente una importación o una carga manual de datos, el proceso de importación siempre agrega comprobantes a los existentes, por lo que podrían quedar movimientos duplicados. Es aconsejable revisar los movimientos luego de realizar la importación.

##### Generación archivo Retenciones IB Bs. As.

Este proceso permite generar el archivo para ser incorporado por cualquiera de estos aplicativos: SIAp Ingresos Brutos, Ingresos Brutos Sirft Baires y Arbaweb.

La información que se genera corresponde a las retenciones de Ingresos Brutos ingresadas en el sistema.  
Si usted emite comprobantes electrónicos, tenga en cuenta que no se procesan los comprobantes electrónicos sin CAE asignado.  
Opcionalmente, es posible emitir un informe con los datos generados.  
Al finalizar el proceso, el sistema indicará para su control, la cantidad de registros grabados.

__Nota

Indique el directorio y el nombre del archivo donde se grabarán los datos exportados.

**Trabajando en los aplicativos  
**Una vez creado el archivo desde Tango importe los datos dentro del sistema de Ingresos Brutos Buenos Aires o de Ingresos Brutos Sirft Baires.  
Para ello, acceda a la opción "Ingresar".  
Luego de agregar los datos de la declaración jurada correspondiente, acceda a la opción Retenciones, Importar, Seleccionar archivo de origen para la importación e indique el nombre del archivo secuencial (IB2.TXT) y la unidad de origen.  
Los registros generados pueden ser consultados o modificados mediante la opción Retenciones.

Formato de importación  
Las posiciones de cada uno de los campos que lo integran, pueden consultarse a través del comando Configurar tipo de registro.  
El formato SIAp - Ingresos Brutos - Provincia de Buenos Aires e Ingresos Brutos Sirft Baires para la importación de retenciones es el siguiente:

**Descripción** | **Desde** | **Hasta** | **Longitud** | **Nota**  
---|---|---|---|---  
CUIT del agente de retención | 1 | 13 | 13 |   
Fecha de la retención | 14 | 23 | 10 |   
Número de sucursal | 24 | 28 | 5 |   
Número de emisión | 29 | 36 | 8 |   
Importe de retención | 37 | 50 | 14 |   
Tipo de operación | 51 | 51 | 1 | Se informa siempre una "a" (Alta)  
  
##### Generación archivo Percepciones IB Bs. As.

Este proceso permite generar el archivo para ser incorporado por cualquiera de estos aplicativos, correspondientes a la provincia de Buenos Aires: SIAp Agente de Recaudación Provincia de Buenos Aires y Agente de Recaudación Sirft Baires.

La información que se genera corresponde a las percepciones de Ingresos Brutos calculadas por el sistema.  
Indique el directorio y el nombre del archivo donde se grabarán los datos exportados.  
Opcionalmente, es posible emitir un informe con los datos generados.  
Al finalizar el proceso, el sistema indicará para su control, la cantidad de registros grabados.

Diseño vigente para operaciones a partir del 01/12/2025: tilde esta opción para generar el archivo de acuerdo con el diseño vigente que corresponde con los comprobantes generados a partir del 01/12/2025. Si lo deja sin tilde, el archivo se genera según el formato vigente hasta el 30/11/2025.

A los efectos de salvaguardar la seguridad e integridad de los datos a transmitir, la Resolución General requiere que los archivos respeten un nombre y secuencia de conformación determinados que se detallan a continuación:

  * Nombrar el archivo TXT generado de la siguiente forma:  
(AR-CUIT-PERIODO-ACTIVIDAD-NOMBRE_DEL_LOTE) 
    * Comprimir el documento a los efectos de generar un nuevo archivo formato ZIP. El mismo deberá mantener el nombre del TXT generado previamente.



Incluir línea en blanco al final del archivo: permite incluir una línea en blanco al final del archivo .TXT generado por el proceso.

**Trabajando en los aplicativos:**

**Formato de importación  
**Las posiciones de cada uno de los campos que lo integran pueden consultarse a través del comando Configurar tipo de registro.  
El formato generado para para la importación de percepciones es el siguiente:

_Método devengado (*):_  
(*): cuando se encuentra sin tilde el check “Completa fecha de percepción con la fecha de emisión de la factura en la presentación de percepciones de ingresos brutos” (solapa Impuestos, de Parámetros de ventas).

Diseño vigente hasta el 30/11/2025

**Descripción** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
CUIT del contribuyente percibido | 1 | 13 | 13  
Fecha de la percepción | 14 | 23 | 10  
Tipo de comprobante | 24 | 24 | 1  
Letra de comprobante | 25 | 25 | 1  
Número de sucursal | 26 | 29 | 4  
Número de emisión | 30 | 37 | 8  
Monto imponible | 38 | 49 | 12  
Importe de la percepción | 50 | 60 | 11  
Tipo de operación | 61 | 61 | 1  
  
Diseño vigente a partir del 01/12/2025

**Descripción** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
CUIT del contribuyente percibido | 1 | 13 | 13  
Fecha de la percepción | 14 | 23 | 10  
Tipo de comprobante | 24 | 24 | 1  
Letra de comprobante | 25 | 25 | 1  
Número de sucursal | 26 | 30 | 5  
Número de emisión | 31 | 38 | 8  
Monto imponible | 39 | 52 | 14  
Alícuota | 53 | 57 | 5  
Importe de la percepción | 58 | 70 | 13  
Tipo de operación | 71 | 71 | 1  
  
_Método percibido (**):  
_(**): cuando se encuentra con tilde la opción Completa fecha de percepción con la fecha de emisión de la factura en la presentación de percepciones de ingresos brutos (solapa Impuestos, de Parámetros de Ventas). En este caso se agrega la columna "Fecha emisión".

Diseño vigente hasta el 30/11/2025

**Descripción** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
CUIT del contribuyente percibido | 1 | 13 | 13  
Fecha de la percepción | 14 | 23 | 10  
Tipo de comprobante | 24 | 24 | 1  
Letra de comprobante | 25 | 25 | 1  
Número de sucursal | 26 | 29 | 4  
Número de emisión | 30 | 37 | 8  
Monto imponible | 38 | 49 | 12  
Importe de la percepción | 50 | 60 | 11  
Fecha emisión (**) | 61 | 70 | 10  
Tipo de operación | 71 | 71 | 1  
  
Diseño vigente a partir del 01/12/2025

**Descripción** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
CUIT del contribuyente percibido | 1 | 13 | 13  
Fecha de la percepción | 14 | 23 | 10  
Tipo de comprobante | 24 | 24 | 1  
Letra de comprobante | 25 | 25 | 1  
Número de sucursal | 26 | 30 | 5  
Número de emisión | 31 | 38 | 8  
Monto imponible | 39 | 52 | 14  
Alícuota | 53 | 57 | 5  
Importe de la percepción | 58 | 70 | 13  
Fecha emisión (**) | 71 | 80 | 10  
Tipo de operación | 81 | 81 | 1  
  
##### Generación de archivo Retenciones SIFERE

Este proceso permite generar el archivo para ser incorporado por el aplicativo SIFERE.

Es condición imprescindible que defina la jurisdicción para la provincia a declarar. Para ello, ejecute el proceso Provincias.  
La información que se genera corresponde a las retenciones de Ingresos Brutos ingresadas en el sistema.  
Si usted emite comprobantes electrónicos, tenga en cuenta que no se procesan los comprobantes electrónicos sin CAE asignado.  
Indique el directorio y el nombre del archivo donde se grabarán los datos exportados.  
Opcionalmente, es posible emitir un informe con los datos generados.  
Al finalizar el proceso, el sistema indicará para su control, la cantidad de registros grabados.  
Usted necesita tener instaladas las versiones actualizadas de dichos sistemas, para poder incorporar la información generada por Tango. Puede obtener el aplicativo en la siguiente dirección: <http://www.ca.gov.ar/comarb/sifere/>

Obtención de la jurisdicción:

Para la obtención de la jurisdicción, el sistema realiza las siguientes validaciones:

  * Si la retención ingresada tiene asignada una provincia, el sistema tomará la jurisdicción asignada a esa provincia.
  * Si la retención no tiene asociada una provincia, el sistema verificará si el código de retención tiene asignada una provincia y asociará la jurisdicción de esa provincia.
  * Si la retención y el código de retención no tienen asignada una provincia, la jurisdicción que se asignará es la correspondiente a la provincia del cliente.



**Trabajando en los aplicativos:**

Formato de importación  
El formato SIAp - SIFERE. para la importación de retenciones es el siguiente:

**Descripción** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
Código de jurisdicción | 1 | 3 | 3  
CUIT del agente de retención | 4 | 16 | 13  
Fecha de retención | 17 | 26 | 10  
Número de sucursal | 27 | 30 | 4  
Número de constancia | 31 | 46 | 16  
Tipo de comprobante | 47 | 47 | 1  
Letra del comprobante | 48 | 48 | 1  
Número de comprobante original | 49 | 68 | 20  
Importe de retención | 69 | 80 | 11  
  
##### Generación de archivo RG 1361

Este proceso genera los archivos requeridos para el cumplimiento de los Títulos I y II de la RG 1361 de la AFIP.

Esto es válido si usted cumple con la Resolución General 2177 (régimen especial de emisión y almacenamiento electrónico de comprobantes originales) y/o con la Resolución General 3066 (régimen especial para la emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación).  
En este caso, se obtendrán los siguientes archivos: archivos de duplicados electrónicos; archivo de percepciones y el archivo de registraciones de operaciones de ventas.  
Si no está adherido a la RG 2177 ni a la RG 3066; o bien, sólo cumple con la RG 3066, invoque este proceso para generar el archivo requerido por el Título II de la RG 1361 de la AFIP.  
Para crear los archivos correspondientes, ingrese los siguientes datos:

Mes a generar: ingrese el mes y año a informar.

CUIT del informante: indique el número de CUIT de su empresa.

Destino: es el directorio donde se generará el archivo.

Archivo a generar: indique el nombre del archivo a generar. Por defecto, se propone el nombre indicado por la AFIP, VENTAS_AAAAMM siendo AAAA el año y MM el mes a generar. Por ejemplo: VENTAS_201906.

**Errores detectados para RG 1361  
**Durante la generación del archivo, el sistema realizará una serie de validaciones a fin de garantizar los requerimientos de la resolución.  
A continuación, se detalla cada uno de los mensajes que puede informar el sistema cuando detecte alguna inconsistencia:

  * Debe indicar el número de CUIT del Cliente: cuando no se trate de un consumidor final.
  * Debe indicar la razón social del cliente con categoría "Responsable Inscripto": sólo puede ocurrir si el cliente es ocasional.
  * Debe indicar la razón social del cliente con categoría "Consumidor Final" debido a que el comprobante supera $1000: sólo puede ocurrir si el cliente es ocasional.



Tenga en cuenta que a pesar de estos errores, el sistema genera el archivo requerido por la AFIP Para corregirlos, utilice el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modifcomprobante_gv).

##### Generación de archivo RG 1575

A través de este proceso es posible generar el archivo que, posteriormente, puede ser incorporado en forma automática al sistema SIAp - CITI Ventas versión 1.0 (RG 1575/2003 y modificatorias).

Para generar el archivo correspondiente a las operaciones de ventas, ingrese los siguientes datos:

Mes a generar: ingrese el mes y año a informar.

Archivo a generar: indique el nombre del archivo a generar. Por defecto, se propone CITI_AAAAMM siendo AAAA el año y MM el mes a generar. Por ejemplo: CITI_200505.

Destino: es el directorio donde se generará el archivo.  
Si usted emite comprobantes electrónicos, tenga en cuenta que no se procesan los comprobantes electrónicos sin CAE asignado.

**Errores detectados para RG 1575  
**Durante la generación del archivo, el sistema realizará una serie de validaciones a fin de garantizar los requerimientos de la resolución.  
A continuación, se detalla cada uno de los mensajes que puede informar el sistema cuando detecte alguna inconsistencia:

  * Debe indicar el número de CUIT del Cliente: cuando no se trate de un consumidor final.
  * Debe indicar la razón social del cliente con categoría "Responsable Inscripto": sólo puede ocurrir si el cliente es ocasional.
  * Debe indicar la razón social del cliente con categoría "Consumidor Final" debido a que el comprobante supera $1000: sólo puede ocurrir si el cliente es ocasional.



Tenga en cuenta que a pesar de estos errores, el sistema genera el archivo requerido por la AFIP Para corregirlos, utilice el proceso Modificación de comprobantes.

**Trabajando en el sistema CITI Ventas Versión 1.0  
**Una vez creado el archivo desde Tango dentro del sistema SIAp - CITI Versión 1.0 se importarán los datos generados.  
Si realizó previamente una importación o una carga manual de datos, tenga en cuenta que el proceso de importación puede agregar o considerar sólo los nuevos, según lo parametrizado en la pantalla de Importación del aplicativo.

Formato de importación  
El formato SIAp - CITI Ventas para la importación de retenciones es el siguiente:

**Descripción** | **Desde** | **Hasta** | **Longitud** | **Observac.**  
---|---|---|---|---  
Tipo de registro | 1 | 1 | 1 | No informar  
Fecha del comprobante | 2 | 9 | 8 |   
Tipo de comprobante | 10 | 11 | 2 |   
Controlador fiscal | 12 | 12 | 1 | No informar  
Punto de venta | 13 | 16 | 4 |   
Número de comprobante | 17 | 36 | 20 |   
Número de comprobante hasta | 37 | 56 | 20 |   
Código de documento identificador del comprador | 57 | 58 | 2 |   
Número de identificación del comprador | 59 | 69 | 11 |   
Apellido y nombre o denominación del comprador | 70 | 99 | 30 |   
Importe total de la operación | 100 | 114 | 15 |   
Total de conceptos que no integran el precio neto | 115 | 129 | 15 |   
Importe neto gravado | 130 | 144 | 15 |   
Alícuota de IVA | 145 | 148 | 4 |   
Impuesto liquidado | 149 | 163 | 15 |   
Importe de operaciones exentas | 179 | 193 | 15 |   
Importe de percepción o pagos a cuenta de impuestos nacionales | 194 | 208 | 15 | No informar  
Importe de percepciones de ingresos brutos | 209 | 223 | 15 | No informar  
Importe de percepciones de impuestos municipales | 224 | 238 | 15 | No informar  
Importe de impuestos internos | 239 | 253 | 15 | No informar  
Tipo de responsable | 254 | 255 | 2 | No informar  
Código de moneda | 256 | 258 | 3 | No informar  
Tipo de cambio | 259 | 268 | 10 | No informar  
Cantidad de alícuotas de IVA | 269 | 269 | 1 |   
Código de operación | 270 | 270 | 1 | No informar  
CAI | 271 | 284 | 14 | No informar  
Fecha de vencimiento | 285 | 292 | 8 | No informar  
Fecha de anulación del comprobante | 293 | 300 | 8 | No informar  
Información adicional | 301 | 375 | 75 | No informar  
Fecha de pago retención | 376 | 383 | 8 |   
Importe retención | 384 | 398 | 15 |   
  
##### Generación de archivo de Transporte de Bienes - Rentas Bs.As.

Por medio de este proceso, usted genera y envía la información correspondiente a remitos electrónicos requerida por Rentas de la Provincia de Buenos Aires, para realizar el traslado o transporte de bienes según lo establece el art. 41 del Código Fiscal (TO 2011) incorporado por la Ley 13.405.

La generación, envío y recepción de los datos para Rentas se realiza de manera "on-line" (en línea), mediante una conexión segura (http o vpn), conforme lo establecido en el art. 11 de la Disposición Normativa "B" 32.  
Para informar a Rentas Bs. As. las operaciones de traslado o transporte de bienes a realizar, realice los siguientes pasos:

  * Complete los datos de la solapa Datos (*).
  * Defina los datos en la solapa Selección de comprobantes.
  * Envíe la información a Rentas presionando la tecla <F10> para establecer la conexión web y recibir la respuesta de Rentas Bs. As. Usted también puede ejecutar la opción Enviar a Rentas seleccionando, en el menú Archivo, la opción "Enviar a Rentas".
  * Una vez enviada la información, usted recibirá un acuse con los comprobantes aceptados y los rechazados (con la indicación de su motivo). Mediante la respuesta dada por Rentas Bs. As. se actualiza automáticamente el Código de Integridad y el Número Comprobante Rentas, para cada uno de los comprobantes aceptados. Tenga en cuenta que el Código de Integridad y el Número Comprobante Rentas es único para todos los comprobantes involucrados en la transacción.
  * Consulte los comprobantes aceptados, los comprobantes rechazados y los errores del envío desde la solapa Resultados.
  * Abandone el proceso presionando la tecla <Esc>.



**(*)** Si usted ingresó todos los datos a los que hace mención la [Puesta en marcha](?p=26546) del Circuito de Operación del Archivo de Transporte de Bienes - Rentas Bs. As., toda la información de la solapa [Datos](https://ayudas.axoft.com/25ar/datostranspbienrenta_gv) aparecerá precargada.

Información que incluye el archivo TXT:

Desde el proceso Generación de Archivo de Transporte de Bienes - Rentas Bs.As. se genera un archivo de texto con el siguiente nombre:  
_TB_ + CUIT empresa + _ + planta + puerta + _ + aaaammdd + _ + secuencia + .txt  
_Por ejemplo: TB_30111111118_003002_20191219_000671.txt  
En este archivo se informan los campos obligatorios, de acuerdo a la siguiente tabla:

**Descripción** | **Obligatorio**  
---|---  
CUIT DE LA EMPRESA | SI  
FECHA DE EMISION | SI  
CODIGO UNICO | SI  
FECHA DE SALIDA DEL TRANSPORTE | SI  
HORA DE SALIDA DEL TRANSPORTE | NO  
SUJETO GENERADOR | SI  
DESTINATARIO CONSUMIDOR FINAL | SI  
DESTINATARIO TIPO DE DOCUMENTO | NO  
DESTINATARIO NRO. DE DOCUMENTO | NO  
DESTINATARIO CUIT | NO  
DESTINATARIO RAZON SOCIAL | NO  
DESTINO DOMICILIO CALLE | SI  
DESTINO DOMICILIO NUMERO | NO  
DESTINO DOMICILIO COMPLEJO | NO  
DESTINO DOMICILIO PISO | NO  
DESTINO DOMICILIO DTO. | NO  
DESTINO DOMICILIO BARRIO | NO  
DESTINO DOMICILIO CODIGO POSTAL | NO  
DESTINO DOMICILIO LOCALIDAD | SI  
DESTINO DOMICILIO PROVINCIA | SI  
PROPIO DESTINO DOMICILIO CODIGO | NO  
ENTREGA DOMICILIO ORIGEN | SI  
ORIGEN CUIT | SI  
ORIGEN RAZON SOCIAL | SI  
ORIGEN DOMICILIO CALLE | SI  
ORIGEN DOMICILIO NUMERO | NO  
ORIGEN DOMICILIO COMPLEJO | NO  
ORIGEN DOMICILIO PISO | NO  
ORIGEN DOMICILIO DTO. | NO  
ORIGEN DOMICILIO BARRIO | NO  
ORIGEN DOMICILIO CODIGO POSTAL | NO  
ORIGEN DOMICILIO LOCALIDAD | SI  
ORIGEN DOMICILIO PROVINCIA | SI  
TRANSPORTISTA CUIT | NO  
TIPO DE RECORRIDO | NO  
RECORRIDO LOCALIDAD | NO  
RECORRIDO CALLE | NO  
RECORRIDO RUTA | NO  
PATENTE VEHICULO | NO  
PATENTE ACOPLADO | NO  
CODIGO UNICO DE PRODUCTO | SI  
RENTAS CODIGO UNIDAD DE MEDIDA | SI  
CANTIDAD | SI  
PROPIO CODIGO PRODUCTO | NO  
PROPIO DESCRIPCION PRODUCTO | NO  
PROPIO DESCRIPCION UNIDAD DE MEDIDA | NO  
CANTIDAD AJUSTADA | NO  
CANTIDAD TOTAL DE REMITOS | SI  
  
RN Nº 30/17:

Jurisdicciones alcanzadas  
Conforman el régimen de Información COT las Provincias de Buenos Aires, la Ciudad Autónoma de Buenos Aires, la Provincia de Santa Fe y la Provincia de Mendoza.

COT telefónico  
Dentro de los cuatro días corridos posteriores a la finalización de la validez del COT, deberá completar los datos a través de la opción Web de Carga Manual.  
El COT telefónico tendrá una vigencia limitada que se extenderá desde la fecha de inicio del viaje hasta una fecha estimada de entrega de los bienes de acuerdo a la distancia total del recorrido, de conformidad con lo siguiente:

**Distancia total del recorrido** | **Fecha estimada de entrega**  
---|---  
Menos de 500 km | Fecha de inicio +1 día  
Entre 500 y menos de 1.000 km | Fecha de inicio +2 días  
Igual o más de 1.000 km | Fecha de inicio +3 días  
  
###### Datos

En esta solapa parametrice los parámetros referidos al transporte, los mismos están organizados en 4 apartados: Origen, Destino, Transporte y Recorrido.  


**_Origen  
_**Ingrese el lugar desde donde se traslada la mercadería. Por defecto, se proponen los datos definidos en la solapa Transporte de bienes (COT) del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes).

Es Tenedor: cuando el sujeto generador del COT sea el emisor de la documentación prevista en la RG 1415-AFIP, deberá informar el carácter de "Tenedor" del mismo.  
Tilde este campo si el emisor de la documentación **NO** es el propietario de la mercadería transportada (puede tratarse del operador logístico, vendedor por cuenta y orden de terceros, intermediario o similar).  
Deje destildado este campo para indicar que el emisor de la documentación **ES EL PROPIETARIO** de los bienes, salvo que seleccione Entrega en domicilio de origen.

**_Destino (datos por defecto)  
_**Mediante esta opción, indique si la entrega se realiza en el domicilio de origen; si la dirección de destino de los bienes es la del transportista asociado a cada comprobante o la del cliente, u otra.  
Si la entrega de la mercadería se realiza en su domicilio, elija la opción 'Entrega en domicilio de origen'. Si usted envía directamente la mercadería a su cliente, elija la opción 'Dirección del cliente'.  
Si usted envía encomiendas o encarga a una empresa de transporte el envío de la mercadería a su cliente, elija la opción 'Dirección del transportista'.  
Si usted elige la opción 'Otra dirección', indique el domicilio, código postal, localidad y provincia. 

Es Tenedor: cuando el sujeto generador del COT sea el emisor de la documentación prevista en la RG 1415-AFIP, deberá informar el carácter de "Tenedor" del mismo. En este caso, identifica si el destinatario tiene o no el carácter de operador logístico, intermediario o similar.

**_Transporte  
_**Complete los datos referentes a la fecha y hora de salida, nombre del transportista que trasladará los bienes, número de patente del transporte y número de patente del acoplado (si corresponde).

**_Recorrido  
_**Seleccione el tipo de recorrido a realizar por el transporte. También es posible indicar la hoja de ruta del transporte (localidad, ruta y calle).

###### Selección de comprobantes

Desde esta solapa puede obtener una grilla con el detalle de aquellos comprobantes para los que se pedirá el COT.

Considera comprobantes que no afectan stock: tilde este parámetro para incluir los comprobantes que no afectan stock y que desee informar a ARBA.  
Tenga en cuenta que este parámetro está disponible sólo para la versión 'Agosto 2019' (para más información, consulte [Parámetros de Ventas](?p=19401), solapa Comprobantes, subsolapa [Transporte de bienes (COT)](?p=19401/#transporte-de-bienes-cot)).  
Desde el botón "Seleccionador de comprobantes" tiene la posibilidad de elegir los comprobantes a procesar, utilizando criterios de selección masiva.

__Nota

Tenga en cuenta que no son considerados los comprobantes anulados o exportados al módulo **Central**.

**Seleccionador de comprobantes  
**Esta herramienta lo guiará en la selección de comprobantes, mediante la aplicación de filtros que facilitan la búsqueda.  
Es posible definir filtros con relación a datos de comprobantes, datos de clientes u otros datos.  
Desde la ventana Seleccionador de comprobantes puede realizar una búsqueda de comprobantes que cumplan con determinada condición. En el apartado Datos de comprobantes podrá especificar el Tipo (considerando o no los comprobantes que afectan stock), elegir un rango para el Número de comprobante o la Fecha de emisión.

Considera comprobantes que no afectan stock: tilde este parámetro para incluir los comprobantes que no afectan stock y que desee informar a ARBA.  
Tenga en cuenta que este parámetro está disponible sólo para la versión 'Agosto 2019' (para más información, consulte [Parámetros de Ventas](?p=19401), solapa Comprobantes, subsolapa [Transporte de bienes (COT)](?p=19401/#transporte-de-bienes-cot)).

Tipo de comprobante: indique el tipo de comprobante a incluir.  
Si está tildado el parámetro Considera comprobantes que NO afectan stock, podrá seleccionar cualquier [tipo de comprobante](?p=19573) (que afecte o no afecte stock). No se incluyen remitos.  
Si NO está tildado el parámetro Considera comprobantes que NO afectan stock, podrá seleccionar como tipo de comprobante: factura, nota de débito, nota de crédito o remito.

Desde - Hasta número de comprobante: si eligió un tipo de comprobante, es posible seleccionar el rango de números de comprobante.

Desde - Hasta fecha: es posible indicar el rango de fechas a considerar para la búsqueda de comprobantes.  
En el apartado Datos de Clientes es posible definir el Cliente, la Provincia, etc.

Selección: este filtro permite indicar si visualiza los comprobantes de los clientes que pertenecen a una carpeta en el 'Clasificador' o bien, si tiene en cuenta solamente los comprobantes de los clientes 'Ocasionales' o de los clientes 'Habituales'.

Cliente: si eligió la opción 'Habituales', puede indicar a qué cliente hace referencia.

Provincia / Localidad: puede seleccionar una provincia o localidad a la que pertenece el cliente o el transporte indicado en el comprobante.

Desde Otros Datos puede parametrizar información referida a:

Zona / Depósito / Transportista / Vendedor: usted puede utilizar estos filtros según lo indicado en el comprobante (en el caso de depósito, transportista y vendedor) o en la ficha del cliente (para la zona).

Además puede indicar que se incluyan aquellos Comprobantes que no afectan Stock tildando la casilla respectiva. Este parámetro permite contemplar aquellos comprobantes que no han registrado movimiento de mercadería e incluirlos en la generación de datos.

Importe total sin impuestos: utilice este filtro para buscar comprobantes basándose en el importe ingresado en la generación de remitos o facturas, en la pantalla de trasporte de bienes.

__Nota

El importe asignado por defecto es definible en el campo _"Importe mínimo sin impuestos"_ del proceso [Parámetros de ventas](?p=19401/#transporte-de-bienes-cot) (solapa _Comprobantes | Transporte de bienes (COT)_).  


Desde cantidad total de Kilos: utilice este filtro si desea filtrar comprobantes según los kilos ingresados en la generación de remitos o facturas, en la pantalla de trasporte de bienes.

__Nota

La cantidad asignada por defecto es definible en el campo _"Cantidad total mínima de kilos"_ del proceso [Parámetros de ventas](?p=19401/#transporte-de-bienes-cot) (solapa _Comprobantes | Transporte de bienes (COT)_).  


Haga clic en el botón "Obtener comprobantes" para obtener, en la parte inferior de la ventana, un listado con todos aquellos comprobantes que se ajustan a los parámetros definidos.  
Si desea seleccionar comprobantes que no poseen valor tanto en Importe total sin impuestos como en Cantidad total de Kilo (en la pantalla de trasporte de bienes), los filtros Importe total sin impuestos y Cantidad total de Kilo deben estar vacíos.  
Una vez seleccionado los comprobantes, en la pantalla de Generación Archivo de trasporte de Bienes - Rentas Bs. As. podrá modificar los valores para la obtención de COT.  
Los comprobantes se presentan ordenados según la columna elegida como referencia. La grilla de selección de comprobantes exhibe la siguiente información: Tipo y Número de Comprobante, Fecha de emisión, Cliente, Razón Social / Localidad / Provincia del cliente, Depósito (correspondiente al renglón del comprobante en el caso de remitos), Vendedor (en facturas y notas de débito), Destino (se exhibe 'Transportista' o 'Cliente', según lo seleccionado en el campo Destino de la solapa Datos), C.P. Entrega / Loc. Entrega / Dom. Entrega (corresponden al código postal, localidad y domicilio de entrega; si es necesario, puede modificar estos datos).  
Al pie de la grilla se exhibe la Cantidad de Registros obtenidos.  
Marque el campo Selección para elegir un comprobante en particular.  
Si acepta la información de la grilla, regresa a la solapa Selección de comprobantes para continuar con el proceso.  
Para ello, luego de seleccionar los comprobantes apropiados, confirme la operación.

__Importante

Para la generación del archivo a partir del 05/08/2019, tenga en cuenta que los comprobantes seleccionados deben observar una numeración diferente entre sí, no aceptándose (en el mismo lote) documentos que coincidan en prefijo y número.  
_Ejemplo: FAC A 00001-00000354 y NC B 00001-00000354  
_Según el ejemplo anterior, estos comprobantes NO serán aceptados en el seleccionador de comprobantes, aun correspondiendo a tipos de comprobantes diferentes.  
Los comprobantes que compartan prefijo y número deben incluirse en lotes diferentes.

Una vez obtenido el código de COT, regístrelo en el sistema desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modifcomprobante_gv) (<F6> \- Cód. Transp. Rentas).  
Ejemplo: N. Débito A 00001-00004587 y FCE A 00001-00004587  
Según el ejemplo anterior, se informa a ARBA la Nota de Débito A 00001-00004587. Al intentar enviar la Factura de Crédito Electrónica A 00001-00004587, ésta será rechazada (aun si se envía en lotes o fechas diferentes).  
Autorice la factura de crédito electrónica desde la web de ARBA y, una vez obtenido el código de COT, regístrelo en el sistema.

_Envío a Rentas  
_Una vez que desde el seleccionador de comprobantes haya elegido todos los comprobantes apropiados y aceptado el ingreso, aparecerán como grilla en la solapa Selección de comprobantes.  
Confirme nuevamente la operación para establecer la conexión web y recibir la respuesta de Rentas Bs. As.  
Usted también puede ejecutar la opción Enviar a Rentas presionando la tecla <F10> o bien, haciendo clic en el comando Archivo y eligiendo la opción Enviar a Rentas. Puede cancelar del proceso (sin haber enviado la información a Rentas Bs. As.) presionando la tecla <Esc>.

###### Resultados

En esta solapa se informa el resultado del envío de comprobantes a Rentas Bs. As.  
Una vez enviada la información, usted recibirá un acuse con los comprobantes aceptados (aquellos que han sido registrados como correctos por Rentas Bs. As.) y los comprobantes rechazados (con la indicación de su motivo).  
Mediante la respuesta dada por Rentas Bs. As. se actualiza automáticamente el Código de Integridad y el Número Comprobante Rentas, para cada uno de los comprobantes aceptados. Tenga en cuenta que el Código de Integridad y el Número Comprobante Rentas es único para todos los comprobantes involucrados en la transacción.  
Además, usted cuenta con la información de los [errores de envío](https://ayudas.axoft.com/25ar/errordetectrentasbsas_gv).  
Ejecute el comando Listar para obtener un listado de cada uno de estos datos.

**Errores detectados por Rentas Bs. As.  
**Los errores, por los que Rentas Bs. As. puede rechazar un comprobante, son los siguientes:

**Código procesado** | **Descripción**  
---|---  
SI | El remito se procesó exitosamente.  
NO | El remito no pudo ser procesado.  
  
Los códigos anteriores se completan con los de la siguiente tabla:

**Código de error** | **Descripción**  
---|---  
01 | Ha ocurrido un error inesperado. Intente más tarde.  
02 | El usuario ingresado y/o la contraseña son inválidos.  
03 | Usuario no habilitado.  
04 | Código postal origen, inválido.  
05 | Código postal destino, inválido.  
06 | Error al intentar obtener COT.  
07 | El usuario ingresado se encuentra bloqueado.  
08 | Error de parámetro.Parámetro requerido: user  
Parámetro requerido: password  
09 | CUIT Empresa en el nombre del archivo recibido no se corresponde al CUIT de la empresa autenticada.  
10 | El nombre del archivo recibido es incorrecto.  
11 | El archivo recibido ya fue procesado con anterioridad.  
12 | No se puede procesar el registro 01-HEADER del archivo recibido. Faltan datos.  
13 | El campo CUIT_EMPRESA no se corresponde con el CUIT de la empresa autenticada.  
14 | No se puede procesar el registro 02-REMITO. Faltan datos.  
15 | No se puede procesar el registro 03-PRODUCTOS. Faltan datos  
16 | No se puede procesar el registro 04-FOOTER. Faltan datos.  
17 | El remito fue procesado con anterioridad.  
18 | Ha ocurrido un error inesperado en el procesamiento del remito. Intente más tarde.  
19 | Ha ocurrido un error inesperado en el procesamiento del archivo. Intente más tarde.  
20 | El campo FECHA_EMISION es inválido o inexistente.  
21 | El campo CODIGO_UNICO es inválido o inexistente. (1)  
22 | El campo FECHA_SALIDA_TRANSPORTE es inválido o inexistente.  
23 | El campo DESTINATARIO_CUIT es inválido o inexistente.  
24 | El campo DESTINATARIO_RAZON_SOCIAL es inválido o inexistente.  
25 | El campo DESTINO_DOMICILIO_CALLE es inválido o inexistente.  
26 | El campo DESTINO_DOMICILIO_NUMERO es inválido o inexistente.  
27 | El campo DESTINO_DOMICILIO_LOCALIDAD es inválido o inexistente.  
28 | El campo DESTINO_DOMICILIO_PROVINCIA es inválido o inexistente.  
29 | El campo ENTREGA_DOMICILIO_ORIGEN es inválido o inexistente.  
30 | El campo ORIGEN_DOMICILIO_CALLE es inválido o inexistente.  
31 | El campo ORIGEN_DOMICILIO_NUMERO es inválido o inexistente.  
32 | El campo ORIGEN_DOMICILIO_LOCALIDAD es inválido o inexistente.  
33 | El campo ORIGEN_DOMICILIO_PROVINCIA es inválido o inexistente.  
34 | El campo TRANSPORTISTA_CUIT es inválido o inexistente.  
35 | No definido.  
36 | El campo TIPO_RECORRIDO es inválido o inexistente.  
37 | El campo PATENTE_VEHICULO es inválido o inexistente.  
38 | El campo PATENTE_ACOPLADO es inválido o inexistente.  
39 | El campo CODIGO_UNICO_PRODUCTO es inválido o inexistente.  
40 | No definido.  
41 | El campo RENTAS_CODIGO_UNIDAD_MEDIDA es inválido o inexistente.  
42 | El campo CANTIDAD es inválido o inexistente.  
43 | El campo CANTIDAD_TOTAL_REMITOS es inválido o inexistente.  
44 | No hay registro 01=HEADER.  
45 | No hay registro 02=REMITO.  
46 | No hay registro 03=PRODUCTOS.  
47 | No hay registro 04=FOOTER.  
48 | No definido.  
49 | El campo CUIT_EMPRESA es inválido o inexistente.  
50 | El campo CUIT_EMPRESA no coincide con el campo CUIT del archivo.  
51 | CUIT del archivo es inválido o inexistente.  
52 | La fecha del archivo es inválida o inexistente.  
53 | El nro. secuencial del archivo es inválido o inexistente.  
54 | No definido.  
55 | No definido.  
56 | El parámetro FILE es inexistente.  
57 | El campo CANTIDAD_TOTAL_REMITOS (comprobantes enviados) no coincide con la cantidad de remitos que envía el archivo.  
58 | No definido.  
59 | No definido.  
60 | El campo HORA_SALIDA_TRANSPORTE supera los 30 minutos desde la partida del transporte.  
61 | El campo DESTINO_DOMICILIO_COMPLE es inválido.  
62 | El campo ORIGEN_DOMICILIO_COMPLE es inválido.  
63 | El campo HORA_SALIDA_TRANSPORTE es inválido.  
64 | El campo RECORRIDO_CALLE es inválido.  
65 | El campo RECORRIDO_RUTA es inválido.  
66 | El campo RECORRIDO_LOCALIDAD es inválido.  
67 | El campo ORIGEN_DOMICILIO_CODIGOPOSTAL es inválido.  
68 | El campo ORIGEN_DOMICILIO_BARRIO es inválido.  
69 | El campo ORIGEN_DOMICILIO_DTO es inválido.  
70 | El campo ORIGEN_DOMICILIO_PISO es inválido.  
71 | El campo DESTINO_DOMICILIO_CODIGOPOSTAL es inválido.  
72 | El campo DESTINO_DOMICILIO_BARRIO es inválido.  
73 | El campo DESTINO_DOMICILIO_DTO es inválido.  
74 | El campo DESTINO_DOMICILIO_PISO es inválido.  
75 | El campo CANTIDAD_AJUSTADA es inválido.  
76 | El campo PROPIO_CODIGO_PRODUCTO es inválido.  
77 | El campo PROPIO_DESCRIPCION_PRODUCTO es inválido.  
78 | El campo PROPIO_DESTINO_DOMICILIO_CODIGO es inválido.  
79 | El campo SUJETO_GENERADOS es inválido o inexistente.  
80 | No se ha establecido un canal seguro.  
81 | El campo PRODUCTO_UNICO es inválido o inexistente.  
82 | El campo DESTINATARIO_CONSUMIDOR_FINAL es inválido o inexistente.  
83 | El campo DESTINATARIO_TIPO_DOCUMENTO es inválido o inexistente.  
84 | El campo DESTINATARIO_DOCUMENTO es inválido o inexistente.  
85 | El campo ORIGEN_CUIT es inválido o inexistente.  
86 | El campo ORIGEN_RAZON_SOCIAL es inválido o inexistente.  
87 | El formulario multipart enviado es incorrecto. Verifique las especificaciones para la aplicación cliente.  
88 | La extensión del archivo recibido es incorrecta.  
89 | El campo PROPIO_DESCRIPCION_UNIDAD_MEDIDA es inválido o inexistente.  
  
**(1)** Este error puede originarse en el caso que el número de comprobante no tenga una letra asociada.

##### Soporte magnético RG 3399

Este proceso es de utilidad para quienes practican percepción de IVA en la facturación. Genera el soporte magnético cuatrimestral con la información de las percepciones practicadas a cada cliente.

Según la RG 4110 de la DGI, a partir de Marzo de 1996, se utilizará el diskette DGI - SICORE para informar las retenciones y percepciones, lo que reemplaza la utilización de este proceso para períodos posteriores.

##### Generación de archivo CITI

A través de este proceso es posible generar un archivo ASCII para su presentación ante la AFIP.

Este proceso genera el archivo DGICITI.TXT que, posteriormente, puede ser incorporado en forma automática al sistema SIAp - CITI Compras versión 4.0.  
Tenga en cuenta que para realizar la importación en el aplicativo tiene que hacerlo seleccionado la opción "Detalle".  
La información se genera en forma detallada por comprobante, sin hacer agrupamientos. El procesamiento de la información se hará en el aplicativo CITI.  
Los comprobantes que se generan corresponden a las notas de crédito tipo 'A' y 'B'.  
Si usted emite comprobantes electrónicos, tenga en cuenta que no se procesan los comprobantes electrónicos sin CAE asignado.  
Tenga en cuenta que sólo se incluyen las alícuotas generales.

**Datos solicitados en pantalla**

Desde / Hasta fecha: ingrese el período a procesar.

Razón social del informante: debe coincidir con la denominación declarada en el SIAp.

CUIT del informante: corresponde al número de CUIT del informante, el que ha sido declarado en el SIAp.

lmprime información para DGI - CITI: es posible emitir en forma opcional un informe con el detalle de la información generada.

Importante:

Si usted ya realizó la generación de CITI en el módulo Compras / Proveedores para el mismo período, el sistema exhibirá el mensaje "El archivo ya existe sobregraba?". Para agregar la información correspondiente al módulo Ventas en el mismo archivo, responda "No". Caso contrario, se eliminará la información existente generada en Compras / Proveedores. Tenga en cuenta que el archivo es único para ambos módulos.

**Trabajando en el sistema SIAp - CITI  
**Una vez generado el archivo desde Tango, dentro del sistema SIAp - CITI se importan los datos generados.

Importante:

Si usted realizó previamente una importación o una carga manual de datos en SIAp - CITI Compras, tenga en cuenta que al importar el archivo generado por Tango, se borrarán los comprobantes existentes, quedando sólo los últimos importados.

Formato de importación  
El archivo ASCII generado por Ventas debe ser importado en la opción Declaración jurada / Importación de datos / Archivo sin procesamiento.  
Las posiciones de cada uno de los campos deben configurarse de la siguiente manera:

**Descripción** | **Desde** | **Hasta** | **Longitud**  
---|---|---|---  
Tipo de comprobante (*1) | 001 | 002 | 2  
Número del comprobante | 003 | 026 | 24  
Fecha del comprobante | 027 | 034 | 8  
CUIT del informante (*2) | 035 | 045 | 11  
Apellido y nombre o denominación (*3) | 046 | 070 | 25  
Impuesto liquidado | 071 | 082 | 12  
CUIT vendedor (*4) | 083 | 093 | 11  
Denominación vendedor (*4) | 094 | 118 | 25  
IVA comisión (*4) | 119 | 130 | 12  
  
**(*1)** Se generará el Tipo de Comprobante "03" que corresponde a Notas de crédito.  
**(*2)** Corresponde al número de CUIT del informante, el que ha sido declarado en el SIAp.  
**(*3)** Debe coincidir con la denominación declarada en el SIAp.  
**(*4)** Estos campos no se informan para el tipo de comprobante "03".

##### Soporte magnético RG 3115

Este proceso permite generar la declaración jurada trimestral correspondiente a la percepción de Ingresos Brutos, para los casos en que se realizan percepciones conforme a la Resolución General 3115 de DGR.

El soporte magnético generado contempla las modificaciones introducidas en la RG 3115 por la Resolución 1014 (DGR MCBA).  
Para completar la información de la declaración jurada, se solicitan los siguientes datos con respecto al trimestre a procesar:

Datos Generales del Usuario: incluye la razón social, domicilio, localidad, número de inscripción como agente de percepción y número de CUIT.

Año: se ingresa el año de la declaración.

Trimestre: se ingresa el trimestre del año (1, 2, 3, 4).  
Luego se ingresarán, si existen, los datos relacionados con los comprobantes de pago efectuados para cada quincena del trimestre a procesar.  
Estos datos no son necesarios para el soporte magnético, pero se imprimen en la declaración jurada opcional.

Provincia: se indicará el código de provincia correspondiente a Capital Federal, de ese modo se incluirán sólo las tasas que tengan asociada la misma jurisdicción.  
Finalmente, se da opción a imprimir por triplicado la información correspondiente a la declaración jurada.

El sistema grabará un archivo con nombre DECLAR en el directorio DGI, en la unidad de disco donde se encuentra instalado el sistema, por ejemplo: C: DGI DECLAR.

##### Soporte magnético Ingresos Brutos Bs.As. 59/98

Este proceso permite generar el soporte magnético correspondiente a las percepciones de ingresos brutos según la Disposición Normativa serie "B" Número 59/98 de la provincia de Buenos Aires.

Se ingresará el rango de fechas a generar y el rango de alícuotas utilizadas para calcular esta percepción.  
El sistema sugerirá como nombre del archivo INGRBRUT.DAT, en el directorio que usted elija.

##### Contenidos relacionados

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/retencpercep_gral_vid/)
