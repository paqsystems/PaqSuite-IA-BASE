# Guía de implementación de transferencias

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=11934/

## Contenido

# Guía de implementación de transferencias

Mediante el uso de los circuitos de transferencia puede enviar información entre las distintas sucursales y entre éstas y su casa central.

##### Circuitos disponibles

  * Transferencia de tablas generales: este circuito le permite enviar información general (artículos, clientes, proveedores, código de impuesto, precios e incluso tablas generales como tipos de comprobantes, países, promociones comerciales, etc.)
  * Transferencia para informes y estadísticas: este circuito está orientado principalmente a consolidar en su casa central la información proveniente de todas las sucursales. De esta forma podrá obtener información consolidada para fines estadísticos y legales como ser: ventas de toda la cadena, ventas por sucursal, promoción comercial con mayor rédito en el mes, artículo más vendido, emisión consolidada del Libro IVA, RG3685, etc. Adicionalmente permite transferir información a todas las sucursales para asistirlas en su gestión diaria; por ejemplo, puede enviar a todas las sucursales el saldo de stock de cada artículo a fin de que los vendedores puedan orientar mejor a sus clientes.
  * Transferencia para gestión central: esta opción le permite transferir información para que continúe el flujo de trabajo en otra sucursal o la casa central. Por ejemplo, la sucursal genera la factura, pero determinados artículos son remitidos desde la casa central. Otros ejemplos pueden ser la transferencia de mercadería entre dos sucursales (en una se registra el egreso y la otra el ingreso) o la rendición de caja a casa central.



**Introducción  
**Formas de transferir información:

  * Manual: en este caso la información se transfiere de una sucursal a otra sólo cuando una persona ejecuta el proceso de exportación en la sucursal origen y otra la importa en la sucursal destino. En este caso el archivo generado debe ser enviado por correo electrónico o en su defecto, utilizando algún FTP o un pendrive para trasladarla.
  * Automática: para automatizar la transferencia de información debe adquirir el servicio de Tangonet. En este caso la información viaja en forma transparente de una sucursal a otra sin intervención humana. Sólo se envían las novedades que se produjeron desde el último envío. Si uno de los sistemas no tiene conexión, acumula información hasta que esta se restablezca.
  * Semiautomática: esta opción es una combinación de las anteriores, en la que la exportación se realiza en forma manual, pero la transferencia y posterior importación se realiza automáticamente mediante Tangonet. Un posible ejemplo de aplicación es cuando la casa central define una nueva promoción comercial y quiere publicarla a toda la cadena.



**¿Cuándo necesita adquirir el módulo Central?  
**Debe adquirir el módulo Central para utilizar cualquier circuito salvo los siguientes:

  * Transferencia de tablas generales.
  * Importación de movimientos de stock.
  * Importación de saldos actuales.



**Recomendaciones**

Codificación: es requisito para el correcto funcionamiento de los circuitos de integración que la codificación de todas las entidades siga un criterio uniforme en toda la cadena.  
Si la entidad representa algo que tiene las mismas características en todas las sucursales, el código debe ser el mismo en cada una de ellas. Por ejemplo, el artículo "TVSOHDSM60" debe significar lo mismo en cada una de las sucursales. Este mismo criterio se extiende a las promociones, países, alícuotas y el resto de la información intercambiada que describe algo que debe verse igual en toda la cadena.  
Si, en cambio, la entidad representa algo que tiene características particulares en las distintas sucursales, como es el caso de depósitos, vendedores o compradores, la codificación debe ser específica y diferente en cada sucursal.  
Si requiere que los clientes y proveedores de cada sucursal sean independientes puede optar por usar una codificación específica en cada una de ellas. Para ello, ingrese a [Parámetros de Ventas](?p=19401), o [Parámetros de Compras](?p=14676) y complete un prefijo específico en cada sucursal. Por ejemplo, todos los clientes de la sucursal "Belgrano" comenzarán con el prefijo "01".

Pruebe el circuito manualmente: le sugerimos que antes de automatizar la transferencia de información utilizando pruebe el circuito completo en forma manual. De esta forma podrá verificar rápidamente que la información fluye sin inconvenientes, y podrá realizar los ajustes requeridos en caso de ser necesario antes de que fluya toda la información sin intervención de un operador.

##### Puesta en marcha básica

Defina todas las sucursales de la cadena: ingrese a [Tablas Generales | Empresas | Sucursales](?p=11989) dentro del módulo Procesos generales y defina todas las sucursales de su cadena.  
Es importante que la codificación de sucursales sea igual en todos los sistemas y en el administrador de [Tangonet](?p=12527).

