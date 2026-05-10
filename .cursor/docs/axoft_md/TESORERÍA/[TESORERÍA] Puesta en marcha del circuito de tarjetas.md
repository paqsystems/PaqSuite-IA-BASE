# Puesta en marcha del circuito de tarjetas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/guia_pm_tajcredeb_sb/

## Contenido

# Puesta en marcha del circuito de tarjetas

Consulte en este capítulo los pasos a seguir para implementar el circuito de tarjetas de crédito y débito.

A continuación se muestra un breve resumen de la configuración a realizar:

**Tema a implementar** | **Modalidad de trabajo**  
---|---  
**POS integrado** | **POS no integrado** | **Ingreso manual**  
**Configuración básica** | ¿Cómo configurar la modalidad POS integrado?  
\- En LaPos  
\- En Posnet  
\- En Payway | ¿Cómo configurar la modalidad POS no integrado? | ¿Cómo configurar la modalidad Ingreso manual?  
**Conceptos de gastos** | ¿Cómo configurar los conceptos de gastos?  
**Descuentos, recargos y promociones** | ¿Cómo configurar los descuentos, recargos financieros y promociones?  
**Movimientos de Tesorería** | ¿Cómo configurar los movimientos automáticos de Tesorería?  
  
__Nota

Tenga en cuenta que en cada uno de los puntos se mencionan sólo los campos más relevantes. Para un conocimiento más profundo del tema le recomendamos leer la ayuda del respectivo proceso.

##### Configurar la modalidad POS integrado en LaPos

**Consideraciones previas  
**Para operar en forma integrada con una terminal POS, debe tener en cuenta las siguientes consideraciones:

  * Contrate el servicio de LaPos (el servicio de validación de tarjetas VISA, que además permite operar con todas las tarjetas de crédito y débito). Para más información sobre este servicio consulte [www.lapos.com.ar.](http:www.lapos.com.ar)
  * Comunique a LaPos que desea trabajar en forma integrada con Tango, para que le suministren una terminal POS preparada para trabajar conectada a una computadora a través de un cable USB. Las terminales POS habilitadas son Ingénico (modelos I5100 y AQ50) y Verifone (modelos Vx510 y Vx520).  
Recomendamos trabajar con equipos de la misma marca en todo su comercio, ya que de esta forma se facilita la implementación del circuito. Tenga en cuenta que cada marca puede utilizar diferentes códigos de host, tarjetas y planes por lo que se verá obligado a efectuar una parametrización específica dependiendo de la marca de cada terminal POS.
  * Verifique que la computadora que se utilizará para trabajar en modo integrado, posea un puerto USB libre.



