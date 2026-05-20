# Guía sobre comprobantes electrónicos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_rg4520_gla/?p=26548/

## Contenido

# Guía sobre comprobantes electrónicos

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
  * Si prefiere no imprimir el comprobante, puede enviarlo por correo electrónico. Tenga en cuenta que las facturas electrónicas en la que intervenga al menos un pedido o remito proveniente de MercadoLibre se redireccionará para ser enviada por la mensajería de MercadoLibre.



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

##### Contenido dependiente

  * [Puesta en marcha del circuito de comprobantes electrónicos](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_comprobelectr_gv/guia_pm_comprobelectr_gv/)
  * [Detalle del circuito de comprobantes electrónicos](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_comprobelectr_gv/guia_dc_comprobelectr_gv/)



##### Contenidos relacionados

  * [Definición de talonarios](https://ayudas.axoft.com/24ar/ayudas/gv/archivos_carp_gv/cargainicial_carp_gv/talonario_gv/talonario_gv/)

  * [Video sobre Facturas MiPymes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/mipymes_gv_vid/)

  * [Video sobre facturación sin controlador fiscal](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factsincf_gv_vid/)

  * [Video sobre regímenes de facturación](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/regfact_gral_vid/)

  * [Videos sobre administración y facturación venta online](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/ventaonline_gral_vid/)

  * [Videos sobre emisión de comprobantes con CAEA](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/caea_gv_vid/)

  * [Videos sobre factura de crédito electrónica](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/fce_gral_vid/)
