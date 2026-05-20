# Guía sobre solicitudes de compra

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=14476/

## Contenido

# Guía sobre solicitudes de compra

A continuación se detallan los pasos y el orden de configuración a seguir para implementar el circuito de solicitudes de compra.

__Nota

Recuerde que la tecla rápida <F3> permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

##### Puesta en marcha

Para implementar el circuito de solicitud de compra, usted debe seguir los siguientes pasos:

  1. Parámetros de Compras: habilite el proceso de solicitudes de compra y defina su comportamiento para comenzar a utilizar el circuito.  
Para más información consulte [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).
  2. Talonarios: es indispensable que defina al menos un talonario para las solicitudes de compra a ingresar.  
Si usted desea imprimir sus solicitudes de compra, deberá definir el dibujo del comprobante que será impreso.  
Para más información, consulte [Talonarios](https://ayudas.axoft.com/25ar/talonario_cp2).
  3. Artículos Genéricos (opcional) (*): defina un conjunto de artículos que podrá ser utilizado en el ingreso de solicitud de compra. Utilice este tipo de artículos en el Ingreso de Solicitud de Compra para indicar al comprador que puede reemplazar el artículo a comprar (nombrado en forma genérica) por otros similares. Para más información vea el siguiente ejemplo o consulte el tópico [Artículos genéricos](https://ayudas.axoft.com/25ar/articulogenerico_cp2).
  4. Motivos (opcional): defina los motivos que utilizará en el momento de cerrar o desautorizar una solicitud de compra.  
Para más información, consulte [Motivos](https://ayudas.axoft.com/25ar/motivos_cp2).
  5. Clasificación 1 y 2 (opcional): mediante este proceso, usted puede crear clasificaciones para las Solicitudes de Compras que le ayudarán a definir subestados o categorías, y además, controlar su comportamiento para una determinada clasificación.  
Para más información, consulte [Clasificación 1](https://ayudas.axoft.com/25ar/clasificacion1_cp2) y [Clasificación 2](https://ayudas.axoft.com/25ar/clasificacion2_cp2).
  6. Textos para comprobantes de compra (opcional): defina distintos tipos de textos que podrán ser usados posteriormente, para el ingreso, impresión y consulta de solicitudes de compra.  
Esta opción es de suma utilidad para ingresar aquellos textos complejos y repetitivos que se utilizan normalmente en estos comprobantes, tales como especificaciones técnicas, condiciones de compra, etc.  
Para más información, consulte [Textos para comprobantes de compra](https://ayudas.axoft.com/25ar/textocomprobcp_cp2).
  7. Perfiles de Solicitud de Compra (opcional): personalice el comportamiento del proceso definiendo perfiles para los usuarios que lo utilizarán.  
Para más información, consulte [Perfiles de solicitud de compra](https://ayudas.axoft.com/25ar/perfsolicitudcp_cp2).



**(*) Ejemplo...**

Como ejemplos de Genéricos se pueden definir:

  * Lapicera
  * Cuaderno



Usted podrá, en el momento de ingresar una Solicitud de Compra, pedir "LAPICERA". En el momento de generar la Orden de Compra, el comprador será el encargado de definir el tipo de lapicera que adquiere, en ese momento se realiza el reemplazo del genérico por un artículo, indicando el código correspondiente.

__Nota

Si usted definió perfiles que sólo aceptan la carga de artículos genéricos, el ingreso de este tipo de artículos será de carácter obligatorio.

##### Detalle del circuito

En la imagen puede ver el diagrama completo del circuito.

A través de los siguientes temas puede profundizar sobre cada uno de los puntos.

**Ingreso de solicitudes de compra  
**Por medio de [este proceso](?p=15411) se ingresan las solicitudes de compra efectuadas por los distintos sectores de la empresa, que quedarán registradas como 'pendientes' hasta el momento en que se genere la orden de compra solicitando los artículos al proveedor, se entreguen los artículos con existencias propias de stock, se desautorice la solicitud, se cierre la solicitud o con algún motivo especificado por el responsable.

**Actualización de solicitudes de compra  
**A través de este ítem de menú, puede modificar, eliminar, consultar y reimprimir solicitudes de compra. Podrá visualizar en una grilla los datos principales de todas las solicitudes de compra.  
Al mismo tiempo, usted cuenta con opciones de filtros, que facilitan la búsqueda de estas solicitudes.  
Para más información, consulte [Actualización de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpactualiz_cp2).

**Autorización de solicitudes de compra  
**Este paso es necesario si usted activó el parámetro Autoriza solicitudes.  
Utilice el punto de autorización para revisar sus solicitudes pendientes, desautorizarlas, o autorizarlas por sus cantidades totales o parciales.  
En este proceso es posible, también, realizar modificaciones a las solicitudes ingresadas.  
Puede realizar cualquiera de estas opciones, tanto a nivel del encabezado de la solicitud, como para cada uno de sus renglones.

**Ejemplo...**

  * Marque la solicitud como 'Revisada' cuando quiera indicar al solicitante que la solicitud fue vista y está a la espera de resolución.
  * Marque la solicitud como 'Autorizada' cuando quiera realizar la compra.
  * Marque la solicitud como 'Desautorizada' cuando no acepte el pedido de compra.



Para más información, consulte [Autorización de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpautoriz_cp2).

**Gestión de solicitudes de compra / generación de ordenes de compra  
**Usted cuenta con dos modalidades para cumplir con las solicitudes de compra ingresadas al sistema:

_1\. Gestión de solicitudes de compra  
_Esta opción resulta de mayor utilidad cuando su empresa procesa gran cantidad de solicitudes de compra y desea analizar los pedidos realizados para efectuar compras consolidadas que permitan optimizar costos.  
Este proceso también le brinda la posibilidad de cerrar una solicitud, que por algún motivo en particular, no es posible cumplir.  
Puede administrar la información a nivel global, o decidir puntualmente para cada solicitud de compra, que artículos comprar, cuales entregar desde Stock y cuales cerrar, especificando el motivo de su decisión.

**Ejemplo...  
**Usted cuenta con 3 solicitudes pendientes:

Solicitud 7:  
30 unidades del artículo genérico "Lapicera"  
10 unidades del artículo genérico "Cuaderno"  
Solicitud 8:  
50 unidades del artículo genérico "Lapicera"  
30 unidades del artículo genérico "Cuaderno"  
Solicitud 9:  
10 unidades del artículo "Ventilador de techo madera 4 palas"  
Si usted accede al proceso de gestión de solicitudes de compra, verá agrupada, por artículo, la información de todas las solicitudes pendientes.  
Una vez confirmadas las cantidades a comprar, un asistente lo guiará en el proceso de generación de ordenes de compra.  
Al finalizar, usted contará con las ordenes de compra generadas y disponibles para continuar con el circuito habitual de compras.

Para más información, consulte la ayuda de [Gestión de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpgestion_cp2).

_2\. Generación de órdenes de compra  
_Desde este proceso puede hacer referencia a una o más solicitudes de compra sin necesidad de utilizar la gestión de solicitudes.  
Esta opción le resultará de mayor interés cuando tenga un bajo volumen de solicitudes o su metodología de trabajo no requiera un análisis conjunto antes de generar la orden de compra.  
Para más información, consulte la ayuda de [Generación de órdenes de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2).

**Ingreso de remito / Ingreso de factura - remito** A partir del momento en que ingresa la mercadería al Stock de la empresa, y usted hace referencia a ordenes de compra en la carga de Remito o de Factura - Remito, la solicitud de compra relacionada con estos comprobantes, quedará en estado 'Cumplida' (*), cerrando de este modo el circuito de compras.  
Operaciones tales como [devolución de remitos](https://ayudas.axoft.com/25ar/remdevolucion_cp2), [anulación de remitos](https://ayudas.axoft.com/25ar/remanulacion_cp2), [cierre de orden de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2), [anulación de orden de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2) y [baja de comprobantes](https://ayudas.axoft.com/25ar/comprobaja_cp2), pueden afectar los saldos pendientes de sus solicitudes de compra. Para mayor detalle sobre cambios de estado y administración de saldos pendientes, consulte la ayuda de cada uno de estos procesos en particular.

(*) La mención al estado 'Cumplida' se realiza al sólo efecto de graficar el cierre del circuito. Es posible que una solicitud permanezca con estado "En curso" si la cantidad ingresada no completa la cantidad autorizada para el comprobante.

**Consultas  
**Consulte información relacionada con las solicitudes registradas en el sistema desde el módulo de consultas Live, accediendo por:

  * Solicitudes pendientes de compra.
  * Solicitudes en curso, aún pendientes de entrega.
  * Saldos pendientes, estados y demás información relacionada con las solicitudes de compra, que podrá agrupar, filtrar y personalizar del modo más conveniente para usted.



Desde el proceso de [Solicitudes de compra](https://ayudas.axoft.com/25ar/solicp_cp2), obtenga información sobre:

  * **Estados de las solicitudes y saldos pendientes:** aplique filtros según los datos que precise ver en cada momento (sucursal, sector, fechas de ingreso, fecha de autorización, clasificaciones, etc.). Dependiendo los datos que precise ver, puede acceder a esta información desde: 
    * [Actualización de solicitudes](https://ayudas.axoft.com/25ar/solicpactualiz_cp2).
    * [Gestión de solicitudes](https://ayudas.axoft.com/25ar/solicpgestion_cp2).
    * [Autorización de solicitudes](https://ayudas.axoft.com/25ar/solicpautoriz_cp2).
  * **Historial de movimientos detallado por artículo:** consulte la "trazabilidad" de un artículo, visualizando información de todos los comprobantes relacionados con éste, mediante la [Actualización de solicitudes](https://ayudas.axoft.com/25ar/solicpactualiz_cp2).
