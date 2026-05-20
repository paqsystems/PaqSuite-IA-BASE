# Guía sobre promociones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promocion_gv/

## Contenido

# Guía sobre promociones

Esta guía le permite conocer los pasos a seguir para comenzar a utilizar promociones comerciales en su empresa, su impacto en los circuitos que siguen a continuación y los informes y consultas que ofrece **Tango**.

Las promociones comerciales son un mecanismo que ofrece incentivos a los consumidores para incrementar la venta de un producto o servicio.

Algunos ejemplos de estos incentivos son:

  * descuentos por medio de pago utilizado,
  * descuentos generales,
  * descuentos por cliente,
  * descuentos por tarjeta de beneficios,
  * descuentos que se aplican sobre artículos,
  * llevar dos productos al precio de uno,
  * obsequios por la compra de determinados artículos,
  * etc.



Tango Gestión cuenta con los siguientes tipos de promoción:

  * General (se aplican sobre el total del comprobante): 
    * Promociones de descuento general.
    * Descuento por cliente.
    * Descuento por medios de pago.
    * [Descuento por tarjeta de beneficios](?p=12493). (*)
    * [Descuento por monto](?p=12495). (*)
  * Por artículo: 
    * Descuento por artículo.
    * [AxB](?p=12486). (*)
    * [A+B](?p=12487). (*)
    * [Porcentaje variable por cantidad](?p=12489). (*)
    * [Porcentaje fijo de descuento](?p=12488). (*)
    * [Porcentaje variable en unidad](?p=12491). (*)
    * [Precio especial](?p=12494). (*)



(*) Este tipo de beneficio requiere de una licencia que habilite el uso de "Promociones" tal lo explicado en la sección de Consideraciones generales. Tenga en cuenta que la presente guía hace foco principalmente en este tipo de promociones.

#### Características generales de las promociones

**Las promociones se aplican a un grupo de artículos:** se entiende por "grupo" a una selección de artículos. Dicha selección puede corresponder a una condición en particular, por ejemplo, de un proveedor determinado, de un talle determinado, de un color determinado, de un rubro determinado, etc. También pueden seleccionarse artículos individualmente. O bien ser una combinación de ambas. Algunas promociones pueden manejar más de un grupo.

__Nota

Seleccionar grandes cantidades de artículos individualmente puede dificultar la creación y funcionamiento de una promoción; por lo tanto, si se requiere agrupar muchos artículos sin un criterio específico se recomienda utilizar el clasificador de artículos, el cual permite la definición libre de agrupaciones utilizando una estructura de árbol.  
Para más información consulte [Clasificador de artículos](?p=17054).  


**Las promociones del tipo "Por artículo" se pueden aplicar sobre cantidades enteras y según el subtipo también sobre cantidades decimales:**

  * Las promociones 'AxB', 'A+B', 'Porcentaje variable en unidad' solo se aplican sobre cantidades enteras y en caso de ingresar una cantidad con decimales se considera la parte entera para la aplicación de la promoción.
  * Las promociones 'Descuento por artículo', 'Porcentaje variable por cantidad', 'Porcentaje fijo de descuento' y 'Precio especial' se aplican sobre cantidades enteras y decimales.



**Las promociones tienen un período de aplicación:** este período está determinado por una fecha de inicio y una fecha de finalización. Tanto el inicio como la finalización tendrán como unidad mínima el día completo.

**Las promociones tienen día/s de vigencia:** dentro del período de aplicación, cada promoción tendrá definido días de vigencia. Por ejemplo, todos los días, todos los martes, etc. Los criterios tendrán como unidad mínima el día completo.

**Las promociones pueden tener un tope de aplicación:** el tope le permite establecer un límite de cantidad sobre las promociones de la empresa. Por ejemplo, "2x1 en bebidas hasta un tope de 1000 unidades". Puede limitar las unidades o la cantidad de promociones aplicadas. Para más información sobre este tema consulte la [guía sobre tope de promociones](?p=10154).

