# Guía sobre implementación de Tango Colectora

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_colectora_st/

## Contenido

# Guía sobre implementación de Tango Colectora

Esta guía está orientada a quienes deseen realizar el conteo de entradas, salidas y tomas de inventario utilizando dispositivos **Android**.

Tango Colectora es una aplicación para dispositivos móviles compatibles con Android (disponible en Play Store) que permitirá realizar conteos físicos de artículos para luego ser procesados desde el sistema durante la confección de movimientos de entrada o salida y tomas de inventario.

**Formatos soportados  
**La aplicación Tango Colectora es compatible con la mayoría de los códigos de barras lineales. Los formatos soportados son:

  * EAN-13
  * EAN-8
  * Code-128
  * Code-39
  * Code-93
  * UPC-A
  * UPC-E
  * QR



Con Tango Colectora usted podrá:

  * Descargar información de las tomas de inventario en el dispositivo para luego realizar su conteo físico.
  * Realizar conteos de entrada o salida para luego registrar ingresos o egresos en el sistema.
  * Utilizar la cámara del dispositivo para contar los productos mediante el código de barras.
  * Utilizar una pistola láser bluetooth conectada al dispositivo para leer códigos de barra con mayor precisión.
  * Utilizar una colectora compatible con Android, con láser integrado.
  * Realizar conteo buscando manualmente artículos e ingresando cantidades.
  * Registrar los saldos de las partidas de cada artículo.
  * Buscar el artículo a incrementar por SKU, sinónimo, código de barras o descripción.
  * Eliminar conteos de toma de inventario descargados previamente o bien conteos de entrada o salida creados desde la aplicación.
  * Agregar renglones al conteo de una toma de inventario.
  * Utilizar varios dispositivos en simultáneo para realizar conteos de una misma toma de inventario.



__Nota

Tenga en cuenta que sólo se pueden utilizar tomas de inventario generadas por el proceso Toma de inventario (Movimientos masivos).

