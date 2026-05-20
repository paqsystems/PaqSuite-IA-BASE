# Guía de implementación sobre RG 3685 - Régimen informativo de compras y ventas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_calcretotras_cp2/?p=11914/

## Contenido

# Guía de implementación sobre RG 3685 - Régimen informativo de compras y ventas

La RG 3685 de AFIP estableció un régimen especial de información sobre las operaciones de compras y ventas. Adicionalmente regula cómo se deben almacenar los duplicados en caso de emitir comprobantes electrónicos.

La obligación de informar alcanza a las siguientes operaciones, sean o no generadoras de crédito o débito fiscal en el impuesto al valor agregado:

  * Compras, locaciones o prestaciones recibidas e importaciones definitivas de bienes y servicios -así como todo otro concepto facturado o liquidado por separado, relacionado con las mismas o con su forma de pago- que, como consecuencia de cualquier actividad que desarrollen, realicen con proveedores, locadores, prestadores, comisionistas, consignatarios, etc.
  * Ventas, locaciones o prestaciones realizadas, exportaciones definitivas de bienes y servicios, así como todo otro concepto facturado o liquidado por separado, relacionado con las mismas o con su forma de pago.
  * Descuentos y bonificaciones otorgadas, quitas, devoluciones y rescisiones efectuadas, que se documenten en forma independiente de las ventas, locaciones y prestaciones.



