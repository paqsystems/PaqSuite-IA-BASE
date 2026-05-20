# Roles

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=9113/

## Contenido

# Roles

Los roles permiten definir el acceso a los distintos procesos de Tango, que serán asignados a uno o más usuarios.

Al crear un rol, asígnele un nombre, una descripción y si posee acceso total al sistema.  
Si el rol no tiene acceso total al sistema, estarán habilitadas la Definición de acceso y la Definición de acceso a consultas externas.

##### Definición de acceso

Defina el alcance funcional de un rol, con la posibilidad de habilitar ramas funcionales y opciones de ejecución del sistema.

**Con respecto a las operaciones:**

Puede definir el alcance del acceso a niveles de operación para los maestros principales, especificando y habilitando acceso por alta, baja y/o modificación de datos. Recuerde que las distintas acciones son posibles de auditar, generando el histórico correspondiente a la operación (Fecha/Hora, Usuario y Terminal que registró la operación). Para mayor información, consulte Configuración de auditoría.

Códigos de los maestros principales (Contabilidad, Sueldos y Control de personal): si el rol tiene habilitado el acceso a la modificación de los datos, adicionalmente podrá indicar si permite la modificación del código que identifica a un registro (es decir, si permite la recodificación del maestro), mediante la definición del parámetro Permite cambiar códigos.

**Filtros de seguridad:**

Sueldos y Control de personal: en caso de haber definido filtros de seguridad para legajos, es posible indicar para cada ítem de menú si deberá considerarse. Active la opción 'No aplica filtro de seguridad' a fines de que el ítem de menú considere la totalidad de los legajos.

**Ejemplo:  
**Se define un filtro de seguridad para Legajos con sueldos superiores a $50.000. Se indica para el Rol 'Liquidador planta' que para el ítem de menú de 'Liquidación de conceptos' se deberá considerar el filtro (desactivando la opción 'No aplica filtro de seguridad'). En cambio para el ítem de menú de 'Familiares', el rol podrá tener acceso a los familiares de todos los legajos (activando la opción 'No aplica filtro de seguridad').

Contabilidad: es posible definir filtros de seguridad para las siguientes entidades del módulo: ejercicios, jerarquías, cuentas, tipos de auxiliares, auxiliares, clases de indicadores contables.  
Para los ítems de menú relacionados a dichas entidades, es posible indicar si deberá considerar el filtro de seguridad, mediante las acciones 'No filtra ejercicio', 'No filtra jerarquías contables', 'No filtra cuentas contables', etc.  
Para mayor información, consulte el tópico Filtros de seguridad. 

##### Definición de acceso a consultas externas

Defina a qué consultas externas de Live tendrá acceso mediante este rol.

**Definición de acceso para Tango AI**

  * **Consultas Live:** seleccione las consultas a las que tendrá acceso desde el chat de Tango AI para consultar información. Podrá definir hasta 10 consultas como máximo.  
Tenga en cuenta que si el usuario tiene asignado más de un rol, las consultas no son acumulables y siempre se tomarán las primeras 10 configuradas entre todos los roles.
  * **Herramientas:** defina si Tango AI tendrá la capacidad de enviar correos electrónicos desde el chat.



**Ejemplo de integración:  
**Para mantener la seguridad del sistema es necesario establecer las funciones que cada usuario podrá realizar para cada empresa.  
Pasos para la implementación de la seguridad en el sistema:

  * Creación del usuario: 
    * Defina un usuario utilizando su apellido como identificación (campo Nombre).
    * Tilde el campo Es usuario de red.
  * Creación del Rol: 
    * En los roles tratamos de reflejar las funciones de los distintos usuarios. A un mismo usuario se le podrán asignar más de un rol y el mismo rol podrá ser asignado a más de un usuario.  
Estos roles podrán ser utilizados para más de una empresa.
    * Realice la 'Definición de accesos' para el rol 'Contable_1', que cumple con la función de Auxiliar contable dentro de la empresa.  
Con este rol se podrán dar de alta y modificar asientos contables en estado 'Borrador' e 'Ingresado'. No podrá dar de baja ni cargar o modificar asientos 'Registrados'.
  * Creación del Filtro de seguridad: 
    * Para la creación del filtro será necesario tener definidas todas las tareas que podrá realizar el usuario de acuerdo a su función dentro de la empresa.
    * Para seguir con el ejemplo, el usuario 'Perez', que realiza tareas de Auxiliar contable sólo podrá operar sobre el ejercicio actual (para eso se define el siguiente filtro).
  * Asignación del permiso: 
    * Una vez asignados los filtros a los usuarios se debe proceder a asignar los permisos. 
      * Seleccione el usuario 'Perez' y el rol 'Contable_1', agregue una o más empresas donde operará el usuario.
      * Una vez terminados estos pasos, el usuario Perez podrá ingresar al sistema.
      * Ingrese usuario y contraseña, seleccione la empresa donde desea realizar las tareas.
      * Al ingresar a la opción de menú de asientos contables, sólo podrá consultar aquellos asientos que pertenecen al ejercicio actual que es el filtro aplicado para el usuario.



##### Contenidos relacionados

  * [Video sobre interés por mora](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/interesmora_gv_vid/)

  * [Video sobre modelo de ingreso de comprobantes](https://ayudas.axoft.com/25ar/videos/sb_carp_vid/modeloingrcompr_sb_vid/)

  * [Video sobre modelos de pedido](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/modelopedido_gv_vid/)

  * [Video sobre perfiles de facturación](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/perfact_gv_vid/)

  * [Video sobre solicitudes de compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/solicitudes_cp2_vid/)

  * [Video sobre usuarios, roles y permisos](https://ayudas.axoft.com/25ar/videos/operacion_carp_vid/perfiles_gral_vid/)

  * [Video sobre órdenes de compra](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/ordencompra_cp2_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)

  * [Videos sobre seguimiento de cheques de terceros](https://ayudas.axoft.com/25ar/videos/sb_carp_vid/chequetercero_sb_vid/)

  * [Videos sobre órdenes de pago individual y masivo](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/ordenpago_cp2_vid/)
