# Guía de Restô sobre perfiles de stock

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st3/guia_perfstock_st3/

## Contenido

# Guía de Restô sobre perfiles de stock

A continuación se detalla la utilidad de los perfiles que puede establecer para cada uno de los procesos del módulo.

La definición de los perfiles tiene como objetivo agilizar o restringir el ingreso de datos, como las distintas opciones que permite realizar cada uno de los procesos de Stock. De esta forma, usted establece para su empresa diferentes perfiles, asignándolos a los distintos usuarios en base a las tareas que realicen, cargos que ocupen o bien restricciones y permisos que los diferencien.  
Recuerde que un [Parámetro General](?p=25988) de Stock se aplica a nivel general. A través de los perfiles puede habilitar algunos de esos parámetros si fueron restringidos a nivel global. Usted puede definir distintos perfiles, y a cada uno de ellos puede tener asociado a uno o más usuarios.  
Se podrán configurar perfiles para las siguientes operaciones:

  * Ingresos de Stock
  * Egresos de Stock
  * Transferencias entre Depósitos
  * Toma de Inventario
  * Ajustes de Inventario
  * Armado



Cabe mencionar que la definición de perfiles no es obligatoria. Si un usuario no tiene asignado ningún perfil, tiene disponibles todas las funciones del proceso. Las posibilidades son las siguientes:

  * Si no se definieron perfiles, se ingresarán todos los datos en forma normal.
  * Si el usuario que ingresa tiene definido un sólo perfil, éste será el que se utilizará en el proceso.
  * Si el usuario que ingresa tiene definido más de un perfil, podrá seleccionar el perfil a utilizar.
  * Si se definieron perfiles pero el usuario que ingresa no está asignado a ninguno de ellos, se ingresarán todos los datos en forma normal (como si no existieran perfiles definidos); es decir, sin restricciones.



Recuerde que el alta y modificación de usuarios se realiza desde el Administrador del Sistema.

##### Puesta en marcha

Para definir que un determinado usuario opere bajo un perfil debe realizar el procedimiento detallado a continuación:

1) Desde Archivos | Carga Inicial | Perfiles elija una de las opciones:

  * de Ingresos de Stock
  * de Egresos de Stock
  * de Transferencias entre Depósitos
  * de Toma de Inventario
  * de Ajustes de Inventario
  * de Armado



2) Defina los parámetros correspondientes a ese perfil, para ello:

  1. Haga clic en el menú Agregar.
  2. Defina un código para el nuevo perfil e ingrese una descripción. Complete el resto de los campos de las ventanas, confirmando con <F10>.



3) Luego de ingresar todos los valores necesarios, indique los usuarios que tendrán el perfil asociado. Tenga en cuenta que no es obligatorio que asigne usuarios en este momento.

Para asociar usuarios a un perfil existente seleccione el comando Usuarios.  
Recuerde que los distintos procesos de inventario tienen operaciones en común, por lo tanto, al momento de asignar perfiles a una persona que utiliza varios procesos procure mantener una relación entre parámetros iguales.  
Si un ayudante sólo puede hacer egresos y ajustes al depósito 'cocina general'. Tenga en cuenta que deberá restringir en el perfil de ajustes, el tipo de ajuste a 'SALIDA' y como depósito al 'cocina general'.

**Ejemplo de implementación...  
**A continuación detallaremos los puntos más importantes a configurar en cada uno de los distintos tipos de perfiles en base a los distintos procesos que se llevan a cabo dentro del módulo de Stock, adjuntando un ejemplo para cada caso.  
El ejemplo se basa en un restaurante que cuenta con varios depósitos, entre ellos: el depósito general y depósito cocina general. Se muestra la actuación de 2 personas en cada uno de los depósitos.

  * El depósito 4 denominado "depósito general", estará a cargo de recepcionar los alimentos que provienen de los proveedores y, a su vez, abastecer al Depósito 6: "depósito cocina general".
  * El depósito 6, designado para el armado de menúes, postres, etc., que van a ser traspasados a los distintos depósitos de venta.



Se determinarán 2 estilos de perfil:

  * El perfil 1 corresponde a Encargado / jefe de depósitos, quienes tienen a su cargo el control del depósito, y a su vez actúan como nexos entre ambos Depósitos y el resto de los depósitos de venta.
  * El perfil 2 corresponde a Repositor / Repostero de sus respectivos depósitos, la tarea de ellos consiste en la registración de los artículos y el armado de comidas que serán posteriormente comercializadas.



