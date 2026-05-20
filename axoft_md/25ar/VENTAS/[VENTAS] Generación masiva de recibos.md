# Generación masiva de recibos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=21361/

## Contenido

# Generación masiva de recibos

Desde este proceso, usted genera en forma masiva los recibos por las cobranzas provenientes de los siguientes orígenes:

  * De una entidad recaudadora (Pagomiscuentas®, Pago Fácil® o Rapipago®).
  * De [Tango Cobranzas](?p=12425).
  * De un formato Tango (archivo .xls).
  * De un ingreso manual.
  * De cobranzas no procesadas.



También es posible generar los comprobantes de ajuste por cobro en fechas alternativas.  
Para ello, ingrese a la solapa Comprobantes de ajuste; tilde el parámetro Genera ajustes por cobro en fechas alternativas / recargo financiero y defina los datos relacionados: Tipo de comprobante (para créditos y/o débitos); Talonarios; Generación de asientos contables; Modalidad de cálculo de impuestos y si corresponde, los Datos para comprobantes electrónicos (indicador de servicio y período). Para imprimir dichos comprobantes, ingrese al proceso [Impresión de Comprobantes de Ajuste](https://ayudas.axoft.com/25ar/imprcomprajuste_gv).  
La fecha de los comprobantes de ajuste por cobro en fechas alternativas será la fecha del recibo o la fecha del día, según lo configurado en [Parámetros de Ventas](?p=19401) (parámetro Fecha a asignar).  
Para más información, consulte la [Guía de implementación sobre fechas alternativas de vencimiento](?p=26634).

Si el origen es una 'Entidad recaudadora' (Pagomiscuentas®, Pago Fácil® o Rapipago®) o [Tango Cobranzas](?p=12425), ingrese el código de [configuración para cobranzas masivas](https://ayudas.axoft.com/25ar/configcobranzamasiva_gv).  
En el caso de cobranzas provenientes de otro origen ('Formato Tango', 'Manual' y 'Cobranzas no procesadas') el ingreso de una configuración no es obligatorio. En estos casos, usted ingresa los datos de configuración en las solapas del proceso ('Datos para recibos', 'Datos para Tesorería' y 'Observaciones').  
Por último, verifique el talonario a utilizar.

Tenga en cuenta:

La generación masiva de recibos no realiza notas de débito por mora. Las mismas pueden ser generadas desde el asistente [Gestión de débitos por mora](?p=21387).

##### Cobranzas de una entidad recaudadora

Desde esta opción, se generan los recibos en forma masiva y automática, por las cobranzas recibidas por una entidad recaudadora (Pagomiscuentas®, Pago Fácil® o Rapipago®).

Consideraciones para _Pagomiscuentas_

  * Los [clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv) se identifican a través del código asignado en el sistema, o bien, de su número de pago electrónico.
  * No se contempla su identificación mediante el número de CUIT o cualquier otro código alternativo.



Consideraciones para _Pago Fácil_

  * Se procesarán las cobranzas recepcionadas por esta entidad, que cumplan con las siguientes características: 
    * Abonadas en efectivo.
    * Asociadas a facturas que tengan impreso un código de barras standard, que respeta el diseño de código de barras de la entidad. Para más información, consulte el proceso [Parámetros para códigos de barra](https://ayudas.axoft.com/25ar/paramcodigbarra_gv).
    * Que hagan referencia a una fecha de vencimiento.
  * Es fundamental la correcta definición del código de barras a imprimir en las facturas. De este paso depende la correcta imputación de la cobranza en el proceso [Generación masiva de recibos](https://ayudas.axoft.com/25ar/generacionmasivarecibo_gv).
  * Para una correcta imputación de las cobranzas desde el proceso [Generación masiva de recibos](https://ayudas.axoft.com/25ar/generacionmasivarecibo_gv), asigne a cada [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) un número de pago electrónico válido.
  * El número de pago electrónico del cliente, la fecha del primer vencimiento (cuota) y el importe al primer vencimiento definen el comprobante de referencia de cada cobranza. Estos datos se toman del código de barra impreso en el comprobante presentado en la entidad recaudadora.
  * Si la fecha de vencimiento informada en el código de barras no existe o fue cancelada, la cobranza quedará 'A cuenta' o bien, imputada según el criterio de imputación definido en el proceso [Parámetros de ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).
  * Para aquellos comprobantes que tengan más de un vencimiento (cuota), el cliente podrá abonar en Pago Fácil el primer vencimiento. Ya que el comprobante tiene un único código de barras.
  * No se contempla la modalidad de operación 'Pago sin factura' (no se exporta información de las facturas a esta entidad).
  * Si en el archivo de transmisión (cobranzas) recibido de la entidad existen transacciones con cheques, éstas no serán consideradas por el proceso [Generación masiva de recibos](https://ayudas.axoft.com/25ar/generacionmasivarecibo_gv). 
    * Estas cobranzas se informan en la ventana de 'Detalle de cobranzas con cheques'.
    * Usted puede imprimirlas o bien, exportarlas a Excel.
    * Para registrarlas en el sistema, utilice el proceso [Cobranzas](https://ayudas.axoft.com/25ar/ingresocobranza_gv).
  * Si para un mismo cliente se detecta más de una factura con igual fecha de vencimiento e importe, el proceso [Generación masiva de recibos](https://ayudas.axoft.com/25ar/generacionmasivarecibo_gv) imputará la cobranza a la primera de esas facturas encontrada.
  * Diseño del archivo de transmisión.  
A través de los Archivos de Transmisión, SEPSA notifica a las empresas las transacciones realizadas en toda su red. La empresa recibirá un Archivo de Transmisión por día, conteniendo las transacciones realizadas el día o días anteriores (este último caso se da los días Lunes, donde se informa lo cobrado el día Viernes, Sábado y Domingo).  
Estos archivos están compuestos por lotes que agrupan hasta 500 transacciones, y cada transacción es informada por tres registros de detalle.



Registro Cabecera del Archivo

**Campo** | **Tipo** | **Longitud** | **Descripción**  
---|---|---|---  
Record Code | Núm. | 1 | Código de registro. Valor '1'.  
Create Date | Núm. | 8 | Fecha de creación. Formato: AAAAMMDD.  
Origin Name | Alf. | 25 | Valor 'PAGO FACIL'.  
Client Number | Núm. | 9 | Número de la Empresa.  
Client Name | Alf. | 35 | Nombre de la Empresa.  
Filler | Alf. | 50 | Completa la longitud fija del registro.  
  
Registro Cabecera del Lote (sólo uno por lote)

**Campo** | **Tipo** | **Longitud** | **Descripción**  
---|---|---|---  
Record Code | Núm. | 1 | Código de registro. Valor '3'.  
Create Date | Núm. | 8 | Fecha de creación. Formato: AAAAMMDD.  
Batch Number | Núm. | 6 | Número del Lote.  
Description | Alf. | 35 | Nombre de la Empresa.  
Filler | Alf. | 78 | Completa la longitud fija del registro.  
  
Registro de detalle. Información detallada de cada transacción.

**Campo** | **Tipo** | **Longitud** | **Descripción**  
---|---|---|---  
Record Code | Núm. | 1 | Código de registro. Valor '5'.  
Record Sequence | Núm. | 5 | Número de secuencia de transacción dentro del Lote.  
Transaction Code | Núm. | 2 | Código de Transacción.  
Work Date | Núm. | 8 | Fecha de Proceso. Formato: AAAAMMDD.  
Transfer Date | Núm. | 8 | Fecha de creación. Formato: AAAAMMDD1.  
Account Number | Alf. | 21 | Identificación de la Transacción (campo “Cliente” del registro del código de barras).  
Currency Code | Alf. | 3 | Moneda Txs.  
Amount | Núm. | 10 | Importe cobrado.  
Terminal Id. | Alf. | 6 | Terminal en la cual se efectuó la transacción.  
Payment Date | Núm. | 8 | Fecha en que se efectuó la Transacción. Formato: AAAAMMDD.  
Payment Time | Núm. | 4 | Hora de la Transacción. Formato: HHMM  
Term Seq. Number | Núm. | 4 | Número de secuencia de transacción dentro de la terminal.  
Filler | Alf. | 48 | Completa la longitud fija del registro.  
  
1 Es también fecha de transferencia del archivo / fondos (sólo dentro de las 24hs.)

Registro de detalle. Código de Barras de la transacción.

**Campo** | **Tipo** | **Longitud** | **Descripción**  
---|---|---|---  
Record Code | Num. | 1 | Código de registro. Valor '6'.  
Bar Code | Num. | 50 | Código de Barras de la Transacción.  
Type Code | Alf. | 1 | Identifica el origen del código de barras. Valores “S” Site, “O” Online, “ “ Tradicional.  
Filler | Alf. | 46 | Completa la longitud fija del registro.  
  
Registro de detalle. Detalle de los instrumentos de pago.

**Campo** | **Tipo** | **Longitud** | **Descripción**  
---|---|---|---  
Record Code | Num. | 1 | Código de registro. Valor '7'.  
Currency Code | Alf. | 3 | Moneda del instrumento de pago. Valor ‘PES’: Pesos.  
Pay Instrument | Alf. | 1 | Código Instrumento de pago. Valores: ‘E’: Efectivo, ‘C’: Cheque.  
Code Bar. Pay Inst. | Alf. | 80 | Código de Barras del instrumento de pago (CMC7 cheques). Ver diseño anexo.  
Amount | Num. | 15 | Importe del instrumento de pago.  
Filler | Alf. | 28 | Completa la longitud fija del registro.  
  
Registro Cola del Lote. Información total del lote (sólo uno por lote).

**Campo** | **Tipo** | **Longitud** | **Descripción**  
---|---|---|---  
Record Code | Num. | 1 | Código de registro. Valor '8'.  
Create Date | Núm. | 8 | Fecha de creación del archivo. Formato: AAAAMMDD.  
Batch Number | Núm. | 6 | Número del Batch.  
Batch Payment Count | Núm. | 7 | Cantidad de transacciones del Lote.  
Batch Payment Amount | Núm. | 12 | Importe total cobrado del Lote.  
Filler | Núm. | 38 | Valor '0'.  
Batch Count | Núm. | 5 | Cantidad de transacciones del Lote.  
Filler | Alf. | 51 | Completa la longitud fija del registro  
  
Registro Cola del Archivo. Información total del archivo (sólo uno por archivo)

**Campo** | **Tipo** | **Longitud** | **Descripción**  
---|---|---|---  
Record Code | Núm. | 1 | Código de registro. Valor '9'.  
Create Date | Núm. | 8 | Fecha de creación del archivo. Formato: AAAAMMDD.  
Total Batches | Núm. | 6 | Cantidad total de los lotes en el Archivo.  
File Payment Count | Núm. | 7 | Cantidad total de transacciones del Archivo.  
File Payment Amount | Núm. | 12 | Importe total cobrado del archivo.  
Filler | Núm. | 38 | Valor '0'.  
File Count | Núm. | 7 | Cantidad total de transacciones del Archivo.  
Filler | Alf. | 49 | Completa la longitud fija del registro.  
  
Consideraciones para _Rapipago_

  * Se procesarán las cobranzas recepcionadas por esta entidad, que cumplan con las siguientes características: 
    * Abonadas en efectivo.
    * Asociadas a facturas que tengan impreso un código de barras que respete el diseño de código de barras reconocido por Tango para esa entidad. Para más información, consulte el proceso [Parámetros para códigos de barra](https://ayudas.axoft.com/25ar/paramcodigbarra_gv).
    * Que hagan referencia a una fecha de vencimiento.
  * Es fundamental la correcta definición del código de barras a imprimir en las facturas. De este paso depende la correcta imputación de la cobranza en el proceso [Generación masiva de recibos](https://ayudas.axoft.com/25ar/generacionmasivarecibo_gv).
  * Para una correcta imputación de las cobranzas desde el proceso [Generación masiva de recibos](https://ayudas.axoft.com/25ar/generacionmasivarecibo_gv), asigne a cada [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) un número de pago electrónico válido.
  * El número de pago electrónico del cliente, la fecha del primer vencimiento (cuota) y el importe al primer vencimiento definen el comprobante de referencia de cada cobranza. Estos datos se toman del código de barra impreso en el comprobante presentado en la entidad recaudadora.
  * Si la fecha de vencimiento informada en el código de barras no existe o fue cancelada, la cobranza quedará 'A cuenta' o bien, imputada según el criterio de imputación definido en el proceso [Parámetros de ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).
  * Para aquellos comprobantes que tengan más de un vencimiento (cuota), el cliente podrá abonar en Rapipago el primer vencimiento. Ya que el comprobante tiene un único código de barras.
  * No se contempla la modalidad de operación 'Pago sin factura' (no se exporta información de las facturas a esta entidad).
  * Si para un mismo cliente se detecta más de una factura con igual fecha de vencimiento e importe, el proceso [Generación masiva de recibos](https://ayudas.axoft.com/25ar/generacionmasivarecibo_gv) imputará la cobranza a la primera de esas facturas encontrada.
  * Diseño del archivo de transmisión  
El archivo de imputación de pagos contendrá un registro "Header" y un registro "Trailer" a efectos de control además de los registros de detalle:  
Nombre: RPddmmaa.eee  
(ddmmaa corresponden a fecha de proceso Gire y eee a código de entidad de transmisión a definir por Gire)  
Longitud de registros: 73



Registro "Header"

**Orden** | **Campo** | **Longitud** | **Formato** | **Observación**  
---|---|---|---|---  
1 | Id_header | 8 | N | Ceros  
2 | Nombre de la empresa. | 20 | C |   
3 | Fh_proceso | 8 | N | aaaammdd  
4 | Id_archivo | 20 | C | "Cobranzas Rapipago"  
5 | Filler | 17 | A | Blancos  
  
Registro Detalle

**Nro.** | **Nombre del campo** | **Longitud** | **Formato** | **Observación**  
---|---|---|---|---  
1 | Fecha de cobro | 8 | N | Aaaammdd  
2 | Importe cobrado | 15 | N | 13e + 2 d  
3 | Código de barras | X | C |   
  
Registro "Trailer"

**Orden** | **Campo** | **Longitud** | **Formato** | **Observación**  
---|---|---|---|---  
1 | Id_trailer | 8 | N | 99999999  
2 | Cant_reg | 8 | N | Cantidad de registros (sin incluir Header y Trailer)  
3 | Importe_tot | 18 | N | [16e + 2d] importe total  
4 | Filler | 39 | A | Blancos  
  
Archivo de cobranzas: por defecto, se exhibe la ubicación definida en la configuración seleccionada. Caso contrario, indique la ubicación del archivo a importar. Utilice el botón "Examinar" para seleccionar la carpeta con facilidad.

##### Cobranzas de Tango Cobranzas

Seleccionando esta modalidad, se pueden generar recibos de cobranzas provenientes de dicho origen que no hayan sido generados automáticamente por el servicio de [Tango Cobranzas](?p=12425).

Tenga en cuenta:

Si se deja en blanco el campo leyenda de la contracuenta en la solapa Datos para Tesorería, se informará el número de transacción del sistema de pago en dicho campo.

##### Cobranzas según un formato Tango (.xls)

En esta modalidad, usted trabaja con un archivo Excel (.xls o .xlsx).  
Haga clic en el botón "Generar planilla". La importación de un archivo Excel tiene el mismo comportamiento que la importación de un archivo de cobranzas proveniente de una entidad recaudadora.  
El proceso verifica el formato y contenido del archivo seleccionado.  
En el caso de existir errores, se exhibe un mensaje de atención y a continuación, el detalle de las inconsistencias detectadas.  
Corrija los errores detectados en la planilla e intente nuevamente generar los recibos en forma masiva.  
Para incluir más de un comprobante en un mismo recibo, complete la grilla de la siguiente manera:

En el ejemplo anterior, se generará un recibo de cobranzas para el cliente '010001' con fecha 23/05/2013 por un importe total de $5.000 y con referencia a las facturas A0001-00000321 - vencimiento 03/05/2012 y a la factura A0001-00000321 - vencimiento 02/06/2012.

##### Cobranzas 'manuales'

Utilice esta opción para registrar de una manera rápida y sencilla, las cobranzas recibidas por cobradores o agentes de su empresa.  
Usted ingresa la información en una grilla, como si operara con una planilla de cálculo.

Grilla de movimientos  
Ingrese el código de cliente, la fecha de cobro, el importe (en moneda corriente) y, de manera opcional, el detalle de los comprobantes afectados a la cobranza.  
Si para el [talonario](https://ayudas.axoft.com/25ar/talonario_gv) elegido no se aplica la numeración automática, usted debe ingresar el Número de recibo para cada cobranza.  
En la columna "Punto de Venta" se propone por defecto, el valor definido en el talonario.

##### Detalle de comprobantes

En la ventana de ingreso de comprobantes a imputar, si el importe a aplicar es menor al importe total del vencimiento, se exhibirá un mensaje de aviso para solicitar su confirmación.  
Si confirma la operación, el valor ingresado quedará imputado.  
Si no confirma la operación, deberá seleccionar otro vencimiento.  
Si el importe cobrado (ingresado en la grilla principal) fue totalmente aplicado, al intentar seleccionar un nuevo comprobante de referencia, se exhibirá un mensaje de atención avisando que el importe cobrado fue totalmente aplicado.

##### Cobranzas no procesadas

Elija esta opción si luego de una generación masiva, quedaron cobranzas sin un recibo generado.  
Estas cobranzas pendientes o no procesadas se informan, diferenciadas por su origen.  
En la grilla de detalle, usted puede conocer el motivo por el que no se generaron los recibos.  
Algunos ejemplos: talonario terminado; problemas con la PC / servidor; problemas con la impresora; no existe una dirección de e-mail para el envío del recibo.  
Pasos a realizar:

  * Solucione el / los inconvenientes que impidieron la generación de los recibos.
  * Recuerde que puede editar o modificar los datos de la grilla si el origen de las cobranzas es 'Manual' o 'Formato fijo'. Para ello, seleccione el registro a modificar y luego, edite la columna correspondiente.
  * Seleccione las cobranzas a procesar. Puede tildar el parámetro Seleccionar todos.
  * Haga clic en el botón "Aceptar" o pulse <F10> para iniciar la nueva generación de recibos.



En el caso de cobranzas provenientes de Pago Fácil®, si el cliente informado en el código de barras no existe; verifique la asignación del código de pago electrónico de sus clientes desde el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv), o bien, utilizando la consulta Live Nómina de clientes. Luego, desde el proceso [Generación masiva de recibos](https://ayudas.axoft.com/25ar/generacionmasivarecibo_gv), opción Cobranzas no procesadas, complete el código de cliente en la grilla de Cobranzas no procesadas y vuelva a procesar el movimiento.

##### Resultado de la generación

Finalizada la generación masiva de recibos, se informan los siguientes datos:

  * origen de las cobranzas.
  * cantidad de cobranzas procesadas (o importadas).
  * cantidad de recibos generados.
  * importe total de los recibos generados.
  * cantidad de correos electrónicos enviados.
  * cantidad de WhatsApp enviados.
  * cantidad de recibos impresos.
  * cantidad de cobranzas no procesadas.
  * importe total de las cobranzas no procesadas.



Desde los botones "Ver detalle" usted puede acceder a las consultas Live de los recibos generados y de las cobranzas pendientes de generar.  
En la consulta de recibos generados, puede activar la columna "Entidad" para ordenar la información por ese criterio.  
Desde la consulta Live Cobranzas por entidad recaudadora, usted tiene información de los recibos generados por entidad.  
Tenga en cuenta que los recibos sin una entidad asignada fueron generados desde el proceso [Cobranzas](https://ayudas.axoft.com/25ar/ingresocobranza_gv).

**Consideraciones generales**

  * La generación masiva de recibos contempla operaciones realizadas en efectivo y en PESOS.
  * No es posible generar en forma masiva, cobranzas a clientes definidos como cláusula moneda extranjera.
  * El proceso de generación masiva toma por defecto los datos de la configuración seleccionada, pero ésta no es determinante para el proceso. Es decir, éstos pueden ser modificados desde cada solapa.
  * Es necesario contar con permisos para la modificación del talonario, la cuenta principal y la contracuenta.
  * Para la imputación de los comprobantes en una cobranza masiva se tiene en cuenta el [parámetro de ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes): Modo de imputación cobranzas masivas. Las opciones disponibles son: 'Automático' o 'A cuenta'.
  * Si el modo de imputación de cobranzas masivas es 'A cuenta' y el importe de la cobranza es mayor al de la factura seleccionada, el valor excedente queda sin imputar (a cuenta).
  * Si el modo de imputación de cobranzas masivas es 'A cuenta' y la cobranza recepcionada no tiene asociado un comprobante de referencia, el valor cobrado queda sin imputar (a cuenta).
  * Si el modo de imputación de cobranzas masivas es 'Automático' y la cobranza recepcionada no tiene asignado un comprobante de referencia, la imputación se realizará según el criterio de prioridad para la asignación de comprobantes a cobrar definido en el proceso [Parámetros de ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos).
  * Si el modo de imputación de cobranzas masivas es 'Automático' y el importe de la cobranza es mayor al de la factura de referencia, el valor excedente será imputado teniendo en cuenta el criterio de prioridad para la asignación de comprobantes a cobrar definido en el proceso [Parámetros de ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos). 
    * Si al importar un archivo Excel con múltiples recibos se producen sobrantes en un recibo anterior, el sistema puede aplicar automáticamente dichos importes a comprobantes pendientes de imputación en recibos posteriores, según el modo de imputación definido y el criterio de prioridad establecido en Parámetros de Ventas.
  * El proceso de imputación masiva respeta un límite máximo de renglones por cobranza. Si la cantidad de comprobantes pendientes supera dicho límite, el sistema imputará solo hasta completar el número máximo permitido. En consecuencia, es posible que algunas cuotas o comprobantes queden sin imputar, aun cuando el importe total de la cobranza sea suficiente para cubrirlos.
  * El proceso [Generación masiva de recibos](https://ayudas.axoft.com/25ar/generacionmasivarecibo_gv) utiliza el mismo criterio para la asignación de comprobantes a cobrar que el proceso [Cobranzas](https://ayudas.axoft.com/25ar/ingresocobranza_gv).
  * Si intenta procesar dos veces un mismo archivo de cobranzas, el sistema exhibirá un mensaje de atención para informar que el archivo seleccionado fue procesado en una generación anterior.
  * Si usted está alcanzado por la ley 27440 y genera comprobante MiPyMEs, para poder incluirlos en un recibo debe primero informar en el sistema para el comprobante el estado, la fecha de aceptación/rechazo y el tipo de aceptación del Receptor desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modifcomprobante_gv). Si el comprobante fue aceptado por el receptor significa que puede generar la cobranza de ese comprobante. En caso de no estar aceptado el recibo queda en estado a cuenta.



Para más información consulte la [Guía de implementación sobre cuentas corrientes](?p=26557).

##### Contenidos relacionados

  * [Video sobre cobranzas masivas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cobramasiva_gv_vid/)

  * [Video sobre facturación masiva de pedidos](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/factmasivpedido_gv_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)