Defina cuál es su sucursal: ingrese a [Tablas generales | Empresa | Datos de la empresa](?p=11851) dentro del módulo Procesos generales e indique la sucursal en la que está trabajando.

El resto de los datos necesarios para que funcione la transferencia de información es detallado en cada uno de los circuitos.

##### Asistentes de transferencias

A través de los asistentes es posible realizar transferencias de datos, pudiendo ser de transferencias de exportación o de importación.

**Asistentes de exportación  
**Todos los asistentes de exportación para transferencia de datos se encuentran estructurados de la misma forma, a continuación se detalla una sucesión de pantallas a modo de ejemplo:

  1. **Parametrización del archivo:** aquí generalmente se solicitan los parámetros de selección específicos del proceso.
  2. **Destino del archivo:** aquí se especifica el nombre del archivo generado comprimido (ZIP). Es posible enviar un duplicado del archivo generado mediante correo electrónico. También es posible proteger el archivo utilizando una contraseña, la misma le será requerida al momento de la importación.  
Al final de la pantalla, en la sección Comentarios es posible redactar un mensaje que será visualizado al momento de importar.
  3. **Generación del archivo:** desde esta pantalla se muestran los filtros definidos en toda la información seleccionada, el modo de exportación (manual o semiautomático) y la información sobre el archivo de exportación. Presione el botón "Terminar" para generar el archivo de exportación en primer plano, o "Procesar tarea" para poder cerrar la pestaña mientras se genera la exportación. En caso de que no existan datos para exportar, el sistema le mostrará el siguiente mensaje: "La exportación ha finalizado, no se encuentran datos para exportar".
  4. **Informe de exportación:** aquí se muestra un resumen de la cantidad de registros exportados por módulo y tarea.



__Nota

Si realiza transferencias semiautomáticas, el envío a las sucursales estará determinado por las sucursales que ha ido seleccionando en los pasos intermedios y en la posterior selección del modo seleccionando 'Tangonet'. Visualizando en el resumen el modo de envío y las sucursales donde se enviará la información.  


**Asistentes de importación  
**Todos los asistentes de importación para transferencia de datos se encuentran estructurados de la misma forma, a continuación se detalla una sucesión de pantallas a modo de ejemplo:

  * **Origen de los datos a importar:** aquí debe especificar la ruta para ubicar el archivo a importar. Adicionalmente, puede ingresar una contraseña.
  * **Confirmación de información:** aquí se detalla el nombre de la sucursal de origen, la fecha de exportación del archivo y a continuación la información correspondiente a la cantidad de registros exportados. También se visualizan aquellas notas que han sido redactadas al momento de exportar. Presione el botón "Terminar" para importar el archivo en primer plano o "Procesar tarea" para cerrar la pestaña y trabajar normalmente mientras se genera la importación.
  * **Informe de importación:** se muestra un resumen de la cantidad de registros exportados, ingresados, con errores y con advertencias. Al hacer clic sobre el campo "Detalle" visualizará la lista detallada de los errores y/ o advertencias.



##### 

##### Automatización de la transferencia de información (Tangonet)

Para automatizar la transferencia de información entre los distintos componentes de la cadena debe utilizar la aplicación [Tangonet](?p=12427). Para utilizar esta aplicación nexo debe haber adquirido previamente el módulo Central y estar abonado al servicio de transferencia.  
Para más información sobre cómo adquirir el módulo Central o abonarse al servicio de Tangonet consulte con su centro de Servicios Tango.

##### Preguntas frecuentes

**1) ¿Cómo puedo verificar el estado de mis exportaciones?**

  1. Acceda al portal de nexo con sus credenciales.
  2. Diríjase a la aplicación Tangonet.
  3. Seleccione el proceso Paquetes a pedido.
  4. Visualizará una planilla con el detalle de las exportaciones, pudiendo filtrar por fecha, estado o mostrar solo los registros que presentan problemas.



**2) ¿Qué permisos necesita el usuario para realizar la exportación?  
**El usuario que desee realizar el proceso de exportación deberá contar con el permiso de administrador o contar con acceso a Procesos generales | Transferencias | Exportaciones (si usted cuenta con una licencia válida, también podrá acceder desde: módulo Central | Transferencias | Exportación).  
Para gestionar usuarios, permisos y establecer roles, realice los siguientes pasos:

  1. Iniciar el menú web desde Tango Gestión.
  2. Diríjase al módulo Administrador.
  3. Seleccione Seguridad.



Para más información sobre la configuración de usuarios, roles y permisos acceda al siguiente [enlace](?p=29158).

**3) ¿Todas las transferencias manuales se pueden hacer de manera automática?  
**Todas las transferencias manuales no necesariamente tienen su contrapartida automática y viceversa.

