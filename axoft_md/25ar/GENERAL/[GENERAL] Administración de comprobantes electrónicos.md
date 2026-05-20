# Administración de comprobantes electrónicos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg4520_gla/?p=19186/

## Contenido

# Administración de comprobantes electrónicos

Usted podrá administrar los comprobantes electrónicos generados por la empresa, obtener los CAE para los comprobantes pendientes o rechazados y enviar los comprobantes electrónicos a los clientes por correo electrónico o por **WhatsApp** , publicarlos en **[Tango Tiendas](?p=12428)** o generar una copia impresa, dependiendo de la licencia de su llave **Tango**.

__Nota

El circuito de comprobantes electrónicos está disponible sólo si su licencia está habilitada. Para más información, consulte con su proveedor de **Tango**.

Utilice esta herramienta para la gestión de sus comprobantes electrónicos del mercado interno como así también los de exportación.  
En la solapa Comprobantes pendientes / rechazados es posible visualizar los comprobantes electrónicos que todavía no poseen CAE o cuyo pedido fue rechazado debido a algún tipo de inconsistencia detectada por la AFIP, y solicitar el CAE para cada comprobante.  
La solapa Comprobantes autorizados detalla los comprobantes ya autorizados por la AFIP permitiendo consultarlos en PDF y XML, imprimirlo , publicarlos en [Tango Tiendas](?p=12428) dependiendo de la licencia de su llave Tango, o enviarlos por correo electrónico o por WhatsApp.  
Desde la solapa Informar CAEA podrá informar a AFIP los comprobantes generados mediante esta modalidad como los CAEA no utilizados en el periodo solicitado.

##### Generalidades

Opciones de la barra de herramientas

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

Permisos y Roles

El Administrador "en línea" no requiere que el usuario tenga permiso de acceso a ese proceso.  
Las columnas "Importes", "Unidades" y "Cotización" estarán visibles según el rol asignado por usuario. De igual manera, la acción "Eliminar rechazados" estará disponible según el rol asignado por usuario.  
Para más información, consulte el proceso [Administrador de roles](?p=9113).

##### Comprobantes autorizados

