# Guía sobre definición de perfiles de ventas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg3685_gla/?p=27001/

## Contenido

# Guía sobre definición de perfiles de ventas

Usted puede definir perfiles según [usuarios](?p=9111), de modo que algunos procesos operen en base a diferentes parametrizaciones y permisos según aquel que los ejecute. Los perfiles permiten adaptar el ingreso de datos a las necesidades de su empresa, como así también determinar restricciones para algunos usuarios en particular, otorgando permisos sobre determinadas operaciones.

De esa manera, usted puede definir distintos perfiles, y cada uno de ellos puede tener asociado a uno o más usuarios.  
Al definir un perfil de usuario, es posible configurar los permisos sobre cualquiera de las siguientes operaciones:

  * [Ingreso de pedidos](?p=19344)
  * [Facturación](?p=19415)
  * [Emisión de notas de crédito](https://ayudas.axoft.com/25ar/emisionc_gv)
  * [Cierre de caja](https://ayudas.axoft.com/25ar/perfilcierrecajapos_gv)
  * [Remitos](https://ayudas.axoft.com/25ar/remito_carp_gv)
  * [Cotizaciones](https://ayudas.axoft.com/25ar/cotizacionperfconsintcli_gv)
  * [Aprobación](https://ayudas.axoft.com/25ar/perfilaprobac_gv)
  * [Gestión de clientes](https://ayudas.axoft.com/25ar/consintegralcliente_gv)
  * [Consulta de precios y saldos de stock](https://ayudas.axoft.com/25ar/perfconsprecstock_gv)



Antes de comenzar con la implementación, le recomendamos tener en cuenta las siguientes consideraciones previas:

  * Por defecto, la definición de perfiles no es obligatoria. Si un usuario no tiene asignado ningún perfil, entonces estarán disponibles todas las funciones y se podrán ingresar todos los datos que prevé el sistema (algunos de estos valores surgen de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-controles), [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv) o [Talonarios](https://ayudas.axoft.com/25ar/talonario_gv)).  
Recuerde que, de ser necesario, puede configurar que la asignación de perfiles sea obligatoria en la sección Parámetros para controles de los [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-controles). De esta manera, si un usuario no tiene un perfil asignado no podrá ingresar al proceso solicitado.
  * De ser necesario, ahora puede deshabilitar un perfil sin necesidad de eliminarlo o de quitarle los usuarios asignados como lo hacía anteriormente. Puede hacerlo de forma provisoria mientras realiza cambios o permanente hasta que decida eliminarlo. Recuerde que, a través de la vista personalizada, puede consultar solo los perfiles habilitados.
  * Puede utilizar la tecla rápida <F3> para buscar un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran. Además, puede realizar búsquedas en la grilla para saber con qué perfiles trabaja un usuario en particular o dentro del perfil para ubicar un campo en particular.
  * Recuerde que, debe realizar el alta y modificación de usuarios desde el [Administrador del sistema](?p=9063).



##### Puesta en marcha

Para definir que un determinado [usuario](?p=9111) opera bajo un perfil, debe realizar el procedimiento detallado a continuación:

1) Desde Archivos | Carga Inicial | Perfiles elija una de las opciones:

  * [Perfiles de pedidos](?p=10286). 
    * Defina [permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv) para aplicar claves de autorización temporaria mientras ingresa pedidos.
  * [Perfiles de facturación](https://ayudas.axoft.com/25ar/perfilfacturacion_gv). 
    * Definir [permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv) para aplicar claves de autorización temporaria mientras factura.
  * [Perfiles de medios de pago para facturas y pedidos](?p=19175).
  * [Perfiles de notas de crédito](https://ayudas.axoft.com/25ar/perfilnotacredito_gv). 
    * Definir [permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv) para aplicar claves de autorización temporaria mientras ingresa comprobantes de crédito.
  * [Perfiles de cierre de caja](https://ayudas.axoft.com/25ar/perfilcierrecajapos_gv).
  * [Perfiles de remitos](https://ayudas.axoft.com/25ar/perfilremito_gv). 
    * Definir [permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv) para aplicar claves de autorización temporaria mientras remite.
  * [Perfiles de gestión de clientes](https://ayudas.axoft.com/25ar/perfconsintegrcliente_gv).
  * [Perfiles de aprobación](https://ayudas.axoft.com/25ar/perfilaprobac_gv).
  * [Perfiles de consulta de precios y saldos de stock](https://ayudas.axoft.com/25ar/perfconsprecstock_gv).



2) Defina los parámetros correspondientes a ese perfil, para ello:

  * Haga clic en el botón "Nuevo" del menú.
  * Defina un código para el nuevo perfil e ingrese una descripción. Complete el resto de los campos requeridos en cada una de las solapas.



3) Luego de ingresar todos los valores necesarios para la creación del perfil, el sistema le preguntará si habilita usuarios, al contestar afirmativamente debe definir el o los usuarios que operarán en base al nuevo perfil.

__Nota

Tenga en cuenta que no es obligatorio que asigne usuarios en este momento.

Seleccione la solapa Usuarios para designar los usuarios habilitados al perfil.

**Ejemplo de implementación:  
**Tomemos el caso de una empresa que comercializa electrodomésticos en forma mayorista y minorista (mostrador). Por lo tanto tiene dos circuitos totalmente diferentes para ambas operaciones.  
Posee 2 vendedores para atender y facturar a los clientes minoristas en el salón, 1 vendedor para la venta mayorista, y el gerente comercial.

  * Alberto Rodríguez (vendedor minorista)
  * Laura González (vendedora minorista)
  * Patricia Quiroga (vendedor mayorista)
  * Juan Rodrigo López (gerente comercial)



_Creación de Usuarios_  
Desde el [Administrador del sistema](?p=9063) se accede al [Administrador de usuarios](?p=9111) para crear los usuarios que intervienen en las operaciones de ventas.  
Para más información sobre el alta y modificación de usuarios, consulte la [sección correspondiente](?p=9111) en la ayuda del Administrador del Sistema.  
En el caso del ejemplo se definen los siguientes usuarios:

  * Alberto Rodríguez (vendedor minorista)
  * Laura González (vendedora minorista)
  * Patricia Quiroga (vendedor mayorista)
  * Juan Rodrigo López (gerente comercial)



_Perfiles de Facturación  
_Para este esquema debemos generar 3 perfiles, uno para cada tarea, y luego relacionar cada usuario con el perfil de su tarea.  
Mencionamos ahora, algunos de los puntos más importantes a definir en dichos perfiles de acuerdo con los circuitos planteados en nuestro ejemplo:

  * _Perfil Vendedor Minorista_
    * Descarga stock al facturar (como efectúa venta mostrador, no existe remito ya que la factura es el comprobante de entrega)
    * No utiliza límite de crédito (las ventas son a clientes ocasionales y al contado).
    * Items Grales para facturas: 
      * No edita comprobantes de referencia (la operación comienza y termina en la factura).
    * Items del encabezado: 
      * Edita talonarios para facturas, pero muestra por defecto el talonario 'B' (habitualmente son consumidores finales, pero eventualmente el cliente puede solicitar factura 'A').
      * No edita bonificación del cliente (no son clientes habituales).
      * No edita lista de precio, y coloco por defecto la lista de precio minorista.
      * Edita vendedor.
    * Items de artículos: 
      * No edita precio del artículo
      * Bonificación del artículo: autoriza fuera del límite (10%). En este caso el sistema solicitara la autorización del Gerente Comercial para bonificar más de un 10%.
    * Items de Tesorería: 
      * Cobro al contado: SI (de esta manera se agiliza la atención al cliente, teniendo la facturación y cobranza en la misma pantalla, y pudiendo calcular recargos automáticos al cobrar con tarjetas de crédito).



Por último, se relaciona este perfil a los dos usuarios (vendedores minoristas).

  * _Perfil vendedor mayorista_
    * No descarga stock al facturar (la mercadería sale respaldada con un remito).
    * Utiliza límite de crédito "a confirmar" (de esta manera el vendedor sabe que la operación excede dicho límite pero puede continuar. De lo contrario podríamos parametrizar controles más estrictos).
    * Items Generales para facturas: 
      * Edita comprobantes de referencia (puede referenciar al pedido ingresado o bien al remito).
    * Items del encabezado: 
      * Edita talonarios para facturas, pero muestra por defecto el talonario 'A' (habitualmente son R.I. los clientes mayoristas, pero eventualmente se puede facturar 'B').
      * Edita bonificación del cliente (ya que dependiendo del volumen de la compra, puede tener descuentos especiales).
      * Edita condición de venta, pero por defecto toma la del cliente.
      * No edita lista de precio, colocando por defecto la lista de precio mayorista.
      * No edita vendedor (por defecto Patricia Quiroga, ya que es la única vendedora del sector).
      * Edita transporte (por defecto colocamos el transporte propio).
    * Items de artículos: 
      * Edita precio del artículo con clave de autorización.
      * Bonificación del artículo: Autoriza fuera del límite (10%), y por defecto trae la bonificación "cliente/artículo". (En este caso el sistema solicitará la autorización del Gerente Comercial para bonificar más de un 10%).
    * Items de Tesorería: No es relevante su parametrización, ya que la facturación a clientes mayoristas nunca es de contado.



Por último se relaciona este perfil al usuario Patricia Quiroga (vendedor mayorista).

  * _Perfil Gerente Comercial:_ gran parte de los parámetros mencionados en los perfiles previos son indiferentes si se utilizará el perfil sólo para autorizar ciertos valores que deseen modificar los vendedores.  
Los campos a autorizar en este ejemplo deben parametrizarse de la siguiente manera: 
    * Items de artículos: 
      * Precio del artículo: Edita
      * Bonificación del artículo: Edita



De esta manera, cuando los vendedores deseen editar un precio o una bonificación más allá de lo permitido en su perfil, el gerente coloca su clave y edita dichos valores.  
Por último, se relaciona este perfil al usuario Juan Rodrigo López (Gerente Comercial).

##### Detalle del circuito

Para implementar el circuito de perfiles, puede realizar cualquiera de los siguientes procedimientos:

  * [Perfiles de pedidos](?p=10286)
  * [Perfiles de facturación](https://ayudas.axoft.com/25ar/perfilfacturacion_gv)
  * [Perfiles de medios de pago para facturas y pedidos](?p=19175)
  * [Perfiles de notas de crédito](https://ayudas.axoft.com/25ar/perfilnotacredito_gv)
  * [Perfiles de cierre de caja ](https://ayudas.axoft.com/25ar/perfilcierrecajapos_gv)
  * [Perfiles de remitos](https://ayudas.axoft.com/25ar/perfilremito_gv)
  * [Perfiles de gestión de clientes](https://ayudas.axoft.com/25ar/perfconsintegrcliente_gv)
  * [Perfiles de aprobación](https://ayudas.axoft.com/25ar/perfilaprobac_gv)
  * [Perfiles de consulta de precios y saldos de stock](https://ayudas.axoft.com/25ar/perfconsprecstock_gv)



Además, usted puede definir [permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv) para indicar las acciones qué sólo pueden ser realizadas mediante el ingreso de una contraseña (clave de autorización temporal) por parte de un usuario autorizado (por ejemplo el ingreso de [perfiles de aprobación](https://ayudas.axoft.com/25ar/perfilaprobac_gv) con descuento o la generación de notas de crédito a partir de un importe determinado).  
Los comportamientos y controles detallados en este tópico son válidos para todos los perfiles definidos.  
En el momento de ingresar a un proceso, de acuerdo con el perfil seleccionado, se aplicarán los siguientes controles:

  * Si no se definieron perfiles, se ingresarán todos los datos en forma normal (sin restricciones). Eso mismo sucederá si se definieron perfiles, pero el usuario que ingresa no está asignado a ninguno de ellos o si el perfil se encuentra inhabilitado.
  * Si el usuario que ingresa tiene definido un sólo perfil habilitado, éste será el que se utilizará en el proceso.
  * Si el usuario que ingresa tiene definido más de un perfil habilitado, podrá seleccionar el perfil a utilizar antes de iniciar el proceso seleccionado.



**Comportamientos de campos**  
Salvo algunos casos especiales que se detallarán en particular, los comportamientos posibles para cada uno de los campos a parametrizar son:

**Comportamiento posible** | **Descripción**  
---|---  
Edita | El campo se edita en forma normal.  
Muestra | El campo no se edita, muestra el valor por defecto asignado.  
Oculta | El campo toma el valor asignado en este proceso pero no se ve en pantalla (oculto).  
Autoriza | El campo será editable en los procesos que utilicen el perfil. Para modificar el valor el usuario habilitado debe ingresar su contraseña en la ventana de solicitud de autorización.  
Autoriza fuera de límite | En este caso se debe asignar el rango dentro del cual es posible realizar la modificación del valor del campo. Este rango se fija mediante un porcentaje que indica el límite superior (porcentaje superior) y el inferior (porcentaje inferior). Usted puede establecer los dos límites o sólo uno de ellos. Si al modificar este valor el dato ingresado está fuera de estos límites, se solicitará autorización.  
  
Además de este parámetro, podrá ingresar valores por defecto para los diferentes campos. Estos valores se comportan de la siguiente manera:

  * Si el campo se edita, el ingreso de un valor por defecto no es obligatorio en el perfil. Si existe un valor por defecto, se utilizará para los clientes ocasionales o cuando no exista el valor habitual en el cliente.
  * Si el campo no se edita, el ingreso de un valor por defecto es obligatorio. Se utilizará para los clientes ocasionales o cuando no exista el valor habitual en el cliente.



Para conocer más sobre las acciones que pueden requerir autorización (comportamiento autoriza o autoriza fuera de límite), consulte [Aplicar permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv).

**Tipos de controles de campos  
**Otros campos detallan el tipo de control que se debe realizar sobre una función (por ejemplo, en el control de límite de crédito):

**Tipo de control posible** | **Descripción**  
---|---  
Estricto | El sistema controla y no deja continuar.  
Flexible con confirmación | El sistema controla y solicita confirmación para continuar.  
Flexible sin confirmación | El sistema no controla y deja continuar.  
  
##### Contenidos relacionados

  * [Facturación masiva de pedidos de Tango Tiendas](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/factmas_carp_posgv/factmaspedtienda_posgv/)

  * [Perfiles de Ventas](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/cargainicial_carp_gv/perfil_carp_gv/)

  * [Video sobre direcciones de entrega](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/direntrega_gv_vid/)

  * [Video sobre manejo de señas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/senas_gv_vid/)

  * [Video sobre perfiles de facturación](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/perfact_gv_vid/)

  * [Videos sobre cierres de caja](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/cierrecaja_gral_vid/)
