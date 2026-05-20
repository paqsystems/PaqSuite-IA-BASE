# Terminales POS

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/?p=10269/

## Contenido

# Terminales POS

Desde este proceso se habilitan las terminales POS a utilizar, leyendo las tarjetas habilitadas desde el POS o bien, ingresándolas en forma manual (si no opera con POS integrado).

**Consideraciones generales**

  * Para poder eliminar una terminal POS, el sistema verifica que no existan cupones generados por la terminal elegida. En ese caso, deshabilite el equipo para su uso en cobranzas.
  * Para poder eliminar una host de tarjetas, el sistema valida que no existan cupones emitidos desde la terminal, para el código de host que se intenta borrar. En ese caso, deshabilite la relación entre el host y la terminal.
  * Para poder eliminar un código de tarjeta, no deben existir cupones emitidos desde la terminal, para el código de tarjeta a borrar. En ese caso, deshabilite la tarjeta para esa terminal.



Para más información, consulte la [Guía de tarjetas de crédito y débito](?p=10559).

##### Principal

Código: asigne un código de tipo numérico a cada terminal POS. Al hacer clic en el botón "Importar datos del POS", se propondrá el número de terminal leído desde el POS. Este dato no es editable. 

Descripción: ingrese un texto o descripción asociado a la terminal POS. Este dato no puede omitirse.

Código de comercio: ingrese el código que sirve para identificar a su comercio. Si la terminal POS es de tipo 'Externo', el código a ingresar es el provisto por esta empresa y el ingreso de este dato es obligatorio.

Habilitado: cuando se da de alta una terminal POS, por defecto este parámetro se muestra tildado.  
Si usted necesita deshabilitar una terminal POS, el sistema validará que la misma no esté asignada a procesos de cobranza. En ese caso, seleccione otra terminal desde el proceso [Parámetros de Tesorería](?p=10293).  
Al deshabilitar una terminal POS, queda inactiva su relación con los host de tarjetas y con las tarjetas que tenía habilitadas.

Tipo de terminal: seleccione el tipo de terminal POS con la que va a operar. Las opciones posibles son las siguientes: 'LaPos', 'Payway', 'Posnet' o 'Externo (Solo Tiendas)'.

Numeración: defina cómo será la numeración del lote y la del cupón. Las opciones posibles son las siguientes: 'Automático', 'Manual' o 'Según POS'.  
Si en el proceso [Parámetros de Tesorería](?p=10293) usted elige como modo de emisión de cupones, la opción 'Con POS integrado'; por defecto, la numeración será 'Según POS', pero usted puede cambiarla.  
En cambio, si usted elige como modo de emisión de cupones la opción 'Manual' o 'Con POS no integrado', la opción 'Según POS' no estará disponible.  
Si elige la numeración 'Automática' o 'Manual', la terminal POS tomará el comportamiento 'Con POS no integrado'. En este caso, el sistema le informa que la terminal no tendrá conexión con POS y solicita su confirmación. Si no confirma esta acción, la numeración será 'Según POS'.  
Si la numeración Del lote es 'Según POS', la numeración Del lote será también 'Según POS'.

