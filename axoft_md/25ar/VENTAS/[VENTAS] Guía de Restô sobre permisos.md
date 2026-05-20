# Guía de Restô sobre permisos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_permisos_gv3/

## Contenido

# Guía de Restô sobre permisos

Ventas Restô permite restringir el acceso a determinadas funciones o bien, manejar claves de autorización para controlar su acceso.

De acuerdo a la estructura y organización de su negocio, le será de gran utilidad implementar mecanismos de permisos para otorgar mayor flexibilidad y seguridad ante determinadas situaciones de trabajo.  
Al utilizar permisos, todas las operaciones transcurren bajo el usuario que está operando, evitándose el deslogueo y logueo de otro usuario para realizar una operación determinada.  
Usted tiene la posibilidad de determinar las operaciones a restringir para cada usuario; dando acceso, si corresponde; solicitando el ingreso de una "clave" -que será proporcionada por un usuario habilitado en el momento de realizar la operación, solicitando el motivo o bien, auditando la acción realizada.  
Mediante esta configuración dará diferentes jerarquías a los usuarios que operan el sistema, posibilitando así un manejo más seguro y con mayor control de la vasta posibilidad de situaciones que se presentan a diario en un puesto de caja o en una terminal de mozo.  
Además, Ventas Restô registra todas las operaciones realizadas, para su posterior auditoría. De esta manera, es posible conocer todos los movimientos efectuados a través de un listado.  
También, se auditan los ingresos de clave fallidos. Estos casos corresponden al ingreso de una clave inválida o bien, de una clave de un usuario que no tiene acceso a una operación o con acceso restringido.

##### Puesta en marcha

Usted dispone de una amplia combinación de opciones para adecuar la parametrización a su esquema de trabajo. Simplemente, determine la necesidad y realice las configuraciones necesarias.  
En primer lugar, es necesario dar de alta la clave de autorización de cada usuario del sistema. Utilice la opción Claves de autorización (en Archivos / Personal del menú). El usuario usará esta clave para habilitar una acción, si su perfil se lo permite.

__Nota

Tenga en cuenta que el sistema interpreta las mayúsculas y minúsculas como caracteres diferentes.

Por último defina los perfiles del personal, con los que desea restringir el acceso a determinadas operaciones. Utilice la opción Definición de perfiles (en Archivos / Personal del menú) para configurar los perfiles de los adicionistas y de los mozos de su local.  
Es posible restringir operaciones de comanda, operaciones de caja y operaciones generales.  
Los usuarios sin perfil quedan exentos de esta parametrización.  
Al definir un perfil, usted configura el comportamiento para cada operación. Las opciones posibles de selección son las siguientes:

  * Sí: con acceso a la operación. El usuario trabaja sin ninguna restricción y no hay registro de las acciones efectuadas.
  * No: sin acceso a la operación. No permite el acceso a la operación.
  * Con Clave: solicita el ingreso de la clave de autorización para ejecutar la operación. Según la función, se registra en la auditoría de operaciones.
  * Con Clave y Motivo: solicita clave y si el ingreso es correcto, solicita el motivo para completar la acción.
  * Ingresa Motivo: con acceso a la operación y solicitud del motivo para completar la acción.
  * Auditado: con acceso a realizar la operación y con registro en la auditoría.



Seleccione para cada operación, la opción que más se adecue a sus necesidades.

###### Consideraciones para trabajar con tarjetas magnéticas

Si usted desea utilizar tarjetas magnéticas para el ingreso de la clave de autorización, además de los pasos mencionados para la parametrización, es necesario que realice el siguiente paso:  
En el directorio EXE de su instalación local, cree un archivo con el nombre Resto.INI, con las siguientes características:

[LOGUEO AUTORIZACION] DISPOSITIVO=OPOS_MSR  
DESCRIPCION=Opos MSR - Magnetic Stripe Reader  
CAMPO=Clave  
PROPIEDAD=Track2Data  
DESDE=1  
CANTIDAD=15

A continuación, explicamos el valor solicitado para cada uno de los identificadores de este archivo:

