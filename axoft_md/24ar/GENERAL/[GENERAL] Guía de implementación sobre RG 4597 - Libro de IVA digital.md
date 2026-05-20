# Guía de implementación sobre RG 4597 - Libro de IVA digital

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_rg4597_gla/

## Contenido

# Guía de implementación sobre RG 4597 - Libro de IVA digital

La RG 4597 establece un régimen de registración electrónica de operaciones (de venta, compra, cesiones, exportaciones e importaciones definitivas de bienes y servicios, locaciones y prestaciones), denominado "Libro de IVA Digital".

La registración electrónica alcanzará a las siguientes operaciones, sean o no generadoras de crédito o débito fiscal en el IVA.

  1. Compras, cesiones, locaciones y prestaciones recibidas e importaciones definitivas de bienes y servicios -así como todo otro concepto facturado o liquidado por separado, relacionado con las mismas o con su forma de pago- que, como consecuencia de cualquier actividad que desarrollen, realicen con proveedores, locadores, prestadores, comisionistas, consignatarios, etc.
  2. Descuentos y bonificaciones recibidas, quitas, devoluciones y rescisiones obtenidas, que se documenten en forma independiente de las compras, cesiones, locaciones y prestaciones.
  3. Ventas, cesiones, locaciones o prestaciones realizadas, exportaciones definitivas de bienes y servicios, así como todo otro concepto facturado o liquidado por separado, relacionado con las mismas o con su forma de pago.
  4. Descuentos y bonificaciones otorgadas, quitas, devoluciones y rescisiones efectuadas, que se documenten en forma independiente de las ventas, cesiones, locaciones y prestaciones.



Más información:

Los montos que deberán consignarse en la declaración jurada determinativa del impuesto al valor agregado correspondiente al período mensual que se liquida, se conformarán por todas las operaciones registradas en el "Libro de IVA Digital" del mismo período mensual, con los ajustes al débito o al crédito fiscal, que correspondan.