Permite pagos QR: se habilita para tipo de terminales Posnet. Tenga en cuenta que, antes de realizar la configuración, debe verificar que la terminal esté actualizada para operar con pagos QR. Para ello valide que tenga la opción PAGOS QR desde el menú de la terminal. Si ingresa por primera vez a esta opción de manera no integrada, el dispositivo le solicitará habilitar el servicio. En caso de no tener disponible la opción PAGOS QR desde el menú de la terminal, comuníquese con su representante de Posnet para solicitarle la actualización de la terminal correspondiente. Para más información acerca de la configuración de pagos QR, consulte la [Puesta en marcha de pagos QR con Posnet](?p=17126).  
Además, se habilita para tipo de terminales Payway. Tenga en cuenta que no pude desmarcar esta opción de configuración ya que todas las terminales incluyen la funcionalidad sin necesidad de actualizar el dispositivo. Para más información consulte la [Puesta en marcha de pagos con Payway](?p=14430/#puesta-en-marcha). 

##### Host a los que se conecta

Cada terminal POS puede conectarse a uno o varios hosts de tarjetas. Para ello, complete la información de la grilla que se exhibe al pie de la ventana.  
Ingrese el número de lote actual si la numeración del lote es 'Automática' o 'Manual'. El sistema valida que no existan cupones con el número ingresado.  
Ingrese el próximo número de cupón si la numeración Del cupón es 'Automática' o 'Manual'. El sistema verifica que el valor ingresado no esté asignado a un cupón existente.  
El valor por defecto de la columna "Habilitado" dependerá de lo definido en el parámetro Habilitado de la solapa Principal. Si ese parámetro está destildado, esta columna de la grilla de hosts aparecerá inactiva. Caso contrario, se mostrará tildado, pero usted puede modificarlo.

El botón "Agregar todos" está disponible sólo si usted opera en la modalidad 'Con POS integrado'. Utilícelo para agregar en forma automática, la información de todos los hosts de tarjetas habilitados en el sistema.  
Usted puede modificar la información de la grilla, eliminando aquellos que no necesita.  
Si el tipo de terminal es Payway, esta configuración debe realizarla manualmente ya que por una limitación de Payway esa información no puede ser recuperada de la terminal.

##### Tarjetas habilitadas

Cada terminal POS tendrá asociada al menos una tarjeta habilitada en el sistema.  
Ingrese la información en pantalla o bien, pulse el botón "Agregar todas" para que la grilla se complete en forma automática.  
Cada tarjeta debe estar relacionada con un código de host.  
El valor por defecto de la columna "Habilitado" dependerá de lo definido en el parámetro Habilitado de la solapa Principal. Si ese parámetro está destildado, esta columna de la grilla de hosts aparecerá inactiva. Caso contrario, se mostrará tildado, pero usted puede modificarlo.

Si la terminal POS está configurada para trabajar en modo integrado, esta grilla se completa en forma automática en el momento de ejecutar el comando Importar datos del POS. Sólo deberá indicar el código equivalente en Tango para las tarjetas obtenidas desde las tablas internas de la terminal POS. Si el tipo de terminal es Payway, esta configuración debe realizarla manualmente ya que por una limitación de Payway esa información no puede ser recuperada de la terminal.

##### Terminal integrada

Es necesario primero configurar en [Parámetros de Tesorería](?p=10293) el modo de emisión de cupones 'Con POS integrado'.  
Computadora a la que está conectada: es el nombre de la computadora o puesto de facturación donde está conectado el dispositivo físico.

Puerto COM: indique el puerto COM de la PC en la cual estará conectado. Aunque el POS utilice un conector USB, indique el puerto COM que emula la conexión USB.  
Los valores posibles de ingreso son: 'COM1' a 'COM256'.

Versión protocolo Lapos: indique la versión utilizada por su equipo. Este dato se presenta en el visor, al encender la terminal POS (sólo para dispositivos Lapos).

Verificar conexión: verifica si es posible conectarse con el dispositivo físico usando la configuración proporcionada.

Importar datos de la terminal: carga los datos proporcionados por el dispositivo que serán utilizados en la carga de tarjetas habilitadas.  
En el caso de Lapos, se cargan los datos de tarjetas y sus planes.  
En el caso de Posnet se cargan las Monedas.

##### Terminal no integrada

Como primera medida, en [Parámetros de Tesorería](?p=10293) es necesario configurar el modo de emisión de cupones 'Con POS no integrado'.  
Se exhibe una grilla para cargar los nombres de las computadoras que usan esta terminal.  
Estas computadoras representan los distintos puestos de facturación que usan por defecto la terminal.

##### Contenidos relacionados

  * [Guía de implementación sobre pagos QR con Posnet](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_qrposnet_gv/)

  * [Guía sobre implementación de pagos con Payway](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_payway_gv/)

  * [Guía sobre tarjetas de crédito y débito](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/)

  * [Puesta en marcha del circuito de tarjetas](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/guia_pm_tajcredeb_sb/)

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre integración con POSNet + QR + PCT](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrposnet-qr-pct_gral_vid/)

  * [Video sobre integración con Payway](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/payway_gv_vid/)

  * [Video sobre integración con dispositivos de tarjeta](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrdisptarjeta_gral_vid/)

  * [Video sobre regímenes de facturación](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/regfact_gral_vid/)

  * [Video sobre tarjetas de regalo](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjregalo_gral_vid/)