##### Puesta en marcha

  1. Defina las [Colectoras](http://ayudas.axoft.com/24ar/colectora_st) que utilizará en el conteo de los artículos.
  2. Descargue, en los dispositivos que utilizará para realizar el conteo de los artículos, la aplicación Tango Colectora desde Play Store. Los requisitos que deben cumplir los dispositivos son: 
     1. Android 8.0 o posterior.
     2. Al menos 100 Mb de espacio disponible en el almacenamiento interno.
     3. Conexión a Internet (Wifi o Datos).
     4. Recomendado, cámara de fotos o pistola láser.
  3. Ingrese a la aplicación y complete los datos de conexión a su sistema Tango. 
     1. Código de colectora: definido en el proceso [Colectoras](http://ayudas.axoft.com/24ar/colectora_st).
     2. Token: para obtener el TOKEN, ingrese al Menú web del sistema | Menú de usuario y seleccione la opción Desarrollador; luego de ingresar pulse sobre el botón "Generar" y obtendrá el Token. Pulse "Aceptar" para guardar el token generado.  
**Importante:** el usuario debe tener permiso de acceso a Empresas, esto se define desde Administrador | Seguridad | Usuarios | Permisos de administración, habilitando el ítem Administrador | Empresas | Empresas (no es necesario habilitar ningún atributo dentro de la rama, sólo el acceso a esta).
     3. Número de llave de su sistema.
     4. Conexión: 
        1. Tango Connect: conéctese sin necesidad de estar en la misma red que su sistema Tango. Para ello, consulte la puesta en marcha de [Tango Connect](?p=30792).
        2. Red local donde se encuentra su servidor: complete el nombre del servidor y el número de puerto.
     5. Presione el tilde en la parte superior derecha para confirmar.



##### Detalle del circuito de conteo para toma de inventario

  1. Cree una nueva toma de inventario desde Stock | Movimientos | Movimientos masivos | Toma de inventario y seleccione los artículos a contar.
  2. Ejecute la acción 'Comenzar conteo' seleccionando como origen 'Aplicación Tango Colectora'. Puede definir si el conteo será multi-colectora mediante el parámetro Permite realizar el conteo desde múltiples colectoras. En caso de estar destildado, deberá indicar una Colectora.
  3. Ingrese al dispositivo en el que ya tiene instalado y configurado Tango Colectora y desde el menú principal seleccione la empresa y el depósito, luego presione "Toma de inventario".  
Seleccione una toma de inventario de la lista (sólo se mostrarán las pendientes para ese dispositivo y/o aquellas que no tienen asignada una colectora). Si confirma se obtendrán los artículos de la toma y quedará registrada como 'En proceso' por este dispositivo. Para realizar este paso es necesario estar conectado a Internet.
  4. Para buscar los artículos a contar podrá hacerlo utilizando: 
     1. El buscador de la parte superior.
     2. La cámara del dispositivo, leyendo un código de barras.
     3. Una pistola bluetooth o láser integrado.  
Tenga en cuenta que si utiliza alguno de los métodos de escaneo de código de barras, automáticamente se incrementará la cantidad del artículo al leerlo.  
Una vez seleccionado un artículo, podrá modificar manualmente la cantidad en caso de querer registrar varias unidades o corregir el valor.  
Si el artículo lleva partidas, se tendrá en cuenta la parametrización de modo de asignación de partidas en toma de inventario (manual o automático) para solicitar el número de la partida a la cual asignar la cantidad registrada, o puede utilizar la cámara o el láser para leer la partida en caso de tenerla disponible en código de barras.
     4. Si el artículo lleva doble unidad de medida, complete las cantidades en ambas unidades.
     5. Podrá filtrar sólo artículos pendientes de contar, para agilizar el trabajo.
     6. Al finalizar el conteo, presione el botón para subir la información a su sistema Tango.
     7. Para continuar con el circuito, desde el sistema ingrese al proceso [Toma de inventario masiva](http://ayudas.axoft.com/24ar/ajusteinventariocolectora_st), seleccione la acción 'Importar conteo de inventario', y elija el comprobante a procesar.
     8. Al seleccionar una toma de inventario que registre conteos desde la aplicación, se mostrará un detalle con los datos obtenidos de la colectora para confirmar y continuar con la toma.
     9. Al finalizar la actualización, se impactarán todas las cantidades ingresadas en la aplicación en la toma de inventario.



A partir de este punto, el circuito de toma de inventario continúa de la misma forma que si la realizara manualmente o a través de Excel:

  * Procesar diferencias.
  * Generar ajuste.



Para más información, consulte [Toma de inventario masiva](http://ayudas.axoft.com/24ar/ajusteinventariocolectora_st).

##### Detalle del circuito de conteo de entrada

  1. Ingrese al dispositivo en el que ya tiene instalado y configurado Tango Colectora y desde el menú principal seleccione la empresa y el depósito, luego presione "Entradas".
  2. Presione el botón "+" para crear un nuevo conteo de entrada. Se solicitará una referencia para identificar dicho conteo.
  3. Seleccione el tipo de comprobante a generar. Las opciones son: 
     1. **Ingreso:** el conteo se utilizará para registrar un ingreso de stock.
     2. **Remito:** el conteo se utilizará para registrar un remito de compras. En caso de seleccionar esta opción, se solicitará ingresar el proveedor del remito.
     3. **Sin definir:** el conteo podrá ser utilizado para registrar tanto un ingreso de stock como un remito de compras.
  4. Para agregar un nuevo artículo al conteo, presionar el botón de código de barras. En la pantalla que se muestra se podrá escanear el artículo que se desee o bien presionar en el botón de lupa y buscar el mismo a través de su descripción. Una vez que se completen todos los datos obligatorios, presionar el tilde para guardar los cambios.
  5. Repetir el paso anterior para todos los artículos que se deseen incluir en el conteo de entrada.
  6. Al finalizar, presionar el botón de subida.



A partir de este punto, el circuito continúa desde el ítem de Ingreso de stock masivo, seleccionando la opción Registrar ingreso de stock, o del ítem Ingreso de remito por Excel o Tango Colectora seleccionando la opción Registrar remito de compras.

Para más información, consulte [Ingreso de stock masivo](http://ayudas.axoft.com/24ar/ingresostmasivo_st), o bien, [Ingreso de remitos por Excel o Colectora](https://ayudas.axoft.com/24ar/ingresoexcelcolect_cp).

##### Detalle del circuito de conteo de salida

  * Ingrese al dispositivo en el que ya tiene instalado y configurado Tango Colectora y desde el menú principal seleccione la empresa y el depósito, luego presione "Salidas".
  * Presione el botón "+" para crear un nuevo conteo de salida. Se solicitará una referencia para identificar dicho conteo.
  * Para agregar un nuevo artículo al conteo, presionar el botón de código de barras. En la pantalla que se muestra se podrá escanear el artículo que se desee o bien presionar en el botón de lupa y buscar el mismo a través de su descripción. Una vez que se completen todos los datos obligatorios, presionar el tilde para guardar los cambios.
  * Repetir el paso anterior para todos los artículos que se deseen incluir en el conteo de salida.
  * Al finalizar, presionar el botón de subida.



A partir de este punto, el circuito continúa desde el ítem de Egreso de stock masivo seleccionando la opción Registrar egreso de stock.  
Para más información, consulte [Egreso de stock masivo](http://ayudas.axoft.com/24ar/egresostmasivo_st).

##### Contenidos relacionados

  * [Colectoras](https://ayudas.axoft.com/24ar/ayudas/st/archivos_carp_st/actualizacion_carp_st/colectora_st/)

  * [Videos sobre Tango Colectora](https://ayudas.axoft.com/24ar/videos/st_carp_vid/colectora_st_vid/)