**Perfil ingreso de stock  
**Los perfiles creados podrán ser utilizados para el [Ingreso de Stock](?p=25958). Estableciendo perfiles agilizará la carga del comprobante. Usted podrá determinar que el perfil ingrese artículos valorizados o no restringiendo los comprobantes a utilizar. Asimismo, de ser necesario, podrá establecer un depósito fijo para el ingreso de los artículos.

_Perfil encargado del Depósito general_

  * Puede utilizar cualquier tipo de comprobante.
  * Tiene asignado el depósito 4 por defecto, con la posibilidad de ser modificado, ya que como Encargado puede sustituir a un Encargado de otro depósito.
  * Valoriza por última compra, visualiza y puede modificar el precio.



_Perfil repositor del Depósito general_

  * Ingresa sólo Comprobantes llamados "ENT".
  * Tiene asignado el depósito 4 por defecto debido a que sólo trabaja para éste depósito.
  * Valoriza por última compra y no edita el precio.
  * Para agilizar el Ingreso, debido al gran volumen de artículos que recepciona, se habilita la opción de carga rápida para utilizar con su pistola (lectora de código de barras).



**Perfil ajustes de inventario de stock  
**Creando perfiles podrá delimitar el tipo de ajuste que realizará cada perfil, como así también definir los depósitos donde se podrá realizar el ajuste. Otra de las opciones que permite predeterminar a nivel perfil es la Sucursal destino hacia la cual se exportará el ajuste.

_Perfil encargado del Depósito general_

  * Realiza Ajustes de tipo Entrada / Salida.
  * Visualiza y modifica la Cotización y Moneda del comprobante.
  * Puede establecer una sucursal destino para la cual se importará el comprobante.



_Perfil repositor del Depósito general_

  * Sólo tendrá permiso a realizar Ajustes de tipo Entrada.
  * No visualiza la Cotización ni la Moneda del comprobante.
  * Tendrá asignado el depósito 4 por defecto.



**Perfil transferencias entre Depósitos  
**La generación de los perfiles le permitirá entre otras opciones restringir los depósitos desde los cuales se llevará acabo la transferencia.

_Perfil encargado del Depósito general_

  * Asigna el depósito 'origen' y 'destino', ya que puede suceder que quiera sacar los insumos del depósito 4 y no enviarlos al depósito cocina general, es decir, enviarlos directamente a cualquier otro depósito destinado a la venta ( ej: depósito sector barra, sector terraza, sector delivery, etc).
  * Agrega observaciones.
  * Puede ver y editar leyendas.



_Perfil repositor del Depósito general_

  * Tiene asignado al depósito 4 como 'origen' y al depósito 6 como 'destino'.
  * No agrega observaciones.
  * No edita leyendas.



**Perfil de armado  
**Los perfiles creados tendrán alcance en los procesos [Armado de recetas](?p=25891) y [Armado según Modelo](?p=25890). Si bien podrá predeterminar el tipo de comprobante y depósitos a utilizar por perfil, puede suceder que a un perfil también se le asigne un modelo de armado en el cual estos parámetros no coincidan con los predeterminados. Luego, en base a lo establecido dentro del perfil, podrá o no modificarlos.

_Proceso de armado  
_Se podrá establecer a nivel perfil los comprobantes disponibles a utilizar en el momento de generar el armado. También es importante poder delimitar el depósito Origen (desde el cual se extraerán los insumos) y el depósito Destino (en el que quedarán los productos listos para vender).

_Armado según modelo  
_Para que este proceso opere bajo las restricciones establecidas dentro de un perfil, deberá asignar dentro del perfil aquellos modelos de armado que podrá utilizar. Una vez asignados los modelos, podrá determinar los perfiles que tendrán acceso a la modificación del modelo (valorización de salidas, método de armado, agregar y/o cambiar artículos).  
Tenga en cuenta que de poder agregar más artículos que los existentes en el modelo, los parámetros: depósito, valorización de salidas, método de armado comenzarán a regirse por el perfil.

_Perfil jefe de Depósito cocina general_

  * Selecciona tanto el depósito 'Origen' como el 'Destino'.
  * En caso de querer modificar la configuración predeterminada, establece cualquier Método de descarga para partidas de insumos.
  * Modifica el Costo Standard sin límites.
  * Se le asignarán todos los modelos de armado (menúes, postres, etc.) con la posibilidad de modificarlos.
  * Accederá a la impresión del Informe de control.Perfil repostero del Depósito cocina general.
  * No modifica los depósitos 'Origen' y 'Destino' ya que sólo utiliza insumos del depósito para el cual trabaja, debiendo dejarlos disponibles en el mismo lugar.
  * No Modifica el Método de la descarga para la partidas de insumos.
  * No tiene permiso para modificar el Costo Standard.
  * Como es repostero, sólo le asignarán modelos de armado referidos a postres, utilizando un método de armado (según artículo) sin posibilidad de modificarlo.