Para más información sobre el régimen, consulte [aquí](http://www.afip.gob.ar/libro-iva-digital/).

**Consideraciones  
**Este nuevo régimen sustituirá al régimen informativo de compras y ventas instaurado por la Resolución General N° 3.685. Su implementación se hará de acuerdo a un cronograma definido por AFIP.  
Para tal fin, AFIP habilitó el servicio denominado "PORTAL IVA", a través de su sitio web institucional (<http://www.afip.gob.ar/sitio/externos/default.asp>).  
Desde este portal, usted accederá a la información de:

  * Libro de IVA digital.
  * Declaración Jurada de IVA



Si necesita modificar la información propuesta por AFIP para el Libro de IVA digital, podrá importar los archivos generados desde Tango Gestión o Liquidador de IVA.

#### Para Gestión

Con Tango, usted cumple con las disposiciones de esta norma, generando el soporte magnético para la RG 4597, habiendo configurado previamente los proveedores y clientes vinculados a su empresa.  
A continuación exponemos los pasos necesarios para poner en marcha el circuito correspondiente a la RG 4597 en Tango Gestión.

##### Puesta en marcha

Para generar los archivos a importar en el Portal IVA de AFIP, configure previamente:

  * [Parámetros de ventas](?p=19401): en la solapa [Clientes](?p=19401/#parametros-para-clientes) complete el tipo de operación habitual según la RG 4597. Este valor se utilizará como valor por defecto para los nuevos clientes, sean habituales u ocasionales.  
En la solapa [Comprobantes](?p=19401/#parametros-para-comprobantes), sección Pedidos, complete el tipo de operación habitual para RG 4597. Este valor se utilizará en la facturación de pedidos por lote.
  * [Clientes](?p=19444): en las solapas Facturación y Cobranzas, complete el tipo de operación habitual según la RG 4597. Este valor es utilizado como valor por defecto durante la emisión de comprobantes. Posteriormente, podrá editarlos desde el proceso [Modificación de comprobantes](?p=20552).
  * [Perfiles de facturación](?p=19415): indique el tipo de operación habitual para los comprobantes que emita y las restricciones de edición (edita, muestra u oculta el campo).
  * [Parámetros de Compras](?p=14676): en la solapa [Principal](?p=14676/#principal), complete el tipo de operación y el código de comprobante habitual para los comprobantes de proveedores ocasionales según la RG 4597.
  * [Proveedores](?p=14686): asigne a su proveedor habitual los valores de Tipo Operación y Comprobante AFIP. Estos valores se utilizan como valor por defecto para los comprobantes que reciba. Posteriormente, podrá editarlos desde el proceso [Modificación de comprobantes](?p=15550).  
Al activar el parámetro Genera Información, todos los comprobantes que ingrese para el proveedor (facturas, créditos y débitos) serán informados en los archivos de soporte magnético para la RG 4597.
  * [Monedas](?p=11955): verifique que las monedas con las que opera su empresa tengan el código de moneda AFIP en la solapa Datos Legales del módulo Procesos Generales.



Los nuevos comprobantes tomarán el valor configurado en el cliente / proveedor, pudiendo ser modificado en el momento de su ingreso o desde los procesos [Modificación de comprobantes](?p=20552) de Ventas o [Modificación de comprobantes](?p=15550) de Compras.

##### Detalle del circuito

Los comprobantes que se informan son los siguientes:

Ventas:

  * Facturas
  * Notas de crédito
  * Notas de débito



Compras:

  * Factura
  * Factura - remito
  * Nota de crédito
  * Nota de débito
  * Despachos



Las condiciones que deben cumplir estos comprobantes son:

  * Deben pertenecer al período seleccionado en el proceso de generación. En el caso de los comprobantes de compras, se toma en cuenta la fecha contable.
  * Deben estar configurados para intervenir en los libros IVA.



Para generar los archivos a importar desde el Portal IVA de AFIP, ingrese al proceso de generación de [RG 4597](?p=11988/#rg-4597).  
Al finalizar el mismo (y si existe información), se generan los siguientes archivos (donde "AAAAMMDDHHMMSS" corresponde al momento en el que se crearon éstos):

**Para Responsables Inscriptos:**

  * **Ventas:**
    * Ordinarias: 
      * Cabecera: LIBRO_IVA_DIGITAL_VENTAS_CBTE
      * Detalle: LIBRO_IVA_DIGITAL_VENTAS_ALICUOTAS
    * Turismo: 
      * LIBRO_IVA_DIGITAL_VENTAS_TurIVA_CBTE
      * LIBRO_IVA_DIGITAL_VENTAS_TurIVA_ALICUOTAS
    * Anulaciones: 
      * LIBRO_IVA_DIGITAL_CBTES_VENTAS_ANULADOS
  * **Compras:**
    * Ordinarias: 
      * Cabecera: LID_COMPRAS_ORDINARIAS_CBTE_AAAAMMDDHHMMSS
      * Detalle: LID_COMPRAS_ORDINARIAS_ALICUOTAS_AAAAMMDDHHMMSS
    * Bienes usados y materiales reciclables: 
      * Cabecera: LID_COMPRAS_USAYREC_CBTE_AAAAMMDDHHMMSS
      * Detalle: LID_COMPRAS_USAYREC_ALICUOTAS_AAAAMMDDHHMMSS
    * Importación de bienes: 
      * Cabecera: LID_COMPRAS_IMPOBIENES_CBTE_AAAAMMDDHHMMSS
      * Detalle: LID_COMPRAS_IMPOBIENES_ALICUOTAS_AAAAMMDDHHMMSS
    * Turismo: 
      * Cabecera: LID_COMPRAS_TurIVA_CBTE_AAAAMMDDHHMMSS



**Para Exentos:**

  * **Ventas:**
    * Ordinarias: 
      * LIBRO_IVA_DIGITAL_VENTAS_CBTE
    * Turismo: 
      * LIBRO_IVA_DIGITAL_VENTAS_TurIVA_CBTE
    * Anulaciones: 
      * LIBRO_IVA_DIGITAL_CBTES_VENTAS_ANULADOS
  * **Compras:**
    * Ordinarias: 
      * LID_COMPRAS_ORDINARIAS_CBTE_AAAAMMDDHHMMSS
    * Bienes usados y materiales reciclables: 
      * LID_COMPRAS_USAYREC_CBTE_AAAAMMDDHHMMSS
    * Importación de bienes: 
      * LID_COMPRAS_IMPOBIENES_CBTE_AAAAMMDDHHMMSS
    * Turismo: 
      * LID_COMPRAS_TurIVA_CBTE_AAAAMMDDHHMMSS



#### Para Liquidador de IVA

A continuación, exponemos los pasos necesarios para poner en marcha el circuito correspondiente a la RG 4597 para Liquidador de IVA, aplicable a cualquiera de los tipos de comprobantes comprendidos en dicha resolución general.  
Para generar el completar el circuito siga los pasos explicitados a continuación.

##### Puesta en marcha

Para generar los archivos a importar en el Portal IVA de AFIP configure previamente:

  * [Monedas](?p=11956): indique en las monedas con las que opera su empresa, el código de moneda AFIP en la solapa Datos Legales del módulo Procesos Generales.
  * [Parámetros de Liquidador de IVA](?p=8426): defina en forma genérica la operación habitual AFIP para comprobantes de ventas y de compras.
  * [Clientes](?p=8349): indique la operación habitual AFIP del cliente para el ingreso de comprobantes de ventas. Además, tenga en cuenta que para poder generar en forma correcta los archivos deberá revisar los datos informados sobre tipo y número de documento según la categoría de IVA definida.
  * [Proveedores](?p=8430): indique la operación habitual AFIP del proveedor para el ingreso de comprobantes de compras. Además, tenga en cuenta que para poder generar en forma correcta los archivos deberá revisar los datos informados sobre tipo y número de documento según la categoría de IVA definida.
  * [Registración de comprobantes](?p=8433): indique el tipo de comprobante AFIP y el código de operación. El sistema propone un valor por defecto para ambos campos siguiendo la lógica que se detalla a continuación: 
    * Tipo de comprobante AFIP: se lo propone en base al tipo de comprobante interno (por ejemplo, factura, nota de crédito, nota de débito) y a la letra del comprobante ingresada.
    * Tipo de operación: propone el tipo de operación asociado el cliente/proveedor o, caso contrario, el de Parámetros Generales.



##### Detalle del circuito

A continuación, se detallan los archivos que genera el proceso cuando la empresa reviste la condición de Responsable Inscripto frente al IVA:

  * LIBRO_IVA_DIGITAL_VENTAS_CBTE  
(Registro Ventas - Cabecera)
  * LIBRO_IVA_DIGITAL_VENTAS_ALICUOTAS  
(Registro Ventas - Alícuotas)
  * LIBRO_IVA_DIGITAL_CBTES_VENTAS_ANULADOS  
(Registro Comprobantes Anulados)
  * LID_COMPRAS_USAYREC_CBTE_AAAAMMDDHHMMSS  
(Registro Compras e Importación de Bienes - Cabecera)
  * LID_COMPRAS_USAYREC_ALICUOTAS_AAAAMMDDHHMMSS  
(Registro Compras - Alícuotas)
  * LID_COMPRAS_IMPOBIENES_CBTE_AAAAMMDDHHMMSS  
(Registro Compras e Importación de Bienes - Cabecera)
  * LID_COMPRAS_IMPOBIENES_ALICUOTAS_AAAAMMDDHHMMSS  
(Registro Importaciones de Bienes - Alícuotas)
  * LID_COMPRAS_ORDINARIAS_CBTE_AAAAMMDDHHMMSS  
(Registro Compras e Importación de Bienes - Cabecera)
  * LID_COMPRAS_ORDINARIAS_ALICUOTAS_AAAAMMDDHHMMSS  
(Registro Compras - Alícuotas)



Cuando la empresa reviste la condición de Exento frente al IVA, el proceso genera los siguientes archivos:

  * LIBRO_IVA_DIGITAL_VENTAS_CBTE  
(Registro Ventas – Cabecera)
  * LIBRO_IVA_DIGITAL_CBTES_VENTAS_ANULADOS  
(Registro Comprobantes Anulados)
  * LID_COMPRAS_USAYREC_CBTE_AAAAMMDDHHMMSS  
(Registro Compras e Importación de Bienes – Cabecera)
  * LID_COMPRAS_IMPOBIENES_CBTE_AAAAMMDDHHMMSS  
(Registro Compras e Importación de Bienes – Cabecera)
  * LID_COMPRAS_ORDINARIAS_CBTE_AAAAMMDDHHMMSS  
(Registro Compras e Importación de Bienes – Cabecera)



Las condiciones que deben cumplir estos comprobantes son:

  * Deben pertenecer al período seleccionado en el proceso de generación. En el caso de los comprobantes de compras, se toma en cuenta la fecha contable.
  * Deben estar configurados para intervenir en los libros IVA.



Para generar los archivos a importar desde el Portal IVA de AFIP, ingrese al proceso de generación de [RG 4597](?p=11988/#rg-4597).

#### Para Central

A continuación, exponemos los pasos necesarios para poner en marcha el circuito correspondiente a la RG 4597 - Libro de IVA digital, en Tango Gestión, de manera centralizada.

##### Detalle del circuito centralizado

Siga estos pasos para generar los archivos requeridos para la RG 4597/19 - Libro de IVA digital, pudiendo consolidar información de varias sucursales o generar información separada para cada una de ellas.

  1. Desde una empresa sucursal, en el proceso [RG 4597](?p=11988/#rg-4597), seleccione la opción 'Gestión' como origen de la información.
  2. Tilde el parámetro Genera información para transferencias a central. Al marcar esta opción, se genera una copia de la información para exportar.
  3. Confirme la generación de los archivos. Al finalizar el proceso (y si existe información), se generan los siguientes archivos, donde "AAAAMMDDHHMMSS" corresponde al momento en el que se generaron los archivos anteriormente mencionados.
  4. Exporte la información habilitada desde la empresa sucursal. Para ello, utilice el asistente de exportación de [Información para RG 4597](?p=29296) desde el módulo Procesos generales o Central.
  5. En la empresa donde desea consolidar la información, importe el archivo .zip del paso anterior, con el asistente de importación del proceso [Información para RG 4597](?p=29309) (desde el módulo Central).
  6. En la empresa donde importó la información, ejecute el proceso RG 4597 en el módulo Procesos Generales, seleccione la opción 'Central' como origen de la información.



Ingrese los datos requeridos, tales como Período a informar, Comprobantes y Tipo de generación.  
Desde allí, genere los archivos con la información correspondiente a ventas y/o compras.

__Nota

Cada archivo se genera con la información de todas las empresas sucursales que usted haya importado para un mismo período.

##### Automatizar la generación y transferencia de la información para el Libro de IVA digital

Puede definir una tarea automática que genere la información de cada sucursal, para luego exportarla.  
Para automatizar la generación de información, siga estos pasos:

  1. Desde una empresa sucursal, en el módulo Procesos generales, desde el proceso [RG 4597](?p=11988/#rg-4597), seleccione (como Origen de la información) la opción: 'Gestión'.
  2. Tilde el parámetro Genera información para transferencias a central.
  3. Antes de comenzar la generación, si corresponde, el proceso le preguntará si desea generar una tarea automática para transferir la información desde la sucursal a la central.  
La tarea automática puede modificarse desde el _Administrador_ , en el menú _Servicios_ , ícono _Automatización de Central_. Usted puede cambiar la frecuencia de ejecución (por defecto, una vez al día). La tarea programada genera información por los comprobantes del mes anterior y por los del mes en curso (hasta la fecha de la transferencia).
  4. Exportación e Importación de la información: 
     1. Si opera manualmente, repita los siguientes pasos (para cada una de las sucursales a procesar):  
i. Exporte la información habilitada desde la empresa sucursal. Para ello, utilice el asistente de exportación de [Información para RG 4597](?p=29296) desde el módulo Procesos generales o Central.  
ii. En la empresa donde desea consolidar la información, importe el archivo .zip del paso anterior, con el asistente de importación de [Información para RG 4597](?p=29309) desde el módulo Central.
     2. Si cuenta con Tangonet, es posible automatizar las exportaciones e importaciones. Esta herramienta permite realizar todo el proceso de generación y transferencia de la información sin la intervención de un operador.
  5. En la empresa donde se importó la información, ejecute el proceso [RG 4597](?p=11988/#rg-4597) (del módulo Procesos generales).  
Seleccione la opción 'Central' como origen de la información.  
Configure los parámetros restantes y genere los archivos con la información consolidada.
