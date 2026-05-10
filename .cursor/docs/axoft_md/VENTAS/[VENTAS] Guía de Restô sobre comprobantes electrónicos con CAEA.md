# Guía de Restô sobre comprobantes electrónicos con CAEA

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_caea_gv3/

## Contenido

# Guía de Restô sobre comprobantes electrónicos con CAEA

El CAEA (Código de Autorización Electrónico Anticipado) es uno de los regímenes de facturación admitidos por la AFIP que reemplaza al CAE (Código de Autorización Electrónico) en situaciones de contingencia como lo puede ser un corte de Internet o la caída del sistema de la AFIP.

A diferencia del CAE (que se obtiene en cada transacción), el CAEA se obtiene en forma anticipada una vez por cada quincena y se los utiliza para todas las transacciones de ese período. Entre 5 y 8 días después de cada quincena, se informa a la AFIP el detalle de estos comprobantes para que los fiscalice.  
Para más información consulte la sección de Preguntas frecuentes.

##### Puesta en marcha

Siga las indicaciones que detallamos a continuación para habilitar este circuito:

  1. Ingrese al sitio web de AFIP para habilitar los puntos de venta que quiere utilizar para CAEA. Para más información consulte ¿Cuántos puntos de venta tengo que habilitar para CAEA?.  
Tenga en cuenta que número de CAEA que se solicita es por contribuyente, por lo tanto, todos los puntos de venta utilizarán el mismo número.
  2. Ingrese a la [definición de talonarios](?p=19579) para reflejar en Tango Restô los puntos de venta creados en el sitio de AFIP. Es importante que seleccione el **tipo de autorización = CAEA** dentro de la solapa Comprobantes electrónicos.
  3. Una vez configurado los talonarios de CAEA puede asociarlos (en el mismo proceso de [definición de talonarios](?p=19579)) a cada uno de los talonarios CAE. Es decir, puede indicar para cada talonario electrónico (CAE) qué talonario CAEA puede utilizar Tango cuando se produzca alguna contingencia. Si bien no es un campo obligatorio, le recomendamos que lo complete para agilizar el cambio de talonario durante la emisión de comprobantes.
  4. Ingrese a [Formulario](?p=25361) para adaptar (en caso de corresponder) el formulario que imprime con cada comprobante (TYP). Busque el texto "CAE" y sustitúyalo por la variable de reemplazo **@TN** que imprime la palabra "CAE" o "CAEA" de acuerdo con lo que le corresponda a cada comprobante. Tenga en cuenta que el nuevo texto ocupa un carácter más que el texto fijo.
  5. Ingrese al Administrador de comprobantes electrónicos y a continuación pulse la opción Obtener CAEA. Complete el período y quincena correspondiente antes de presionar "Consultar CAEA". Si no posee conexión a Internet, puede ingresar manualmente los datos de CAEA obtenidos, por ejemplo, desde otra terminal o sucursal. Tenga en cuenta que número de CAEA que se solicita es por contribuyente, por lo tanto, todos los puntos de venta utilizarán el mismo número. Para más información consulte ¿Tengo que obtener un CAEA por cada punto de venta?.



__Nota

Tenga en cuenta que, los talonarios del tipo CAEA deberán estar asociado a un talonario CAE y asegúrese que en la sección numeración (_Próximo número a emitir_) sea el número esperado por AFIP, ya que los comprobantes de venta emitidos con CAEA se ponen a disposición de manera inmediata al cliente final por tener un código de autorización electrónico anticipado.

##### Detalle del circuito

El circuito de trabajo habitual de CAEA se distribuye de la siguiente forma:

  * Obtención quincenal de CAEA.
  * Emisión de comprobantes ante situaciones de contingencia.
  * Información de los comprobantes emitidos con CAEA.



**Obtención quincenal de CAEA  
**Tal como mencionamos en la introducción de esta guía, la vigencia del CAEA es quincenal, por lo que debe obtenerse un nuevo CAEA cuando esté por terminarse su vigencia. Tenga en cuenta que puede anticipar la solicitud hasta 5 días corridos antes del inicio de cada quincena.  
Para más información sobre este punto consulte el punto 4 de la Puesta en marcha.