**Perfil toma de inventario  
**Creando perfiles puede dividir el circuito en 2 etapas, la [Toma de inventario](?p=26151) y el [Ajuste que resulta de las diferencias](?p=25885). También puede permitir a nivel perfil distintas acciones y opciones pertenecientes a la Toma de Inventario.

_Perfil jefe del Depósito cocina general_

  * Puede agregar y eliminar marcadería.
  * Realiza ajuste y puede seleccionar comprobantes disponibles.
  * Anula diferencias.



_Perfil repostero del Depósito cocina general_

  * Agrega artículos pero no puede eliminarlos.
  * Realiza toma de inventario ciega.
  * No puede anular la toma.
  * No anula diferencias.
  * No procesa diferencias.
  * No anula conteo.



**Perfil egreso de stock  
**La creación de los perfiles le permitirá restringir el depósito desde el cual se realizará el egreso, y la Sucursal Destino hacia la cual se exportará el comprobante.

_Perfil jefe del Depósito cocina general_

  * Establece el depósito y Sucursal Destino.
  * Egresa Bienes de Uso.
  * Agrega descripción adicional.
  * Valoriza por última compra, visualiza y puede modificar el precio.



_Perfil repostero del Depósito cocina general_

  * Tiene asignado por defecto al depósito 6 por medio del cual realiza los egresos.
  * No puede egresar bienes de uso.
  * Valoriza por última compra, visualiza pero no puede modificar el precio.



##### Detalle del circuito

El circuito de perfiles incluye los siguientes procedimientos:

  * Perfil de ingreso de stock
  * Perfil de egresos de stock
  * Perfil de transferencia entre Depósitos
  * Perfil de toma de inventario
  * Perfil de ajustes de inventario
  * Perfil de armado ( Proceso de armado - Armado según modelo)



Además, usted puede definir [Permisos Eventuales](?p=26097) para indicar las acciones qué sólo pueden se realizadas mediante el ingreso de una contraseña (clave de autorización temporal) por parte de un usuario autorizado.

**Valores en perfiles de Stock** En el momento de ingresar a un proceso, de acuerdo al perfil o los perfiles aplicados al usuario registrado en el sistema, se aplicarán los siguientes controles:

  * Si no se definieron perfiles, se ingresarán todos los datos en forma normal (con las restricciones indicadas en [Parámetros generales](?p=25988)). Eso mismo sucederá si se definieron perfiles, pero el usuario que ingresa no está asignado a ninguno de ellos.
  * Si el usuario que ingresa tiene definido un sólo perfil, éste será el que se utilizará en el proceso.
  * Si el usuario que ingresa tiene definido más de un perfil, podrá seleccionar desde una ventana el perfil a utilizar.



Para cada perfil es posible definir el comportamiento de cada uno de los campos:

**Valor posible** | **Descripción**  
---|---  
E | El campo se edita en forma normal.  
M | El campo no se edita, muestra el valor por defecto asignado.  
O | El campo toma el valor asignado en este proceso pero no se ve en pantalla (oculto).  
Z | El campo será editable en los procesos que utilicen el perfil. Para modificar el valor el usuario habilitado debe ingresar su contraseña en la ventana de solicitud de autorización.  
J | En este caso se debe asignar el rango dentro del cual es posible realizar la modificación del valor del campo. Este rango se fija mediante un porcentaje que indica el límite superior (% Sup.) y el inferior (% Inf.). Usted puede establecer los dos límites o sólo uno de ellos. Si al modificar este valor el dato ingresado está fuera de estos límites, se solicitará autorización.  
  
Además de este parámetro, podrá ingresar valores por defecto para los diferentes campos. Estos valores se comportan de la siguiente manera:

  * Si el campo se edita, el ingreso de un valor por defecto no es obligatorio en el perfil.
  * Si el campo no se edita, el ingreso de un valor por defecto es obligatorio.



Para obtener un modelo de implementación de estos valores, consulte los tópicos [Aplicar permisos eventuales](?p=26097).

**Cambio de perfiles  
**Si una vez dentro de un proceso del módulo Stock es necesario cambiar de perfil, por ejemplo por cambio de turno del personal, simplemente seleccionar la opción Perfil del menú de la ventana del proceso y elija el perfil desde el listado.  
Al volver a emitir comprobantes de stock operará en base al último perfil seleccionado.
