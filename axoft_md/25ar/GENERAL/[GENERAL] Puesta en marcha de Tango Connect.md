# Puesta en marcha de Tango Connect

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Operación
- URL: https://ayudas.axoft.com/25ar/documentos/operacion/acceso_oper/connect_oper/?p=30826/

## Contenido

# Puesta en marcha de Tango Connect

Diseñamos esta guía para dejar operativa la aplicación Tango Connect.

Explicaremos como poner en marcha el circuito y los pasos a seguir para adaptarlo a sus necesidades.

##### Puesta en marcha

Para la puesta en marcha de esta aplicación, debe loguearse en el sistema con un perfil de Tango que posea asociada una cuenta nexo válida, o bien loguearse directamente con las credenciales de su cuenta nexo asociada. Para más información consulte [Asociar usuario Tango a una cuenta nexo](?p=12560/#asociar-usuario-tango-a-una-cuenta-nexo).

Luego, ingrese, desde el menú de Tango al módulo Aplicaciones nexo y elija la opción "Connect".  
Se iniciará un asistente paso a paso, donde podrá configurar y adquirir la aplicación.

  * **Primer paso:** acepte los términos y condiciones de la aplicación.
  * **Segundo paso:** controle y confirme que los datos de configuración de la aplicación sean correctos.



Pulse en "Terminar" para finalizar con la adquisición y configuración de la aplicación.

##### Detalle del circuito

Tango connect le permite acceder a su sistema Tango desde cualquier dispositivo con acceso a Internet.  
Una vez adquirida la aplicación puede administrarla desde el sitio: <https://nexo.axoft.com/connect>

##### **Control de acceso a Connect**

La configuración del control de acceso se realiza desde Tango Nexo, y está disponible únicamente para usuarios con rol de Administrador.

**¿Cómo acceder?**

Existen dos formas de acceder a la configuración. Ambas opciones dirigen a la misma pantalla de configuración del sistema:

  1. Desde el acceso a Connect. 
     * Ingrese a nexo.
     * Acceda a Aplicaciones | Connect.
     * En el mosaico del sistema, seleccione el ícono de configuración (engranaje).
  2. Desde la configuración del tenant. 
     * Ingrese a nexo.
     * Acceda a Administración | Configuración.
     * Seleccione el Empresa (tenant) correspondiente.
     * Ingrese a la sección Sistema.



Dentro de la configuración del sistema podrá definir los permisos de conexión:

  * **Acceso a Web:** permite habilitar o deshabilitar el acceso al sistema desde la interfaz web.
  * **Acceso a API:** permite habilitar o deshabilitar el acceso al sistema mediante integraciones externas (API).



**Visualización del estado**

En la pantalla principal de Connect, cada mosaico muestra su estado mediante chips:

  * **Web / API en verde:** acceso habilitado.
  * **Web / API en rojo:** acceso deshabilitado.



Esto permite identificar rápidamente qué tipo de conexión está disponible.

**Comportamiento según el rol**

El acceso y las opciones disponibles varían según el tipo de usuario:

  * **Administrador**
    * Puede visualizar el estado de las conexiones.
    * Puede acceder a la configuración mediante el ícono de engranaje.
    * Puede modificar los permisos en cualquier momento.
  * **Operador**
    * Solo puede visualizar el estado general del sistema en el mosaico correspondiente (Naranja: conectado / Grisado: fuera de línea).
    * No visualiza el detalle de habilitación de Web o API.
    * No tiene acceso a la configuración.
    * Si el acceso web está deshabilitado, no podrá ingresar al sistema aunque tenga el link de acceso.