Cuando la Terminal POS esté operando en modo integrado, sólo podrá realizar operaciones desde el sistema Tango. No podrá utilizarla manualmente indicando las operaciones desde el menú de su Terminal POS. Con esta configuración las operaciones de Venta, Anulación, Devolución y Cierre de lote debe efectuarlas desde Tango. En caso que se verifiquen inconvenientes técnicos que le impida realizar esas operaciones del sistema, le recomendamos leer el punto [¿Cómo trabajar si la terminal POS no funciona correctamente?](?p=10559/#%c2%bfcomo-trabajar-si-la-terminal-pos-no-funciona-correctamente).

**Configuración**

  * Configuración del equipo suministrado por LaPos: en el menú de la terminal POS seleccione la opción Más (o Menú según el equipo utilizado), luego Funciones y configure la opción Pos Integrado con el valor 'Si'.
  * [Parámetros de Tesorería](?p=10293): ingrese a este proceso y haga clic en la solapa Administración de tarjetas; a continuación complete los siguientes campos: 
    * Modo de emisión de cupones: "Con POS integrado".
    * En el sector inferior de la pantalla (Datos para uso de POS de tarjetas integrado) indique el puerto COM al que se encuentra conectado el equipo y la versión interna que éste utiliza (visible al encender la terminal POS). Tenga en cuenta que esta información debe ingresarla directamente en la computadora que tiene conectada la terminal POS ya que este dato se graba en un archivo local del equipo.  
Si usted opera con varias terminales POS, es necesario que ingrese a este proceso desde cada una de las computadoras que tengan conectada una terminal POS, e indique en cada caso el puerto COM correspondiente.
  * [Planes](?p=10265): ingrese a esta opción para registrar los planes de tarjeta con los que trabaja su comercio. Si bien esta información es provista por las administradoras de tarjetas, habitualmente se trabaja con al menos dos planes, uno denominado 'Un pago' y otro llamado 'Plan cuotas'. La cantidad de cuotas correspondiente a cada plan debe ser ingresada en el siguiente punto.
  * [Tarjetas (primera etapa)](?p=10263): acceda a este proceso para crear cada una de las tarjetas con las que trabaja su comercio. Durante la puesta en marcha inicial, la creación de tarjetas se debe realizar en dos etapas, en la primera se completan los datos básicos de cada tarjeta mientras que en la segunda se completan datos relacionados con los planes de la tarjeta. Esta última etapa sólo puede realizarse con posterioridad a la creación de las terminales POS.  
Durante la primera etapa no tilde la opción Utiliza conexión con terminal POS y solo complete el tipo de Numeración para cupones manuales y la Hora de cierre de lote. Estos datos son necesarios en caso que deba emitir cupones manuales o efectuar un cierre de lote en modo Pos no integrado, debido a inconvenientes técnicos de la terminal POS. Puede optar entre una numeración manual o automática.
  * [Terminales POS](?p=10269): utilice este proceso para definir cada una de las terminales POS con las que trabaja su comercio. Verifique que la terminal POS esté encendida y conectada a la computadora y pulse el botón "Importar datos del POS" para obtener el código de terminal y los códigos de host, plan y tarjeta que utiliza la terminal POS.  
Le recomendamos que no modifique el código de terminal POS (asignado automáticamente al leer los datos del POS) ya que dicha información es utilizada por el sistema para conectarse al equipo.  
Después de haber importado los datos del POS, complete automáticamente la grilla Host a los que se conecta (en la solapa Principal).  
También se completa automáticamente la grilla Tarjetas habilitadas (en la solapa homónima). Para finalizar este proceso, haga clic en la solapa Tarjetas habilitadas y asigne a cada una de las tarjetas existentes en el POS el código de tarjeta que usted utiliza en Tango. Esta relación entre los códigos de Tango y los del POS, es indispensable para que Tango**.** pueda interactuar con la terminal POS.  
Sólo es necesario que utilice nuevamente el botón "Importar datos del POS" cuando se hayan configurado nuevas tarjetas, planes o host en su terminal POS. Esa configuración es realizada por un técnico de la empresa proveedora de la terminal POS.  
Si posee varias terminales POS debe crearlas desde cada una de las computadoras a las que están conectadas o de lo contrario, conectar en forma secuencial cada uno de los equipos a la computadora donde esté creando las terminales POS.
  * [Tarjetas (segunda etapa)](?p=10263): una vez importados los datos de la terminal POS puede completar la información relacionada a cada tarjeta. Tilde la opción Utiliza conexión con terminal POS y siga los pasos enunciados a continuación: 
    * Haga clic sobre la solapa Datos para la venta y complete la sección Definición de planes para la venta que se encuentra en el sector inferior de la pantalla. En esta sección relacione cada uno de los planes definidos en la terminal POS (importados en el punto anterior) con los códigos de [plan](?p=10265) definidos en Tango. Para una configuración básica debe completar la cantidad mínima y máxima de cuotas del plan.
    * Haga clic sobre la solapa Datos para el comercio y complete la sección Períodos y descuentos para la acreditación que se encuentra en el sector inferior de la pantalla. En esta sección debe completar el tipo de acreditación del cupón (única o por cuotas), el tipo de período (horas, días hábiles, días corridos, etc.) y el período de acreditación. Habitualmente las ventas en cuotas se abonan a las 48 horas del [cierre de lote](?p=10149) y las ventas en un pago se acreditan a los 20 días corridos siendo acreditado el dinero en un solo pago (tipo de acreditación única).
  * [Cuentas de Tesorería](?p=10235): una vez que ha definido las tarjetas con las que trabaja, debe asignarles una cuenta de tesorería. Para ello ingrese a este proceso y defina una cuenta para cada tarjeta existente; para cada cuenta tilde la opción 'Tarjeta' en la sección Tipo de cuenta dentro de la solapa Principal y a continuación ingrese a la solapa Tarjeta para asignar el código de tarjeta que representa y los planes que estarán habilitados para la cuenta que está definiendo. Si bien puede definir varias cuentas que representen los distintos planes de la tarjeta recomendamos trabajar con una única cuenta por tarjeta. Un plan de una tarjeta no puede estar asociado a más de una cuenta.
  * [Host](?p=10271): los valores de ese proceso se crearon automáticamente al importar los datos desde la terminal POS. Habitualmente las terminales POS trabajan con cuatro host: Visa, Diners, Posnet y American Express.



Recuerde que los pasos arriba enunciados forman parte de la configuración básica del circuito de tarjetas.

##### Configurar la modalidad POS integrado en Posnet

**Consideraciones previas  
**Para operar en forma integrada con una terminal POS, debe tener en cuenta las siguientes consideraciones:

  * Contrate el servicio de Posnet (que permite operar con todas las tarjetas de crédito y débito). Para más información sobre este servicio consulte [www.posnet.com.ar](http:www.posnet.com.ar).
  * Comunique a Posnet que desea trabajar en forma integrada con Tango, para que le suministren una terminal POS preparada para trabajar conectada a una computadora.
  * Verifique que la computadora que se utilizará para trabajar en modo integrado con el dispositivo Posnet, posea un puerto USB libre.



Importante:

Para los dispositivos Posnet se debe configurar, en el equipo, la aplicación "TRANSACT - TRANSACT" para que pueda comunicarse con la computadora. Esta configuración la realiza el personal de Posnet.

__Nota

Recomendamos trabajar con equipos de la misma marca en todo su comercio, ya que de esta forma se facilita la implementación del circuito. Tenga en cuenta que cada marca puede utilizar diferentes códigos de host, tarjetas y planes por lo que se verá obligado a efectuar una parametrización específica dependiendo de la marca de cada terminal POS.

**Configuración del equipo suministrado por Posnet**

  * [Parámetros de Tesorería](?p=10293): ingrese a este proceso y haga clic en la solapa Administración de tarjetas; a continuación complete los siguientes campos: 
    * Modo de emisión de cupones: "Con POS integrado".
    * En el sector inferior de la pantalla (Datos para uso de POS de tarjetas integrado) indique el puerto COM al que se encuentra conectado el equipo. Tenga en cuenta que esta información debe ingresarla directamente en la computadora que tiene conectada la terminal Posnet ya que este dato se graba en un archivo local del equipo.
  * [Planes:](?p=10265) ingrese a esta opción para registrar los planes de tarjeta con los que trabaja su comercio. Si bien esta información es provista por las administradoras de tarjetas, habitualmente se trabaja con al menos dos planes, uno denominado 'Un pago' y otro llamado 'Plan cuotas'. La cantidad de cuotas correspondiente a cada plan debe ser ingresada en el siguiente punto.  
Si usted opera con varias terminales POS, es necesario que ingrese a este proceso desde cada una de las computadoras que tengan conectada una terminal POS, e indique en cada caso el puerto COM correspondiente.
  * [Tarjetas (primera etapa)](?p=10263): acceda a este proceso para crear cada una de las tarjetas con las que trabaja su comercio. Durante la puesta en marcha inicial, la creación de tarjetas se debe realizar en dos etapas, en la primera se completan los datos básicos de cada tarjeta mientras que en la segunda se completan datos relacionados con los planes de la tarjeta. Esta última etapa sólo puede realizarse con posterioridad a la creación de las terminales POS.  
Durante la primera etapa no tilde la opción Utiliza conexión con terminal POS y solo complete el tipo de Numeración para cupones manuales y la Hora de cierre de lote. Estos datos son necesarios en caso que deba emitir cupones manuales o efectuar un cierre de lote en modo Pos no integrado, debido a inconvenientes técnicos de la terminal POS. Puede optar entre una numeración manual o automática.
  * [Terminales POS](?p=10269): utilice este proceso para definir cada una de las terminales Posnet con las que trabaja su comercio. Verifique que la terminal esté encendida y conectada a la computadora. Para definir las terminales, seleccione en la solapa principal la opción "Posnet" y a continuación, para obtener los datos del dispositivo, pulse el botón "Importar datos del POS".  
Le recomendamos que no modifique el código de terminal POS (asignado automáticamente al leer los datos del POS) ya que dicha información es utilizada por el sistema para conectarse al equipo.  
Después de haber importado los datos del POS, complete la grilla Host a los que se conecta. Estos host no se obtienen automáticamente y los debe ingresar el usuario en forma manual en el proceso Terminales POS.  
En la solapa Tarjetas habilitadas debe agregar en la grilla los datos de las Tarjetas, los Host, Moneda. Tilde la casilla Habilitado.  
Para más información consulte Host.  
Si posee varias terminales POS debe hacer este procedimiento desde cada una de las computadoras a las que están conectadas. De lo contrario, conecte en forma secuencial cada uno de los equipos a la computadora donde esté creando las terminales **Posnet**.  
Configure la terminal para que permita pagos QR en la sección [Principal](?p=10269/#principal) de Terminales POS de Tesorería. Tenga en cuenta que, antes de realizar la configuración, debe verificar que la terminal esté actualizada para operar con pagos QR. Para ello valide que tenga la opción PAGOS QR desde el menú de la terminal. Si ingresa por primera vez a esta opción de manera no integrada, el dispositivo le solicitará habilitar el servicio. En caso de no tener disponible la opción PAGOS QR desde el menú de la terminal, comuníquese con su representante de Posnet para solicitarle la actualización de la terminal correspondiente. Para más información acerca de la configuración de pagos QR consulte la [Puesta en marcha de pagos QR con Posnet](?p=17126).
  * [Tarjetas (segunda etapa)](?p=10263): una vez importados los datos de la terminal Posnet puede completar la información relacionada con cada tarjeta. Tilde la opción Utiliza conexión con terminal POS y siga los pasos enunciados a continuación: 
    * Haga clic sobre la solapa Datos para la venta y complete la sección Definición de planes para la venta que se encuentra en el sector inferior de la pantalla. En esta sección relacione cada uno de los planes definidos en la terminal POS (importados en el punto anterior) con los códigos de [plan](?p=10265) definidos en Tango. Para una configuración básica debe completar la cantidad mínima y máxima de cuotas del plan.
    * Haga clic sobre la solapa Datos para el comercio y complete la sección Períodos y descuentos para la acreditación que se encuentra en el sector inferior de la pantalla. En esta sección debe completar el tipo de acreditación del cupón (única o por cuotas), el tipo de período (horas, días hábiles, días corridos, etc.) y el período de acreditación. Habitualmente las ventas en cuotas se abonan a las 48 horas del [cierre de lote](?p=10149) y las ventas en un pago se acreditan a los 20 días corridos siendo acreditado el dinero en un solo pago (tipo de acreditación única).
  * [Cuentas de Tesorería](?p=10235): una vez que ha definido las tarjetas con las que trabaja, debe asignarles una cuenta de tesorería. Para ello ingrese a este proceso y defina una cuenta para cada tarjeta existente; para cada cuenta tilde la opción 'Tarjeta' en la sección Tipo de cuenta dentro de la solapa Principal, y a continuación ingrese a la solapa Tarjeta para asignar el código de tarjeta que representa y los planes que estarán habilitados para la cuenta que está definiendo.  
Si bien puede definir varias cuentas que representen los distintos planes de la tarjeta, recomendamos trabajar con una única cuenta por tarjeta. Un plan de una tarjeta no puede estar asociado a más de una cuenta.
  * [Host](?p=10271): los estos valores los debe completar de la siguiente manera:[](https://ayudas.axoft.com/wp-content/uploads/2020/06/clipsb01331.gif)
    * Imprima la consulta de configuración desde el dispositivo Postnet, ingresando a Menú | Funciones | Imp. Configuración.
    * Una vez impresa la consulta de configuración del dispositivo, el ticket indicará los Host y las Monedas que se utilizarán (además de otra información).
    * A continuación acceda al menú de Host de tarjetas del módulo Tesorería.
    * Agregue un host.



Importante:

La descripción del Host debe coincidir con alguno de los que muestra el ticket emitido por el dispositivo Posnet (en la consulta de configuración del dispositivo).

Recuerde que los pasos arriba enunciados forman parte de la configuración básica del circuito de tarjetas.

##### Configurar la modalidad POS integrado en Payway

**Consideraciones previas  
**Para operar en forma integrada con una terminal POS, debe tener en cuenta las siguientes consideraciones:

  * Contrate el servicio de Payway (el servicio de validación de tarjetas VISA, que además permite operar con todas las tarjetas de crédito y débito). Para más información sobre este servicio consulte [www.payway.com.ar](https://www.payway.com.ar/).
  * Comunique a Payway que desea trabajar en forma integrada con Tango, para que le suministren el permiso de acceso al integrador. Tenga en cuenta que, por limitación de Payway, no es posible operar de manera integrada y no integrada con la misma terminal.
  * Payway comercializa el modelo Smart (Newland N910) para operar de manera integrada.
  * Por limitación de Payway, no podrá hacer devoluciones de pagos no referenciados realizados con QR (tarjetas de crédito o débito y transferencias inmediatas (PCT)). Tampoco podrá hacer anulaciones de pagos referenciados realizados con transferencias inmediatas (PCT).



__Nota

Recomendamos trabajar con equipos de la misma marca en todo su comercio, ya que de esta forma se facilita la implementación del circuito. Tenga en cuenta que cada marca puede utilizar diferentes códigos de host, tarjetas y planes por lo que se verá obligado a efectuar una parametrización específica dependiendo de la marca de cada terminal POS.  


Cuando la terminal POS esté operando en modo integrado, sólo podrá realizar operaciones desde el sistema Tango. No podrá utilizarla manualmente indicando las operaciones desde el menú de su terminal POS. Con esta configuración las operaciones de Venta, Anulación, Devolución y Cierre de lote debe efectuarlas desde Tango. En caso que se verifiquen inconvenientes técnicos que le impida realizar esas operaciones del sistema, le recomendamos leer el punto [¿Cómo trabajar si la terminal POS no funciona correctamente?](?p=10559/#como-trabajar-si-la-terminal-pos-no-funciona-correctamente/).

**Configuración**

  * [**Parámetros de Tesorería:**](?p=10293) ingrese a este proceso y haga clic en la solapa Administración de tarjetas; a continuación seleccione el valor 'Con POS integrado' para el campo Modo de emisión de cupones.
  * **[Planes](?p=10265):** ingrese a esta opción para registrar los planes de tarjeta con los que trabaja su comercio. Si bien esta información es provista por las administradoras de tarjetas, habitualmente se trabaja con al menos dos planes, uno denominado 'Un pago' y otro llamado 'Plan cuotas'. La cantidad de cuotas correspondiente a cada plan debe ser ingresada en el siguiente punto.
  * **[Tarjetas (primera etapa)](?p=10263): **acceda a este proceso para crear cada una de las tarjetas con las que trabaja su comercio. Durante la puesta en marcha inicial, la creación de tarjetas se debe realizar en dos etapas, en la primera se completan los datos básicos de cada tarjeta mientras que en la segunda se completan datos relacionados con los planes de la tarjeta. Esta última etapa sólo puede realizarse con posterioridad a la creación de las terminales POS.  
Durante la primera etapa **no tilde** la opción Utiliza conexión con terminal POS y solo complete el tipo de Numeración para cupones manuales y la Hora de cierre de lote. Estos datos son necesarios en caso de que deba emitir cupones manuales o efectuar un cierre de lote en modo Pos no integrado, debido a inconvenientes técnicos de la terminal POS. Puede optar entre una numeración manual o automática.
  * **[Terminales POS](?p=10269):** utilice este proceso para definir cada una de las terminales Payway con las que trabaja su comercio. Seleccione en la solapa principal la opción 'Payway' como tipo de terminal. Tenga en cuenta que, todos los dispositivos configurados con este tipo de terminal permitirán pagos QR. Además, configure manualmente el código de la terminal y asigne una descripción para identificar la misma. Tanto código de la terminal o Terminal Id como el código de comercio o Establecimiento los puede obtener desde el Menú de aplicaciones | Datos del establecimiento del dispositivo.  
Luego, complete la grilla de [Host a los que se conecta](?p=10269/#host-a-los-que-se-conecta). Tenga en cuenta que, esta configuración debe realizarla manualmente ya que por una limitación del integrador de Payway esa información no puede ser recuperada de la terminal.  
En la solapa [Tarjetas habilitadas](?p=10269/#tarjetas-habilitadas) debe agregar manualmente en la grilla los datos de las tarjetas Tango, los host y los códigos de tarjeta del POS que por una limitación de Payway no pueden ser recuperados de la terminal.  
Para más información consulte la [Puesta en marcha de pagos con Payway](?p=14430).
  * **[Tarjetas (segunda etapa)](?p=10263):** una vez configurados los datos de la terminal POS puede completar la información relacionada a cada tarjeta. Tilde la opción Utiliza conexión con terminal POS y siga los pasos enunciados a continuación: 
    * Haga clic sobre la solapa Datos para la venta y complete la sección Definición de planes para la venta que se encuentra en el sector inferior de la pantalla. En esta sección relacione el plan por defecto con los códigos de plan definidos en Tango. Para una configuración básica debe completar la cantidad mínima y máxima de cuotas del plan.
    * Haga clic sobre la solapa Datos para el comercio y complete la sección Períodos y descuentos para la acreditación que se encuentra en el sector inferior de la pantalla. En esta sección debe completar el tipo de acreditación del cupón (única o por cuotas), el tipo de período (horas, días hábiles, días corridos, etc.) y el período de acreditación.
  * **[Cuentas de Tesorería](?p=27349):** una vez que ha definido las tarjetas con las que trabaja, debe asignarles una cuenta de tesorería. Para ello ingrese a este proceso y defina una cuenta para cada tarjeta existente; para cada cuenta tilde la opción 'Tarjeta' en la sección Tipo de cuenta dentro de la solapa Principal y a continuación ingrese a la solapa Tarjeta para asignar el código de tarjeta que representa y los planes que estarán habilitados para la cuenta que está definiendo. Si bien puede definir varias cuentas que representen los distintos planes de la tarjeta, recomendamos trabajar con una única cuenta por tarjeta. Un plan de una tarjeta no puede estar asociado a más de una cuenta.
  * **[Host](?p=10271):** los valores de ese proceso se crearon automáticamente al importar los datos desde la terminal POS. Habitualmente las terminales POS trabajan con cuatro host: Visa, Diners, Posnet y American Express.



Recuerde que los pasos arriba enunciados forman parte de la configuración básica del circuito de tarjetas.

##### Configurar la modalidad POS no integrado

  * [**Parámetros de Tesorería**](?p=10293)**:** ingrese a este proceso y haga clic en la solapa Administración de tarjetas; a continuación seleccione el valor 'Con POS no integrado' para el campo Modo de emisión de cupones.
  * [Planes](?p=10265): ingrese a esta opción para registrar los planes de tarjeta con los que trabaja su comercio. Si bien esta información debe ser provista por las administradoras de tarjetas, habitualmente se trabaja con al menos dos planes, uno denominado 'Un pago' y otro llamado 'Plan cuotas'. La cantidad de cuotas correspondiente a cada plan será ingresada en el siguiente punto.
  * [Tarjetas](?p=10263): acceda a este proceso para crear cada una de las tarjetas con las que trabaja su comercio. Complete los datos que se detallan a continuación: 
    * No tilde la opción Utiliza conexión con terminal POS.
    * Hora de cierre de lote: esta hora es utilizada por el [cierre de lote](?p=10149) para determinar la fecha de acreditación de los cupones. Por ejemplo, si el cierre se genera con posterioridad a la hora aquí ingresada el sistema incrementa automáticamente un día a la fecha de acreditación esperada para los cupones que integran el lote cerrado.
    * Numeración para cupones manuales: este dato es necesario en caso que deba emitir cupones manuales debido a inconvenientes técnicos de la terminal POS. Puede optar entre una numeración manual o automática.
    * Haga clic sobre la solapa Datos para la venta y complete la sección Definición de planes para la venta que se encuentra en el sector inferior de la pantalla. En esta sección debe indicar los [planes](?p=10265) (definidos en el punto anterior) que puede utilizar la tarjeta que está definiendo. Para una configuración básica debe completar la cantidad mínima y máxima de cuotas del plan.
    * Haga clic sobre la solapa Datos para el comercio y complete la sección Períodos y descuentos para la acreditación que se encuentra en el sector inferior de la pantalla. En esta sección debe completar el tipo de acreditación del cupón (única o por cuotas), el tipo de período (horas, días hábiles, días corridos, etc.) y el período de acreditación. Habitualmente las ventas en cuotas se abonan a las 48 horas del [cierre de lote](?p=10149) y las ventas en un pago se acreditan a los 20 días corridos.
    * [Host](?p=10271): ingrese los host a los que se conectan sus terminales POS. Habitualmente las terminales POS trabajan con cuatro host: Visa, Diners, Posnet y American Express. Para conocer los host que utilizan sus terminales siga los pasos que se detallan a continuación: las terminales Ingénico / Verifone no brindan información impresa de la relación directa entre las tarjetas y los host que las administran. Para mas información sobre este tema, puede contactarse con el proveedor de la terminal, para solicitar los datos necesarios. Como orientación general, tenga en cuenta que cada host, suele administrar las siguientes tarjetas: **Visa:** Visa crédito, Electrón (Visa débito), Visa Naranja. **American Express:** American Express. **Diners:** Diners Club. **Posnet:** MasterCard, Argencard, Maestro, Italcred, Tarjeta Shopping, Cabal, CMR, Favacard, Naranja, Lider, etc. El valor del código de host puede ser ingresado de acuerdo a sus preferencias, ya que en la modalidad "POS no integrado" Tango no se comunica con la terminal POS y por lo tanto puede no respetar la codificación de ese equipo.  
Si trabaja con terminales de distintas marcas puede ocurrir que cada una de ellas asigne un nombre diferente a un mismo host. Bajo esta modalidad de trabajo (POS no integrado) no hace falta que 'duplique' los host de acuerdo al criterio de cada marca sino que basta que decida qué codificación utilizar para identificar a cada uno de los cuatro host que se utilizan habitualmente.  
Conserve la información impresa por la terminal ya que le será de utilidad cuando defina las [terminales POS](?p=10269).
    * [Terminales POS:](?p=10269) utilice este proceso para definir cada una de las terminales POS con las que trabaja su comercio. Aunque no es requisito obligatorio, le recomendamos que el código de terminal utilizado en Tango coincida con la identificación real de la terminal POS. De esta forma facilitará la identificación de los cupones durante el proceso de [conciliación](?p=10169).Para conocer la identificación de la terminal consulte la configuración impresa en el punto anterior. En la impresión de equipos Ingénico / Verifone la identificación se muestra como 'Term.ID.' A continuación indique el tipo de numeración a utilizar para los lotes y cupones emitidos por la terminal. A fin de minimizar los errores durante la emisión de cupones le recomendamos seleccionar la opción 'Automática'.  
En la sección Host a los que se conecta pulse el botón "Agregar todos" para asociar todos los [host](?p=10271) a la terminal POS. Para cada uno de ellos debe completar el número de lote actual y el próximo número de cupón. Este último dato puede consultarlo desde la configuración impresa por la terminal POS en el punto anterior.  
En caso que no tenga acceso a esta información, asigne 1 (uno) en cada campo.  
Si trabaja con perfiles de facturación, habilite los parámetros Permite editar número de lote y Permite editar número de cupón. Si no trabaja con perfiles, estos datos siempre son editables.  
Al generar un cupón, tipee el número de lote y cupón que se exhibe en el comprobante impreso. Al confirmarlo, el sistema registrará en la configuración de su Terminal POS los datos ingresados y, en caso de haber seleccionado la opción 'Automática' para el tipo de numeración de lote y cupón, los utilizará para sugerir la información del próximo cupón.  
Si el tipo de terminal es Posnet, configure la terminal para que permita pagos QR en la sección [Principal](?p=10269/#principal) de Terminales POS de Tesorería. Tenga en cuenta que, antes de realizar la configuración, debe verificar que la terminal esté actualizada para operar con pagos QR. Para ello valide que tenga la opción PAGOS QR desde el menú de la terminal. Si ingresa por primera vez a esta opción de manera no integrada, el dispositivo le solicitará habilitar el servicio. En caso de no tener disponible la opción PAGOS QR desde el menú de la terminal, comuníquese con su representante de Posnet para solicitarle la actualización de la terminal correspondiente. Para más información acerca de la configuración de pagos QR consulte la [Puesta en marcha de pagos QR con Posnet](?p=17126).
  * Para finalizar la configuración de la terminal POS haga clic en la solapa Tarjetas habilitadas y pulse el botón "Agregar todas" para que se complete la grilla con las tarjetas previamente definidas. En caso de que alguna tarjeta no se encuentre disponible en esta terminal puede eliminarla o en su defecto deshabilitarla.
  * [Cuentas de Tesorería](?p=10235): una vez que ha definido las tarjetas con las que trabaja debe asignarles una cuenta de tesorería. Para ello ingrese a este proceso y defina una cuenta para cada tarjeta existente; para cada cuenta tilde la opción 'Tarjeta' en la sección Tipo de cuenta dentro de la solapa Principal y a continuación ingrese a la solapa Tarjeta para asignar el código de tarjeta que representa y los planes que estarán habilitados para la cuenta que está definiendo.



__Nota

Si bien puede definir varias cuentas que representen los distintos planes de la tarjeta recomendamos trabajar con una única cuenta por tarjeta. Tenga en cuenta que un plan de una tarjeta no puede estar asociado a más de una cuenta.

Recuerde que los pasos arriba enunciados forman parte de la configuración básica del circuito de tarjetas.

##### Configurar la modalidad de ingreso manual

  * [Parámetros de Tesorería](?p=10293): ingrese a este proceso y haga clic en la solapa Administración de tarjetas; a continuación seleccione el valor 'Manual' para el campo Modo de emisión de cupones.
  * [Planes](?p=10265): ingrese a esta opción para registrar los planes de tarjeta con los que trabaja su comercio. Si bien esta información debe ser provista por las administradoras de tarjetas, habitualmente se trabaja con al menos dos planes, uno denominado 'Un pago' y otro llamado 'Plan cuotas'. La cantidad de cuotas correspondiente a cada plan será ingresada en el siguiente punto.
  * [Tarjetas](?p=10263): acceda a este proceso para crear cada una de las tarjetas con las que trabaja su comercio. Complete los datos que se detallan a continuación: 
    * Numeración para cupones manuales: indique la modalidad que prefiere utilizar. A fin de minimizar los errores durante la emisión de cupones le recomendamos seleccionar la opción 'Automática' (siempre y cuando disponga de un talonario correlativo para cupones manuales).
    * Haga clic sobre la solapa Datos para la venta y complete la sección Definición de planes para la venta que se encuentra en el sector inferior de la pantalla. En esta sección debe indicar los [planes](?p=10265) (definidos en el punto anterior) que puede utilizar la tarjeta que está definiendo. Para una configuración básica debe completar la cantidad mínima y máxima de cuotas del plan.
    * Haga clic sobre la solapa Datos para el comercio y complete la sección Períodos y descuentos para la acreditación que se encuentra en el sector inferior de la pantalla. En esta sección debe completar el tipo de acreditación del cupón (única o por cuotas), el tipo de período (horas, días hábiles, días corridos, etc.) y el período de acreditación. Habitualmente las ventas en cuotas se abonan a las 48 horas del haber [depositado los cupones](?p=10210) y las ventas en un pago se acreditan a los 20 días corridos siendo acreditado el dinero en un solo pago (tipo de acreditación única).
    * [Cuentas de Tesorería](?p=10235): una vez que ha definido las tarjetas con las que trabaja debe asignarles una cuenta de tesorería. Para ello ingrese a este proceso y defina una cuenta para cada tarjeta existente; para cada cuenta tilde la opción 'Tarjeta' en la sección Tipo de cuenta dentro de la solapa Principal y a continuación ingrese a la solapa Tarjeta para asignar el código de tarjeta que representa y los planes que estarán habilitados para la cuenta que está definiendo.  
Si bien puede definir varias cuentas que representen los distintos planes de la tarjeta recomendamos trabajar con una única cuenta por tarjeta. Tenga en cuenta que un plan de una tarjeta no puede estar asociado a más de una cuenta.



Recuerde que los pasos arriba enunciados forman parte de la configuración básica del circuito de tarjetas.

##### Configurar los conceptos de gastos

Siga los pasos que se detallan a continuación para definir los conceptos que aplican las administradoras de tarjetas.  
Algunos de estos conceptos puede transferirlos al cliente como ser los recargos financieros de la venta en cuota.

  * [Conceptos de gastos:](?p=10166) ingrese a este proceso para definir cada uno de los conceptos de gasto que le cobran las administradoras de tarjeta. Por ejemplo podemos citar: cargo de acceso a internet, gastos de envío, gastos administrativos, etc.  
A continuación complete los siguientes datos:



  * Forma de cálculo: indique si el concepto se aplica como un importe fijo o como porcentaje sobre una determinada base de cálculo.
  * Datos para el cálculo: seleccione la base de cálculo que se debe utilizar para calcular el monto del concepto.
  * Aplica sobre: indique si el gasto se calcula sobre todos los cupones, los emitidos por la terminal POS, los emitidos manualmente o sólo sobre los cupones rechazados o sobre la liquidación mensual.


* [Tarjetas](?p=10263): ingrese a este proceso para indicar los gastos que le cobra cada una de las administradoras de tarjeta. 

  * Solapa datos para el comercio: dentro de esta solapa debe completar todos los gastos que le cobra al comercio la administradora de tarjetas.  
Entre ellos se destacan:



  * Arancel: ingrese el arancel o comisión que le cobran por prestación del servicio.
  * Gastos habituales: en esta sección debe completar los gastos (impuestos) que habitualmente se aplican al cupón. Si lo prefiere puede utilizar alícuotas del módulo Compras; de lo contrario ingrese las alícuotas que se deben aplicar.
  * Otros gastos: indique en esta sección los conceptos de gastos definidos anteriormente (cargo de acceso a Internet, gastos de envío, gastos administrativos, etc.)
  * Períodos y descuentos para la acreditación: puede indicar un descuento que se aplique al comercio cuando emite cupones con un determinado plan.


* Solapa datos para la venta: aunque esta solapa está orientada a la información relacionada con la venta incluye un concepto que influye en el monto final que cobra su comercio.  
Este concepto es el recargo financiero que se cobra al cliente final. Dentro de la sección Tabla general para el cálculo de recargos financieros ingrese los valores que le envía la administradora de tarjetas.  
En la sección Definición de planes para la venta indique si quiere trasladar los recargos financieros al cliente de acuerdo al plan y cantidad de cuotas utilizados. Para ello detalle los coeficientes particulares en la columna homónima.

Tenga en cuenta que si no realiza cambios a esta grilla se trasladarán los recargos financieros a sus clientes.  
Puede, por ejemplo, no trasladarle al cliente el recargo financiero hasta 3 cuotas y de ahí en adelante sí o o incluso cobrarle un recargo financiero mayor al que le aplica la tarjeta a su comercio.

__Nota

Tenga en cuenta que los gastos relacionados al cupón sólo se calculan durante la emisión y no vuelven a generarse aún cuando re-implemente el sistema.

##### Configurar descuentos, recargos financieros y promociones

Una vez definidas las tarjetas con las que trabaja su comercio, usted dispone de las siguientes alternativas para trabajar con descuentos o recargos financieros:

  * Por tarjeta: utilice esta modalidad para ingresar la tabla de coeficientes de recargos financieros por cantidad de cuotas que le envía la administradora de tarjetas.  
En el caso de ingresar los coeficientes en la tabla que se destaca en la imagen, Tango aplicará el mismo coeficiente, tanto en el momento de la venta (hacia el cliente), como al efectuar el cálculo de neto estimado a cobrar (descuento efectuado por la administradora de la tarjeta en concepto de aceleración en el pago, para el caso de ventas efectuadas en cuotas, acreditadas al comercio en un único pago).  
Haga clic en la solapa Datos para la venta, e ingrese la fecha en la que entrarán en vigencia los coeficientes. Puede ingresar coeficientes con fecha posterior a la actual, Tango comenzará a aplicarlos a partir del día indicado en el campo Fecha de vigencia.  
  
Utilice el formato 'Coeficiente' para ingresar los valores tal como los presenta la administradora de la tarjeta.  
Haga clic en el botón "Copiar coeficientes" para obtener una tabla similar previamente ingresada en otra tarjeta. Puede invocar la tabla y luego modificar algunos datos en particular.  
En el caso que el recargos financieros a aplicar sea el mismo para varias cuotas, puede indicarlo del siguiente modo:  
  
En este caso, si usted efectúa una venta en 5 pagos, el coeficiente a aplicar será el especificado para 6 cuotas.  
Tenga en cuenta que si opta por definir las cuotas como en el ejemplo, debe especificar las cuotas que NO tienen recargos financieros (por ejemplo, la cuota 1), de lo contrario, se interpretará que debe aplicar un recargo financiero del 3.36% desde la cuota 1 hasta la cuota 3.  
Para más información sobre este tema consulte la opción Tabla general para el cálculo de recargos financieros dentro del proceso [Tarjetas](?p=10263).
  * Por plan: utilice esta opción cuando el descuento o recargo financiero dependa de la tarjeta y plan a utilizar.  
En el proceso [Tarjetas](?p=10263) haga clic en la solapa Datos para la venta, e ingrese un porcentaje de descuento en la columna "Bonificación" de la grilla Definición de planes para la venta.  
  
También es posible indicar si quiere trasladar los recargos financieros al cliente de acuerdo al plan y cantidad de cuotas utilizados. Para ello detalle los coeficientes particulares en la columna homónima de la grilla Definición de planes para la venta.  
  
Tenga en cuenta que si no realiza cambios a esta grilla se trasladarán los recargos financieros a sus clientes (definidos en la Tabla general para el cálculo de recargos financieros).  
Por ejemplo, puede optar por no trasladarle al cliente el recargo financiero de las 4 primeras cuotas, y aplicarle el recargo financiero a partir de la 5º cuota. Incluso podría cobrarle un recargo financiero mayor al que le aplica la administradora de la tarjeta a su comercio.  
Para más información sobre este tema consulte la opción Definición de planes para la venta dentro del proceso [Tarjetas](?p=10263).  
Recuerde que los descuentos o recargos financieros asociados a la tarjeta o el plan se aplicarán en forma automática sólo cuando utilice la modalidad cobro al contado en el proceso [Factura Punto de Venta](?p=19302).
  * Por promoción: aplique esta modalidad cuando el descuento dependa de varios factores como pueden ser un período de vigencia, los días de la semana en los que se aplica, la marca comercial de las tarjetas involucradas y/o el banco emisor del plástico.  
En el proceso [Promociones](?p=10267) defina un porcentaje de aplicación a descontar al cliente. Este porcentaje puede ser aplicable en línea de caja, o por reintegro en el resumen del usuario de la tarjeta.  
Seleccione la opción 'en línea de caja' para que este porcentaje se aplique a la factura de venta.  
  
Recuerde que los descuentos asociados a la promoción, se aplicarán en forma automática en la línea de caja, sólo cuando utilice la modalidad cobro al contado en el proceso [Factura Punto de Venta](?p=19302).  
Indique las tarjetas relacionadas con la [promoción](?p=10267) en la solapa Datos Alternativos. Puede asignar un [banco](?p=11836) en esta solapa, para ayudar al vendedor a seleccionar la promoción apropiada en el momento de la venta.  
  
Defina coeficientes para ventas en cuotas, particulares para la promoción. Por ejemplo, puede definir una promoción que no aplique recargo financiero en ventas hasta 6 cuotas. Esto prevalecerá por sobre los recargos financieros que pueda haber definido en la tarjeta o el plan.  
En el caso de haber pactado un convenio con la empresa de tarjetas, donde los recargos financieros por ventas en cuotas son absorbidos por la administradora, defina la tabla de recargos financieros del siguiente modo:  
[](https://ayudas.axoft.com/wp-content/uploads/2020/06/clip01121.gif) En el caso de que la promoción sea propia de su comercio, sin mediar un convenio con la empresa de tarjetas, esta le descontará el coeficiente de recargos financieros en el momento de liquidar el cupón, sin tener en cuenta si usted aplicó el recargo financiero en el momento de la venta.  
Para promociones de este tipo, defina la tabla del siguiente modo:  
[](https://ayudas.axoft.com/wp-content/uploads/2020/06/clip01131.gif) Si la empresa actúa como casa central, puede asociar las promociones a sus sucursales para filtrar la información al momento de exportar. Al dar de alta una nueva promoción, indique que sucursales la van a utilizar.  
Recuerde que los descuentos o recargos financieros asociados a la tarjeta, plan o promoción se aplicarán en forma automática sólo cuando utilice la modalidad cobro al contado en el proceso [Factura Punto de Venta](?p=19302).



**Tipos de descuento  
**Dependiendo del convenio firmado con la administradora de tarjetas (y/o el banco emisor) el descuento se puede aplicar bajo alguna de las siguientes modalidades:

  * En línea de caja: seleccione esta modalidad cuando el descuento se debe aplicar en la factura que está generando. De esta forma el cliente ve reflejado el descuento al momento de efectuar su compra.
  * En el resumen del cliente: opte por este criterio cuando el importe del descuento es reintegrado por la administradora de tarjetas en el siguiente resumen de la tarjeta. En este caso el descuento no se ve reflejado en la factura.



Tenga en cuenta que el tipo de descuento 'Por reintegro' 'En el resumen del cliente' sólo está disponible cuando se aplica una promoción.

##### Configurar movimientos automáticos de Tesorería

Siga los pasos que se detallan a continuación para configurar la generación automática de [Movimientos de Tesorería](?p=10296) desde los procesos de administración de tarjetas.

  * [Parámetros](?p=10293): ingrese a este proceso y tilde la opción Genera movimientos de Tesorería automáticamente al realizar procesos de administración de cupones.
  * [Tarjetas](?p=10263): dentro de la solapa Datos para Tesorería complete la siguiente información para cada una de las tarjetas existentes: 
    * Cierre de lote / depósito de cupones manuales: indique el tipo de comprobante y la cuenta de tesorería que se debe utilizar para la generación del movimiento.
    * Conciliación de cupones: ingrese el tipo de comprobante y las cuentas de tesorería que se deben utilizar para la generación del movimiento (para el arancel, cupones rechazados, costos financieros, etc.). Puede utilizar una única cuenta de tesorería para imputar todos los impuestos registrados durante la conciliación o generar el movimiento utilizando cuentas particulares para cada uno.  
Tenga en cuenta los siguientes requisitos que debe cumplir un [Tipo de comprobante](?p=10253) para que pueda ser utilizado en generaciones automáticas de [Movimientos de Tesorería](?p=10296): 
      * Asigne al tipo de comprobante la clase 3.
      * Configure la numeración como automática.
      * Marque como no editables la clase en el ingreso del movimiento, la cuenta principal, y el número de comprobante.
  * [Conceptos de gastos](?p=10166): ingrese a este proceso para indicar la cuenta de tesorería que se debe utilizar para imputar cada concepto de gasto.  
Tenga en cuenta que el movimiento relacionado con la emisión del cupón (como resultado de la cobranza de una venta) se genera automáticamente sin requerir de la configuración arriba mencionada.



Importante:

En caso que la parametrización descripta se encuentre incompleta, el sistema actuará del mismo modo que si el parámetro Genera movimientos de Tesorería automáticamente al realizar procesos de administración de cupones no hubiera sido seleccionado.

Para más información sobre los movimientos que se pueden generar consulte el capítulo [Generación automática de movimientos de Tesorería](?p=10559/#generacion-automatica-de-movimientos-de-tesoreria).

##### Definir descuentos y recargos financieros asociados a tarjetas

Una vez definidas las tarjetas con las que trabaja su comercio usted dispone de las siguientes alternativas para trabajar con descuentos o recargos financieros:

  * Por tarjeta: utilice esta modalidad para ingresar la tabla de coeficientes de recargos financieros por cantidad de cuotas que le envía la administradora de tarjetas. Para más información sobre este tema consulte la opción Tabla general para el cálculo de recargos financieros dentro del proceso [Tarjetas](?p=10263).
  * Por plan: utilice esta opción cuando el descuento o recargo financiero dependa de la tarjeta y plan a utilizar. Un ejemplo típico de uso resulta el recargo financiero que se aplica a la venta en cuotas para determinadas marcas de tarjetas. Para más información sobre este tema consulte la opción Definición de planes para la venta dentro del proceso [Tarjetas](?p=10263).
  * Por promoción: aplique esta modalidad cuando el descuento dependa de varios factores como pueden ser un período de vigencia, los días de la semana en los que se aplica, la marca comercial de las tarjetas involucradas y/o el banco emisor del plástico. Para más información sobre este tema consulte [Promociones](?p=10267).



Más información:

Recuerde que los descuentos o recargos financieros asociados a la tarjeta, plan o promoción se aplicarán en forma automática sólo cuando utilice la modalidad [cobro al contado](?p=19415) en el proceso [Factura Punto de Venta](?p=19302).

**Tipos de descuento  
**Dependiendo del convenio firmado con la administradora de tarjetas (y/o el banco emisor) el descuento se puede aplicar bajo alguna de las siguientes modalidades:

  * En línea de caja: seleccione esta modalidad cuando el descuento se debe aplicar en la factura que está generando. De esta forma el cliente ve reflejado el descuento al momento de efectuar su compra.
  * En el resumen del cliente: opte por este criterio cuando el importe del descuento es reintegrado por la administradora de tarjetas en el siguiente resumen de la tarjeta. En este caso el descuento no se ve reflejado en la factura.



Tenga en cuenta que el tipo de descuento 'Por reintegro' sólo está disponible cuando se aplica [una promoción](?p=10267).