Ingrese a esta solapa cuando desee visualizar, imprimir o enviar por correo electrónico o por WhatsApp los comprobantes ya autorizados por la AFIP.  
Mediante la utilización de filtros, usted puede consultar los comprobantes electrónicos aplicando un criterio de selección particular (cliente, vendedor, talonario, comprobante, fecha de emisión).  
Por defecto, el criterio de búsqueda es Fecha de emisión, considerando la fecha del día como rango de fechas a aplicar.  
Desde la grilla resultante será posible visualizar el comprobante en PDF y XML, y seleccionar cualquiera de ellos para imprimirlos, publicarlos en [Tango Tiendas](?p=12428), dependiendo de la licencia de su llave Tango o enviarlos por correo electrónico o por WhatsApp.  
Para cada uno de los comprobantes se detalla el CAE obtenido y su respectiva fecha de vencimiento, la cantidad de impresiones y/o envíos por correo electrónico o por WhatsApp realizados.  
Un comprobante puede tener CAE y haber sido 'Observado' por AFIP. Para más información, consulte el ítem [Comprobantes observados](https://ayudas.axoft.com/25ar/comprobanteobservado_gv).  
Para visualizar los comprobantes, indique el criterio de búsqueda deseado y pulse el botón "Obtener comprobantes".  
Seleccione el o los comprobantes y pulse el botón "Enviar a". Desde la ventana con el título Emitir comprobantes, seleccione la operación a realizar: imprimir, enviar por correo, enviar por WhatsApp y/o generar a directorio, o publicarlos en [Tango Tiendas](?p=12428), dependiendo de la licencia de su llave Tango.

Código QR

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

##### Informar CAEA

Ingrese a esta solapa cuando desee informar a AFIP los movimientos con CAEA.  
Mediante la utilización de filtros, usted puede consultar los comprobantes electrónicos o puntos de ventas para el periodo y quincena a informar.  
Para visualizar los comprobantes, indique el criterio de búsqueda deseado y pulse el botón "Obtener movimientos".  
Puede consultar la fecha de vencimiento de la presentación en la opción "Obtener CAEA" de la barra de herramientas.

CAEA con movimientos

Desde la grilla resultante podrá visualizar los comprobantes generados con CAEA, informar aquellos pendientes y consultar los rechazos si los hubiera, ingresando a la opción "Motivo". Desde allí podrá realizar la corrección y enviarlo nuevamente.  
Pulse el botón "Informar CAEA" para presentar estos comprobantes a AFIP.

CAEA sin movimientos

Si durante el periodo de vigencia de CAEA no se generaron comprobantes con este modo de autorización, desde esta solapa podrá consultar e informar a AFIP los puntos de ventas que no tuvieron movimientos para el periodo y quincena seleccionado.

##### Comprobantes pendientes / rechazados

Desde esta solapa solicite a la AFIP el código de autorización de emisión (CAE).  
En la misma pantalla se visualizan los comprobantes pendientes de autorización y aquellos que fueron rechazados (por habérseles detectado algún tipo de inconsistencia).  
En este último caso, pulse sobre la columna "Motivo rechazo" para conocer la causa del rechazo. Para más información, consulte el ítem Rechazo de comprobantes electrónicos.  
Pulse el botón "Obtener CAE" para solicitar el código de autorización correspondiente a cada comprobante. En forma simultánea, puede proceder a la emisión del comprobante electrónico, para ello, en la acción 'Según lo indicado en el talonario' tilde para cada talonario la columna "Imprimir", "Enviar correo", "Enviar WhatsApp", "Publica comprobante" o "Graba en directorio" según corresponda (pudiendo tildar más de una).  
Por otra parte, desde la acción 'Según lo indicado en el Facturador' puede enviar los comprobantes según la forma de envío indicada durante la generación de cada uno de ellos.

__Nota

Tenga en cuenta que la emisión del comprobante (impresión, envío por correo electrónico y/o envío por WhatsApp) puede ser realizada en forma diferida a la obtención del CAE. Dicha opción está disponible en la solapa _Comprobantes Autorizados_.

Rechazo de comprobantes electrónicos

  * AFIP rechazará la solicitud de autorización de un comprobante electrónico cuando se detecten inconsistencias en los datos vinculados al emisor.  
En este caso, el emisor del comprobante puede emitir un comprobante a través del "Controlador Fiscal" o en forma manual, o solicitar nuevamente la autorización de emisión electrónica, una vez subsanado el inconveniente.
  * Si la fecha del comprobante electrónico está fuera del rango permitido por AFIP (+/- 5 días o bien, +/- 10 días, según el tipo de operación), se rechazará la solicitud de autorización. En este caso, corrija la fecha del comprobante desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modifcomprobante_gv). Consulte la ayuda del proceso para conocer las validaciones aplicadas por el sistema.
  * Si opera con la versión 'Notificación Juez' de Webservices y obtiene el rechazo de un comprobante; consulte el motivo del rechazo y, si corresponde a: "Código de Producto / Servicio es inválido. La longitud no puede ser mayor a 13 caracteres" o"El campo Código de Producto / Servicio es obligatorio dado que el ítem no es una seña o descuento", realice los siguientes pasos: 
    * Ingrese al proceso Artículos (del módulo Stock) y verifique el Código de Barras de cada uno de los artículos del comprobante rechazado. El código de barras es un dato obligatorio y su longitud no puede superar los 13 caracteres.
    * Ingrese al proceso [Administración de comprobantes electrónicos](https://ayudas.axoft.com/25ar/procesofacturacion_gv) (del módulo Ventas) y haga clic en el botón "Obtener CAE" .
  * Ante cualquier otro de caso de rechazo de un comprobante electrónico, comuníquese con el Departamento de Servicios.



Más información:

Tenga en cuenta que no es posible anular mediante el proceso [Anulación de comprobantes](?p=21138), un comprobante electrónico ya generado o bien, la numeración de un talonario que genere comprobantes electrónicos. Ante el rechazo de un comprobante electrónico, utilice la opción Eliminar rechazados de la barra de herramientas.

Eliminación de comprobantes electrónicos rechazados

La opción Eliminar rechazados de la barra de herramientas permite realizar la eliminación o borrado de los comprobantes electrónicos rechazados por AFIP.  
De esta manera, no se verá afectado el circuito de facturación electrónica.  
El sistema exhibirá en una nueva ventana, los comprobantes electrónicos con estado 'Rechazado', agrupados por Talonario.  
Por defecto, el sistema propone la eliminación de todos los comprobantes rechazados; pero es posible cambiar esta selección -por ejemplo, para elegir sólo el primer comprobante rechazado de un talonario.

__Nota

Tenga en cuenta que, si optó por eliminar sólo algunos comprobantes electrónicos rechazados, deberá verificar el próximo número a emitir del talonario asociado - previo a continuar con la facturación.

__Nota

Si el comprobante a eliminar tiene _cupones de POS integrado_ , el sistema avisará que genere un cupón de devolución. Para ello, sugerimos generar una nota de crédito (no electrónica) y sin referencia a una factura, para registrar la devolución del cupón original (de POS integrado). Luego de registrado este comprobante de ajuste, elimine la factura desde el _Administrador de comprobantes electrónicos_.

El sistema realizará, por cada comprobante seleccionado, las siguientes acciones:

  1. La anulación del comprobante seleccionado. Se aplican validaciones y controles similares a los del proceso [Anulación de comprobantes](?p=21138) (para la opción 'Comprobante generado').
  2. La eliminación o borrado del comprobante de las tablas del sistema.
  3. La actualización del Próximo número a emitir en el talonario del comprobante.



__Nota

El proceso puede demorar unos minutos dependiendo de la cantidad de comprobantes a eliminar y las tablas o archivos a actualizar.

Obtener CAEA

Desde esta opción puede obtener o consultar los datos CAEA para un período y quincena dado por AFIP, como también ingresarlo manualmente cuando no posea conexión a Internet.

Información de CAEA obtenido

CAEA: número de CAEA dado por AFIP que será utilizado para la autorización de los comprobantes electrónicos.

Fecha de solicitud: fecha en la cual se pidió CAEA para el período y quincena seleccionado.

Fecha desde y hasta vigencia: es el periodo en el cual el CAEA solicitado se puede utilizar para generar comprobantes.

Fecha tope para informar comprobantes: fecha hasta la cual se puede presentar los comprobantes autorizados con CAEA o los puntos de venta sin movimientos a AFIP ingresando a la solapa Informar CAEA.

##### Comprobantes observados

Si durante el proceso de autorización de comprobantes clase 'A', AFIP detecta inconsistencias en los datos del receptor, autorizará el comprobante electrónico asignándole un "CAE" junto con el detalle de las irregularidades encontradas.  
Ejemplos de situaciones posibles de observación: CUIT inválida del cliente receptor del comprobante electrónico; el receptor no se encuentra categorizado como Responsable Inscripto en el Impuesto al Valor Agregado, etc.  
Para conocer el detalle de las observaciones, pulse sobre la columna 'Observación AFIP' en la grilla de comprobantes autorizados.

El impuesto discriminado en tales comprobantes no podrá computarse como crédito fiscal del Impuesto al Valor Agregado.

Tenga en cuenta que el ejemplar impreso del comprobante electrónico debe incluir los códigos y leyendas de cada una de las observaciones de AFIP.  
Para ello, agregue las variables de reemplazo para comprobantes electrónicos: @OK para el código de la observación y @HK para su descripción en el diseño de sus comprobantes (archivos TYP).  
Contemple la posibilidad de imprimir más de una observación en un mismo comprobante.

Importante:

Las variables de reemplazo @Z1, @Z2, @Z3, @O1, @O2 y @O3 para la impresión de los códigos y leyendas de crédito fiscal no computable ya no son reconocidas por el sistema. Elimínelas de sus diseños de comprobantes.

##### Contenidos relacionados

  * [Guía de implementación sobre RG 5616/2024 - Emisión de comprobantes](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_rg5616_gv/)

  * [Video sobre Ley 27618 de monotributo](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/leymonotributo_gral_vid/)

  * [Video sobre facturación sin controlador fiscal](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/factsincf_gv_vid/)

  * [Video sobre regímenes de facturación](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/regfact_gral_vid/)

  * [Videos sobre emisión de comprobantes con CAEA](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/caea_gv_vid/)

  * [Videos sobre factura de crédito electrónica](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/fce_gral_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)
