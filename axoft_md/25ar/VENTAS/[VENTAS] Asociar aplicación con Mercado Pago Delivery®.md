# Asociar aplicación con Mercado Pago Delivery®

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_mpd_gv3/?p=20554/

## Contenido

# Asociar aplicación con Mercado Pago Delivery®

A continuación, explicamos la configuración específica a aplicar para recibir las notificaciones de pedidos desde **Mercado Pago Delivery®** y sincronizarlos con **Tango Restô**.

Aclaración:

Para poder utilizar esta funcionalidad debe tener contratada una licencia comercial Tango Tiendas Restô.

Ingrese a la opción de menú Mercado Pago Delivery. Presione el botón "Asociar" e introduzca los datos de la cuenta de Mercado Pago®.  
Si ha iniciado sesión en Mercado Pago® en el navegador de Internet donde esté ejecutando Tango Tiendas, y desea asociar una nueva cuenta, recuerde que debe cerrar la sesión activa. Se mostrará la pantalla donde le concede el permiso a Mercado Pago® a asociarse con el sitio, donde debe presionar el botón "Permitir". Esta pantalla solo aparecerá si es la primera vez que realiza la asociación en su cuenta de Mercado Pago® y su cuenta de Tango Tiendas.

##### Configuración

###### Comercios sin sucursales

Si no definió sucursales en **Mercado Pago Delivery®** no hace falta realizar otra configuración desde **Tango Tiendas** , puede continuar con los pasos de la [Guía de implementación de Mercado Pago Delivery®](?p=26911) en **Tango Restô**.

###### Comercios con sucursales

Si su comercio cuenta con varias sucursales definidas debe especificar a continuación qué sucursal de **Mercado Pago Delivery®** va a ser atendida por el sistema **Tango Restô** que está relacionando en esta acción.  
En el ejemplo que mostramos a continuación puede ver como recomendamos vincular cada una de las sucursales de**Tango Restô** con cada sucursal de **Mercado Pago Delivery®**

Tenga en cuenta que para realizar esta acción debe vincular **Tango Tiendas** a cada uno de los sistemas.  
A continuación brindamos una guía de ejemplo para la configuración:

  * Ingrese a **Tango Restô** de la empresa 1, luego acceda al módulo Aplicaciones Nexo\Tango Tiendas y asocie la empresa 1 siguiendo los pasos mencionados mencionados mas arriba en el punto "Asociar aplicación con Mercado Pago Delivery", en la sección de sucursales tilde la fila que representa a la Sucursal 1 (no seleccione las filas que representan a las sucursales 2 y 3)
  * Ingrese a **Tango Restô** de la empresa 2, siga los mismos pasos especificados en el punto anterior, pero tilde en este caso la fila que representa a la sucursal 2. En esta ocasión la primera fila estará deshabilitada (ya que la sucursal está asociada a la empresa 1)
  * Ingrese a **Tango Restô** de la empresa 3, siga los mismos pasos especificados en el punto anterior, pero en este caso tilde la fila que representa a la sucursal 3. En esta ocasión la primera y segunda fila estarán deshabilitadas (ya que las sucursales están asociadas a las empresas 1 y 2)



Independientemente de la empresa con la que ingrese a Tango Tiendas siempre verá todas las sucursales definidas en **Mercado Pago Delivery®,** ya que pertenecen a la misma cuenta, pero solo podrá modificar la que corresponda a la empresa de Tango con la que ingresó.

#### 

###### Consideraciones en el caso que prefiera atender desde un Tango Restô varias sucursales de Mercado Pago Delivery

En el caso que quiera atender varias sucursales de **Mercado Pago Delivery®** desde un solo sistema Tango, siga las indicaciones del punto de configuración para "Comercios con sucursales", pero tilde las sucursales que quiere atender con el sistema que está configurando. Por ejemplo, puede configurar a **Tango Tiendas** para que el sistema 1 de **Tango Restô** atienda a las sucursales 1 y 2 de **Mercado Pago Delivery®** y que el sistema **Tango Restô** 2 atienda a la sucursal 3 de **Mercado Pago Delivery®**.

Importante:

Tenga en cuenta que una vez que ingreso un pedido a un sistema **Tango Restô** no puede ser derivado a otro para que lo atienda.

Para conocer cómo parametrizar su instalación de Tango Restó y recibir pedidos de Mercado Pago Delivery® consulte la [Guía de implementación de Mercado Pago Delivery®](?p=26911) en Tango Restô.
