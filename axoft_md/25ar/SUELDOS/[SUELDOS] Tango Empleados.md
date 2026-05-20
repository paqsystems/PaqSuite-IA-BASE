# Tango Empleados

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_vacaciones_sua/?p=12448/

## Contenido

# Tango Empleados

Con Tango Empleados podrá acceder a un portal de interacción y comunicación entre empleados y empleador a través del área de RRHH, que permite publicar recibos de sueldos y otros documentos referidos al sector, con posibilidad de firmarlos electrónicamente, agilizando la gestión del Capital Humano de una forma segura, disponible en cualquier momento y accesible desde cualquier dispositivo móvil o de escritorio.

Ingrese a través del portal de nexo a la aplicación Tango Empleados: desde nexo seleccione la aplicación Empleados haciendo clic en el mosaico correspondiente.  
Seleccione la empresa de Tango Empleados que desee abrir. Esta acción se activa, únicamente, si tiene acceso a más de una empresa.  
Luego se abrirá la pantalla principal de consulta de documentos. De acuerdo con el perfil del usuario con el cual ingrese, se desplegarán diferentes opciones, según sea [Empleador](?p=12557) o [Empleado](?p=58548).

##### Circuitos, roles y permisos

Contamos con dos modalidades de trabajo según su perfil: 'Empleador' o 'Empleado'. En la siguiente sección describimos el circuito para ambas modalidades.  
Un usuario con perfil 'Empleador' puede tener, además, un rol de 'Administrador' o un rol de 'Operador'.  
Como 'Administrador', usted podrá configurar los permisos sobre los usuarios operadores del sistema, mientras que como 'Operador' no tendrá acceso a las opciones de configuración y tendrá habilitados los permisos que le haya otorgado un 'Administrador'. Para más información, consulte [Permisos de operadores](?p=12557/#permisosoper).

Transición de estados de los documentos según configuración y tipo de usuario

A continuación puede observar el circuito de estados (o sea, las distintas etapas que componen el circuito), dependiendo del perfil utilizado. Estos perfiles pueden estar referidos al empleador o al empleado, siendo su flujo de trabajo completamente distinto.  
El empleador definirá el circuito de los documentos a través de opciones de [configuración](?p=12557/#config) para condicionar los diferentes estados por los que el documento puede ir pasando a partir del momento en que son sincronizados desde Tango Sueldos.  
Las acciones determinarán los posibles estados. Por ejemplo, si define que un documento requiere autorización por parte del empleador, el primer estado será 'pendiente de autorización' y requerirá de la acción 'Autorizar' para pasar al estado siguiente.

En las secciones [Perfil Empleador](?p=12557) y [Perfil Empleado](?p=58548) detallaremos el flujo de trabajo para ambas modalidades.

Acciones sobre los documentos según su estado

**Acciones del empleador  
**En los siguientes apartados exponemos las acciones posibles que usted podrá realizar como empleador sobre los documentos, en función del estado de estos y al circuito que haya definido en las opciones de configuración para cada uno de sus tipos. Los usuarios con perfil 'Administrador' tendrán permisos para realizar todas las acciones, mientras que los que tengan perfil de 'Operador', requerirán que se les habilite cada permiso en particular, por parte de un Administrador.

**Acciones en línea  
**Estas acciones se realizarán de manera instantánea, al presionar el botón correspondiente y la mayoría de ellas intervienen directamente en el cambio de estado de un documento para pasar al siguiente, según se haya definido en el [Circuito de documentos](?p=12504/#definicion-del-circuito-de-documentos).

**Estado/Acción** | **Autorizar** | **Firmar** | **Publicar** | **Exportar para firmar** | **Ver** | **Eliminar** | **Descargar** | **Condición**  
---|---|---|---|---|---|---|---|---  
Pendientes de autorización | SI | NO | NO | NO | - | - | - |  • Ser usuario administrador o usuario operador con permiso 'Autoriza'. • Tener habilitada la opción Requiere autorización en el Circuito de Documentos.  
Pendientes de firma | NO | SI | NO | SI | - | - | - |  • Ser usuario administrador o usuario operador con permiso 'Firma' y/o 'Exporta/Importa'. • Tener habilitada la opción Requiere firma electrónica o Requiere firma digital en el Circuito de documentos.  
Pendientes de publicación | NO | NO | SI | NO | - | - | - |  • Ser usuario administrador o usuario operador con permiso 'Pública'. • Tener habilitada la opción Requiere publicación en el Circuito de documentos.  
Todos los estados | - | - | - | - | SI | SI | SI | • Ser usuario administrador o usuario operador con permiso 'Elimina'.  
  
Para más información, consulte las descripciones de los estados detalladas en [Recibo de sueldo e Impuesto a las ganancias](?p=12557/#recibo-de-sueldo-e-impuesto-a-las-ganancias).

**Procesos  
**Estas acciones intervienen en procesos de lotes para firmar documentos por fuera de Tango Empleados, es decir, a través de una herramienta externa. El resultado será que un documento pase de estado 'Pendiente de firma' a 'Pendiente de publicación' o a 'Publicado', según se defina en el circuito del documento desde el menú de configuración.

**Proceso/Acción** | **Descargar** | **Importar firmados** | **Condición**  
---|---|---|---  
Exportación/Descargar | SI | NO | • Ser usuario administrador o usuario operador con permisos 'Firma' y/o 'Exporta/Importa'.  
• Tener habilitada la opción Habilita firma con herramienta externa (electrónica o digital).  
Importación/Importar firmados con herramienta externa | NO | SI | • Ser usuario administrador o usuario operador con permisos 'Firma' y 'Exporta/Importa'.  
• Tener habilitada la opción Habilita firma con herramienta externa (electrónica o digital).  
  
**Acciones del empleado  
**El siguiente cuadro esquematiza las acciones posibles que podrán realizar los empleados sobre los documentos publicados en su portal de autogestión.

**Estado/Acción** | **Aceptar conforme** | **Aceptar no conforme** | **Ver** | **Descargar** | **Importar PDF firmado** | **Nota**  
---|---|---|---|---|---|---  
Pendientes | SI | SI | SI | SI | NO |   
No conformes | SI | NO | SI | SI | SI | Un documento que haya sido aceptado no conforme puede, luego, ser aceptado conforme, siendo ésta la última instancia posible para iterar sobre el mismo.  
Conformes | NO | NO | SI | SI | SI |   
  
##### Menú de usuario

Las siguientes opciones se encuentran disponibles tanto para la modalidad '[Empleador](?p=12557)' como para el '[Empleado](?p=58548)'.

###### Mi perfil

Desde esta opción podrá consultar y editar los datos de su perfil de usuario, establecer el uso horario de su zona, asociar nuevas cuentas de correo a nexo y cambiar la contraseña. Al acceder se encontrará en modo consulta de manera predeterminada y para cambiar cualquier valor, debe presionar "Editar", mientras que los cambios quedarán confirmados luego de presionar el botón "Aceptar".

###### Seguridad

Desde el apartado Seguridad (para el Empleador disponible desde la opción Configuración de usuario) se podrá elegir el método de autenticación de dos factores que desee aplicar al momento de realizar operaciones sensibles en el sistema, por ejemplo: firmar documentos. Si un mismo usuario posee rol de empleador y de empleado a la vez, la configuración elegida estará vigente para ambos roles.  
Las alternativas son:

  * **Recibirlo por correo electrónico:** cada vez que el sistema requiera un token de seguridad el mismo será enviado a la cuenta de correo electrónico con la que ingresó al sistema. La duración del token en este caso es de cinco minutos.
  * **Utilizar una aplicación móvil de autenticación:** usted podrá optar por configurar una aplicación móvil de autenticación de dos factores a elección, para obtener el token de seguridad, cada vez que el sistema lo requiera. Dicha aplicación tendrá que estar instalada previamente en su móvil. A continuación, se enumeran algunas aplicaciones sugeridas: 
    * Google Authenticator.
    * Microsoft Authenticator.
    * FreeOTP.
    * AndOTP.
    * Authy.
  * Cuando se elija esta última opción, se desplegará en pantalla un Código QR y las instrucciones para configurar el token. Usted deberá completar los siguientes pasos para escanear el QR con aplicación móvil de autenticación: 
    * Abrir la aplicación de autenticación móvil de su smartphone.
    * Seleccionar la opción de agregar cuenta, mediante escaneo de Código QR.
    * Escanear el Código QR a través de la cámara de su smartphone.
    * El token de seguridad quedará registrado en su aplicación móvil de autenticación en una cuenta con el nombre: Axoft Argentina (Tango Empleados). Desde esta cuenta se obtendrá el token, cuando el sistema lo requiera y la duración de este es de treinta segundos.



__Importante

Cada vez que se cambien las opciones de seguridad y vuelva a elegirse la utilización de una aplicación móvil para obtener el token, se generará una nueva clave secreta de usuario, por lo tango el código QR será diferente y será necesario eliminar la cuenta generada en la aplicación móvil y repetir los pasos anteriormente detallados.

###### Datos de usuario

Esta opción está disponible únicamente para el Empleador y permite proveer los datos necesarios para que Tango Empleados gestione un certificado electrónico propio que se puede utilizar para firmar los documentos que se publican a los empleados. De este modo, Tango Empleados genera un certificado personalizado para el rol Empleador, según el usuario que esté conectado, nutriéndose de los siguientes datos:

  * **Apellido y nombre:** complete los datos del usuario, los mismos se mostrarán en la primera fila de la firma electrónica.
  * **Texto adicional:** puede agregar una segunda fila a la firma electrónica para mostrar el texto deseado, por ejemplo, el cargo del firmante.
  * **CUIL:** complete el CUIL del usuario, ya que es un dato necesario para la generación del certificado.



###### Volver a Tango Nexo

Mediante esta opción podrá salir de Tango Empleados, el sistema lo redirigirá al portal de aplicaciones de Tango Nexo y le ofrecerá las opciones que tenga disponibles, de acuerdo con su licencia comercial.

###### Cerrar sesión

Debe presionar esta opción para salir del sistema y cerrar la sesión en todas las solapas de su navegador.