**Identificador** | **Valores posibles** | **Descripción**  
---|---|---  
DISPOSITIVO | OPOS_MSR | Valor fijo.  
DESCRIPCION |  | Configurable, a modo descriptivo  
CAMPO | CLAVE | Valor fijo.  
PROPIEDAD | TRACK1DATA  
TRACK2DATA  
ACCOUNTNUMBER  
FIRSTNAME  
SURNAME  
TITLE  
SUFFIX | Indica en qué propiedad de la tarjeta estará grabado el campo (clave de autorización).  
DESDE | 1 | Para la propiedad elegida, desde qué carácter se indica la clave de autorización.  
CANTIDAD | 15 | Indica cuántos caracteres de la propiedad se deben leer.  
  
Si usa tarjetas magnéticas para el logueo de mozos, el archivo Resto.INI ya existe. Por lo tanto, agregue debajo del texto existente, el bloque de texto correspondiente a la clave de autorización.  
El mozo podrá loguearse y desloguearse sin inconvenientes, en tanto no se solicite el ingreso de una clave de autorización. Si intenta hacerlo, aparecerá el mensaje "Clave inválida", interpretándose que se intentó autorizar la operación con un código que no está definido como usuario autorizante.

##### Detalle del circuito

Una vez configurado el sistema, de acuerdo al perfil del usuario que se encuentre operando, se presentan diferentes alternativas:

  * solicitud de clave;
  * solicitud de motivo;
  * solicitud de clave y motivo;
  * permiso para realizar la acción con registro en la auditoría;
  * permiso para realizar la acción sin registro en la auditoría;
  * sin acceso para realizar la acción.



El ingreso de la clave de autorización puede realizarse utilizando teclado, touch screen o bien, un lector de tarjetas magnéticas.  
Mediante el ingreso de la clave de autorización queda habilitada la operación, sólo para una acción. Es decir, cada vez que tuviese que efectuar una operación para la que no está habilitado, deberá solicitar el permiso correspondiente mediante el ingreso de la clave de autorización.  
En el caso de ingresar incorrectamente la clave de autorización, se genera un registro por operación fallida, que será informado en el Listado de Auditoría de Operaciones.  
Si la clave ingresada corresponde a un usuario con perfil limitado para esa acción, también quedará registrada como intento fallido.  
Una vez ingresada la clave correcta, se habilita la acción para la que fue requerida.  
Cuando para realizar una acción (por ejemplo: anular una comanda) se solicita el motivo, se permite un texto libre pero de ingreso obligatorio para poder concluir la operación.  
Puede suceder que la persona encargada de autorizar una operación no se encuentre en el local. Para este caso, defina en el perfil del adicionista o del mozo, la auditoría de las operaciones (elija la opción 'Auditado'). De esta manera, evita la solicitud de la clave de autorización (lo que pasará inadvertido por su personal), pero garantiza el registro de las operaciones realizadas.  
En el Listado de Auditoría de Operaciones verá reflejadas todas las operaciones que en la configuración del perfil haya considerado de utilidad que sean auditadas.  
Si no está disponible la opción 'Auditado' para la operación a realizar, elija la opción 'Si' en el perfil, para tener acceso a la operación. Luego, realice el control correspondiente a través de los informes de auditoría.

**Ejemplo de aplicación de permisos...  
**Explicamos cómo es la forma de trabajar con el sistema si usted aplica permisos a las distintas operaciones.  
El usuario con el que ingresa el adicionista está vinculado a un perfil con determinadas restricciones. Una de ellas se refiere a la edición de precios, que sólo le está permitida a través del ingreso de una clave autorizante.  
En una determinada comanda es necesario modificar el precio de un artículo.  
El adicionista utiliza la función 'Editar precio unitario' pero antes de exhibirse la pantalla de esta función, se solicita el código de autorización, que será ingresado por el encargado para habilitar esta operación.  
La clave debe corresponder a un usuario cuyo perfil tenga acceso a esa acción y que no esté limitado por el ingreso de clave de autorización.
