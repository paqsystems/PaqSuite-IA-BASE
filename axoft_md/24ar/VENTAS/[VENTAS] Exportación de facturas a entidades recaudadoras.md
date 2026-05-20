# Exportación de facturas a entidades recaudadoras

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=21358/

## Contenido

# Exportación de facturas a entidades recaudadoras

Este proceso permite enviar a la entidad recaudadora (Pagomiscuentas), la información de las facturas que la empresa desea poner a disposición de sus clientes, para ser pagadas a través de los canales con los que opera la entidad.

##### Parámetros

Los datos a ingresar para la generación del archivo a exportar son los siguientes:

Configuración: ingrese la [configuración para cobranzas masivas](https://ayudas.axoft.com/24ar/configcobranzamasiva_gv) a utilizar. El sistema requiere este dato para obtener la ubicación del archivo de facturas a exportar.

Incluye comprobantes (vencimientos) exportados: active este parámetro si necesita volver a exportar vencimientos de comprobantes ya procesados.  
Ejemplos de aplicación:

  1. Este parámetro será de utilidad si la entidad recaudadora le solicita un nuevo archivo de exportación por no haber podido procesar el archivo originalmente enviado.
  2. Active este parámetro para exportar nuevos vencimientos de comprobantes ya exportados.



Tenga en cuenta que Pagomiscuentas sólo procesa novedades. Es decir, los comprobantes (vencimientos) ya recepcionados son ignorados.

Destino de la exportación: es el directorio donde se grabará el archivo a exportar a la entidad recaudadora (Pagomiscuentas).  
Se propone la ubicación definida en la configuración para cobranzas masivas seleccionada.  
Si en la configuración para cobranzas masivas, usted no definió una ubicación para el archivo de exportación, utilice el botón "Examinar" para elegir el destino de la exportación.

Archivo a exportar: se exhibe el nombre del archivo a enviar a la entidad recaudadora.  
El nombre del archivo a exportar lo define la entidad recaudadora. Este dato no es editable.

Para Pagomiscuentas:

El archivo es compatible con el **código de diseño 102** con longitud de registros de 280 caracteres.  
El nombre está compuesto por las siglas: FACXXXX.ddmmaa sin ninguna extensión, donde:  
XXXX: es el número que asigna la entidad recaudadora a la empresa.  
ddmmaa: es el día, mes y año de generación del archivo.  
Es posible publicar más de un archivo en un mismo día, siendo 10 el límite diario.  
En este caso, el nombre del archivo será FACXXXX.ddmmaa.## donde #: es el número de envío (que podrá variar de 01 a 09).  


Para más información consulte la [Guía de implementación sobre cuentas corrientes](?p=26557).

Información a exportar  
Se exportan los vencimientos (cuotas) 'pendientes', con fecha mayor o igual a la del día.  
En la exportación no se incluyen los siguientes comprobantes:

  * Facturas centralizadas para su cobranza.
  * Facturas de clientes ocasionales.
  * Facturas anuladas.
  * Facturas pagadas.
  * Facturas electrónicas sin CAE.
  * Facturas emitidas en moneda extranjera.
  * Facturas de clientes Cláusula moneda extranjera.



Resultado del proceso  
Al finalizar la exportación, se informa en pantalla: la cantidad de facturas procesadas, la cantidad de vencimientos exportados y el importe total de la operación.  
Haga clic en el botón "Ver detalle" para acceder a la consulta Live del detalle de exportación de facturas a entidades recaudadoras.  
Haga clic en el botón "Aceptar" para abandonar el proceso y regresar al menú principal del sistema.

Último envío  
El sistema le informa la fecha del último envío realizado y la cantidad de vencimientos procesados en esa operación.  
Haga clic en el botón "?" para acceder a los datos de auditoría, o bien, presione las teclas <Ctrl + U>.  
Del último envío realizado se informa la fecha, hora, usuario, terminal, cantidad de vencimientos exportados, total en pesos y se indica si se procesaron vencimientos ya exportados.  
Haga clic en el botón "Detalle de exportación" para acceder al detalle de la última exportación de facturas a entidades recaudadoras.

Clientes  
Por defecto se incluyen todos los clientes (exceptuando los definidos como Cliente cláusula moneda extranjera).  
Usted puede cambiar la condición de selección desde esta solapa.

##### Contenidos relacionados

  * [Video sobre cobranzas masivas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cobramasiva_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)
