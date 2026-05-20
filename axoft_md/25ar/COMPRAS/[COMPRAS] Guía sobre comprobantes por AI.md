# Guía sobre comprobantes por AI

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_compai_cp2/

## Contenido

# Guía sobre comprobantes por AI

A través del proceso [Administrador de comprobantes con AI](?p=13473) usted podrá recibir, procesar e importar comprobantes de sus proveedores recibidos mediante correo electrónico, **WhatsApp** o descargados en una carpeta de red.

##### Puesta en marcha

Para comenzar a importar los comprobantes de sus proveedores debe configurar primero los orígenes de comprobantes a utilizar (correo electrónico, WhatsApp o carpeta de red).  
Siga estos pasos:

  * En Parámetros de Compras, en la sección Importación por AI, complete los parámetros relacionados a los diferentes orígenes a utilizar.
  * Si utiliza el origen 'Correo electrónico', deberá configurar adicionalmente la cuenta de correo de recepción de comprobantes, en Parámetros para correo electrónico de Procesos generales.
  * Por último, defina los perfiles para el administrador de comprobantes por AI, para configurar que usuarios podrán utilizar el circuito y definir algunas configuraciones adicionales



Adicionalmente, deberá adquirir créditos en [Tango Billing](https://billing.axoft.com/) para utilizar esta funcionalidad. La primera vez que ingrese al Administrador de comprobantes por AI (o cuando el crédito se agote) se le solicitará una "API Key Credencial", la cual puede adquirir desde el sitio de [Tango Billing](https://billing.axoft.com/) ingresando con su usuario de Tango nexo. Para más información, ingrese a [Tango Billing](https://billing.axoft.com/).

##### Detalles del circuito

Una vez configurados los destinos de recepción usted podrá:

  1. Consultar desde el Administrador de comprobantes por AI los documentos recibidos. Seleccionando uno o varios comprobantes, podrá enviarlos a Procesar por la AI.
  2. Consultar los comprobantes que se encuentran en proceso de análisis.
  3. Revisar y registrar los comprobantes analizados por la AI, tomando los datos interpretados automáticamente.
  4. Revisar y completar la información en comprobantes que no se hayan interpretado en su totalidad.
  5. Consultar todos los comprobantes que ingresaron dentro de un tiempo determinado.



Para más información, acceda a [Administrador de comprobantes por AI](?p=13473).

##### Preguntas frecuentes

**¿Qué es el Administrador de comprobantes con AI?  
**Es un proceso a través del cual puede configurar para que, masiva y automáticamente, ingresen a Tango comprobantes recibidos de sus proveedores. Para ello deberá configurar los orígenes de los cuales desea ingresar información.

**¿De qué forma puedo importar comprobantes?  
**Existen 3 formas de incorporar comprobantes:

  * **Correo electrónico:** configure una casilla de correo donde desea recibir los comprobantes (por ejemplo: proveedores@suempresa.com), y cada vez que reciba un correo con un PDF adjunto, automáticamente será incorporado al [Administrador de comprobantes por AI](?p=13473).
  * **WhatsApp:** si utiliza una cuenta de WhatsApp para conectarse con sus proveedores, podrá asociarla para que cada vez que se inicie una conversación y reciba un PDF adjunto, se importe automáticamente en el [Administrador de comprobantes por AI](?p=13473).
  * **Carpeta de red:** si recibe comprobantes por alguna otra vía, por ejemplo con un enlace para descargar del sitio web del proveedor, puede descargar los documentos directamente a una carpeta de red configurada en Parámetros de Compras, para que automáticamente se incorporen al [Administrador de comprobantes por AI](?p=13473).



**¿Cuánto cuesta utilizar este servicio?  
**El costo depende de varios factores:

  * **El modelo utilizado:** en los Perfiles para el [Administrador de comprobantes por AI](?p=13473) puede seleccionar entre 2 modelos de AI ('Básico' y 'Avanzado'). Cada uno de estos modelos es útil para diferentes situaciones. Por ejemplo, si su proveedor envía comprobantes con muchos ítems, o con muchas imágenes y en un formato particular, seguramente el modelo 'Avanzado' interprete mejor el comprobante pero tendrá un costo mayor. Para comprobantes sencillos, con pocos ítems, puede utilizar el modelo 'Básico'.
  * **La cantidad de información del comprobante:** si procesa un comprobante que cuenta con varias hojas, o con mucha cantidad de ítems, el costo del procesamiento puede ser mayor.
  * **Si en su perfil tiene activada la opción "Analiza detalle" de los comprobantes:** esta opción le permite indicar si desea que la AI procese los renglones, o directamente los datos generales del comprobante (por ejemplo, para facturas de servicios o impuestos).



**¿Qué es lo que hace la AI?  
**Desde el [Administrador de comprobantes por AI](?p=13473) puede interactuar con la AI de forma sencilla, enviando comprobantes en PDF para ser analizados, y recibir la información procesada lista para registrar el comprobante.  
La información que la AI resuelve es la que solamente viene contenida en el PDF, por ejemplo: fecha de emisión, CUIT del proveedor, tipo y número de comprobante, importes, etc.  
Para el resto de la información requerida por un comprobante de compras, se obtiene del perfil de facturas de compras, por ejemplo: lista de precios, modelo de asiento, depósito, etc.

**¿Qué tipo de archivos se pueden analizar con la AI?  
**Solo se pueden analizar archivos en formato PDF, ya sea un documento digital o una imagen que haya sido convertida previamente a PDF.

**¿Qué tipos de comprobante puedo importar?  
**Se pueden importar facturas, créditos y débitos (tanto de artículos como de conceptos).  
Se podrán registrar comprobantes que cuenten además con estas condiciones:

  * Comprobantes en cuenta corriente, es decir, con condición de compra que no sea al contado.
  * Comprobantes de proveedores existentes (no se pueden registrar como proveedores ocasionales).



##### Contenidos relacionados

  * [Administrador de comprobantes por AI](https://ayudas.axoft.com/25ar/ayudas/cp2/comprobantes_carp_cp2/compia_carp_cp2/adincompai_cp2/)

  * [Perfiles para el administrador de comprobantes por AI](https://ayudas.axoft.com/25ar/ayudas/cp2/archivos_carp_cp2/cargainicial_cp2/perfiles_carp_cp2/perfadmincompai_cp2/)

  * [Revisión de comprobantes](https://ayudas.axoft.com/25ar/ayudas/cp2/comprobantes_carp_cp2/compia_carp_cp2/revicioncompia_cp2/)

  * [Sincronización de comprobantes](https://ayudas.axoft.com/25ar/ayudas/cp2/comprobantes_carp_cp2/compia_carp_cp2/sincrocompia_cp2/)

  * [Videos sobre Tango AI](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/tangoai_gla_vid/)