**Las promociones se aplican a sucursales:** las promociones son válidas en aquellas sucursales para las que se las habilitó.

**Definición de las promociones:** las promociones se definen en la empresa que tenga el módulo Ventas.  
Por ejemplo, en el caso de cadenas, las promociones se pueden definir en casa central y luego ser enviadas a las sucursales mediante Tangonet. En el caso de locales independientes, las promociones las puede definir la propia sucursal siempre que cuente con la licencia comercial para la definición de promociones.

**Los artículos pueden participar en más de una promoción a la vez:** un artículo puede aparecer en dos promociones al mismo tiempo. Para definir los criterios (prioridad) de aplicación ingrese a [¿Qué es una política de promociones?](?p=18520/#politica-de-promociones).

**Las promociones pueden acumularse con otras promociones:** en algunos casos, las promociones pueden acumularse. Para más detalle ingrese a [¿Qué es la política de promociones?](?p=18520/#politica-de-promociones).

#### Puesta en marcha

__Nota

Antes de comenzar la implementación de este tema le recomendamos consultar las Consideraciones generales para tener en cuenta para este circuito.  


  * **Defina la "Política de promociones" de su empresa:** tilde la opción Utilizar promociones, defina la prioridad que tendrá cada tipo de promoción y especifique qué debe hacer el sistema en caso de que un artículo forme parte de dos tipos de promociones con el mismo peso.  
Tenga en cuenta que dispone de un tutorial en este proceso para comprender mejor cómo se debe indicar la prioridad de cada promoción. De esta forma podrá indicar por ejemplo que si se aplica una "promoción por medio de pago" no de debe aplicar otras promociones o por el contrario que sea acumulable con otras.  
Si necesita definir una política distinta por cada sucursal debe hacerlo desde el Visor de promociones. También puede hacerlo desde Central | Archivos | Política de promociones por sucursal.  
Para utilizar las promociones "descuento por cliente", "por medio de pago", "descuento general" y "descuento por artículo" no es necesario habilitar ningún parámetro ya que está incluidas en la licencia básica de su sistema.  
Tenga en cuenta que el descuento por medio de pago se aplica siempre de acuerdo con lo definido en el proceso [Cuentas](?p=10235) de Tesorería. En cambio, la combinación o no del descuento por cliente y por artículo se resuelve en función a lo establecido por el parámetro Bonificación por cliente y artículo definido dentro de la solapa Ítems del cuerpo de [Perfiles de facturación](?p=19415).
  * **Ingrese al["Visor de promociones"](?p=19545)** para definir cada una de las promociones de su empresa. Tenga en cuenta que también puede definirlas ingresando en forma individual a cada uno de los procesos que se encuentra en Ventas | Archivos | Actualizaciones | Promociones.  
La principal ventaja del visor es que puede consultar todas las promociones en un único lugar, analizar aquellas que están por vencer, las finalizadas, inhabilitadas y las que se aplicarán en el futuro pudiendo consultar la información por sucursal. Tenga en cuenta que algunas de las promociones no se definen desde el Visor. En dichos casos detallaremos las instrucciones específicas para que pueda definirlas.  
Para obtener más información sobre las particularidades de cada tipo de promoción ingrese a los siguientes enlaces: 
    * Promociones generales (se aplican sobre el total del comprobante): 
      * Descuento general: al momento de emitir un comprobante puede indicar el porcentaje o importe a descontar en la opción Descuentos | Recargos que se encuentra dentro de la solapa Pagos del Facturador.
      * Descuento por cliente: ingrese al proceso [Clientes](?p=19444) e indique el porcentaje de bonificación que se le otorgue.
      * Descuento por medios de pago: defina las promociones relacionadas con tarjetas de crédito desde la opción [Promociones](?p=10267) del módulo Tesorería.
      * Descuento por [tarjeta de beneficios](?p=12493).
      * Descuento por [monto](?p=12495).
    * Por artículo: 
      * Descuento por artículo: ingrese al proceso [Artículos](?p=17035) e indique el porcentaje de bonificación que le corresponda.
      * [AxB](?p=12486).
      * [A+B](?p=12487).
      * [Porcentaje variable por cantidad](?p=12489).
      * [Porcentaje fijo de descuento](?p=12488).
      * [Porcentaje variable en unidad](?p=12491).
      * [Precio especial](?p=12494).
    * **Configure las[Preferencias](?p=18516) del Facturador:** adicionalmente a los dos parámetros que detallamos en la sección en la próxima sección relacionadas con la "adaptación de formularios" configure las siguientes opciones que se encuentran bajo la sección Comprobantes | Promociones: 
      * **Aplicar promociones al finalizar el ingreso de artículos:** tilde esta opción para calcular las promociones al salir de la solapa de artículo. Por defecto este parámetro se encuentra destildado haciendo que las promociones se calculen a medida que se ingresa cada artículo.
      * **Aplicar promociones al referenciar comprobantes:** tilde esta opción para calcular promociones al referenciar pedidos / remito.  
Tenga en cuenta que si no tiene tildado este parámetro no se respetarán las promociones calculadas en el pedido (en el caso de que las tenga).
  * **Adapte sus[Formularios](?p=11874)** para imprimir la información de promociones en sus comprobantes, de esta forma su cliente verá claramente los descuentos obtenidos.



Adaptación de formularios:

Detallamos a continuación las variables de reemplazo relacionadas con las facturas. Para obtener la lista de variables relacionadas con pedidos consulte la [Guía sobre pedidos con promociones](?p=40079).  
Utilice la variable de impresión **@TP** para imprimir el importe total de las promociones aplicadas en el comprobante como se muestra en el siguiente ejemplo.

En este ejemplo se muestran los precios de cada renglón ya ajustados por la aplicación de la promoción y al pie a la izquierda el resumen del total ahorrado por la aplicación de las promociones.  
Tenga en cuenta que adicionalmente al importe total de promociones puede detallar las aplicadas al comprobante. Estas se imprimirán a continuación del último artículo; de esta forma, su cliente podrá conocer el ahorro obtenido por cada una de las promociones conseguidas.  
Para imprimir esta información active el parámetro Imprimir promociones como ítems del comprobante dentro de la solapa [Comprobantes](?p=18386) en las Preferencias del Facturador.  
En el ejemplo que mostramos a continuación puede observar cómo se vería un comprobante con dos promociones aplicadas.

__Nota

El mismo ejemplo _Sin imprimir promociones como ítems del comprobante_ no las detallaría a continuación de los artículos, sino que imprimiría directamente el precio ya bonificado de cada uno de los artículos afectados por alguna promoción. En ese caso, le recomendamos utilizar la variable **@TP** para detallar al menos el total ahorrado debido a la aplicación de las promociones.  


Por otro lado, utilizando la opción Agrupar promociones al imprimir comprobante puede:

  * Imprimir las promociones aplicadas agrupadas en un solo ítem para cada código, en este caso muestra las dos promociones 2x1 aplicadas en un solo renglón.



  * Imprimir el detalle de cada una de las promociones aplicadas en forma independiente. En este caso muestra cada una de las promociones 2x1 en un renglón independiente.



Tenga en cuenta que estos ejemplos fueron realizados teniendo activo el parámetro _Imprimir promociones como ítems del comprobante_.  
De no haber estado activo ese parámetro se las promociones no se detallarían, sino que impactarían directamente sobre el precio de los artículos afectados.

Como complemento de esta guía le recomendamos consultar los siguientes videos:

  * [Promociones en pedidos](?p=27070).
  * [Promociones comerciales](?p=28810).



#### Detalle del circuito

##### Ingreso de Facturas

Las promociones se aplican en la generación de facturas y tickets en forma automática y según la [política de promoción](?p=18520/#politica-de-promociones) utilizada y las promociones definidas.  
En general no es necesario la intervención del operador salvo en determinados casos como:

  * Asignación de tarjeta de beneficios.
  * Incorporación del artículo de regalo en el caso de las promociones [A+B](?p=12487).
  * Ingreso de los medios de pago con los que abona el cliente.



Las promociones comerciales se detallan en la solapa homónima dentro del Facturador; en ella puede:

  * Consultar las promociones aplicadas en la factura,
  * Consultar las promociones del día,
  * Seleccionar la tarjeta de beneficio que utilizará el cliente,
  * Conocer las acciones pendientes que son necesarias para que se aplique una promoción; por ejemplo: 
    * Visualizar qué artículo se debe entregar para activar una promoción A+B (por ejemplo, dar un cinturón cuando se venden 3 jeans)
    * Saber qué medios de pago debe utilizar para que se aplique una promoción.



Más información:

Tenga en cuenta que esta solapa esta activa solo cuando haya promociones aplicadas o tarjetas de beneficio o acciones necesarias para aplicar una promoción.  


Las promociones aplicadas en la factura se verán como un ítem de bonificación al final del comprobante utilizando la leyenda indicada en cada una de las promociones dentro de la sección Datos para ticket.

##### Consideraciones para tener en cuenta al aplicar promociones

  * Las promociones se aplican en la generación facturas teniendo en cuenta la fecha que figura en el encabezado del comprobante.
  * No se incluirán en la aplicación de las promociones de artículos aquellos que: 
    * Se les haya modificado el precio, la bonificación o la unidad de medida del renglón.
    * Las devoluciones de artículos con códigos distintos a otros ingresados en la factura.
  * Las promociones se aplicarán al agregar los artículos al comprobante o bien al salir de la solapa Artículos, de acuerdo con lo configurado en las Preferencias del Facturador.



##### Consideraciones ante la aplicación de varias promociones

En un comprobante pueden aplicarse, en general, más de una promoción por artículo. Cuando un artículo participa en este tipo de promociones queda marcado y no puede ser usado en otra promoción por artículo en el mismo comprobante.  
Por ejemplo, supongamos que definió las siguientes promociones para los pantalones de jeans:

**Promo1 (por artículo):** 2×1 en jeans.  
**Promo2 (por artículo):** 15% de descuento en jeans blanco con tachas.

  * Si al comprobante agregó dos jeans azules, se aplicará la promoción 1.
  * Si vendió un jean blanco con tachas se aplica la promoción 2.
  * Si el comprobante incluye un jean azul y otro con tachas blanco, este último sólo puede participar de una de las dos promociones. De acuerdo con la [política de promociones](?p=18520/#politica-de-promociones) se aplicará una u otra.
  * Si en cambio facturó 1 jean común y 2 jeans blanco con tachas el sistema aplicaría las siguientes promociones: 
    * 1 promoción 2x1 en jean (el común + uno de los blancos con tacha) y otra por el 15% del jean blanco restante; suponiendo que la promoción AxB tiene más prioridad que la promoción por porcentaje de descuento fijo.
    * 1 descuento del 15 % en los dos jeans blanco con tacha; suponiendo que la promoción por porcentaje de descuento fijo tiene más prioridad que la promoción AXB.
    * En caso de que ambas promociones tengan la misma jerarquía el sistema aplicará las promociones de acuerdo con el orden en que se cargaron los artículos al comprobante.



Las promociones por artículo también pueden combinarse con las generales. Por ejemplo, si además de las promociones anteriores define otra que otorga un 10% abonando el comprobante con tarjeta de débito las promociones podrán acumularse siempre y cuando así lo defina en la [política de promociones](?p=18520/#politica-de-promociones).

**Otras consideraciones sobre la aplicación simultánea de promociones  
**Para determinar el importe mínimo, el sistema considera cada promoción individualmente. Si en el comprobante existen artículos para aplicar dos veces la misma promoción, ambas deben cumplir con las condiciones para su aplicación.  
Por ejemplo, al aplicar una promoción de porcentaje fijo de descuento donde se definió que aplica se aplica a partir de $100.000 y se agrega un artículo (que está definido dentro de la promoción) de $500.000 se aplicará la promoción. Luego, si se agrega otro artículo cuyo precio es $90.000 (que también está definido dentro de la promoción) no se la aplicará porque el artículo agregado no supera el importe mínimo establecido.  
Por otro lado, el tope de reintegro se distribuye entre todas las promociones aplicadas (del mismo código).  
Por ejemplo, al aplicar una promoción y utilizar un tope de $30.000, si la promoción es de 50% de descuento y el artículo tiene un precio de $40.000 en el comprobante, se realizará un descuento de $20.000.  
Luego, si se agrega un nuevo artículo y se aplica otra vez la misma promoción, el descuento de $20.000 será limitado a $10.000 ya que el tope máximo de reintegro de la promoción es de $30.000 ($20.000 otorgado al primer artículo y los $10.000 restantes al segundo).

##### Ejemplos de cómo se aplican las promociones

Detallamos a continuación algunos ejemplos de aplicación de cada promoción:

  * [AXB](?p=12486/#axb_ej1).
  * [A+B](?p=12487/#amasb_ej1).
  * [Porcentaje fijo](?p=12488/#promocionfijo_ej1).
  * [Porcentaje variable por cantidad](?p=12489/#promocioncant_ej1).
  * [Porcentaje variable en unidad](?p=12491/#promocionporcunid_ej1).
  * [Tarjetas de beneficios](?p=12493/#promociontarjbenf_ej1).
  * [Precio especial](?p=12494/#promocionprecioesp_ej1).
  * [Descuento por monto](?p=12495/#promociondescmonto_ej1).



**Promoción (por artículo) Descuento por artículo  
**Si bien técnicamente hablando el descuento por artículo no pertenece al módulo de promociones, el sistema lo trata como tal para que pueda participar dentro de la [política de promociones](?p=18520/#politica-de-promociones) como cualquier otra. De esta forma puede especificar qué prioridad darles a estos descuentos e indicar si se deben aplicar cuando existan otros beneficios.  
Este descuento se lo define en el proceso [Artículos](?p=17035).

__Nota

Tenga en cuenta que, a nivel pantalla, este descuento no se refleja descuento del renglón sino como un renglón de promoción especial para explicitar el beneficio a sus clientes. Internamente y en las consultas generales de venta sí observará el descuento aplicado en el mismo renglón que el artículo.  


__Nota

Si necesita trabajar con descuentos por artículo le recomendamos hacerlo con la promoción [Descuento por porcentaje fijo](?p=12488) ya que ofrece varias ventajas como por ejemplo asignación masiva, período de vigencia, días de aplicación, definición de topes, asignación por sucursal, etc.  


**Ejemplo: 15% descuento en jeans.  
**

**Artículo con descuento asignado en el proceso _Artículos_ :** jeans.  
**Descuento:** 15%

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Jean | $50.000 | $42.500  
Remera | $11.000 | $11.000  
Total antes de la promoción | $61.000 |   
Aplicación de la promoción  
(descuenta 15% en jean) | -$7.500 |   
**Total** | **$53.500** | **$53.500**  
  
Aplica un 15% de descuento en el jean tal cual lo definido en el proceso [Artículos](?p=17035).

##### Ingreso de pedidos

Para implementar este circuito le recomendamos seguir los pasos detallados en la [Guía sobre pedidos con promociones](?p=40079).

##### Consultas en Tango Live

Utilice las consultas de Tango Live para obtener información relacionada con el uso de promociones en facturación. Para el caso de pedidos consulte las detalladas en el punto anterior.

  * Ventas | Precios|Promociones
  * Ventas | Precios | Promociones por sucursal
  * Ventas | Facturación | Promociones facturadas por código de promoción
  * Ventas | Facturación | Promociones facturadas por tipo de promoción
  * Ventas | Facturación | Promociones facturadas por año / mes / día
  * Ventas | Facturación | Resumen por artículo con promociones
  * Central | Facturación | Promociones facturadas por código de promoción
  * Central | Facturación | Promociones facturadas por tipo de promoción
  * Central | Facturación | Promociones facturadas por año / mes / día
  * Central | Facturación | Resumen por artículo con promociones
  * Central | Transferencias | Auditoría de transferencia de promociones



#### Preguntas frecuentes

Consulte en esta sección las respuestas a las preguntas más frecuentes que puede tener sobre la aplicación de tope en las promociones comerciales de artículos.

**¿Cómo puedo conocer todas las promociones que están activas?  
**Si usted es la persona encargada de administrar las promociones le recomendamos utilizar el [Visor de promociones](?p=19545) desde donde puede consultar fácilmente todas las promociones de su empresa, pudiendo filtrar rápidamente aquellas activas, vencidas y las que están por vencer.  
Adicionalmente puede utilizar las siguientes consultas live filtrando las consultas por el campo Estado = 'Vigente':

  * Ventas | Precios | Promociones
  * Ventas | Precios | Promociones por sucursal



Si en cambio usted es un vendedor le recomendamos utilizar la opción Política de promociones desde el menú principal del Facturador. Las promociones aplicables en el día están resaltadas en color azul; haga clic sobre el título de cada una para acceder a las condiciones para su aplicación.

**¿Cómo puedo conocer todas las promociones que están por vencer?  
**Si usted es la persona encargada de administrar las promociones le recomendamos utilizar el [Visor de promociones](?p=19545) desde donde puede consultar fácilmente todas las promociones de su empresa, pudiendo filtrar rápidamente aquellas activas, vencidas y las que están por vencer.  
Adicionalmente puede utilizar las siguientes consultas live filtrando las consultas por el campo Estado = 'Por finalizar':

  * Ventas | Precios | Promociones
  * Ventas | Precios | Promociones por sucursal



__Nota

Tango considera que una promoción está "por vencer" cuando esté a menos de 5 días de su fecha de finalización o cuando su saldo disponible sea menor al 10% del tope establecido para la promoción.  


**¿Cómo defino, asigno y consulto la información relacionada con promociones cuando trabajo con sucursales?**

  * **Política de promociones x sucursal:** ingrese al proceso [Visor de promociones](?p=19545) y seleccione la opción Política de promociones por sucursal para definir las correspondientes a cada sucursal. De no indicar una específica, enviaremos a todas las sucursales la definida en el proceso [Política de promociones](?p=18520/#politica-de-promociones). Por ejemplo. puede definir una política de promociones específica para la costa atlántica durante la temporada de verano que sea completamente distinta a lo que rija en la ciudad de Buenos Aires.
  * **Asignación de promociones por sucursal:** al definir cada una de las promociones comerciales posiciónese en la solapa sucursales en indique para qué sucursales estará vigente la promoción. En el caso de trabajar con [topes](?p=10154) puede indicar la cantidad asignada a cada sucursal.
  * **Envío de información desde/hacia sucursales:** para enviar las promociones y la política asignada a cada sucursal utilice la opción Procesos generales | Transferencias | Exportación | Tablas generales y seleccione, dentro de la rama Ventas, la opciones Promociones y Política de promociones.  
Tenga en cuenta que esta es una exportación común a todas las sucursales, pero durante la importación Procesos generales | Transferencias | Importación| Tablas generales cada sucursal tomará solo la información específica para ella.
  * **Consulta de información por sucursal:** además del [Visor de promociones](?p=19545) puede utilizar las siguientes consultas **Live** : 
    * Ventas | Precios | Promociones por sucursal
    * Central | Facturación | Promociones facturadas por código de promoción
    * Central | Facturación | Promociones facturadas por tipo de promoción
    * Central | Facturación | Promociones facturadas por año / mes / día
    * Central | Facturación | Resumen por artículo con promociones
    * Central | Transferencias | Auditoría de transferencia de promociones



**¿Qué tipo de promociones maneja Tango?  
**Para obtener información sobre este aspecto le sugerimos consultar la sección del [Visor de promociones](?p=19545) dentro del capítulo de puesta en marcha donde encontrará cada una de las promociones con los que trabaja Tango en el enlace a cada una de ellas donde encontrará el detalla de cada uno junto con ejemplos de aplicación de cada una.

**¿Cómo puedo imprimir las promociones aplicadas en la factura?  
**Para configurar sus formularios de forma tal que detallen los beneficios obtenidos por el cliente en función de la aplicación de las promociones consulte la sección Adaptación de formularios dentro del capítulo de puesta en marcha.

**¿Qué sucede con las promociones si devuelvo un artículo en el mismo comprobante?  
**Las devoluciones registradas en el mismo comprobante se netean entre sí por lo que artículo saliente es considerado para la aplicación de promociones (la cantidad real es cero, ya que entra uno y sale uno), por ejemplo, cuando cambio un televisor por otra unidad de mismo debido a una falla. En cambio, si devuelve un televisor para llevarse uno de otra marca u otro producto ese nuevo artículo sí participara de las promociones vigentes.

**¿Cómo puedo conocer las promociones del día para un artículo específico?**  
Para conocer sus promociones ingrese el [modificador](?p=18475) "?" antes de escribir el código o descripción del artículo. De esta forma accederá a una ventana en la que puede consultar información adicional del artículo como ser precio, saldo, foto y las promociones en el que participa ese día.  
En el caso que realice una búsqueda parcial en que la búsqueda devuelva varios artículos (por ejemplo "Smart") haga doble clic sobre el artículo para consultar la información adicional y las promociones del día.

**¿Cómo puedo consultar las promociones que aplican en el día desde el Facturador?  
**Utilice la opción Política de promociones desde el menú principal del Facturador. Las promociones aplicables en el día están resaltadas en color azul; haga clic sobre el título de cada una para acceder a las condiciones para su aplicación.

**¿Puedo aplicar topes para una promoción?  
**Sí, puede definir tope para controlar la cantidad de unidades máximas que se pueden vender con la promoción (por ejemplo, 2x1 en gaseosas hasta un tope de 500 unidades) o limitar la cantidad máxima de promociones que se pueden aplicar.  
Para más información sobre este tema consulte la [Guía sobre tope de promociones](?p=10154).

**¿Puedo aplicar promociones desde el circuito de pedidos?  
**Sí, puede aplicar promociones desde el circuito de pedidos, esto es de especial utilidad en los comercios en los que el vendedor realiza toda la gestión comercial desde los pedidos siendo el Facturador utilizado por el cajero para realizar la cobranza y emitir la factura propiamente dicha.  
Para más información sobre este tema consulte la [Guía sobre pedidos con promociones](?p=40079).

**¿Puedo aplicar promociones desde el circuito de cotizaciones?  
**No, actualmente el circuito cotizaciones no contempla el cálculo y aplicación de promociones comerciales.  
Tenga en cuenta que al referenciar una cotización desde el [Ingreso de pedidos](?p=19344) puede pulsar el botón "Recalcular" (dentro del panel de promociones) para aplicarlas al comprobante.

**¿Un artículo puedo formar parte de más de una promoción?  
**La respuesta del caso en cuestión:

  * Si se trata de promociones generales (y no de artículos) la respuesta es un "Si" ya siempre se aplican sobre el comprobante en general y no sobre artículos en particular.
  * Si en cambio hablamos de promociones por artículo la respuesta es un "depende": 
    * Una "unidad" del artículo solo puede participar de una promoción de artículos a la vez, pero puede combinarse con otra de tipo de general.
    * Ahora bien, si tengo varias unidades de un mismo artículo, por ejemplo, 3 remeras cada una de ellas puede participar de una promoción distinta. Por ejemplo las dos primeras pueden participar en un AXB como ser "2x1 en jeans" y la tercera en un A+B del tipo "por cada jean te llevás un cinturón de regalo" si así lo establece la [política de promociones](?p=18520/#politica-de-promociones).



**¿Puedo trabajar con promociones, aunque no tenga contratado dicho módulo en mi sistema?  
**Sí, el módulo no es requerido para la aplicación de las promociones pero sí para su definición así como también para establecer la [política de promociones](?p=18520/#politica-de-promociones).  
En caso de trabajar en una cadena con sucursales solo es necesario que la casa central posea dicho módulo ya que será ella quien defina las promociones, establezca la política y luego transfiera a las sucursales toda la información para que sean aplicadas.

**¿Puedo impedir la aplicación de una promoción o eliminar una promoción aplicada?  
**No, el Facturador no permite que el vendedor decida si quiere aplicar una promoción, sino que las asigna en forma automática respetando lo definido por la [política de promociones](?p=18520/#politica-de-promociones) de su empresa.  
Sí puede alterar los medios de pago, artículos y otras condiciones que impactan sobre la aplicación de las promociones, pero una vez asignadas no puede eliminarlas.

**¿Cómo aplico promociones relacionadas con las tarjetas de beneficios durante la facturación?  
**Al acceder a la solapa Promociones se mostrarán las tarjetas de beneficios que tengan promociones vigentes para aplicar al comprobante detallando el descuento que recibirá el cliente en caso de utilizarla.  
Al seleccionar una tarjeta de beneficios, se abrirá una ventana para registrar los datos del cupón que respalde el uso de esta tarjeta. La emisión del cupón se realizará en forma integrada o no integrada con el dispositivo POS según la configuración de la tarjeta. Para más información sobre el uso integrado o no integrado con las terminales POS consulte esta [guía de implementación](?p=10586).  
Luego de completar esta información, oprima "Guardar" para aplicar la promoción al comprobante.

__Nota

Recuerde que las promociones de tarjetas de beneficios, como cualquier otra, se aplicarán según la prioridad establecida por la [Política de promociones](?p=18520/#politica-de-promociones) configurada.  


Luego de haber agregado la tarjeta de beneficios, al avanzar a la solapa Pagos observará el subtotal de la factura y el descuento aplicado por la promoción.  
Para eliminar la aplicación de esta promoción posiciónese sobre la misma y oprima el botón "Anular promoción". Tenga en cuenta que si trabaja con la modalidad POS integrado debe volver a pasar la tarjeta de beneficio por el dispositivo para anular el cupón previamente generado.

#### Consideraciones generales

Tenga en cuenta que la definición y actualización de promociones, así como la definición de sus topes, requiere tener incluido en su licencia el uso de éstas. Esa licencia no es necesaria para utilizarlas desde el Ingreso de pedidos o desde el Facturador. Para más información consulte con su representante comercial.

**Procesos del circuito de ventas que trabajan con promociones**

  * Facturador (Facturas)
  * Pedidos



**Procesos del circuito de ventas que no trabajan con promociones**

  * Pedidos automáticos (Ventas | Pedidos | Pedidos automáticos).
  * Notas de débito.
  * Notas de crédito.
  * Facturación masiva de pedidos (Ventas | Facturación | Facturación de pedidos) (*)
  * Pedidos originados en alguno de estos circuitos: 
    * Cotizaciones.
    * Tango Tiendas.
    * XTango.



(*) Tenga en cuenta que a partir de la versión **Delta 3** incorporamos una nueva opción para realizar la facturación masiva de pedidos. Para ello, ingrese a _Facturador | Facturación masiva | Pedidos manuales_. Esta opción sí contempla la facturación masiva de pedidos con promociones para el caso de pedidos con condición de venta "cuenta corriente".

##### Contenidos relacionados

  * [Guía sobre pedidos con promociones](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promociones_gv/)

  * [Guía sobre tope de promociones](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_topepromocion_gv/)

  * [Política de promociones](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/politicapromocion_gv/)

  * [Promociones](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/)

  * [Video sobre novedades en promociones](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/novedpromocion_gv_vid/)

  * [Video sobre promociones de venta](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/promociones_gv_vid/)

  * [Videos sobre promociones comerciales](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/promocomercial_gral_vid/)

  * [Videos sobre promociones en pedidos](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/pedidoautom_gv_vid/)

  * [Visor de promociones](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/visorpromocion_carp_gv/)
