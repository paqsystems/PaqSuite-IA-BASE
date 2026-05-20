# Guía de Restô sobre el Registro de Compras y Ventas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_registro_gv3/

## Contenido

# Guía de Restô sobre el Registro de Compras y Ventas

A partir de Agosto 2017, la Información Electrónica de Compras y Ventas es reemplazada por el Registro de Compras y Ventas (confeccionado por el SII).

El Registro de Compras y Ventas es un nuevo sistema disponible en [www.sii.cl](http://www.sii.cl).  
Este sistema tiene como finalidad, respaldar las operaciones afectas, exentas y no afectas a IVA efectuadas por el contribuyente, permitiendo controlar el _Impuesto al Valor Agregado_.  
El Registro de Compras y Ventas está compuesto por 2 registros: un Registro de Compras (RC) y un Registro de Ventas (RV).

Acerca del RCV:

  * El Registro de Ventas es uno de los dos registros que componen el _Registro de Compras y Ventas_.
  * Este registro da cuenta de todas las operaciones de ventas realizadas por un contribuyente, de acuerdo a los documentos tributarios electrónicos recibidos en el SII.
  * En el caso de los documentos tributarios emitidos en soporte distinto al electrónico, deberán ser informados al SII para que sean incorporados al _Registro de Venta_.



##### Caracterización de las ventas

  * Las ventas se caracterizan por cada uno de los documentos emitidos, y éste no podrá contener más de una clasificación de tipo de venta.
  * Las opciones de caracterización son las siguientes:



**Opción** | **Detalle a exhibir**  
---|---  
1 | Ventas del giro  
2 | Venta de activo fijo  
3 | Venta de bienes raíces  
4 | Emisión nota de crédito por vale de máquinas registradora  
  
La opción 4 - Emisión nota de crédito por vale de máquinas registradora es válida sólo para notas de crédito no electrónicas.

  * El Tipo de Transacción de Compras es una sugerencia para el comprador. Indica qué tipo de compra es para el receptor de la factura. Los valores posibles de selección son los siguientes:



**Opción** | **Detalle a exhibir**  
---|---  
1 | Compras del giro  
2 | Compras en supermercados o similares  
3 | Adquisición bien raíz  
4 | Compra activo fijo  
5 | Compra con IVA uso común  
6 | Compra sin derecho a crédito  
7 | Compra que no corresponde incluir  
  
  * Si requiere modificar el Tipo de Transacción de Ventas, sólo podrá hacerlo si el documento es electrónico y NO está aceptado por el SII.



De no cumplirse las condiciones mencionadas, deberá anular el documento original mediante nota de crédito y emitir un nuevo documento.

##### Detalle del circuito

  * Procesos de ingreso de documentos (facturas, notas de débito y notas de crédito):
    * Por defecto, el sistema asigna el valor 1 - Ventas del Giro como Tipo de Transacción de Venta, a los documentos que ingrese con fecha posterior al 31 de julio del 2017.
    * Por defecto, el sistema asigna el valor 1 - Compras del Giro como Tipo de Transacción de Compra, a los documentos que ingrese con fecha posterior al 31 de julio del 2017.
    * Invoque la tecla de función <Alt + K> para cambiar o consultar el Tipo de Transacción.
  * Modificación de Comprobantes:
    * Invoque la tecla de función <Alt + K> para cambiar o consultar el Tipo de Transacción (de Venta y/o de Compra).
  * Consultas Live:
    * Es posible consultar el Tipo de Transacción de Venta y el Tipo de Transacción de Compra, asignados a cada documento, desde las siguientes consultas: 
      * Consulta de Facturación
      * Ficha del comprobante Live
    * Es necesario seleccionar las columnas indicadas para su exhibición.
  * Administrador de documentos electrónicos - Registro de Ventas:
    * Podrá consultar la información de los documentos emitidos (electrónicos y no electrónicos) en un determinado período.
    * Usted podrá comparar estos datos con lo informado por el Registro de Compras y Ventas, en el sitio web del Servicio de Impuestos Internos.
    * Si es necesario, genere el archivo de Documentos NO electrónicos emitidos y súbalo al sitio web del SII.
    * Si es necesario, genere el archivo de Resúmenes de Venta por las boletas emitidas en el período, y súbalo al sitio web del SII.
    * Concilie la información registrada en el Servicio de Impuestos Internos con los datos de su sistema Astor, para detectar posibles diferencias y solucionarlas previo a la presentación de la Declaración de IVA.



##### Preguntas frecuentes

**¿Puedo modificar el Tipo de Transacción asignado a un documento?**

  * Para modificar el Tipo de Transacción (de Ventas y/o de Compras) de un documento electrónico, tenga en cuenta que sólo podrá hacerlo si el documento está 'Pendiente' de envío al SII o bien, está 'Rechazado'.
  * Si se trata de un documento NO electrónico, no es posible modificar esta información.



De no estar habilitada la modificación, deberá anular el documento original mediante nota de crédito o nota de débito (según corresponda) y emitir un nuevo documento.

**¿Cómo puedo modificar el Tipo de Transacción asignado a un documento antes de su entrega al cliente?  
**Si se trata de un documento electrónico, puede hacerlo cambiando la modalidad de conexión con el SII (a 'Diferido'), desde el comando 'Documento electrónico', en los procesos emisores de DTEs. La modificación del Tipo de Transacción se realizará en este caso, desde el proceso [Modificación de comprobantes](?p=20552).  
Si se trata de un documento NO electrónico, mediante la tecla de función <Alt + K> durante el ingreso del documento.

**¿Cómo consulto el Tipo de Transacción asignado a cada documento?  
**Es posible consultar el _Tipo de Transacción de Venta_ y el _Tipo de Transacción de Compra_ asignados a cada documento, desde las siguientes consultas:

  * Consulta de Facturación.
  * Ficha del comprobante Live.



No olvide seleccionar las columnas indicadas para su exhibición.

**¿Cuándo debo complementar el Registro de Ventas?  
**Para informar al SII, las ventas respaldadas en soporte no electrónico.

  * Para informar al SII las boletas emitidas (electrónicas como no electrónicas).



En el caso de efectuar ventas al detalle, que son respaldadas con boletas o vales en reemplazo de boletas, deberá complementar el registro de ventas (RV) informando sólo un resumen a fin de mes.

**¿Qué funcionalidad brinda la opción 'Conciliar' del Registro de Ventas?  
**La conciliación de los documentos permite detectar diferencias entre lo registrado en el servicio y la información de su sistema.

**¿Cuándo debo conciliar los documentos del Registro de Ventas?  
**Ejecute esta opción del Registro de Ventas, antes de presentar la Declaración de IVA.

**¿Es posible conciliar los documentos del Registro de Ventas más de una vez en un mismo período?  
**Usted define la frecuencia con la que realiza la conciliación de sus documentos (diaria, semanal, quincenal o mensual).  
En cada oportunidad, descargue el archivo desde el sitio web del Servicio, para procesar la información actualizada.

**¿Qué documentos se excluyen de la conciliación?  
**No se concilia la información correspondiente a boletas (electrónicas y manuales, afectas y exentas).  
Dado que estos documentos se informan al SII de manera resumida por día, de presentarse alguna diferencia, no es posible detectar el documento que la origina.

**¿Qué datos debo ingresar al solicitar la conciliación?  
**Seleccione el período y el archivo a procesar.

**¿Cómo obtengo el archivo a procesar?  
**El archivo que el sistema concilia corresponde al archivo de descarga (.csv) que contiene los documentos registrados en el servicio.  
Para obtenerlo, ingrese a la página del _Servicio_ , acceda al _Registro de Compras y Ventas_ y cliquee el botón "Descargar Detalles" del registro de ventas.

**¿Qué resultados arroja la conciliación de documentos?  
**Finalizada la comparación de los datos, el sistema exhibe una ventana de resultados en la que podrá consultar los documentos procesados, el detalle de las diferencias encontradas y/o el detalle de los documentos sin diferencias.

**¿Es posible parametrizar los datos de la ventana de resultados?  
**En la ventana de selección de archivos, tilde el parámetro _Informa sólo las diferencias_ para consultar en la grilla de resultados, los documentos que presentan diferencia.  
En la ventana de resultados puede cambiar el tipo de datos a exhibir ('Todos' o 'Sólo con diferencia') si no tildó el parámetro _Informa sólo las diferencias_.

**¿Las diferencias detectadas en la conciliación se corrigen de manera automática?  
**En el caso de existir diferencias, no se actualiza automáticamente la información del sistema.  
Es necesario analizar cada diferencia y aplicar la corrección correspondiente.

**¿Qué significa el mensaje "Documento Ok" obtenido como resultado de la conciliación de un documento?  
**Este mensaje indica que los datos registrados en el SII coinciden con los datos registrados en el sistema **Astor**.

**¿Qué significa el mensaje "Documento inexistente en el SII, para el período seleccionado"?  
**El documento está registrado en su sistema Astor pero no fue recepcionado por el SII.  
Si se trata de un documento no electrónico, genere el "Archivo de Documentos no electrónicos emitidos" (desde el _Registro de Ventas_) y súbalo en el sitio web del Servicio.  
Si se trata de un documento electrónico, verifique su estado en el [Administrador de comprobantes electrónicos](?p=17774) ('Pendiente', 'Enviado' o 'Rechazado').  
Si el documento está 'Pendiente', envíelo al SII para su aceptación.  
Si el documento está 'Enviado', gestione su reenvío al SII.  
Si el documento está 'Rechazado', corrija los errores detectados y vuélvalo a enviar.

##### Recomendaciones

  * La Propuesta de Declaración de IVA se construirá a partir del nuevo Registro de Compras y Ventas, que el SII confeccionará automáticamente con la información de los documentos electrónicos de cada período.
  * El RCV construido por el SII es el único válido, y no existe la opción de integrarlo con otros softwares de facturación.



**Links de interés**

Para más información, consulte los siguientes ítems en el sitio web del SII:

  * Menú Normativa y Legislación: [Resolución N° 61 (del 12 de Julio de 2017), Circular N° 4 (de 2017) y Circular N° 35 (de 2017)](http://www.sii.cl/normativa_legislacion/circulares/2017/circu35.pdf)
  * [Menú de Preguntas Frecuentes](http://www.sii.cl/preguntas_frecuentes/catastro/arbol_documentos_tributarios_1173.htm)
