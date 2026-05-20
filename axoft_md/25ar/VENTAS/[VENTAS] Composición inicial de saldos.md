# Composición inicial de saldos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=21159/

## Contenido

# Composición inicial de saldos

Mediante este proceso se define la composición inicial del saldo en la cuenta corriente de cada cliente.

Definir la composición inicial implica ingresar todos aquellos comprobantes del cliente que no se encuentren cancelados, y que conforman el saldo de ese cliente al momento de comenzar a utilizar el sistema.

__Nota

Los saldos iniciales son muy útiles para la puesta en marcha del sistema.

Más información:

Tenga en cuenta que todos estos comprobantes no serán incluidos en el informe IVA Ventas, informes legales, estadísticas de ventas ni en la generación del archivo DGI - CITI. Únicamente formarán parte de los informes y procesos referidos a cuentas corrientes.  
Asimismo, los comprobantes no se consideran para el cálculo automático de diferencia de cambio y/o interés por mora, cuando son imputados para su cobro desde el proceso [Cobranzas](?p=21323).

Usted puede comenzar a facturar sin haber ingresado los comprobantes de carga inicial, ya que éstos pueden ser registrados en cualquier momento.  
Todos los importes de los comprobantes se ingresan en moneda 'Corriente' o 'Extranjera contable'. Para cada comprobante, indique la cotización correspondiente para obtener los valores en la otra moneda ('Extranjera contable' si la moneda del comprobante es 'Corriente' o viceversa).  
Los comprobantes que se ingresan a través de este proceso son:

  * Facturas: el código que corresponde a este comprobante es 'FAC'.
  * Recibos: el código que corresponde a este comprobante es 'REC'. Es necesario ingresar únicamente los recibos de cobranzas generadas por cobros a cuenta que se encuentren pendientes de imputación a facturas.
  * Notas de crédito y Notas de débito: es necesario que se definan previamente, a través del proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv), aquellos tipos a utilizar. Los códigos que correspondan a estos tipos de comprobante serán los definidos por usted.



En el caso de existir dentro de la composición inicial del saldo de un cliente una factura parcialmente cancelada, solo debe ingresar el comprobante por el importe pendiente.  
Las notas de débito y crédito que se ingresen pueden ser imputadas a las facturas que le dieron origen, por lo que estas facturas se incorporarán antes que las notas de débito y de crédito. En este caso, una vez finalizado el ingreso del registro correspondiente a la nota de débito o crédito, aparecerá el símbolo "*" en el registro del comprobante de referencia. Este símbolo indica que para ese comprobante no pueden ser borrados ni modificados los campos Tipo de comprobante y Número de comprobante, ya que se encuentran relacionados a otro comprobante. En este caso, modifique o anule primero la imputación de referencia en la nota de crédito o débito.  
En este proceso se ingresarán los siguientes datos:

Saldo: indique el saldo de la cuenta del cliente a la fecha de ingreso de la composición inicial. Si el saldo del cliente es acreedor, ingrese el importe con signo negativo. Tenga en cuenta que el saldo está expresado en la moneda según la definición del campo cláusula moneda extranjera del cliente.

Fecha de saldo: indique la fecha del saldo inicial de la cuenta del cliente. Si ya hay comprobantes registrados en el sistema, esta fecha debe ser anterior a la fecha de todos los comprobantes del cliente que se encuentren registrados.

Diferencia: en este campo el sistema irá desplegando la diferencia entre el campo Saldo y los importes de los comprobantes que se van ingresando en este proceso. Esto tiene la finalidad de controlar la correcta composición del saldo.

Detalle de comprobantes que componen el saldo: en esta sección se ingresan los comprobantes pendientes del cliente.

Moneda: seleccione la moneda ('Corriente' o 'Extranjera contable') de cada uno de los comprobantes que componen el saldo.

Cotización: ingrese la cotización de origen del comprobante, siempre y cuando éste no haya sido originado por diferencia de cambio, en cuyo caso la cotización es cero. Esta cotización se utiliza para componer el saldo del cliente en la otra moneda ('Extranjera contable' si la moneda del comprobante es 'Corriente' o viceversa).

En la definición de tipos de comprobante, el campo Registra diferencia de cambio permite parametrizar si un tipo de comprobante es utilizado para representar las diferencias de cambio.  
La ventana que contiene las columnas Fecha de vencimiento e Importe al vencimiento será activada únicamente en los casos en que se ingrese como tipo de comprobante el código 'FAC' (correspondiente a facturas).  
Los campos Tipo de comprobante de referencia y Número de comprobante de referencia serán activados cuando el tipo de comprobante corresponda a una nota de crédito o nota de débito.

##### Importación de datos desde Excel

Utilice la herramienta de importación desde un archivo externo de Excel, para facilitar el ingreso de la composición inicial de saldos de sus clientes en el módulo Ventas.  
Los pasos a seguir son los siguientes:

  * Generar la plantilla de importación desde Excel.
  * Indique el nombre y el destino del archivo a generar.
  * [Ingrese la información en la planilla](https://ayudas.axoft.com/25ar/ingrdatplancompsaldo_gv) de Excel y grábela.
  * Desde el proceso [Composición inicial de saldos](https://ayudas.axoft.com/25ar/compinicialsaldo_gv), importe los datos desde Excel.
  * Al finalizar la importación, el sistema exhibirá el [Reporte de resultados](https://ayudas.axoft.com/25ar/reportrestimpcompsaldo_gv).



##### Generación de plantilla

Para realizar la importación de la composición inicial de saldos, el sistema utiliza una plantilla de Excel.  
El sistema propone como nombre de archivo: "ComposicionInicialdeSaldos.xls" y como destino o ubicación: el directorio comunes ubicado en el servidor de su sistema.  
Ejemplo: \NombreDelServidorCOMUN######### donde "#########" representa el número de llave de su sistema.  
Si la plantilla ya existe, el sistema solicitará su confirmación para el reemplazo del archivo.

##### Ingreso de datos en la planilla

Complete los datos de la planilla, para luego importarla en el sistema.  
Las columnas para las que puede haber más de un valor posible, tienen un indicador rojo en el extremo superior derecho. Acerque el mouse para visualizar el detalle de los valores posibles de ingreso o despliegue el combo asociado.

**Ejemplo:**

Las columnas que tienen un formato particular también tendrán el indicador en su extremo superior derecho. Ejemplo:

Ayuda: la planilla incluye una solapa con el nombre Ayuda, en la que podrá consultar un ejemplo de ingreso de datos en la planilla.

##### Importar

La importación procesará la planilla generada, validando cada uno de los datos.  
En el caso de detectarse errores, se rechazará la composición de ese cliente.  
Si el reporte de resultados incluye errores:

  * Abra la planilla desde Excel.
  * Corrija cada uno de los errores encontrados.
  * Reprocese la planilla. 
    * En la planilla, para los valores correspondientes a 'Importe Pendiente', '1er. Importe Alternativa' y '2do. Importe Alternativa' es posible ingresar un máximo de 4 decimales.
    * El sistema rechazará los movimientos cuyos importes tengan más decimales que los parametrizados en el Administrador de decimales (para los importes en moneda corriente o extranjera).



##### Reporte de resultados de la importación

Finalizada la importación de la planilla confeccionada, el sistema exhibe un reporte con los resultados de la importación.  
En este resumen se indican los registros procesados, los aceptado y los rechazados (con el detalle del motivo del rechazo).  
Si lo desea, es posible imprimir o enviar a Excel los resultados obtenidos.

##### Contenidos relacionados

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)
