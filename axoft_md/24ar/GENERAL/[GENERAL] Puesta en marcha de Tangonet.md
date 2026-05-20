# Puesta en marcha de Tangonet

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_transfer_reut/guias_gestioncentral_transf_reut/?p=12527/

## Contenido

# Puesta en marcha de Tangonet

Diseñamos esta guía para que pueda dejar operativa la aplicación Tangonet.

Explicaremos cómo poner en marcha el circuito y los pasos a seguir para adaptarlo a sus necesidades.

##### Puesta en marcha

Para la puesta en marcha de esta aplicación, debe loguearse en el sistema con un perfil de Tango que posea asociada una cuenta nexo válida, o bien loguearse directamente con las credenciales de su cuenta nexo asociada. Para más información consulte [Asociar usuario Tango a una cuenta nexo](?p=12560/#asociar-usuario-tango-a-una-cuenta-nexo).

Luego, ingrese, desde el menú de Tango al módulo Aplicaciones nexo y elija la opción "Tangonet".  
Se iniciará un asistente paso a paso, donde podrá configurar y adquirir la aplicación.

**Primer paso:** acepte los términos y condiciones de la aplicación.

**Segundo paso:** controle y confirme que los datos de configuración de la aplicación sean correctos.

Pulse en "Terminar" para finalizar con la adquisición y configuración de la aplicación.

##### Detalle del circuito

**Circuito operativo**

El esquema de funcionamiento de Tangonet, a modo de ejemplo, es el siguiente:

Una vez realizados los pasos definidos en la [Guía de puesta en marcha de Tangonet](?p=12527) usted tendrá funcionando las transferencias automáticas de información definidas bajo la lógica representada en el diagrama.

**Monitor de transferencias**

Para monitorear el estado y resultado de sus transferencias cuenta dos funcionalidades:

  * **Monitor de paquetes  
**Dentro de Tangonet, escoja el mosaico "Monitor de paquetes".  
El monitor de paquetes le permite tener una visión integradora del estado de sus transferencias, las cantidades de información transferida y, si lo desea, consultar el historial de ejecuciones de sus transferencias.
  * **Seguimiento de transferencias en Live  
**Para observar el resultado de la transferencia y obtener mayor detalle de la misma, en la empresa destino acceda a Procesos generales de Tango ingrese al proceso Auditoría, el mismo se encuentra en Consultas | Transferencia.



##### Preguntas frecuentes

¿Puedo modificar el número de sucursal de mi empresa en Tangonet?  
Es posible cambiar el número de sucursal de sus empresas en Tangonet. Para ello:

  1. Escoja el mosaico "Empresas".
  2. Escoja la empresa a la cual le desea modificar el número de sucursal.
  3. Pulse "Editar".


  * Si aún no vinculó la empresa, modifique el valor libremente y acepte los cambios.
  * Si ya se encuentra vinculada la empresa, deberá habilitar su edición activando la opción: Habilitar la edición de Número de sucursal y Número de llave.
  * Modifique el número de sucursal y acepte los cambios.



Tenga presente que al editar el número de sucursal de una empresa vinculada, la misma se desvinculará. Deberá realizar nuevamente el proceso de vinculación con la nueva parametrización. Para más información [haga clic aquí](?p=12427#vincempresa).

¿Cómo sé el número de sucursal de mi empresa en Tango?  
Si desconoce el número de sucursal de su empresa, inicie Tango y en las opciones del proceso Datos de la empresa (Procesos generales | Tablas generales | Empresa) verá el campo Número de sucursal indicado en el apartado Identificación de la sucursal para transferencia de datos.

¿Puedo modificar el número de sucursal de mi empresa en Tango?  
Sí, puede modificar el número de sucursal de su empresa de Tango, editando su valor desde el proceso Datos de la empresa. Lo puede ejecutar dirigiéndose a: Procesos generales | Tablas generales | Empresa.  
Modifique su valor dentro del apartado Identificación de la sucursal para transferencia de datos.  
La modificación del número de sucursal sólo es posible si la misma no se encuentra vinculada a Tangonet. En cuyo caso, debe desvincular la sucursal previamente antes de modificar su numeración.

__Nota

A partir de**Tango 18** , si ya contaba con movimientos utilizando ese número de sucursal, tendrá la posibilidad de “recodificar” su sucursal, editando el número de sucursal de su empresa por otro y convirtiendo sus movimientos para utilizar el nuevo número de sucursal.

¿Como sé si la información está llegando al destino?  
Puede controlar la información de dos maneras:

  * Monitoreando la transferencia.
  * Auditando la información presente en la consulta Live, dentro del sistema Tango de la empresa destino, ubicada en: Procesos generales | Consultas | Transferencia | Auditoría.



¿Cómo puedo saber si tengo empresas que aún no fueron vinculadas?  
Para saber si posee empresas que aún no fueron vinculadas, dentro de la aplicación Tangonet:

  1. Diríjase a "Empresas".
  2. Una vez dentro verá listadas sus empresas de Tangonet.
  3. Aquéllas que posean el estado 'Desvinculado' indican que aún no realizaron el [proceso de vinculación](?p=12427#vincempresa).



¿Tangonet es gratis?  
No, Tangonet es un servicio que tiene cargo mensual. Para más información contáctese con su Centro de Servicios Tango.

¿Cómo hago para comenzar a utilizarlo?  
Una vez adquirido, debe habilitar la aplicación desde Tango nexo (desde el menú principal del sistema).  
A continuación, siga los pasos detallados en la [puesta en marcha de Tangonet](?p=12527).  
Finalmente, vincule cada una de las sucursales Tango con cada empresa de Tangonet.

¿Cada cuánto tiempo se transfiere la información?  
La información se intenta transferir en ciclos. Estos ciclos se encuentran separados por un período de 30 segundos. Una vez se inicia el ciclo, si hay información para transferir o recibir, se demorará el tiempo que conlleve su procesamiento.

¿Qué información se puede transferir automáticamente?  
Hay 3 tipos de circuitos que se pueden automatizar:

  * Transferencia de tablas generales: este circuito le permite enviar información general (artículos, clientes, proveedores, precios, países, promociones comerciales, etc.).
  * Transferencia para informes y estadísticas: este circuito está orientado principalmente a consolidar en su casa central la información proveniente de todas las sucursales. De esta forma podrá obtener información consolidada para fines estadísticos y legales como ser: ventas de toda la cadena, ventas por sucursal, promoción comercial con mayor rédito en el mes, artículo más vendido, emisión consolidada del Libro IVA, RG3685, etc. Adicionalmente permite transferir información a todas las sucursales para asistirlas en su gestión diaria; por ejemplo, puede enviar a todas las sucursales el saldo de stock de cada artículo a fin de que los vendedores puedan orientar mejor a sus clientes.
  * Transferencia para gestión central: esta opción le permite transferir información para continuar el flujo de trabajo en otra sucursal o en la casa central. Por ejemplo, la sucursal genera la factura, pero determinados artículos son Remitidos desde la casa central. Otros ejemplos pueden ser la transferencia de mercadería entre dos sucursales (en una se registra el egreso y la otra el ingreso) o la rendición de caja a casa central.



¿Cómo se si el servicio está funcionado correctamente?  
Tangonet incluye un módulo semaforizado de monitoreo que le permite analizar el estado de las transferencias. Adicionalmente envía notificaciones al detectar anormalidades en las transferencias o problemas de conexión de alguna sucursal.

**¿Cómo puedo reemplazar el número de llave por un nombre de empresa?**

  1. Desde nexo, ingresar a Administración/Configuración.
  2. Se desplegará una grilla con el detalle de las aplicaciones disponibles y su correspondiente número de llave. El sistema asigna por defecto el número de llave al nombre de Empresa. Para editarlo, seleccione la fila de la aplicación Tangonet, que desee actualizar.
  3. Se mostrarán los botones con las acciones posibles. Presionando "Empresa", se accede a la pantalla de edición de esta.
  4. Realice los cambios en el campo Nombre y presione "Aceptar" para confirmarlos.



**¿Qué significa habilitar y deshabilitar empresas?  
**Usted cuenta con la facilidad de deshabilitar una empresa para dejar de transferir información desde y hacia la misma, sin necesidad de desvincularla o de modificar las definiciones de transferencias (tareas, rutas, etc.). De este modo, si vuelve a habilitarla, ésta retomará las transferencias que tuviera previamente definidas, utilizando las correspondientes rutas, sin tener que realizar ninguna reconfiguración.  
Seleccionando el mosaico Empresas podrá habilitarlas o deshabilitarlas, de manera individual o masiva, presionando los botones respectivos que se encuentran en la parte superior de la grilla. De igual modo, podrá realizar las mismas funciones, ingresando a una empresa en particular, presionando el botón "Editar" y marcando o desmarcando el campo Habilitada.  
En la grilla de empresas cuenta con la columna "Estado" que le permitirá monitorear las transiciones por las podrá pasar una empresa, en caso de operar con esta funcionalidad.  
Si usted deshabilita una empresa, la misma quedará en estado 'Deshabilitando' hasta que los procesos automáticos detecten este cambio y la pase al estado 'Deshabilitado'. A partir de este momento se interrumpen todas las transferencias que tuviera asociadas, por lo que no se generará información cuyo origen o destino sea una empresa deshabilitada. Si usted la habilita nuevamente, pasará a estado 'Habilitando' hasta que los procesos automáticos detecten este cambio y pase nuevamente al estado 'Operativo', momento en el cual comenzarán nuevamente transferencias desde y hacia esta empresa, ya que se mantendrán los datos de transferencias y rutas que tuviera previamente configurados.
