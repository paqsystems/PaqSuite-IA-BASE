# Valores por defecto para controlador e impresora fiscal

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_rg4520_gv3/?p=25050/

## Contenido

# Valores por defecto para controlador e impresora fiscal

Configura datos adicionales: si activa este parámetro, se habilita la edición de las líneas que podrán ser configuradas con variables de impresión, para ser impresas en las facturas y tickets-facturas en todos los modelos de controlador e impresoras fiscales implementados en el sistema.

Para la impresora fiscal EPSON LX-300 existen algunas limitaciones con respecto a la configuración de datos adicionales para el encabezado y pie, que dependen del tamaño de hoja configurado en la memoria fiscal. En los tamaños de hoja de 8 y 8x6 pulgadas, se podrá configurar solamente la línea 1 y 2 del encabezado. Para el resto de los tamaños, se podrá configurar de la línea 1 a 3 en el encabezado y de la línea 12 a 13 en el pie.  
La configuración de líneas en los ítems es igual para todos los modelos. Esto posibilitará que en el momento de facturar, se impriman en el lugar deseado, datos variantes referentes a la factura, como mozo o repartidor, depósito, etc.  
No es obligatorio configurar todas las líneas, sino que podrá seleccionar algunas de ellas, tanto para la zona del encabezado, pie o ítems.  
Es posible ingresar por línea, hasta dos variables de impresión y un texto fijo opcional, para indicar una leyenda referente a los datos impresos en cada línea.  
Para cualquier modelo de controlador fiscal y para la impresora fiscal EPSON LX-300F, el tamaño de cada línea del encabezado y pie será de 40 caracteres. En tanto que en la impresora fiscal HASAR 320F / 321F / 322F / 330F será de 50 caracteres. Todo dato que exceda estos tamaños será truncado.Para los controladores fiscales de última generación, es posible utilizar las líneas 15 a 21 en la sección Pie del comprobante, siempre que el parámetro Impresoras nueva generación se encuentre habilitado.[/axcond].  
Se utilizan sólo algunas variables de impresión ya existentes para los .TYP, las que se podrán seleccionar de una lista. Para más información, consulte el [Buscador de variables de reemplazo](?p=35730), donde se detalla la lista de variables de impresión para el encabezado y pie, y para la impresión de ítems.  
Las líneas del encabezado y pie que se configuren con variables de impresión, no podrán ser utilizadas para cargar un dato fijo desde el proceso Operación para controladores fiscales, ya que éstas tienen prioridad y el dato fijo configurado en la misma línea sería borrado, pues se utiliza el mismo mecanismo para ingresar textos adicionales en el controlador o impresora fiscal.  
Es aconsejable indicar que, cuantas más líneas se configuren con datos, más será el tiempo que lleve en generarse un comprobante, ya que estos datos variables deben ser enviados al inicio de cada comprobante, y borrados después de generarlo para dejar el encabezado y pie sin datos para las siguientes facturas que se generen o para cualquier otro comprobante no fiscal como Cierre X, Z o auditoría.

Imprime comanda en comprobante no fiscal: cuando este parámetro está activo, se imprime junto al ticket o factura fiscal un comprobante no fiscal con los datos de la comanda a facturar en ese momento (de utilidad para aquellos restaurantes que no posean otros dispositivos de impresión).  
El formato de la comanda a imprimir puede adaptarse mediante un formulario especial. Para más información, consulte el ítem [Formularios de comandas](formulariocomanda_gv3).  
Esta opción es independiente de la configuración de destinos de impresión para artículos.

Activa grabación de auditoría fiscal: cuando este parámetro está activo, se registran en un archivo .log, todos los comprobantes generados por controlador fiscal y al efectuar un cierre Z, el sistema compara lo emitido por el controlador con la información registrada en este archivo. Si existen diferencias, se informan en un resumen, indicando el motivo de las mismas.  
Tenga en cuenta que para poder desactivar este parámetro no deben existir comprobantes generados por controlador fiscal a partir del último cierre Z. Si existieran estos comprobantes y se requiere desactivar el parámetro, deberá efectuar un cierre Z en forma previa.