**Emisión de comprobantes ante situaciones de contingencia  
**Si conoce que su empresa o comercio tiene problemas de conexión, o sabe que los servidores de AFIP no están respondiendo o cualquier otra contingencia que impida conectarse con AFIP, puede optar por emitir comprobantes con CAEA.  
Para hacerlo debe activar la modalidad CAEA activo que se encuentra en la configuración de la terminal, en la solapa Documentos electrónicos. Esta modalidad asigna automáticamente el talonario CAEA asociado al talonario habitual que utiliza para facturar y muestra solo los talonarios de tipo CAEA como talonarios disponibles para facturar.  
Tenga en cuenta que para que funcione correctamente la modalidad 'CAEA activo', debe tener asignado un talonario CAEA a cada talonario CAE que use en facturación.  
Cuando detecte que la situación de contingencia se ha normalizado, bastará cn desactivar el parámetro CAEA activo que se encuentra en la configuración de la terminal, en la solapa Documentos electrónicos, para volver a emitir comprobantes con CAE.  
En las modalidades de tickets '1' y '2', así como en los circuitos de facturar mesa y facturar cliente, en la vista del facturador, puede utilizar el botón "Probar conexión" que está ubicado abajo a la derecha, para verificar la conexión a Internet y/o que los servidores de AFIP están respondiendo correctamente.

**Información de los comprobantes emitidos con CAEA  
**Tenga en cuenta que debe realizar una presentación a la AFIP con los comprobantes emitidos bajo esta modalidad para que pueda preceder a su fiscalización.  
Puede consultar la fecha de vencimiento de cada período dentro del [Administrador de comprobantes electrónicos](?p=17774), opción Obtener CAEA. Habitualmente, el vencimiento se produce entre los 5 y 8 días corridos contados desde el día inmediato siguiente al de finalización de cada período quincenal; esa fecha es informada por AFIP al entregar el CAEA de cada quincena.  
Dentro del mismo proceso, utilice la solapa Informar CAEA para notificar a la AFIP los comprobantes generados con CAEA.

__Nota

Tenga en cuenta que si solicitó CAEA, también debe informar a la AFIP si en ese período no emitió comprobantes (es decir que ese CAEA no fue utilizado).

##### Preguntas frecuentes