**Por ejemplo:**  
La transferencia de comprobantes de tesorería para informes y estadísticas solo se pueden transferir de manera automática.  
La transferencia automática de cotizaciones de moneda solo se realiza de manera automática.  


**4) ¿Todas las transferencias se pueden llevar a cabo desde el módulo Central o desde el módulo de Procesos generales?  
**En el módulo Procesos generales, las tareas de importación son limitadas en comparación con las que posee el módulo Central, por lo que deberá tenerlo en cuenta al momento de enviar información entre las sucursales.

**5) ¿Cuándo es necesario adquirir el módulo Central?  
**Debe adquirir el módulo Central para utilizar cualquier circuito salvo los siguientes:

  * Procesos generales | Transferencias | Importación | Tablas generales
  * Procesos generales | Transferencias | Importación | Saldos actuales
  * Procesos generales | Transferencias | Importación | Movimientos de stock



**6) ¿Cómo hago para enviar una copia del archivo de una exportación manual por mail?  
**Realice los siguientes pasos:

  1. Ingrese a la opción de menú: Inicio | Ayudas | Ayudas sobre Procesos generales | Tablas generales | Parámetros de correo electrónico.
  2. Diríjase a la solapa: Transferencias.
  3. Realice la configuración siendo requerido el servidor SMTP, el usuario, remitente, y la clave si es que realiza la autenticación.
  4. Luego en cada transferencia manual podrá indicar mediante la selección de la opción “Envía duplicado por correo electrónico” el envío de una copia del archivo a la dirección de e-mail que deberá informar.



**7) ¿Cuántos modos o formas de transferencias existen?  
**Existen los siguientes modos de transferencias:

  1. **Manual** : en este caso la información se transfiere de una sucursal a otra sólo cuando una persona ejecuta el proceso de exportación en la sucursal origen y otra la importa en la sucursal destino. En este caso el archivo generado debe ser enviado por correo electrónico o en su defecto, utilizando algún FTP o un pendrive para trasladarla.
  2. **Automática** : para automatizar la transferencia de información debe adquirir el servicio Tangonet. En este caso la información viaja en forma transparente de una sucursal a otra sin intervención humana. Sólo se envían las novedades que se produjeron desde el último envío. Si uno de los sistemas no tiene conexión, acumula información hasta que esta se restablezca.
  3. **Semiautomática (Tangonet)** : esta opción es una combinación de las anteriores, en la que la exportación se realiza en forma manual, pero la transferencia y posterior importación se realiza automáticamente mediante Tangonet. Un posible ejemplo de aplicación es cuando la casa central define una nueva promoción comercial y quiere publicarla a toda la cadena.



**8) ¿Cómo selecciono las sucursales de envío cuando se hace la transferencia por el modo Tangonet - semiautomático?  
**Una vez que seleccione el modo de transferencia 'Tangonet', visualizará el seleccionador de sucursales para indicar a que sucursales desea enviar la información.  
En los procesos de transferencias donde es posible seleccionar una sucursal destino, al seleccionar el modo de transferencia 'Tangonet' el seleccionador de sucursales se completrá automáticamente con la sucursal destino seleccionada anteriormente y estará inhabilitada para su edición.

##### Contenido dependiente

  * [Transferencia de tablas](https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/guias_transftablas_reut/)
  * [Informes y estadísticas](https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/guias_informestadist_transf_reut/)
  * [Gestión central](https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/guias_gestioncentral_transf_reut/)
  * [Guía para Central: circuito de transferencias](https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/guias_carp_ct/)
  * [Guía para Central: implementación de maestro por sucursal](https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/guia_transfmaestros_reut/)



##### Contenidos relacionados

  * [Guía sobre stock entre sucursales](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiastockentresuc_gla/)

  * [Parámetros de transferencias de Procesos generales](https://ayudas.axoft.com/25ar/ayudas/gla/transferencias_carp_gla/paramtransfer_gla/)

  * [Transferencias entre depósitos](https://ayudas.axoft.com/25ar/ayudas/st/movimiento_carp_st/transferencdeposit_st/)

  * [Video sobre centralización cuentas corrientes de Compras](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/cccentral_gral_vid/)

  * [Video sobre parametrización contable centralizada](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralizaparamcontab_gral_vid/)

  * [Video sobre transferencia de cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralizacioncuentcorr_gral_vid/)

  * [Video sobre transferencia de maestros](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfmaestros_gral_vid/)

  * [Videos sobre administración de precios](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/adminprecios1_gral_vid/)

  * [Videos sobre centralización y transferencia de pedidos y remitos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralpedido_gral_vid/)

  * [Videos sobre transferencia de mercadería](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfstock_gral_vid/)

  * [Videos sobre transferencia de valores](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfvalor_gral_vid/)
