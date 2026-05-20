# Guía de Restô sobre invitaciones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_invitaciones_gv3/

## Contenido

# Guía de Restô sobre invitaciones

**Restô** le permite especificar, mediante permisos, quienes pueden realizar invitaciones parciales o sobre toda la comanda.

Además:

  * Determinar que artículos admiten ser invitados.
  * Registrar las invitaciones realizadas asociándole un motivo.
  * Volver atrás una invitación de manera rápida y práctica.
  * Realizar un control total sobre las invitaciones: 
    * Consultar cuantos artículos se invitaron (importe y número de invitaciones).
    * Consultar ¿quién? ¿de que depósito? ¿en qué momento? ¿autorizado por quién? realizó una invitación.
    * Conocer en todo momento cuánto representa en dinero las invitaciones realizadas.
    * Conocer el detalle de las invitaciones realizadas al cerrar turno.
    * Centralizar la información pertinente a fin de obtener la sucursal que más invitaciones realiza, o cual es el monto medio que se invita en nuestra cadena o bien en que momento del año se realizan más invitaciones, a que clientes estamos invitando, etc.



##### Puesta en marcha

###### ¿Cómo parametrizar la base de datos para registrar el circuito de invitaciones?

**Paso 1: indique que artículos pueden ser invitados.  
**Para ello, utilice la opción Archivos en la carpeta del menú principal de su sistema [Archivos | Artículos.](articulo_carp_gv3)  
Allí configure el parámetro Admite invitación definiendo si este artículo puede ser aplicado en una invitación o no en una comanda.  
Tenga en cuenta que si se realiza una invitación total de la comanda, no se tendrá en cuenta esta configuración.

**Paso 2: defina que usuarios pueden registrar invitaciones y bajo que control.  
**Utilice la opción Perfiles en la carpeta del menú principal de su sistema [Archivos | Personal](personal_gv3).  
Los parámetros a modificar son:

invitaciones: mediante este permiso defina si el personal asociado al perfil puede realizar o no +++++++++++++++++++++++++++++ parciales, es decir, sobre uno o más artículos de la comanda, pero no sobre el total de la misma.

invitaciones completa: mediante este permiso defina si el personal asociado al perfil puede registrar una invitación por el total de la comanda.

En cada uno de los parámetros mencionados indique bajo que control se realizan las invitaciones, es decir:

  * Sí: con acceso a la operación. El usuario trabaja sin ninguna restricción y no hay registro de las acciones efectuadas.
  * No: sin acceso a la operación. No permite el acceso a la operación.
  * Con Clave: solicita el ingreso de la clave de autorización para ejecutar la operación. Según la función, se registra en la auditoría de operaciones.
  * Con Clave y Motivo: solicita clave y si el ingreso es correcto, solicita el motivo para completar la acción.
  * Ingresa Motivo: con acceso a la operación y solicitud del motivo para completar la acción.
  * Auditado: con acceso a realizar la operación y con registro en la auditoría.



Finalmente asocie al perfil correspondiente a sus mozos y adicionistas.

**Paso 3: Cree los posibles motivos de invitación.  
**Si lo desea, puede crear motivos de invitación, para ello utilice la opción Motivos de invitación en la carpeta del menú principal de su sistema [Archivos | Artículos](articulo_carp_gv3), para definir las causas por las que un ítem de una comanda o una comanda completa puede ser incluida en una invitación.  
El mozo / adicionista tendrá acceso a esta información automáticamente, al realizar la invitación, siempre que por perfil configure que debe ingresar un motivo de invitación.

**Paso 4: Modifique sus formularios de impresión.  
**Utilice la opción Comandas en la carpeta del menú principal de su sistema [Archivos | Carga Inicial | Formularios](formulariocomanda_gv3) o bien Definición en la carpeta del menú principal [Archivos | Carga inicial | Talonarios](talonariodefinic_gv3) si desea destacar los renglones invitados y especificar el motivo de la o las invitaciones, use la variable @MI disponible para los renglones de comandas y facturas.

##### Detalle del circuito

**Trabajando con invitaciones** Como se mencionó anteriormente, es posible registrar invitaciones parciales (sobre algún ítem en particular de la comanda) o bien sobre la comanda completa.  
En ambos casos la invitación puede realizarse antes de ingresar un artículo, o bien cuando el artículo ya esta ingresado. Para ello presione el botón "invitaciones" sobre el artículo a invitar.  
Inmediatamente, en la comanda el artículo se mostrará con precio 0.  
Tenga en cuenta que si en el perfil definió que se solicite motivo de invitación, al momento de realizar la invitación y se existe más de un motivo habilitado se despliega una pantalla para que seleccione el motivo correspondiente.

**¿Cómo revertir una invitación?  
**Es posible deshacer una invitación utilizando el mismo botón de invitación.  
Para ello, posiciónese sobre el renglón a afectar y presione el botón "invitaciones".  
Como otra opción para realizar esta operación, puede utilizar el botón "Lista" y seleccionar la opción 'Precio original'.

**Control de invitaciones** A continuación se detallan las diferentes formas para controlar las invitaciones realizadas en su local.  
Consultas | Comandas | invitaciones Utilice esta consulta Live y analice la información según sus necesidades.  
Informes | Comandas | Auditoría  
Si en el proceso Perfiles de adicionista / mozo configuró en el campo correspondiente la opción 'Con Clave', 'Con Motivo', 'Con Clave y Motivo' o 'Auditado', mediante este informe accederá a conocer ¿quién? ¿de que depósito? ¿en qué momento? ¿autorizado por quién? ¿por qué motivo? realizó una invitación.

Cierre de turno  
Además es posible seleccionar que al realizar el cierre de turno se incluya el Informe de invitaciones, detallado por artículo, detallado por usuario o en formato resumido.

**Centralización de la información  
**Si centraliza información, tenga en cuenta que los datos de las invitaciones realizadas son exportados con las comandas, por lo tanto es posible realizar el control de las invitaciones realizadas por cada sucursal de su cadena, a través de la consulta Live invitaciones, también disponible en Central.
