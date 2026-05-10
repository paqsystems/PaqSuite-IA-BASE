# Guía de implementación sobre RG 5614/2024 - Ley de Transparencia Fiscal 27743/2024

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_rg5614_gv/

## Contenido

# Guía de implementación sobre RG 5614/2024 - Ley de Transparencia Fiscal 27743/2024

Esta guía de implementación le indica los pasos a seguir para poner en marcha este circuito. La RG 5614/2024 especifica que los emisores Responsables Inscriptos deben discriminar el IVA e Impuestos Nacionales Indirectos (impuestos internos) que incidan en el precio, en la impresión de los comprobantes de ventas (Comprobantes tipo 'B') que emitan a Consumidores Finales y Exentos.

__Nota

Para más información referida a este tema, puede observar [este video](https://www.youtube.com/watch?v=8x0M5SiZDz8). También puede consultar la reglamentación y ley 27743 en <https://www.boletinoficial.gob.ar/detalleAviso/primera/318151/20241213> y <https://www.boletinoficial.gob.ar/detalleAviso/primera/310191/20240708> (Titulo VII, Régimen de Transparencia Fiscal al Consumidor) respectivamente.  


Para comenzar a utilizar el circuito debe seguir estos pasos:

  * Ingrese a [Parámetros de Venta](?p=19401), solapa Comprobantes, sección General y tilde la opción RG 5614 - Ley de Transparencia Fiscal 27743/2024.
  * Si emite comprobantes electrónicos o pre-impresos, ingrese al proceso [Formularios](?p=11875) del módulo Procesos generales (Tablas generales | Formularios | Ventas) de aquellos formularios que utilice para comprobantes letra 'B' y agregue en el espacio inferior izquierdo (la normativa así lo indica) las leyendas y variables de impresión que se detallan a continuación según el tipo de comprobante.



**Variable de impresión** | **Significado**  
---|---  
@T8 | Muestra el total de IVA en Facturas.  
@T2 | Muestra el total de IVA en notas de crédito y débito.  
@TI | Muestra el total de impuestos internos incluido el adicional y sobretasas de impuestos internos.  
  
Luego:

  * En formularios de facturas la leyenda a agregar es:



  * En formularios de notas de crédito y notas de débito, la leyenda a agregar es:



De esta manera, en el comprobante la leyenda aparecerá como se muestra en la siguiente imagen.

  * Si emite comprobantes fiscales ingrese a Parámetros de Venta y tilde la opción Configura datos adicionales en la solapa Controlador fiscal. En la sección Pie agregue en algunas de las líneas 12, 13 y 14 las leyendas y las variables de impresión **@IV** y **@TI**. Cabe destacar que debe utilizar dos líneas consecutivas, por ejemplo: 
    * En línea 12 agregue la variable **@IV** en el primer campo Código de variable (el situado más a la izquierda) y el texto "IVA" en el campo Texto para variable.
    * En línea 13 agregue la variable **@TI** en el primer campo Código de variable (el situado más a la izquierda) y el texto "IMP INT" en el campo Texto para variable.



De esta manera, queda libre una línea para que en caso de que lo requiera pueda agregar otra variable adicional.  
La variable **@IV** muestra el total de IVA y la variable **@TI** muestra el total de impuestos internos incluido el adicional y sobretasas de impuestos internos. Ambas variables muestran los importes correspondientes en facturas, notas de crédito y débito.

Más información:

Aquellos clientes habituales que discriminan impuestos internos deben tener tildadas las opciones ya existentes Liquida impuestos internos y Discrimina impuestos internos en el proceso de carga de clientes del módulo Ventas (Archivos | Actualizaciones | Clientes) dentro de la solapa Facturación. Si se tilda la nueva opción RG 5614 - Ley de transparencia fiscal 27743/2024 comentada en el primer paso de esta guía, pero no se tildan las opciones de impuestos internos en el cliente, entonces en el comprobante no se va a calcular el monto de los impuestos internos. Lo mismo ocurre para el caso de clientes ocasionales, en su proceso de carga es necesario que se tilde la opción Liquida impuestos internos de la solapa Impuestos, caso contrario no se calculará el monto de los impuestos internos.  
Cabe destacar que es posible realizar una actualización masiva de clientes habituales desde el proceso [Actualización masiva de clientes](?p=19174) (Archivos | Actualizaciones) del módulo Ventas, en donde debe tildar las opciones Liquida impuestos internos y Discrimina impuestos internos de la sección Facturación, y luego utilizar los filtros disponibles para filtrar los clientes a actualizar.  


##### Contenidos relacionados

  * [Video sobre RG 5614 - Ley de Transparencia Fiscal 27743/2024](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/rg5614_gv_vid/)
