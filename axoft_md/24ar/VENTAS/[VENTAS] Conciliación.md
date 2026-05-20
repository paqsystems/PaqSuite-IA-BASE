# Conciliación

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_nexocobr_gv/?p=10169/

## Contenido

# Conciliación

Mediante este proceso usted establecerá una comparación entre los movimientos bancarios de una cuenta (registrados contablemente mediante los comprobantes ingresados) y los movimientos que el banco u otra entidad le informa a través del extracto.

El objetivo de una conciliación es cotejar el extracto bancario contra las registraciones de la empresa. Dado que en general, el saldo contable de una cuenta no coincide con el saldo informado por el banco, la idea es encontrar las diferencias y analizar el motivo. Si se detectan las diferencias y sus causas, se habrá alcanzado el objetivo de la tarea de conciliar; es decir, saber si se produjeron las diferencias de los dos saldos y su justificación.

##### Situaciones causantes de diferencias

Son tres las situaciones causantes de diferencias:

  1. El banco afectó la cuenta por movimientos no registrados aún por la empresa.
  2. La empresa registró operaciones bancarias que aún no se han concretado en el banco.
  3. Errores por parte de la empresa o del banco.



__Nota

Generalmente, el motivo es la diferencia en las fechas de acreditación y débito de las cuentas.

**Ejemplos de las situaciones anteriores:**

  * Al recibir el extracto, la empresa se entera de una serie de débitos o créditos a su cuenta ocasionados en general por: gastos por mantenimiento de cuenta, impuesto a los cheques emitidos, intereses ganados, gastos de transferencias o giros, gastos por uso de cajero, gastos de emisión de extracto, etc.
  * Se realiza un pago a un proveedor con efectivo y cheques propios. La empresa contablemente acreditó la cuenta bancaria el día del pago, afectando su saldo. Hasta que esos cheques sean depositados por el proveedor y acreditados por el banco, éste aún no los tiene contabilizados; es decir que el saldo bancario no incluye dichos movimientos. Esta sería entonces una diferencia lógica al conciliar.
  * Errores de imputación en fechas, montos o cuentas tanto por parte del cliente como por parte del banco.



Si se trata de errores del cliente, procederá a su corrección y, si son por parte del banco, realizará la observación correspondiente

**Motivos de diferencia entre el saldo contable y el bancario:**

  * Depósitos contabilizados pendientes de acreditación por parte del banco.
  * Cheques librados pero no presentados al cobro.
  * Notas de débito o crédito computadas por el banco pero pendientes de contabilización en la empresa.
  * Errores por parte de la empresa: imputar cuentas erróneas, registrar importes incorrectos, omitir registraciones.
  * Errores por parte del banco: imputar cuentas erróneas, imputar cuentas por un importe incorrecto.



__Nota

Sugerimos como buena práctica, que al abrir la conciliación bancaria y previo a la conciliación automática, realice la conciliación de los movimientos de Tesorería que fueron revertidos (original y el que revierte). De esta forma evitará la conciliación automática entre los importes del extracto con importes de movimientos de reversión (movimiento revertido y movimiento que revierte).

##### Conciliación

Para facilitar la conciliación, este proceso le permite:

  * Visualizar con rapidez los movimientos que fueron conciliados.
  * Realizar una selección múltiple de movimientos y conciliarlos.
  * Ordenar los datos por columnas y agrupar.
  * Agregar columnas con datos referentes a movimientos, para un mejor agrupamiento o análisis.
  * Visualizar las modificaciones realizadas, mediante la identificación por colores.
  * Deshacer los cambios realizados.
  * Exportar la grilla a Excel o enviar a Vista preliminar.



