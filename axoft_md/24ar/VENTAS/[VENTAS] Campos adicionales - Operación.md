# Campos adicionales - Operación

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=38893/

## Contenido

# Campos adicionales - Operación

Los procesos disponibles en la nueva plataforma te permiten definir campos adicionales para adaptar al sistema a tus necesidades.

Además de crear nuevos campos, ahora podés organizarlos en solapas e indicar la cantidad de columnas que preferís utilizar en la pantalla para que agrupes y distribuyas los campos de acuerdo con tus necesidades.  
Podés definir campos adicionales de los siguientes tipos:

  * **Texto:** por ejemplo, para que el usuario final ingrese una leyenda.
  * **Texto fijo:** por ejemplo, para que les escribas una aclaración al usuario final.
  * **Links a una URL:** por ejemplo; [www.axoft.com](https://www.axoft.com)
  * **Link dinámico:** permite mantener una URL ingresada por el usuario, en lugar de mantener fija la URL. Puede ser utilizada, por ejemplo, para que el usuario pueda ingresar un link a su propio sitio web.
  * **Número:** por ejemplo, para que ingreses una edad, cantidad o importe.
  * **Fecha:** para que puedas ingresar alguna fecha de referencia al registro. También podés trabajar con fechas relativas utilizando las variables **@Ayer** , **@Hoy** , **@Mañana** , **@Primer_dia_semana** , **@Ultimo_dia_semana** , **@Primer_dia_mes** , **@Ultimo_dia_mes** , **@Primer_dia_año** , **@Ultimo_dia_año**. Si es necesario podés especificar que se muestre también la hora cuando lo creas necesario.
  * **Casilla de verificación:** por ejemplo, para que registres valores cuya respuesta sea Si/No.
  * **Cuadro combinado:** por ejemplo, cuando necesites seleccionar una opción entre valores predefinidos, por ejemplo, sexo masculino o femenino.
  * **Área de texto:** para que el usuario final pueda escribir una leyenda amplia (por ejemplo, la especificación técnica de un producto)



Cada tipo de campo ofrece configuraciones propias, como ser longitud, valores posibles, ingreso obligatorio, cantidad de decimales, mínimo y máximo, etc.  
Para definir campos adicionales seleccioná la opción homónima en la barra de herramientas del proceso.

__Nota

Tené en cuenta que para definir campos adicionales debés tener un permiso específico. Para asignarlo, ingresá al Administrador general > Seguridad > Usuarios > Permisos de administración y, dentro de la rama de permisos correspondiente a Administrador > Empresas > Empresas, seleccioná la opción "Definición de campos adicionales".

Para conocer más sobre campos adicionales mirá este video.

##### Primeros pasos en la definición de campos adicionales

Lo primero que tenés que pensar es cómo vas a organizar la pantalla. Hay dos propiedades que te ayudan en este punto:

  * **Solapas:** al igual que hacemos nosotros, podés organizar tus campos adicionales en distintas solapas. Por defecto los nuevos campos se crearán dentro de una solapa llamada "Campos adicionales", pero si necesitas crear sub-solapas esta herramienta te permitirá hacerlo. Por ejemplo, en el proceso de clientes podrías crear una solapa para datos de marketing y otra para campos específico para tu gestión de clientes.
  * **Disposición vertical:** el próximo tema que debés definir es la cantidad de columnas en la que vas a distribuir los nuevos campos. Por defecto te proponemos hacerlo en 3 columnas que es como mostramos los campos en la mayoría de nuestros procesos, aunque en los que tienen más campos como clientes, artículos, proveedores, etc. trabajamos con cuatro columnas.  
Estas columnas "invisibles" te permiten alinear los campos en pantalla ya que actúan como contenedores donde colocás los campos. Tené en cuenta que tal como te mostramos en el ejemplo que sigue a continuación, podés trabajar en determinadas zonas con un esquema de múltiples (3 en el ejemplo) columnas y otras zonas con una sola columna.



Las columnas también se utilizan cuando ajustamos la pantalla para que se adapten a los dispositivos móviles.

Una vez que definiste cómo vas a organizar tu pantalla, debés comenzar a colocar los campos propiamente dichos. Para ello basta con que los arrastres a su ubicación en pantalla y a continuación pulses el lápiz (en el sector superior derecho del control) para configurar sus propiedades, como ser longitud, valores posibles, ingreso obligatorio, cantidad de decimales, mínimo y máximo, etc.  
Si querés eliminarlo, basta con que pulses sobre el cesto de residuos que se encuentra a la izquierda del lápiz mencionado en el párrafo anterior.  
Una vez que terminaste de configurar la pantalla solo falta que aceptes los cambios.  
Cuando ingreses al proceso verás tu solapa de campos adicionales como te mostramos a continuación:

__Nota

Durante la carga de datos, el botón "Configurar" solo será visible si tenés permiso para crear campos adicionales.

##### ¿En qué lugares del sistema podés utilizar los campos adicionales?

Podés consultar o editar los campos adicionales desde los siguientes procesos:

  * Los procesos donde los creaste.
  * Los [seleccionadores](https://ayudas.axoft.com/24ar/seleccionador_oper).
  * En la [impresión de comprobantes](?p=12000).
  * [Tango Live](?p=9189).
  * [Vistas](https://ayudas.axoft.com/24ar/vistas_oper).
  * [Enviar a...](https://ayudas.axoft.com/24ar/enviar_oper)
  * [API](https://ayudas.axoft.com/24ar/api_oper).
  * En la [importación/exportación desde Excel](https://ayudas.axoft.com/24ar/excel_oper).



A medida que continuemos transformando procesos a la nueva plataforma, podrás utilizar los campos adicionales como criterio de búsqueda; por ejemplo:

Para habilitar esta opción debés tildar la opción "Campo disponible para búsquedas" dentro de las propiedades del campo adicional. Te recomendamos que sólo habilites esta opción en aquellos campos que realmente vas a utilizar para buscar registros, ya que un abuso en la cantidad de campos de búsqueda puede afectar la performance del sistema durante la búsqueda.

##### Contenidos relacionados

  * [Video sobre administración de artículos](https://ayudas.axoft.com/24ar/videos/st_carp_vid/adminarticulos_st_vid/)

  * [Videos sobre conceptos y fórmulas de sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/conceptos_sua_vid/)

  * [Videos sobre historial, vistas, apertura y campos adicionales](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/campoadic__oper_vid/)