**¿Quiénes pueden solicitar la adhesión al régimen CAEA de la AFIP?  
**Para obtener información sobre este punto le recomendamos consultar la página de la [AFIP](https://www.afip.gob.ar/).

**¿Cada cuánto tiempo tengo que solicitar un nuevo CAEA?  
**El CAEA se debe solicitar en forma quincenal de acuerdo con siguiente criterio:

  * **Primer período:** entre los días 1 y 15 de cada mes, ambos inclusive.
  * **Segundo período:** entre los días 16 y último de cada mes, ambos inclusive.



**¿Tengo que obtener un CAEA para cada punto de venta?  
**No, la AFIP otorga un número CAEA por cada contribuyente, no por punto de venta.

**¿Cuántos puntos de venta tengo que habilitar para CAEA?  
**Antes que nada, es importante resaltar que a cada punto de venta tiene una dirección fiscal, por lo que al menos debe crear uno por cada una de sus sucursales.  
Si bien podría usar uno por cada sucursal, le sugerimos crear uno por cada punto de venta que tenga actualmente, de forma de tener mayor control de los comprobantes emitidos por CAEA.

**¿Cada comprobante tiene un CAEA distinto?  
**No, de acuerdo con lo establecido por AFIP, el sistema asigna el mismo número de CAEA a todos los comprobantes emitidos durante el período de vigencia de ese CAEA.

**¿Cada cuánto tiempo tengo que enviar a AFIP la información de los comprobantes emitidos?  
**Siempre que haya solicitado CAEA para una quincena, debe informar los comprobantes emitidos con esta modalidad. También debe informar a AFIP sobre aquellos puntos de ventas que no generaron comprobantes con CAEA (no tuvieron movimientos).  
Habitualmente, el vencimiento se produce 8 días corridos contados desde el día inmediato siguiente al de finalización de cada período quincenal.

**¿Cuáles son los controles que aplica la AFIP para detectar irregularidades?  
**Se considera que no se cumple con la condición de excepcionalidad cuando, durante 2 meses consecutivos o 3 meses alternados en un año calendario, se observe alguna de las siguientes irregularidades:

  1. Que la emisión de comprobantes con CAEA excedan significativamente el nivel de facturación regular, es decir que la cantidad de comprobantes emitidos mensualmente por excepción representen un 5% o más, respecto del total de la sucursal.
  2. La contingencia con CAEA, como alternativa de la emisión de comprobantes electrónicos, medida en tiempo, no deberá superar el 5% del lapso total de disponibilidad de servicios ofrecidos por AFIP en forma mensual, medido por sucursal.



**¿Debo adaptar mis formularios?  
**Sí, le sugerimos que reemplace el texto "CAE" por la palabra de control **@TN** que imprime la palabra "CAEA" o "CAE" de acuerdo con lo que corresponda a cada comprobante.  
El número de CAEA tiene la misma cantidad de dígitos que el de CAE por lo que no requiere adaptar sus formularios en este sentido.

**¿Qué ocurre si no tengo internet cuando quiero obtener un nuevo CAEA?  
**Actualmente la AFIP no permite obtener el número de CAEA en forma manual, sino que debe realizarse a través de sistemas informáticos, por lo que en caso de no contar con Internet en su terminal / sucursal, deberá hacerlo desde una que sí lo tenga y luego transcribir manualmente el número de CAEA en el mismo proceso en el que se obtiene desde AFIP (Administrador de comprobantes electrónicos, opción "Obtener CAEA"). Recuerde que puede solicitar el número de CAEA con 5 días corridos de anticipación al comienzo de cada quincena.

**¿Qué hago si un comprobante quedó sin obtener CAE?  
**En el caso que un comprobante no obtenga CAE por problemas de conexión, quedará registrado con estado “Pendiente”. Estos comprobantes quedarán en ese estado hasta que recupere la conexión a Internet y pueda fiscalizarlo AFIP. Los comprobantes a emitir luego de esta situación, sí podrá realizarlos con CAEA.

**¿Puedo utilizar CAEA en situaciones de contingencia de mi controlador fiscal?  
**Si bien CAEA apunta principalmente a funcionar como un método de contingencia para comprobantes electrónicos, también está habilitado por AFIP para funcionar como alternativa ante fallas de controladores o impresoras fiscales. Tenga en cuenta que para solicitar CAEA debe utilizar los web services de AFIP, por lo que debe realizar la [puesta en marcha del circuito de comprobantes electrónicos](?p=30232).

**¿Puedo programar la obtención del CAEA y su posterior presentación?  
**Para programar la ejecución de estas acciones, parametrice las tareas de automatización desde el Administrador de Servicios.  
Las tareas a utilizar son:

  * [Tarea de automatización de obtención de CAEA](?p=31000/#tareas-de-automatizacion-de-obtencion-de-caea).
  * [Tarea de automatización para informar CAEA](?p=31000/#tareas-de-automatizacion-de-presentacion-de-comprobantes-caea).



**Consideraciones de la versión actual  
**Los circuitos de facturación remota y facturación desde Mobile no están contemplados para la emisión de comprobantes de ventas con CAEA.

**Otras consultas  
**Si su consulta no fue respondida por la presente guía, lo invitamos a contactar a nuestro centro de servicios o consultar las [preguntas frecuentes de AFIP](https://www.afip.gob.ar/genericos/guiavirtual/directorio_subcategoria_nivel3.aspx?id_nivel1=562id_nivel2=603&id_nivel3=1663).