También desde este proceso podrá consultar los extractos electrónicos importados desde [Importación de extractos electrónicos](?p=10344) y ejecutar una [conciliación automática](?p=10169#%c2%bfcomo-conciliar-automaticamente) entre el extracto y los movimientos registrados en Tesorería, ahorrando de esta forma tiempo en la realización de este proceso.

##### Movimientos a conciliar

Se solicita el ingreso de la información que detallamos a continuación.

Cuenta a conciliar: corresponde a una [cuenta](?p=10235) de tipo 'Banco' u 'Otras' que posea la opción 'Conciliable' habilitada.  
El sistema valida que el código de cuenta a conciliar esté definido en un único formato de extracto electrónico. De no ser así, se exhibe un mensaje de atención y no será posible continuar con la conciliación. Para más información, consulte el ítem Múltiples formatos de extracto electrónico.

Rango de fechas del extracto: es el rango de fechas del extracto a conciliar.  
Los movimientos que se concilien durante el proceso, tendrán asociados una fecha que corresponderá al período del extracto. Luego de realizar una conciliación, el sistema guardará el período conciliado para que usted pueda trabajar reiteradamente sobre él. Por ello, una nueva conciliación no deberá tener intersección de fechas con respecto a las conciliaciones ya realizadas.  
El sistema permite trabajar sobre uno existente, para ello selecciónelo presionando el botón "Buscar conciliaciones", o bien, generar un nuevo período de conciliación.  
Por defecto, se propone como fecha inicial la siguiente al último período conciliado. Si la cambia por una fecha ya incluida en otra conciliación, se presenta una lista de los períodos existentes. Puede optar por uno de ellos o ingresar una fecha que no pertenezca a un período procesado.  
En el caso de que el saldo inicial no coincida con el saldo final del último periodo conciliado, el sistema exhibirá un mensaje en donde podrá corregir esta diferencia.

Saldo inicial del extracto bancario: es el saldo inicial del extracto enviado por el banco.

  * Si hay una conciliación anterior a la que se va a realizar, el sistema propone su saldo como saldo inicial, pero lo puede modificar. Si sus conciliaciones fueron respetando los períodos de los extractos y fueron concluidas, estos saldos deben coincidir.
  * Si está reprocesando un período ya conciliado, el sistema propone el saldo inicial consignado en esa conciliación.
  * Si es la primera vez, el sistema no propone ningún valor.



Fechas para movimientos pendientes de conciliación: mediante este rango de fechas, el sistema incorporará en la pantalla para la conciliación, todos aquellos movimientos bancarios registrados en el módulo Tesorería cuyas fechas contables  (fechas de los comprobantes que generaron el movimiento) o bien fechas de cheques, pertenezcan al rango ingresado y que aún permanecen pendientes de conciliar.  
Es decir, los que aún no forman parte de ningún extracto conciliado.  
Por defecto, el sistema propone la Fecha Desde vacía y la Fecha Hasta igual a la fecha tope del extracto. De esta manera, usted se asegura de incluir todos los movimientos pendientes de conciliación hasta el momento de inicio del extracto, y todo lo que se ingresó en el sistema hasta la fecha en que el banco confeccionó el extracto.  
No obstante, estas fechas pueden acotarse o extenderse a su voluntad. Los cheques propios se tomarán por su fecha, el resto de los movimientos, por su fecha contable. Los comprobantes revertidos que involucraban a la cuenta y su correspondiente reversión se toman por fecha contable.

Saldo final del extracto: puede ingresar el saldo final que figura en el extracto, para verificar a que valor se debe llegar luego de la conciliación.

Genera reporte detallado: indique si al finalizar el proceso de conciliación desea generar el detalle de los movimientos conciliados, pendientes de registrar y los saldos resultantes.

##### Conciliar movimientos

El sistema exhibe una grilla en la que se muestran los movimientos comprendidos en los parámetros ingresados en la ventana anterior y se habilita la columna "Conciliar", dando la posibilidad de tildar los movimientos que coinciden con el extracto como de suprimirlo. Es decir que permite conciliar, desconciliar y si lo desea incluir un comentario.

Cada vez que se concilia un movimiento se asociará la fecha del extracto correspondiente. Por defecto, el sistema propone la fecha hasta de extracto procesado.

Movimientos

La información a visualizar de los movimientos asociados a la cuenta a conciliar son los siguientes:

  * **Fecha:** corresponde a la fecha del comprobante.
  * **Tipo:** tipo de comprobante ('REC', 'O/P', 'DEP', etc.).
  * **Nro. de comprobante:** número y dígito del comprobante.  
Haga clic sobre el número de comprobante para ingresar a la ficha Live del mismo.
  * **Detalle:** cuando el comprobante posee asociado cheques propios o cheques de tercero se detalla el número y fecha del mismo
  * **Importe:** el importe detallado en esta columna depende del tipo de visualización seleccionado y del tipo de comprobante.



__Nota

Para visualizar mas información de los comprobantes o de cheques, ingrese a la opción _Columnas_ de la barra de herramientas y habilite los datos que desea ver en la grilla.

Más información:

Si en la opción visualización se posee habilitada la opción "Total por comprobante" se mostrará el importe total de los comprobantes ingresados en Tesorería excepto aquellos que poseen asociados cheques propios, en este caso se visualizará el importe de este último.  
En este caso, para la boleta de depósito 000000000020/0 se muestra el total de la misma, pudiendo conciliar este comprobante por el importe total.

En cambio, si en la opción Visualización se encuentra habilitada la opción Comprobante detallado, para aquellos comprobantes que poseen asociados cheques de terceros se mostrarán los importes de los mismos, de lo contrario se visualizará el importe total del comprobante.  
En este caso, la boleta de depósito 000000000020/0 posee asociado tres cheques, los cuales en esta vista se visualizan en forma detallada. Esto permite visualizar el valor de cada cheque y conciliar cada uno por separado.

**Tenga en cuenta:  
**Si en la vista Total por comprobante se concilia un comprobante y éste está integrado por más de un cheque de tercero o efectivo, como ser una boleta de depósito, los movimientos que lo componen quedarán conciliados.  
Siguiendo con el ejemplo anterior, si se concilia la boleta de depósito 000000000020/0:

Al cambiar a la vista Comprobante detallado se mostrarán todos los cheques que la componen como conciliados:

Si en la vista Comprobante detallado se concilia un cheque de tercero (que pertenece a una boleta de depósito), y el resto de los cheques o efectivo que componen el comprobante no se concilian, al cambiar a la vista Total por comprobante se mostrará el comprobante asociado al cheque conciliado como parcialmente conciliado.  
Continuando con el ejemplo, si se concilia únicamente el cheque 127002 de la boleta de depósito 000000000020/0:

Al cambiar a la vista Total por comprobante se mostrará el comprobante parcialmente conciliado:

Recuerde que:

  * Los valores negativos se muestran entre () en color rojo.
  * Los importes se encuentran expresados en la moneda de la cuenta.



Saldos

Al pie de la grilla puede visualizar los saldos según los movimientos conciliados, éstos están compuestos por:

Saldo inicial: es el consignado al comenzar el proceso.

Saldo según movimientos conciliados: contiene el saldo inicial afectado por todos los movimientos que se hayan marcado como conciliados.

Total pendiente de registración: es la suma de movimientos que se encuentran en la pantalla de movimientos pendientes de registración.

__Nota

Si está activado _"Actualiza automáticamente saldos de conceptos pendientes de registrar"_ en _Parámetros de Tesorería_ y marca como conciliado un concepto pendiente del extracto, este importe se restará del total pendiente de registración  


Saldo resultante de la conciliación: contiene el saldo inicial afectado por los movimientos conciliados y los pendientes de registración.  
Este saldo será el que se proponga para el próximo período.

Saldo final del extracto: corresponde al importe ingresado en la pantalla anterior, al cual se debería llegar.

Diferencia: corresponde a la diferencia entre el Saldo resultante de la conciliación y el Saldo final del extracto, este importe es de utilidad para identificar la diferencia entre los movimientos de tesoreríay el extracto bancario.

**Funcionalidades y barra de herramientas**

En la barra de herramientas posee una serie de funcionalidades, ellas lo ayudarán a conciliar y a configurar cómo y qué datos de los movimientos desea visualizar. Estas funciones también pueden ser invocadas haciendo clic en el botón derecho del mouse sobre los campos de la grilla.

__Nota

Será posible aplicar estas funciones en más de una celda, utilizando la modalidad de multiselección.

Celda modificada: una celda es modificada cuando se ha editado (conciliado o desconciliado), cuando poseía un valor grabado, y dicho valor es cambiado.  
En este caso al modificar el precio la celda cambia a color verde pastel.

Conciliar: mediante está opción se marcan los movimientos seleccionados como conciliados.  
Desconciliar: mediante está opción se marcan los movimientos seleccionados como desconciliados.  
Deshacer: devuelve el valor original de o las celdas seleccionadas.  
Columnas: mediante esta opción puede seleccionar que columnas adicionales desea visualizar en la grilla en relación a los movimientos.  
Las columnas posibles son:

  * Tipo movimiento: tipo de movimiento en cuestión, las opciones posibles son: 'Comprobante', 'Efectivo', 'Cheque propio', 'Cheque propio rechazado', 'Cheque de tercero' y 'Cheque de tercero rechazado'.
  * Situación: se indica la situación del comprobante, si es 'Normal', 'Anulado' o un 'Contrasiento', como es en el caso de reversiones.
  * Tipo de cheque: se indica si el cheque es 'Común' o 'Diferido'.
  * Fecha cheque: corresponde a la fecha del cheque
  * Bco.: el código Banco al cual corresponde el cheque detallado. Los datos de esta columna se muestran cuando tipo de visualización es 'Comprobante detallado'.
  * Nombre: nombre Banco al que corresponde el cheque detallado. Los datos de esta columna se muestran cuando el tipo de visualización es 'Comprobante detallado'.
  * Suc. Bco. Emisor: sucursal del Banco emisor al que corresponde el cheque detallado. Los datos de esta columna se muestran cuando el tipo de visualización es 'Comprobante detallado'.
  * Nombre Bco. Emisor: el nombre del Banco emisor al que corresponde el cheque detallado. Los datos de esta columna se muestran cuando el tipo de visualización es 'Comprobante detallado'.
  * CP: el código postal ingresado en el cheque detallado. Los datos de esta columna se muestran cuando el tipo de visualización es 'Comprobante detallado'.
  * Clearing: el Clearing ingresado en el cheque detallado. Los datos de esta columna se muestran cuando el tipo de visualización es 'Comprobante detallado'.
  * Días: cantidad de días ingresado en el cheque detallado. Los datos de esta columna se muestran cuando el tipo de visualización es 'Comprobante detallado'.
  * Cód. Proveedor/Cliente: código de proveedor/cliente asociado al cheque detallado. Los datos de esta columna se muestran cuando el tipo de visualización es 'Comprobante detallado'.
  * Proveedor/Cliente: nombre de proveedor/cliente asociado al cheque detallado. Los datos de esta columna se muestran cuando el tipo de visualización es 'Comprobante detallado'.
  * Leyenda: corresponde a la leyenda ingresada en el renglón del movimiento de la cuenta en conciliación.
  * Total: esta opción es de utilidad cuando se utiliza el tipo de visualización por 'Comprobante detallado', ya que muestra el total de que aquellos comprobantes que poseen detalle (efectivo y cheques de terceros).



Visualización: mediante esta opción podrá configurar cómo y que movimientos desea ver en la grilla.

  * Movimientos: seleccione los movimientos que desea visualizar: 
    * Todos: se visualizan todos los movimientos (con y sin modificaciones).
    * Con cambios: se muestran únicamente los movimientos que poseen modificaciones.
    * Sin cambios: se muestran los movimientos que no poseen modificaciones.
  * Tipo de vista: mediante esta opción se podrá indicar que como desea visualizar los datos en la grilla de conciliación: 
    * Por comprobante detallado: visualizará el detalle de aquellos comprobantes que poseen efectivo y cheques de terceros (por ejemplo: boletas de depósito), los comprobantes sin detalle (por ejemplo: egreso) y los cheques propios (por ejemplo: orden de pago).  
En este ejemplo, la boleta de depósito 000000000020/0 posee asociado tres cheques, los cuales en esta vista se visualizan en forma detallada lo que permite conciliar cada uno por separado.



  *     * Por comprobante: para visualizar el importe total de aquellos comprobantes compuestos por efectivo y cheques de terceros, también los comprobantes sin detalle y los registros correspondientes a cheques propios.  
Continuando con el ejemplo, en la boleta de depósito 000000000020/0 se muestra el total de ésta, pudiendo conciliar el comprobante por el importe total.



Referencias: seleccione esta opción para conocer el significado de cada color aplicado en la grilla.

  * Verde: celda modificada.
  * Amarillo: comprobantes conciliados relacionados.
  * Rojo: importe negativo.



Conciliación automática: esta opción se habilita cuando se visualiza el extracto electrónico y ejecuta una conciliación entre los movimientos de Tesorería y del extracto en forma automática.  
Buscar: mediante esta opción se habilita, en el sector inferior de la grilla, un campo de búsqueda en la base a los datos de las columnas de la grillas.  
Enviar a Excel: exporta a Excel la grilla en pantalla. Si existen agrupaciones, será posible indicar si visualiza todas las agrupaciones en forma expandida.  
Vista preliminar: muestra el resultado que se obtendrá al imprimir la grilla en pantalla. Además, podrá modificar el estilo y el formato de impresión.  
Mostrar conciliados: presione este botón para obtener la grilla de aquellos movimientos que se encuentran conciliados.  
Mostrar no conciliados: presione este botón para obtener una grilla con aquellos movimientos que no se encuentran conciliados.  
Extracto: mediante esta opción visualizará los datos de los extractos electrónicos importados desde el proceso de [Importación de extractos electrónicos](?p=10344), y podrá ejecutar una conciliación previa con los movimientos de tesorería en forma automática.  
Para mas información consulte [¿Cómo conciliar automáticamente?](?p=10169#%c2%bfcomo-conciliar-automaticamente).  
Pendientes: esta opción se habilita cuando se visualiza el extracto electrónico, presionándolo se muestran los movimientos que han quedado pendientes de registrar como resultado de la conciliación automática.

###### ¿Cómo conciliar automáticamente?

Para conciliar automáticamente, previamente se debió importar el archivo .csv enviado por la entidad desde el proceso [Importación de extractos electrónicos](?p=10344).  
Seleccione las fechas de los movimientos a conciliar desde la opción extracto e indique si realiza una conciliación previa entre los registros del extracto y los movimientos de tesorería que se visualizan en la grilla en forma automática.

Período a procesar: seleccione las fechas desde/hasta del extracto que desea conciliar.

Datos de importación: seleccione en forma opcional de que extracto desea obtener los movimientos.  
Indique si realiza una conciliación automáticamente previa. En el caso de que no seleccione un número de importación indique que tipo de configuración se tendrá en cuenta para este proceso, si la definición de columnas del formato 'General' o 'Cheque'.  
Se habilitará una nueva grilla donde se muestran los datos del extracto electrónico y si se ejecutó la conciliación automática, a medida que se desplaza en la grilla puede visualizar los movimientos de tesorería que fueron conciliados con los movimientos del extracto identificados con color amarillo. Debe conciliar aquellos movimientos que no tienen coincidencia con los movimientos registrados en Tesorería.  
Para conciliar aquellos movimientos que quedaron pendientes, debe ingresar a la modalidad 'Relacionar'.  
Luego seleccione los comprobantes de tesorería que desea conciliar (haciendo clic sobre ellos, cuando debe seleccionar más de un movimiento debe mantener presionada la tecla <Ctrl>) y su correspondiente en el extracto. En este ejemplo conciliaremos los cheques 100 y 101 de la boleta 0000024/0 cuyo valor es de $2000,00 y $ 374,19 respectivamente ingresados en tesorería, con el "Depósito de cheques 48 hs." de valor $2374.90:  
Posteriormente, presione "Conciliar".  
De esta forma los movimientos seleccionados de Tesorería y del extracto quedan conciliados y relacionados.

Para visualizar como quedaron los movimientos, debe salir del modo relación presionando nuevamente el botón "Relacionar" y posicionarse sobre el movimiento conciliado:  
Al visualizar el extracto no verá aquellos valores correspondientes a comisiones bancarias, impuesto al cheque, IVA, etc., que previamente se han definido como conceptos pendientes de registrar en [Definición de formato del extractos electrónicos.](?p=10209) Ello le permitirá trabajar solamente con aquellos movimientos que le interesan. Si desea visualizar los registros que han quedado pendientes de registrar, presione el botón "Pendientes".

**¿Cómo se comparan los movimientos?  
**Para la ejecución de la conciliación automática se tiene en cuenta la configuración de columnas definida en [Definición de formato de extracto electrónico](?p=10209) en el sector Conciliación automática.

**Ejemplo:  
**Para el caso de la definición de un archivo con formato 'Delimitado', el dato 'Fecha' del extracto interviene en la conciliación automática buscando que sea 'Igual' a la fecha del comprobante de tesorería.

La misma configuración es tenida en cuenta para el resto de las columnas. En el caso de que se utilice la equivalencia 'Contiene' al conciliar automáticamente se buscara que, por ejemplo, el número de comprobante de tesorería se encuentre en la columna "Nro. de comprobante" del extracto.

  * En la conciliación no se tiene en cuenta aquellos movimientos que ya se encuentran conciliados.
  * Para los depósitos se concilia el total del comprobante o por el importe de cada cheque.



_Pendientes de registrar  
_En el caso de aquellos registros del extracto electrónico que deben quedar como conceptos pendientes de registrar, el sistema tendrá en cuenta lo configurado en [Definición de formato de extracto electrónico](?p=10209) en la solapa Pendientes de registrar.

###### Pendientes de registrar

Posteriormente accederá a la actualización de conceptos existentes en el extracto y que no tiene registrados: si está reprocesando un extracto y ya existen conceptos cargados para la cuenta, el sistema los mostrará en pantalla.  
Estos conceptos componen el total pendiente de registración. En general, son movimientos que el cliente de un banco conoce cuando recibe el extracto (gastos, comisiones, recargos, etc.).  
Usted podrá navegar entre las dos pantallas, observando en cada una el saldo conciliado.

__Nota

Si está activado <<Actualiza automáticamente saldos de conceptos pendientes de registrar>> en Parámetros de tesorería, se restará al saldo de cada concepto - fecha de los renglones del extracto que hayan estado marcado como pendientes de registrar y hayan sido conciliados en este proceso. En caso de existir dos o más renglones para un mismo concepto y fecha se descontará del primero.  


Fecha: es la fecha con la que se registrará la transacción.

Concepto a registrar: ingrese el código de concepto de conciliación a registrar, o selecciónelo mediante la función Buscar presionando <F7>.

D/H e Importe: indique el tipo de movimiento de la cuenta (deudor o acreedor) y el importe correspondiente en la moneda de la cuenta.

Si desea eliminar una un concepto pendiente de registrar, pulse la tecla <Supr>.  
Al igual que en la pantalla anterior, aquí también se visualizan los saldos resultantes de la conciliación pero se tienen en cuenta los nuevos conceptos pendientes de registrar ingresados:

Saldo inicial: es el consignado al comenzar el proceso.

Saldo según movimientos conciliados: contiene el saldo inicial afectado por todos los movimientos que se hayan marcado como conciliados.

Total pendiente de registración: es la suma de movimientos que se encuentran pendientes de registración.

Saldo resultante de la conciliación: contiene el saldo inicial afectado por los movimientos conciliados y los pendientes de registración. Este saldo será el que se proponga para el próximo período.

Saldo final del extracto: corresponde al importe ingresado en la pantalla anterior, al que se debería llegar.

Diferencia: corresponde a la diferencia entre el Saldo resultante de la conciliación y el Saldo final del extracto, este importe es de utilidad para identificar la diferencia entre los movimientos de tesorería y el extracto bancario.

###### Informe

Una vez confirmado todo el proceso, el sistema emitirá un informe con el detalle de los movimientos conciliados, conceptos pendientes de registrar y los saldos resultantes.

__Nota

Luego de realizar la conciliación, usted debe efectivizar los movimientos anotados como pendientes de registración, y en algún momento, reprocesar la conciliación para que pasen a ser movimientos conciliados.

Puede consultar mas información de los movimientos conciliados, no conciliados y pendientes de registrar, desde Live.

##### Múltiples formatos de extracto electrónico

Si existe más de un formato de extracto electrónico con la misma cuenta asociada, debe definir cuál de todos los formatos utilizará para esa cuenta.  
Los formatos restantes deben eliminarse o bien, modificarse (para eliminar los códigos de conceptos ingresados en la solapa Pendientes de registrar). Para ello, ejecute la opción [Definición de formato de extracto electrónico](?p=10209).  
Si al eliminar un formato de extracto electrónico existe una importación de extracto asociada, deberá depurar esa importación. Para ello, ejecute la opción [Depuración de extractos electrónicos](?p=10213).  
Una cuenta sólo podrá estar asociada a un formato de extracto electrónico.

##### Contenidos relacionados

  * [Video sobre conciliación bancaria](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/concilbancaria_sb_vid/)

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre movimientos masivos de Tesorería](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/movimasivo_sb_vid/)

  * [Videos sobre conciliación bancaria automática](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/concilbancautom_sb_vid/)

  * [Videos sobre el Facturador](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/facturador_gv_vid/)
