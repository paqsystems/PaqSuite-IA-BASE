# Aplicar permisos eventuales en Stock

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/gua_perfil_st/?p=17228/

## Contenido

# Aplicar permisos eventuales en Stock

Si trabaja con perfiles de stock puede definir permisos eventuales para que un usuario determinado, mediante una clave temporal, autorice la modificación de ciertos campos (con restricciones para ese perfil) al momento de estar ingresando o egresando artículos.

El usuario a ingresar debe estar definido como un usuario del sistema.  
No es necesario que la contraseña que usted ingrese en este proceso coincida con la definida en el sistema.  
Los usuarios autorizantes deben tener asociado el perfil de stock en el cual se encuentre los datos a autorizar y para éstos la opción 'Edita'.  
Si eligió para un dato la opción 'Autoriza' o 'Fija Límite', es necesario que defina desde este proceso, un nombre de usuario y su contraseña para cada una de aquellas personas habilitadas para autorizar.  
De esa manera, podrá definir acciones que deberán ser autorizadas por un usuario responsable, por ejemplo, un supervisor.  
La correcta configuración de permisos eventuales permite que todas las operaciones transcurran bajo el usuario que está operando, evitándose el egreso e ingreso al sistema de otro usuario para realizar una operación determinada, obteniendo mayor flexibilidad y seguridad ante determinadas situaciones de trabajo.

Las acciones que puede requerir autorización serán las que afecten al total del comprobante:

  * Modificación del Precio Unitario.
  * Modificación del Costo Standard (para el Proceso de Armado).



Desde los renglones es posible invocar la función Autorización, a través de las Funciones Disponibles para seleccionar los campos a autorizar e ingresar la contraseña una sola vez.  
Para los renglones del comprobante, la función Autorización permite afectar todos los renglones o bien, sólo el actual (renglón en el que se encuentra posicionado).  
Cada vez que modifique un dato que requiere autorización, se graba una auditoria de autorizaciones. Para más información, consulte el proceso [Auditoría de autorizaciones](?p=17042).

##### Comando Usuarios

Una vez generado un perfil, es necesario asociar a los usuarios habilitados para utilizarlo.

A través de este comando, se ingresarán los usuarios habilitados para el perfil activo (el que se encuentra en pantalla).

El sistema sugerirá, por defecto, el usuario que está trabajando en ese momento en el sistema, siendo posible agregar otros.

Luego de ingresar el último usuario, es necesario posicionarse en el renglón siguiente pulsando <Enter> y confirmar el proceso para que se almacenen los datos ingresados.

**Ejemplo de aplicación de permisos eventuales**

En el siguiente ejemplo, explicamos cómo es la forma de trabajar con el sistema si usted aplica claves de autorización a distintos datos dentro de un proceso de stock (Ingresos, Egresos, Ajustes, Transferencias, Proceso de Armado).

El usuario que ingresa un comprobante está vinculado a un perfil con determinadas restricciones. Una de ellas se refiere a la modificación del precio unitario de los artículos, que sólo le está permitida a través del ingreso de una clave autorizante.

Al ingresar un determinado comprobante es necesario modificar el precio de un artículo. En ese caso, el sistema solicita un código de autorización o contraseña, que será ingresado por el encargado de autorizar este cambio.

Al salir del campo no se podrá volver a realizar ninguna modificación sobre el mismo. Para ello, se debe ingresar nuevamente la clave correspondiente.

##### Contenidos relacionados

  * [Video sobre movimientos masivos de stock](https://ayudas.axoft.com/24ar/videos/st_carp_vid/movimasivo_st_vid/)

  * [Video sobre parámetros de stock](https://ayudas.axoft.com/24ar/videos/st_carp_vid/parametrostock_st_vid/)

  * [Video sobre perfiles y movimientos de stock](https://ayudas.axoft.com/24ar/videos/st_carp_vid/perfmovstock_st_vid/)

  * [Video sobre permisos eventuales](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/permisoevent_gral_vid/)
