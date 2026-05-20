# Guía de Punto de Venta sobre precios

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_precio_gv2/

## Contenido

# Guía de Punto de Venta sobre precios

Esta guía está orientada al usuario que necesita operar con los precios de venta. A continuación, detallamos la puesta en marcha del circuito y describimos los pasos a seguir para implementar los circuitos que mejor se adapten a sus necesidades.

##### Puesta en marcha

Para definir las listas de precios de venta con los que trabaja su empresa ingrese al proceso [Listas de precios](https://ayudas.axoft.com/25ar/definiclistaprecio_gv2).  
Existen 4 consideraciones importantes en el momento de definir una lista de precios:

**¿En qué moneda está expresada?  
**Puede definir listas de precios en moneda local o extranjera. Dependiendo de la moneda del comprobante el sistema convertirá el precio de venta utilizando la cotización vigente. Una lista de precios en moneda extranjera puede facilitarle el mantenimiento de precios cuando sus artículos son importados.

Más información:

Denominamos moneda extranjera a aquella definida como tal en el proceso [Monedas](?p=11955). Esta moneda, junto con la corriente es la que permite obtener cualquier consulta o informe re-expresado a esas monedas.

**¿Incluye impuestos?  
** El sistema se encargará de incluir o excluir los impuestos al facturar teniendo en cuenta la categoría impositiva del cliente.

**¿Cuántos decimales necesita para definir sus precios?  
**Indique la cantidad de decimales que necesita para definir sus precios. Es independiente de la cantidad de decimales definida para los importes del módulo Ventas (por ejemplo; el precio total del renglón). En general, los artículos que se comercializan con unidades de medida pequeñas requieren mayor cantidad de decimales para no perder precisión durante la emisión de comprobantes.  
Tenga en cuenta que los controladores fiscales no soportan precios unitarios con más de 3 decimales.

**¿Es una lista independiente o depende de otra?  
**Tango le permite trabajar con listas independientes o con criterios de actualización de precios.  
Los criterios de actualización son aquellos que están compuestos, entre otras cosas, por una base de cálculo que es tomada como precio de referencia para la actualización de los precios de la lista principal a la que se asigne. Por ejemplo, la lista de precios "Venta mostrador" tiene asociado un criterio de actualización que posee una lista de precios "Precios de compra" más un 25% de recargo. De esta forma, cada vez que se actualice la lista de compras se actualizará la lista de ventas.  
Usted puede definir varios criterios de actualización y modalidades de actualización con diferentes fechas de actualización de la lista. Para más información consulte [Listas de precios](?p=19278).

**¿Políticas de redondeo, donde y para que se utiliza?  
**Las políticas de redondeo tienen su propio proceso de carga dentro del menú de Precios de venta. Esto le dará una gran flexibilidad para armar sus rangos de precios con métodos y direcciones de redondeo diferentes, permitiéndole aplicar máscaras acorde al valor del articulo y a sus necesidades.  
El armado de la política de redondeo es independiente a los demás procesos, sin embargo, puede ser usado por el proceso [Actualización global](?p=19180) y en la actualización automática de precios con el uso del planificador. Cabe aclarar que, para modificaciones de precios realizadas desde Excel, esto no se utiliza.

##### 

##### Detalle del circuito

La siguiente sección detalla las distintas opciones de actualización de precios, modificaciones durante la emisión de comprobante, auditoría, impresión e informes relacionados con el tema precios.

**¿Cómo puedo actualizar el precio de los artículos?  
**Una vez que definió las listas de precios con las que trabaja, ingrese los precios para cada artículo.  
Tenga en cuenta que debe ingresar los precios expresados en la unidad de medida de stock. Si al emitir un comprobante utiliza la presentación de ventas, el sistema multiplicará el precio unitario por equivalencia entre la unidad de medida de ventas y la de stock.

**Ejemplo:**

  * Unidad de medida de stock: Unidad
  * Unidad de medida de ventas: Caja
  * Equivalencia: 10
  * Precio unitario: 100$



Si vende 1 unidad de stock el total para ese artículo será de 100$.  
Si vende 1 unidad de ventas el total para ese artículo será de 1000$.

Usted dispone de las siguientes opciones para actualizar el precio de sus artículos:

  * [**Actualización individual por artículo**](?p=19181): esta opción está orientada a actualizar los precios de un artículo en particular, en cualquiera de sus listas de precio.
  * **[Actualización individual](?p=9753):** esta opción está orientada a actualizar el precio de un artículo para un lista de precios en particular. Además, al ingresar al proceso ofrece una vista rápida de los diferentes precios para cada uno de los artículos.
  * [**Actualización global**](?p=19180): utilice esta opción para actualizar en forma masiva el precio de sus artículos en base a distintos criterios. Puede resultarle de mayor utilidad cuando no necesita ver / trabajar con los precios actualizados. Por ejemplo, la actualización del 10% de toda la lista.
  * [**Administración de precios**](?p=19189): este proceso es el que le ofrece mayor flexibilidad en el momento de actualizar precios ya que permite: 
    * Actualizar un grupo de artículos en base a distintos criterios.
    * Actualizar un conjunto de listas en simultáneo.
    * Comparar precios entre listas.
    * Igualar precios según un artículo de referencia.
    * Visualizar rápidamente los precios modificados.
    * Exportar los precios a Excel para editarlos e importarlos nuevamente.
    * Actualizar los precios de una lista en base a otra y luego seguir editando.
  * [**Importación de precios desde Excel**](?p=19189/#importacion-de-precios-desde-excel): utilice esta opción cuando prefiera actualizar sus precios utilizando Excel.  
Utilice la opción Exportar precios dentro del [Administrador de precios](?p=19189) para exportarlos a Excel y luego impórtelos desde el mismo proceso una vez que los haya actualizados.  
Si su proveedor utiliza Tango puede importar directamente la lista que le haya enviado. Para más información consulte la sección [Listados de precios](?p=27438/#precios).
  * [**Definición de artículos**](?p=19178): esta opción le permite modificar el precio de un artículo desde la actualización de artículos. Para poder editar los precios debe estar habilitado el [parámetro](?p=19401/#parametros-para-articulos) Actualiza listas de precios desde el proceso Artículo y además el usuario debe tener acceso al proceso [Actualización individual por artículo](?p=19181).
  * [**Trabajar con criterio de actualización:**](?p=19278)se encuentran dentro del proceso Lista de precios. Están compuestos, entre otras cosas, por una base de cálculo que es de donde se toman los precios de referencia para la actualización de los precios de la lista principal a la que se asigne. Por ejemplo, la lista de precios "Venta mostrador" tiene asociado un criterio de actualización que posee una base de cálculo 'Precios de compra' más un 25% de recargo. De esta forma, cada vez que se actualice la lista de compras, se actualizará la lista de ventas.  
Este tipo de listas se pueden actualizar automáticamente en base a:



  * La frecuencia definida para el servicio de [Automatización de ventas](?p=9174) a la opción [Servicios](?p=9174) dentro del Administrador del sistema.
  * Una fecha y hora prestablecida, esta opción le permite programar la actualización de una lista de precios para una fecha y hora establecida.



Para más información de este tema consulte [aquí](?p=19278).

__Nota

Cualquiera sea el método de actualización de precios seleccionado debe indicar si desea actualizar el precio de los pedidos ya ingresados en base a los nuevos importes.  
_Tenga en cuenta las consideraciones explicadas dentro de cada método._

**¿Cómo puedo programar un cambio de precios?  
**Para programar un cambio de precios debe trabajar con criterios de actualización. Dentro del proceso de [Listas de precios](?p=19278) puede indicar la modalidad y la fecha y hora en la que se debe actualizar la lista de precios.  
Si lo que necesita es actualizar la misma lista, por ejemplo "Lista minorista", le recomendamos definir una lista borrador con el ajuste correspondiente (por ejemplo, un 10%) o con los ajustes que considere necesarios, utilizando cualquiera de las opciones enunciadas en el punto [¿Cómo puedo actualizar el precio de los artículos](?p=26572)? y luego programar la actualización de la "Lista minorista" en base al criterio de actualización configurado con la "Lista borrador".  
De esta forma puede dejar programado que, por ejemplo, el próximo Lunes 1° de Marzo a las 05:00 am se actualicen los precios de la "Lista minorista".  
Para más información de este tema consulte [aquí](?p=19278).

**Manejo de precios durante la emisión de comprobantes  
**La presente sección le detalla las distintas opciones relacionadas con el precio de los artículos en la emisión de comprobantes.

**¿Cómo evito que un vendedor modifique un precio?  
**Por defecto cualquier vendedor que emita comprobantes puede modificar el precio de un artículo. Para restringir el permiso a esta modificación debe configurar y asignarle un [perfil de facturación](?p=19415) al vendedor.  
A continuación le indicamos las principales restricciones que le puede aplicar mediante el uso de perfiles:

  * **Lista de precios:** puede impedir que el vendedor cambie la lista de precio o que lo haga solo con el permiso de un supervisor. También puede configurar el sistema para que al facturar proponga la lista de precios asignada al cliente, a la condición de venta o una específica para los usuarios asignados a ese perfil.
  * **Precio del artículo:** puede impedir que modifique el precio, que sólo lo aumente, sólo lo disminuya, sólo lo haga dentro de un determinado porcentaje o que únicamente lo pueda modificar previa autorización de un supervisor.
  * **Respeta precios de comprobantes de referencia:** esta opción le impide al vendedor, independientemente del permiso que tenga, alterar el precio cuando fue establecido por un comprobante de referencia, como por ejemplo un pedido.



Puede consultar otros aspectos relacionados con precios en el punto ¿Cómo puedo aplicar descuentos y promociones?.

**¿Cómo autorizo a un supervisor para que permita que un vendedor cambie momentáneamente un precio?  
**Para que un supervisor pueda autorizar el cambio debe tener asignado un perfil que le permita a él realizar esa modificación. Por ejemplo, para autorizar un cambio de precio él debe poder modificar un precio.  
Para que el vendedor pueda solicitar la autorización para modificar un precio, debe tener configurado en el perfil la opción 'Autoriza' en el campo Precio del artículo.

__Nota

Esta funcionalidad se aplica a otros ítems como descuento del cliente, del artículo, condición de venta, lista de precios y otros temas que afectan al total del comprobante.

Para más información consulte [aquí](?p=19233).

**¿Cómo consulto los precios durante la emisión de comprobantes?  
**A continuación detallamos las distintas opciones que ofrece el sistema para consultar el precio de un artículo.

  * En el campo de selección de artículos puede ingresar "?" y a continuación la identificación del artículo para visualizar el precio, saldo y las promociones disponibles para ese artículo. Desde aquí también puede acceder a la consulta de precios y saldos que se menciona más abajo.
  * En la grilla de resultado de la búsqueda de artículo puede pulsar la tecla <F11> \- Precio y stock para conocer el precio y saldo de stock de acuerdo a la lista de precios y depósito del comprobante. Si pulsa nuevamente la tecla la tecla <F11> \- Más accede a la consulta de precios y saldos que no solo le ofrece los precios en las distintas listas vigentes sino el saldo de stock en las distintas sucursales, incluyendo información geo-referencial para llegar a ese destino. Ingrese a [Perfiles para consulta de precios y saldos](?p=19411) para configurar la información que pueden ver sus vendedores.  
Para más información sobre este tema consulte [aquí](?p=18404).
  * Si requiere ingresar directamente a la consulta de precios y saldos pulse la tecla <P> desde el menú del [Facturador](?p=18393). Para más información sobre este tema consulte [aquí](?p=18397).



**¿Cómo puedo aplicar descuentos y promociones?  
**El sistema le ofrece distintas opciones para manejar descuentos y promociones.  
Descuentos clásicos: entre los descuentos que podemos denominar "clásicos" encontramos:

  * [Descuentos por cliente](?p=19444)
  * [Descuentos por artículo](https://ayudas.axoft.com/25ar/articulo_carp_st)
  * [Descuentos por cliente - artículo](?p=19178)
  * [Descuentos por medio de pago](?p=19302)



Dentro de los procesos [Parámetros de ventas](?p=19401) y [Perfiles de facturación](?p=19415) puede indicar qué prioridad debe aplicar el sistema cuando se superponen descuentos por cliente y los descuentos por artículo.

**Promociones comerciales**

El manejo de promociones comerciales es exclusivo del [Facturador](?p=18393). Entre otras opciones le permite aplicar promociones del tipo A+B, AxB, Descuento por monto, Descuento variable por cantidad, Precio especial además de los descuentos enunciados en el punto anterior.  
Estas promociones se aplican en forma automática sin la intervención del vendedor; puede transferirse o limitarse a determinadas sucursales y puede establecer si son acumulables entre sí.  
Para más información consulte [Definición de promociones](?p=18520/#definir-promocion) o mire este video.

**¿Cómo aplico una lista de precios a una fecha retroactiva?  
**Para aplicar precios vigentes a una fecha retroactiva debe habilitar esta acción en los perfiles de ingreso de comprobantes.  
Durante la emisión de comprobantes pulse la tecla <Alt + H> para ingresar la fecha de referencia que se debe utilizar para aplicar los precios. Puede indicar la fecha de referencia para todo el comprobante o para algún artículo en particular.

**Auditoría y evolución de precios**

Usted dispone de las siguientes consultas Live para conocer los cambios a precios:

  * **Historial de precios:** le permite obtener una lista de todos los cambios realizados a un determinado grupo de artículos para un rango de fechas y listas de precio determinado
  * **Precios vigentes a una fecha:** le ofrece la posibilidad de reconstruir una lista de precios a una fecha determinada
  * **Evolución de precios mensual:** esta consulta le permite analizar gráficamente la evolución de precios de un grupo de artículos
  * **Ficha del artículo:** dentro de la ficha de artículos puede conocer los precios actuales e históricos para el artículo que está analizando. Recuerde que puede acceder a la ficha del artículo desde cualquier consulta Live donde esté el campo artículo o directamente desde la opción Buscar fichas.



Adicionalmente, dispone de las siguientes consultas para conocer los cambios realizados durante la emisión de comprobantes por el vendedor y aquellos autorizados por un supervisor:

  * **Auditoría de precios:** este grupo de consultas Live le permite conocer los cambios de precios realizados durante la emisión de comprobantes (cotizaciones, pedidos, facturación) ya sea por un cambio manual del precio o por una modificación a la bonificación del renglón. Incluye los cambios autorizados por un supervisor.
  * **Auditoría de autorizaciones:** este informe está orientado específicamente para conocer las autorizaciones realizadas por los supervisores, entre otros motivos por cambios de precios.



**Listados de precios**

Usted dispone de las siguientes opciones para obtener listas de precios, ya se para uso interno o externo.

  * **Emisión de listas de precios:** este informe le permite generar un listado de precios con hasta 5 listas. Le permite imprimir la lista adicionando un porcentaje de aumento, este aumento únicamente se ve reflejado en la impresión.
  * **Precios por artículo:** esta consulta Live le permite generar un listado de precios para un grupo de artículos y listas de precio.
  * **Precios vigentes a una fecha:** esta consulta Live le permite reconstruir una lista de precios a una fecha determinada.
  * **Nexo clientes:** esta aplicación **nexo** le permite comunicar y poner a disposición de sus clientes información comercial y financiera incluyendo la posibilidad de consultar y descargar la lista de precios vigente. Para más información sobre este tema consulte aquí.
  * **Exportación a Excel:** cada una de las opciones anteriores ofrece una exportación a Excel para su posterior procesamiento.
  * **Integración entre sistemas Tango:** desde la exportación a xls del [Administrador de precios de venta](?p=19189) y desde [Tango Clientes](?p=12564) puede generar la lista de precios en el formato necesario para que su cliente la pueda importar desde el proceso [Administrador de precios de compra](?p=14600).



**Impresión de precios en comprobantes y etiquetas**

Para conocer las variables de reemplazo que debe utilizar en la definición de los formularios de impresión consulte la ayuda de [Modelos de impresión de comprobantes](?p=21557) y la del Buscador de [variables de reemplazo](?p=21557), ambas dentro de la ayuda del módulo Ventas. Dentro de la ayuda del buscador de variables puede consultar las variables de reemplazo ingresando el texto "Precio" en el encabezado de la columna "Descripción".  
Adicionalmente, Tango le permite imprimir el precio en las etiquetas para artículos. Puede optar por imprimir etiquetas en modo texto o etiquetas en modo gráfico utilizando impresoras dedicadas.

__Nota

Tenga en cuenta que para imprimir etiquetas gráficas debe utilizar impresoras de la marca **Zebra** (ZPL/EPL) o **Sato**.

Para más información sobre este punto consulte la ayuda del proceso [Formularios de stock](?p=11871) dentro del módulo Procesos generales y [Generación de etiquetas](?p=17038/#generacion-de-etiquetas) dentro del módulo Stock.

**Trabajando con sucursales**

Si su empresa trabaja con sucursales y tiene precios específicos para algunas de ellas, le recomendamos que lea la [Guía de implementación de transferencias](?p=11934).  
Una vez configurado el circuito, podrá especificar a qué sucursal o sucursales estarán asociadas cada lista de precios, facilitándose así la exportación de precios (y otra información) a cada sucursal.  
Para automatizar las transferencias entre sus sucursales, consulte [aquí](?p=12427).

##### Manejo de precios especiales

Esta sección explica el manejo de precios específicos para determinados clientes y otras consideraciones especiales de acuerdo al tipo de artículo como ser aquellos de tipo Kits, doble unidad de medida o con manejo de escalas.

**Precios por cliente**

Si requiere definir precios específicos para una parte de su cartera de clientes puede optar por:

  * Asociarle a cada cliente una lista de precios específica: esta opción es recomendable cuando la mayor parte de los precios son diferentes a los de la lista general de la empresa.
  * Definir precios específicos dentro de la lista general: sugerimos que utilice esta opción cuando el cliente solo tiene precios especiales para un grupo menor de artículos. De esta forma trabaja con una única lista general pero con algunos precios especiales para determinados clientes. Al imprimir o consultar la lista de precios se tiene en cuenta el cliente para mostrar los precios específicos.



Más información:

Si opta por trabajar con precios específicos dentro de una lista general consulte la ayuda de cada uno de los procesos mencionados en el capítulo [¿Cómo puedo actualizar el precio de los artículos?](?p=26572) para conocer cómo trabajar con esta modalidad.

**Precios de artículos con escala**

Denominamos artículos con escalas a los productos que poseen especializaciones o variantes. Esta modalidad de artículos se puede utilizar, por ejemplo, cuando se requiere administrar el stock de una prenda que se comercializa en diferentes talles y colores.  
Puede asignar un precio uniforme a todas las especializaciones o, por ejemplo, modificarlo para determinados talles, colores o una combinación de éstos.  
Para más información sobre este tipo de artículos consulte la [Guía de implementación sobre artículos con escala](?p=17101) en la ayuda del módulo Stock. Dentro de esa guía puede consultar también la sección dedicada a [listas de precios](?p=17101/#puesta-en-marcha) para este tipo de artículos.

**Precios de artículos tipo "kits"**

Denominamos "kit" a un grupo de dos o más artículos, que se venden en conjunto bajo una denominación común. Al facturarlo se utiliza el precio definido para el kit, y se descargan de stock sus componentes (no el kit propiamente dicho).  
El sistema le permite trabajar con kit fijos o variables. En el primer caso el cliente no puede elegir qué componente del kit quiere comprar sino que está previamente definido por la empresa. Por ejemplo el KIT SONY AV está compuesto por el TV SONY SMART 50” modelo SW87 más Home Theather SONY modelo HTR567.  
En el caso de trabajar con kits variables puede definir insumos opcionales que en caso de incluirlos pueden incrementar el precio total del kit; para eso el artículo debe formar parte de una categoría valorizada.  
Para más información sobre este tipo de artículos consulte la [Guía de implementación sobre kits](?p=27264) en la ayuda del módulo Ventas.  
El sistema le permite administrar artículos con doble unidad de medida de stock, una de ellas se utiliza para llevar el stock y la otra para valorizar las operaciones; por ejemplo hormas de queso que se venden por unidad pero cotizan por kilo.  
Tenga en cuenta que la unidad de medida que se utiliza para definir lo precios de venta es la que configure como unidad de medida 1.  
Para más información sobre este tipo de artículos consulte la [Guía de implementación sobre artículos con doble unidad](?p=17119) de medida en la ayuda del módulo Stock.

##### Contenidos relacionados

No se ha encontrado ninguno
