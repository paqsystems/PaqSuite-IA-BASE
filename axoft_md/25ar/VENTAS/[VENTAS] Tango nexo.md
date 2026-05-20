# Tango nexo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_nexocobr_gv/?p=12560/

## Contenido

# Tango nexo

Tango nexo es un portal de aplicaciones que brinda el acceso a una serie de soluciones web que amplían el alcance de los sistemas Tango. Las mismas permiten realizar operaciones claves del negocio en la nube, desde cualquier dispositivo móvil, con posibilidad de compartir información y/o documentos con terceros.

A continuación, se explicarán o detallarán los términos utilizados en esta ayuda.

##### Usuario de nexo (cuenta nexo)

Una cuenta nexo, es una cuenta de correo creada para operar, a modo de **usuario nexo** , las aplicaciones web que ofrece Tango en su portal nexo. Es totalmente gratuita y se da de alta a través de la aplicación web Tango nexo ([www.tangonexo.com](https://www.tangonexo.com/)).

Dichas cuentas de correo pueden ser:

  * **Nativas:** son las que se registran desde "Crear una cuenta" (https://nexo.axoft.com/Account/Registration).
  * **Externas:** son las que se crean a través algún proveedor de identidad externo, tal como Google, Facebook, Microsoft, entre otros.



##### Aplicación nexo

También denominada la aplicación de nube, es la relación entre _Sistema (número de llave) - Empresa (_ nexo _) - Aplicación (_ nexo _)_ , se trata de una combinación única que nos sirve para identificar unívocamente a la misma (Tenant).

##### Empresa nexo

La _empresa en nexo_ es solo un nombre para identificar a la aplicación de nube en referencia con la empresa de tierra, en general, al crearse la aplicación de nube el nombre coincide con esta última.

##### Tipo de aplicaciones nexo

  * **Aplicaciones de sistema:** son aquellas que no necesitan vincularse con una empresa de tierra, pero que operan para todo el sistema de Tango (por ejemplo: Tango Backup, Tango Update, Tango Connect).
  * **Aplicaciones de empresa:** son aquellas que se vinculan con una empresa de tierra (Tango), para sincronizar información entre la base de datos de tierra con la aplicación de nexo en la nube (por ejemplo: Tango Clientes, Tango Cobranzas, Tango Reportes, Tango Tablero).
  * **Aplicaciones independientes:** son aquellas que no requieren vincular con una empresa en tierra, ni interactúan con el sistema en general, es decir, operan en forma independiente (por ejemplo: Tango Fichadas).



##### Adquisición de aplicaciones nexo

Al ingresar desde Tango al módulo Aplicaciones nexo, luego de elegir una aplicación en particular se abrirá un asistente que le permitirá:

  * Adquirir la aplicación seleccionada, si se trata de la primera vez.
  * Reconfigurarla o dejar de utilizarla, en caso haber sido vinculadas previamente.



Cuando se adquiere una aplicación nexo, el asistente le mostrará las siguientes opciones:

  * La empresa de nexo con el mismo nombre de la empresa de Tango en la que está posicionado.
  * Otras empresas de nexo, previamente creadas para la misma aplicación.



También en cada opción se indicará el estado de estas en nube, por ejemplo:

  * Si es la primera vez, indicará (crear nueva).
  * En caso de haber sido vinculada previamente dirá (vinculada), ya que reconocerá que ya existe una empresa con ese nombre para el sistema (número de llave) en cuestión.



En ocasiones, es necesario reconfigurar la aplicación, por ejemplo, cuando se restaura una copia de seguridad o se reinstala el sistema Tango.  
También es posible realizar la desvinculación de tierra con nube eligiendo en el asistente, la acción "Dejar de utilizar la aplicación".

##### Cambio de administrador

Usted puede cambiar el administrador de una aplicación nexo mediante la acción Reconfigurar aplicación.  
Con este proceso (sin necesidad de modificar la parametrización ya configurada), el usuario de nexo asociado al usuario de Tango que ejecute la acción será agregado automáticamente como nuevo administrador de la aplicación.  
Esto resulta útil cuando no tiene o perdió el acceso con la cuenta de nexo del administrador anterior.

__Importante

**Importante:** si ya posee acceso a la aplicación nexo (nube) con un usuario administrador, puede agregar más administradores desde el menú:  
Tango nexo | Configuración | Aplicación | Administradores.

##### Administración desde nexo (nube)

Siendo usted un usuario administrador de nexo, al acceder a la opción "Configuración" (dentro de la sección Administración), se podrán visualizar todas las aplicaciones adquiridas y al seleccionar cualquiera de ellas, se habilitarán diferentes opciones:

  * **Volver:** para retornar a la pantalla anterior.
  * **Administradores:** mediante esta opción se pueden designar nuevos administradores o actualizar los ya existentes.
  * **Sistema:** permite asignarle una descripción a la llave seleccionada y despliega el estado de esta.
  * **Empresa:** permite editar el nombre de la empresa en nube y asignarle el link a una página web. Tenga en cuenta que el nombre es meramente informativo, pero no modifica la vinculación con su correspondiente en tierra (sistema Tango).
  * **Usuarios:** despliega la pantalla de administración de usuarios.
  * **Eliminar:** mediante esta opción se puede eliminar el tenant seleccionado.
  * **Asistente:** permite acceder a un asistente de configuración, mediante el cual se puede personalizar la apariencia de la empresa o crear invitaciones para nuevos operadores o administradores de la aplicación en cuestión.
  * **Información:** contiene información adicional correspondiente a la fila seleccionada
  * **Términos y condiciones:** los mismos se encuentran a disposición en este apartado para poderlos consultar.



##### Asociar cuentas de correo

Tango nexo le permite asociar dos o más cuentas de correo a su perfil. Para asociar la cuenta de correo a nexo, pulse en opciones del perfil en la esquina superior derecha del portal de nexo.  
Presione el botón "Editar" para que se habiliten las nuevas opciones, en la sección Cuentas de correo tendrá las siguientes opciones. A continuación, se detallan los pasos de las principales funciones que podrá realizar:

  * Asociar una cuenta de nexo a través de Agregar cuenta.
  * Convertir una cuenta asociada a cuenta principal en Convertir en principal.
  * Eliminar una cuenta asociada desde Eliminar.



**Agregar cuenta  
**Desde esta opción usted podrá asociar varias cuentas de nexo a una cuenta principal, de forma que los accesos de todas las cuentas se consoliden bajo una única cuenta principal que usted seleccionará durante el proceso de asociación, siendo la cuenta principal de su perfil aquella con la cual se identificará al usuario en las aplicaciones nexo.

__Nota

Toda cuenta que no tuvo ninguna asociación es una cuenta principal. Las cuentas asociadas (secundarias o no principales) son aquellas cuentas que intervinieron en una asociación.

A continuación listamos las condiciones que deben cumplir las cuentas a asociar:

  * Deben ser cuentas registradas en Tango nexo ya sean propias de nexo o por otros IP (Google, Yahoo, Microsoft, Hotmail).
  * Deben estar seleccionadas como 'Cuenta principal'.



Al acceder a Agregar cuenta se presentará un formulario en el cual usted debe ingresar el e-mail que desea asociar a su cuenta.  
Una vez agregada, se abrirá una nueva vista en donde tendrá que ingresar el código de verificación que fue enviado a la casilla de correo de la cuenta ingresada.

__Importante

**Atención: es recomendable estar completamente seguro antes de asociar las cuentas, ya que los accesos de todas las cuentas se consolidarán en la cuenta principal, y esta acción no se podrá revertir. Si desasocia las cuentas no se restablecerán los permisos de las mismas, quedando los permisos consolidados en la cuenta principal. Podrá utilizar las otras cuentas, pero deberá asociarlas nuevamente a cada una de las aplicaciones nexo que desee utilizar.**

**Convertir en principal  
**Desde esta opción usted podrá seleccionar una cuenta de su lista de cuentas asociadas para hacer de ella su cuenta principal.  
La que hasta entonces era su cuenta principal pasará a ser cuenta asociada, pasando la configuración de una cuenta a la otra.

**Eliminar cuenta asociada  
**Con esta opción usted podrá eliminar una de las cuentas asociadas de su perfil. Si usted desea eliminar la cuenta principal de su perfil, primero debe elegir otra cuenta como la principal y luego eliminar la cuenta deseada.

__Importante

**Atención: al eliminar una cuenta asociada tenga presente que algunas de las siguientes aplicaciones de nexo pueden presentar problemas una vez deshecha la asociación. Estas aplicaciones son: Tango Delivery, Tango e-Commerce y Portal Tango Factura.**

##### Asociar usuario Tango a una cuenta nexo

Para asociar su usuario de Tango a una cuenta nexo, ingrese al sistema Tango, pulse en opciones del perfil en la esquina superior derecha e ingrese al proceso Asociar cuenta nexo.
