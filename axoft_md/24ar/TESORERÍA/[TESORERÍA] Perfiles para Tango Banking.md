# Perfiles para Tango Banking

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_tangobanking_sb/?p=8376/

## Contenido

# Perfiles para Tango Banking

Este proceso actualiza los perfiles de usuarios para _Tango Banking_. Los perfiles pueden ser utilizados en el proceso  _Consultas de saldos y movimientos_.

Los perfiles para Tango Banking permiten determinar valores habituales y restricciones para los usuarios en el proceso de consulta de Tango Banking, según las necesidades propias de su empresa.  
La definición de perfiles no es obligatoria. De no existir ningún perfil definido, se observarán todos los datos que prevé el sistema.  
Para cada perfil definido se asignarán los usuarios autorizados a utilizar el perfil.  
En el momento de ingresar al proceso correspondiente, el sistema realizará los siguientes controles:

  * Si no se definieron perfiles, se observarán todos los datos en forma normal.
  * Si el usuario que ingresa tiene definido un sólo perfil, éste será el que se utilizará en el proceso.
  * Si se definieron perfiles pero el usuario que ingresa no está asignado a ninguno de ellos, se observarán todos los datos en forma normal (como si no existieran perfiles definidos); es decir, sin restricciones.



Al definir un perfil usted visualizará distintas solapas, cada una de ellas contiene un grupo de parámetros correspondiente a las distintas características del proceso.

##### Principal

Código: identifica al perfil. Ingrese el código a asignar o bien, al menos un dígito. Este código es determinado por usted.

Descripción: nombre del perfil.

Muestra saldo de Tesorería y diferencia: será posible aplicar la condición de mostrar u ocultar el saldo de Tesorería y la diferencia en el proceso de Consulta de cuentas de Tango Banking al perfil que se está creando.

Muestra últimos movimientos: será posible aplicar la condición de mostrar u ocultar los últimos movimientos realizados en el proceso Consulta de cuentas de Tango Banking al perfil que se está creando.

Periodo: será posible definir por defecto que periodo desea ver en últimos movimientos del proceso Consulta de saldos y movimientos.

##### Cuenta

Tipo de selección de cuentas: usted podrá seleccionar la o las cuentas que desee relacionar con el perfil. Podrá relacionar todas las cuentas que tenga asociadas a Tango Banking o bien solo relacionar las que desee, siempre que éstas se encuentren relacionadas desde el maestro de Cuentas de Tesorería.

  * Si elige Todas las cuentas vinculadas a Tango Banking verá todas las cuentas que tenga vinculadas o que vincule en el futuro con Tango Banking.
  * Si elige Solo cuentas seleccionas debe tener en cuenta que sólo podrá seleccionar entre las cuentas existentes al momento de crear el perfil, pero no aparecerán las cuentas que se creen a futuro. Las cuentas que se agreguen después de creado el perfil, se verán solo si desde el perfil se agregan para su visualización.



##### Usuarios

Esta solapa le permite seleccionar desde la lista de usuarios creados aquellos a los cuales les asignará el perfil creado.

##### Observaciones

Esta solapa es un campo de texto libre que le permite ingresar las observaciones que usted considere necesarias para el perfil creado.

__Importante

Tenga en cuenta que, para simplificar los procesos de consulta, sólo se permite asignar un perfil a cada usuario. Puede asignar muchos usuarios a un perfil, pero sólo podrá asignar un perfil por usuario.
