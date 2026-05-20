# Jerarquías de plan de cuentas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=9794/

## Contenido

# Jerarquías de plan de cuentas

Registre y mantenga actualizadas las jerarquías del plan de cuentas.

La jerarquía del plan de cuentas es una estructura de tipo árbol, que sirve como herramienta para dar un orden lógico a las [cuentas contables](?p=9774).  
En la jerarquía se definen los rubros y subrubros (o cuentas contables no imputables) del plan de cuentas.  
En la opción [Parámetros de Contabilidad](?p=9811) es posible definir una Jerarquía principal. Esta jerarquía se propone por defecto para la búsqueda de cuentas en la carga de asientos.  
Contabilidad divide los datos de una jerarquía en tres solapas: [Principal](?p=9794#principal), [Rubros](?p=9794#rubros) y Observaciones.  
Sus opciones son las siguientes:

##### Principal

Esta solapa contiene los datos de identificación o características generales de una jerarquía.

Código y Descripción: son los datos que identifican a la jerarquía.

Utiliza máscara: es posible definir una máscara para la codificación de rubros, subrubros y cuentas imputables dentro de la jerarquía. Esta máscara es totalmente independiente de la máscara para [cuentas contables](?p=9774). Si activa este parámetro, el ingreso del código de rubro, subrubro y cuenta imputable se ajustará a la máscara parametrizada.

Separador: seleccione el tipo de separador de la máscara. Puede optar por un punto, guión o blanco.

Máscara: defina la máscara para la carga de los códigos de rubros, subrubros y cuentas imputables de la jerarquía. Para ello, utilice el separador seleccionado y el caracter X (equis mayúscula). La longitud de la máscara es de 40 posiciones.

##### Rubros

Esta solapa contiene la definición de la estructura de árbol con sus rubros, subrubros y las cuentas imputables asociadas.

**Cómo definir un rubro  
**En primer lugar, en la solapa Principal, defina el código de jerarquía y de manera opcional, ingrese su descripción e indique la máscara a aplicar.  
A continuación, ingrese a la solapa Rubros y defina cada uno de los rubros para el código de jerarquía seleccionado.  
Haga clic en el botón "Insertar" o bien, presione las teclas <Shift + Ins> o haga clic sobre el botón derecho del mouse, para insertar un nuevo rubro.  
Asígnele un código de identificación, respetando el formato de la máscara definida en la solapa "Principal".  
Ingrese una descripción e indique el tipo de operación a asociar (suma o resta) y el saldo habitual (deudor o acreedor).  
El tipo de operación se aplica sobre el saldo de la cuenta conservando su signo. Esto se utiliza en la obtención de los listados por jerarquía.

Definimos en una jerarquía un rubro con dos subrubros dependientes.  
Si el primer subrubro tiene un saldo positivo y el tipo de operación suma, y el segundo subrubro tiene un saldo negativo y el tipo de operación también suma entonces como resultado del rubro muestra la diferencia entre el primer subrubro y el segundo subrubro.  
Si el primer subrubro tiene un saldo positivo y el tipo de operación suma, y el segundo subrubro tiene un saldo negativo y el tipo de operación resta entonces como resultado del rubro muestra la suma entre el primer subrubro y el segundo subrubro.  
El saldo habitual de los rubros padres se aplica sobre el saldo del rubro y tendrá el mismo funcionamiento que el saldo habitual de las cuentas en los listados donde se pueda seleccionar la opción Muestra saldos según saldo habitual.  
Para agregar otro rubro, repita los tres pasos anteriores.

**Cómo definir un subrubro  
**Para insertar un subrubro o subnivel del rubro actual, siga los siguientes pasos:

  1. Haga clic en el botón "Insertar subnivel" o bien, presione las teclas <Ctrl + Ins> o haga clic sobre el botón derecho del mouse.
  2. Asígnele un código de identificación, respetando el formato de la máscara definida en la solapa [Principal](?p=9794).
  3. Ingrese una descripción e indique el tipo de operación a asociar (suma o resta).



__Nota

Para agregar otro subrubro, repita los tres pasos anteriores.

**Otros datos a ingresar**

Cuenta: si corresponde, asigne un código de [cuenta contable](?p=9774) al subrubro en pantalla. Para más información, consulte el ítem [Selección de una cuenta contable](?p=9358/#definiciones-previas-sobre-contabilidad).

Operación: seleccione el tipo de operación que se aplica sobre el saldo de la cuenta conservando el signo (suma o resta) del rubro o subrubro, a tener en cuenta en los listados por jerarquía.

Saldo habitual: indique el saldo ('Deudor' o 'Acreedor') que habitualmente tendrá el rubro.

Los siguientes parámetros se habilitan si el rubro no tiene asociada una cuenta y serán tenidos en cuenta en el [estado de situación patrimonial](?p=9761/#estado-de-situacion-patrimonial).

Ubicación sumarización del rubro: indique si desea imprimir la sumarización del rubro o subrubro.

Ubicación de la sumarización: indique la ubicación de los importes sumarizados (inicio o final).

Imprime rubro de nivel 1: elija la ubicación (derecha o izquierda) del rubro o subrubro.

**Botones y teclas del árbol de jerarquías  
**Utilice los botones que se exhiben al pie del árbol de jerarquías o presione las teclas de acceso rápido o haga clic sobre el botón derecho del mouse para ejecutar las siguientes acciones:

<Shift + Ins> | Insertar nuevo rubro.  
---|---  
<Ctrl + Ins> | Insertar un subnivel en el rubro.  
<Ctrl + Alt + M> | Modificar datos del rubro.  
<Del> | Eliminar un rubro o subrubro.  
<Ctrl + Up> | Subir el subrubro, una posición.  
<Ctrl + Down> | Bajar el rubro o subrubro, una posición.  
<Ctrl + Alt + Up> | Subir el subrubro, un nivel.  
<Ctrl + Alt + D> | Deasignar cuentas contables del rubros o subrubro.  
<Ctrl + Alt + E> | Expandir todos los rubros.  
<Ctrl + Alt + C> | Contraer todos los rubros.  
<Ctrl + Alt + A> | Visualizar cuenta no asignadas.  
  
Condiciones para eliminar una jerarquía:

Es posible eliminar una jerarquía completa siempre y cuando no esté definida como jerarquía principal en la opción [Parámetros de Contabilidad](?p=9811).

##### Contenidos relacionados

  * [Herramientas para integración contable](https://ayudas.axoft.com/25ar/ayudas/gla/datoscontabl_carp_gla/herramientasintcontable_gla/)

  * [Video sobre planes de cuentas contables](https://ayudas.axoft.com/25ar/videos/cna_carp_vid/plancuentas_cna_vid/)

  * [Videos sobre parametrización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/paramcontab_gral_vid/)