Para más información sobre el régimen consulte [aquí](http://www.afip.gob.ar/comprasyventas/).

##### Para Gestión

Con Tango, usted cumple con las disposiciones de esta norma, generando el soporte magnético para la RG 3685, habiendo configurado previamente los proveedores y clientes vinculados a su empresa.  
A continuación exponemos los pasos necesarios para poner en marcha el circuito correspondiente a la RG 3685 en Tango Gestión. Para ello siga los pasos enunciados a continuación.  
Para generar los archivos de aplicativo SIAp y los archivos para el almacenamiento de los duplicados electrónicos, configure previamente:

  * [Parámetros de Ventas](?p=19401): en la solapa [Clientes](?p=19401/#parametros-para-clientes) complete el tipo de operación habitual según la RG 3685. Este valor se utilizará como valor por defecto para los nuevos clientes ya sean habituales u ocasionales. En la solapa [Comprobantes,](?p=19401/#parametros-para-comprobantes) sección Pedidos, complete el tipo de operación habitual para RG 3685. Este valor se utilizará en la facturación de pedidos por lote.
  * [Clientes](?p=19444): en la solapa [Facturación](?p=19444/#facturacion) complete el tipo de operación habitual según la RG 3685. Este valor es utilizado como valor por defecto durante la emisión de comprobantes. Posteriormente podrá editarlos desde el proceso [Modificación de comprobantes](?p=20552).
  * [Perfiles de facturación](?p=19415): indique el tipo de operación habitual para los comprobantes que emita y las restricciones de edición (edita, muestra u oculta el campo).
  * [Parámetros de Compras](?p=14676): en la solapa [Principal](?p=14676/#principal) complete el tipo de operación y el código de comprobante habitual para los comprobantes de proveedores ocasionales según la RG 3685.
  * [Proveedores](?p=14686): asigne a su proveedor habitual los valores de Tipo Operación y Comprobante AFIP. Estos valores se utilizan como valor por defecto para los comprobantes que reciba. Posteriormente podrá editarlos desde el proceso [Modificación de comprobantes](?p=15550).  
Al activar el parámetro Genera Información todos los comprobantes que ingrese para el proveedor (facturas, créditos y débitos) serán informados en los archivos de soporte magnético para RG 3685.
  * [Monedas](?p=11955): verifique que las monedas con las que opera su empresa tengan el código de moneda AFIP en la solapa Datos Legales del módulo Procesos Generales.



**Consideraciones para usuarios que ya tenían implementado CITI Ventas / Compras o la RG 1361**

  * Si su empresa ya informaba CITI Compras, CITI Ventas y/o RG 1361, los comprobantes ingresados con anterioridad (desde el 01 de Enero de 2015 a la fecha de actualización de su sistema), tomarán automáticamente los valores registrados para dichas normas.
  * Si su empresa no informa CITI Compras, CITI Ventas y/o RG 1361, los comprobantes ingresados desde el 01 de Enero de 2015 tomarán los valores registrados en los procesos Clientes y Proveedores o en su defecto en Parámetros Generales de Ventas y Compras.
  * Los nuevos comprobantes tomarán el valor configurado en el cliente / proveedor, pudiendo ser modificado en el momento de su ingreso o desde los procesos [Modificación de comprobantes](?p=20552) de Ventas o [Modificación de comprobantes](?p=15550) de Compras.



##### Para Liquidador de IVA

A continuación exponemos los pasos necesarios para poner en marcha el circuito correspondiente a la RG 3685 para Liquidador de IVA.  
Para ello siga los siguientes pasos...

Para generar los archivos de aplicativo SIAp, configure previamente:

  * [Monedas](?p=11956): indique en las monedas con las que opera su empresa, el código de moneda AFIP en la solapa Datos Legales del módulo Procesos Generales.
  * [Parámetros de Liquidador de IVA](?p=8426): defina en forma genérica la operación habitual AFIP para comprobantes de ventas y de compras.
  * [Clientes](?p=8349): indique la operación habitual AFIP del cliente para el ingreso de comprobantes de ventas. Además, tenga en cuenta que para poder generar en forma correcta los archivos deberá revisar los datos informados sobre tipo y número de documento según la categoría de IVA definida.
  * [Proveedores](?p=8430): indique la operación habitual AFIP del proveedor para el ingreso de comprobantes de compras. Además, tenga en cuenta que para poder generar en forma correcta los archivos deberá revisar los datos informados sobre tipo y número de documento según la categoría de IVA definida.
  * [Registración de comprobantes](?p=8433): indique el tipo de comprobante AFIP y el código de operación. El sistema propone un valor por defecto para ambos campos siguiendo la lógica que se detalla a continuación: 
    * Tipo de comprobante AFIP: se lo propone en base al tipo de comprobante interno (por ejemplo, factura, nota de crédito, nota de débito) y a la letra del comprobante ingresada.
    * Tipo de operación: propone el tipo de operación asociado el cliente/proveedor o, caso contrario, el de Parámetros Generales.



__Nota

Tenga en cuenta que los comprobantes con tipo interno igual a 'Retención' y aquellos que no participan en el Libro IVA no son exportados al aplicativo.

**Consideraciones para usuarios que ya tenían implementado CITI Ventas / Compras**

  * Si su empresa ya informaba CITI Compras y/o CITI Ventas, los comprobantes ingresados con anterioridad (desde el 01 de Enero de 2015 a la fecha de actualización de su sistema), tomarán automáticamente los valores registrados para dicha norma.
  * Si su empresa no informa CITI Compras y/o CITI Ventas, los comprobantes ingresados desde el 01 de Enero de 2015 tomarán los valores registrados en los procesos Clientes y Proveedores o en su defecto en Parámetros Generales.
  * Los nuevos comprobantes tomarán el valor configurado en el cliente / proveedor, pudiendo ser modificado en el momento de su ingreso o desde el proceso [Registración de comprobantes](?p=8433).



##### Para Central

A continuación, exponemos los pasos necesarios para poner en marcha el circuito correspondiente a la RG 3685 en Tango Gestión con el módulo Central.  
Para ello siga los pasos enunciados a continuación.  
Siga estos pasos para generar los archivos requeridos para la RG 3685/14 desde el módulo Central, pudiendo consolidar información de varias sucursales, o generar información separada para cada una de ellas.

  1. Desde una empresa sucursal, en el proceso [RG 3685](?p=11988/#rg-3685), seleccione el origen de información 'Gestión'.
  2. Marque la opción Genera información para transferencias a central. Al marcar esta opción se genera una copia de la información para exportar.
  3. Confirme la generación de los archivos, al finalizar el proceso (y en caso de existir información) se generan los siguientes archivos:  
\- ventascomprobantes*.txt  
\- ventasalicuotas*.txt  
\- comprascomprobantes*.txt  
\- comprasalicuotas*.txt  
\- comprasimportaciones*.txt
  4. Exporte la información habilitada desde la empresa sucursal. Para ello, utilice el asistente de exportación de [Información de RG 3685](?p=11948) desde el módulo Procesos generales o Central.
  5. En la empresa donde desee consolidar la información, importe el archivo .zip del paso anterior con el asistente de importación de Información de RG 3685 desde el módulo Central.
  6. En la empresa donde importó la información, ejecute el proceso [RG 3685](?p=11988/#rg-3685), seleccione el origen de información 'Central'. Indique los parámetros que habitualmente utiliza, tales como período a informar, comprobantes y tipo de generación. Desde allí genere los archivos con la información para:  
\- ventascomprobantes*.txt  
\- ventasalicuotas*.txt  
\- comprascomprobantes*.txt  
\- comprasalicuotas*.txt  
\- comprasimportaciones*.txt  
Cada archivo se genera con la información conjunta de todas las empresas sucursales que usted haya importado para un mismo período.



**Automatizar la generación y transferencia de la información para RG 3685/14  
**Puede generar una tarea automática que genere la información de cada sucursal, para luego ser exportada. Si además cuenta con la herramienta Tangonet, puede automatizar las exportaciones e importaciones, permitiendo así realizar todo el proceso de generación y transferencia de la información en forma automática.  
Para automatizar la generación de información, siga estos pasos:

  1. Desde una empresa sucursal, en el proceso [RG 3685](?p=11988/#rg-3685), seleccione el origen de información 'Gestión'.
  2. Seleccione el parámetro Genera información para transferencias a central. Antes de comenzar con la generación, el proceso le preguntará si desea generar una tarea automática para generar información para exportar.



La tarea automática puede modificarse desde el Administrador general, en el menú Servicios | Automatización de central. Usted puede modificar la frecuencia de ejecución (por defecto una vez al día).  
Repita los pasos 4, 5 y 6 del apartado anterior en caso de exportar manualmente la información. Si utiliza Tangonet, simplemente genere los archivos desde la empresa que importa información.

##### Detalle del circuito

El presente circuito contempla los pasos a seguir para generar los archivos requeridos para importar al aplicativo SIAp - Compras y Ventas y guardar como almacenamiento de duplicados electrónicos.

  * Archivos correspondientes a SIAp: 
    * ventascomprobantes*.txt
    * ventasalicuotas*.txt
    * comprascomprobantes*.txt
    * comprasalicuotas*.txt
    * comprasimportaciones*.txt
  * Formulario electrónico 4502 correspondiente a AFIP.
  * Archivos salvados en disco: 
    * duplicadoscabecera*.txt
    * duplicadosdetalle*.txt
    * duplicadosotrospercep*.txt



Los comprobantes que se informan son los siguientes:

Para Gestión:

Ventas

  * Facturas
  * Notas de crédito
  * Notas de débito



Compras

  * Factura
  * Factura - remito
  * Factura de importación
  * Nota de crédito
  * Nota de débito
  * Despachos



Para Liquidador de IVA:  
Cualquiera de los tipos de comprobantes comprendidos en la RG 3685.  
Las condiciones que deben cumplir los comprobantes son las siguientes:

  * Deben pertenecer al período seleccionado en el proceso de generación. En el caso de los comprobantes de compras se toma en cuenta la fecha contable.
  * Deben estar configurados para intervenir en los libros IVA.



Para generar el archivo, ingrese al proceso de [generación de RG 3685](?p=11988/#rg-3685).
