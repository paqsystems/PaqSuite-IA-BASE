# Guía sobre percepciones definibles

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_percepdefin_gv/

## Contenido

# Guía sobre percepciones definibles

Esta opción permite definir distintos tipos de percepciones. Su beneficio radica en su mayor flexibilidad (más bases de cálculo, asignación de alícuotas o bases de cálculo de acuerdo a distintas clases de clientes) y la oportunidad de asociarle un modelo de formato de archivo ASCII para la generación de soportes magnéticos requeridos por la autoridad de aplicación del impuesto.

Las percepciones definibles pueden combinarse con "clasificaciones auxiliares" que permiten condicionar la aplicación de la percepción de acuerdo a la clasificación indicada en el cliente, en el artículo y en la propia percepción definible. Dicha clasificación permite por ejemplo aplicar una base de cálculo determinada para responsables inscriptos y otra para el resto de los clientes.  
Desde el [Facturador](https://ayudas.axoft.com/25ar/pos_gv) puede consultar las percepciones calculadas en el comprobante ingresando desde la solapa Pagos a la opción Más acciones y luego al ítem Impuestos o también presionando <F6>.

Más información:

Recuerde que la tecla rápida <F3> permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

**¿Cómo conviene definir las percepciones?  
**Usted puede implementar las percepciones de ingresos brutos mediante alguna de las siguientes opciones:

  * [Alícuotas](https://ayudas.axoft.com/25ar/alicuota_gv): es la forma básica de definir percepciones. Aunque cubre la mayor parte de las necesidades posee algunas limitaciones con respecto a las percepciones definibles.
  * [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv): esta opción permite definir distintos tipos de percepciones. Su beneficio radica en su mayor flexibilidad (más bases de cálculo, asignación de alícuotas o bases de cálculo de acuerdo a distintas clases de clientes) y la oportunidad de asociarle un modelo de formato de archivo ASCII para la generación de soportes magnéticos requeridos por la autoridad de aplicación del impuesto.



##### Puesta en marcha

A continuación se explicarán los pasos necesarios para implementar correctamente el circuito de percepciones definibles.

**Creación de las percepciones definibles  
**Ingrese al proceso [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv) para crear el nuevo impuesto. Indique los datos identificatorios del nuevo impuesto (código y descripción) y a continuación seleccione la base de cálculo a utilizar, el [modelo del archivo ASCII](https://ayudas.axoft.com/25ar/percepdefin_carp_gv) a generar según lo requerido por la autoridad de aplicación (este dato es opcional y puede ingresarse con posterioridad) y las alícuotas de la percepción.

Consideraciones a tener en cuenta cuando decida modificar la forma de implementar percepciones::

Tenga en cuenta que si decide modificar la forma de implementar percepciones (deja de trabajar con sobretasas relacionadas con códigos de [Alícuotas](https://ayudas.axoft.com/25ar/alicuota_gv) y pasa a trabajar con [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv) o viceversa) debe modificar la parametrización impositiva de todos sus clientes y artículos. Por ejemplo, si trabajaba con percepciones de ingresos brutos asociadas a alícuotas y ahora decide trabajar con percepciones definibles no basta con agregar el código de percepción definible y su correspondiente alícuota sino que debe indicar "N" en el campo Percepción ingresos brutos tanto a nivel cliente como artículo; de lo contrario, se liquidará dos veces el impuesto.  


Para más información sobre este tema consulte [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv).

**¿Para qué se utiliza la clasificación para percepciones definibles?  
**Si bien en la mayoría de los casos no es necesario utilizarla, esta clasificación permite flexibilizar la aplicación y cálculo de las percepciones definibles. Dicha clasificación puede utilizarse para:

  * Aplicar distintas bases de cálculo de acuerdo al tipo de cliente: por ejemplo, existen regímenes de percepción que requieren utilizar la base de cálculo Total del comprobante para un determinado tipo de cliente mientras que para otros se debe aplicar Neto Gravado + IVA. En este caso, debe definir dos clasificaciones para asignar una base de cálculo particular para cada una de ellas en el proceso [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv).  
Tenga en cuenta que sólo es necesario que clasifique los clientes con un comportamiento diferente al general. Para el resto de los clientes sólo debe definir una base de cálculo no asignada a una clasificación específica.  
Basándonos en lo mencionado en el párrafo anterior, bastaría con definir por ejemplo una clasificación para los clientes cuya base de cálculo sea Total del comprobante. De esta forma evita tener que clasificar a todos los clientes de la empresa.  
Recomendamos definir como base de cálculo habitual (sin clasificación) a aquella que se aplique a la mayor cantidad de clientes de su empresa.
  * Aplicar distintas alícuotas del impuesto de acuerdo al artículo y tipo de cliente: otros regímenes requieren aplicar una alícuota de percepción para una determinada combinación cliente / artículo. Por ejemplo, el régimen de percepción de medicamentos de la provincia de Bs.As. indica que se deben aplicar las siguientes alícuotas: 
    * Una alícuota del ## % cuando se facture a laboratorios y distribuidores.
    * Una alícuota del ## % cuando se facture a sujetos comprendidos en convenio multilateral.
    * Otra alícuota diferente cuando se facture a farmacias.



Para este caso debe definir tres clasificaciones para asignarle tres alícuotas de percepción diferentes (al mismo artículo) en el proceso Actualización de artículos.

Importante:

Recuerde que si necesita utilizar el concepto de clasificación para [percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv) debe asignarla a cada uno de los clientes, artículos y bases de cálculo que así lo requieran.

__Nota

A modo de resumen podemos afirmar que las clasificaciones para percepciones definibles actúan como condicionantes de las bases de cálculo y las alícuotas.

###### Asignación a clientes

Una vez definida las percepciones, debe ingresar a los procesos [Actualización de clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv) y [Actualización de clientes potenciales](https://ayudas.axoft.com/25ar/clientepotencial_gv) para asignarle el código de percepción definible que se le debe liquidar dentro de la pantalla Características de Facturación (bajo el título "Percepciones definibles").  
Si completa el campo Alícuota, el sistema liquidará dicha percepción teniendo en cuenta este valor sin importar la alícuota especificada a nivel artículo. De todas formas es requisito que el artículo tenga asignada la percepción para que se la liquide.  
Por el contrario, si no especifica un valor para la alícuota del cliente se tomará en cuenta la alícuota del artículo.

Más información:

Recuerde que si trabaja con clasificación para percepciones definibles debe asignársela a cada uno de los clientes que así lo requieran. De lo contrario sólo se le calculará el impuesto al cliente si existe una alícuota (asignada al artículo) y una base de cálculo (de la percepción definible) que no tengan una clasificación asociada.

En caso de tener que aplicar distintas bases de cálculo en función del tipo de cliente consulte [¿Para qué se utiliza la clasificación para percepciones definibles?](?p=27041/#puesta-en-marcha).  
Si se encuentra habilitada la opción Edita percepciones definibles en la solapa Impuestos del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) será posible agregar o eliminar los códigos de percepción parametrizados en el cliente o cambiar la alícuota asignada. Estas modificaciones pueden realizarse desde los procesos de [Facturación](https://ayudas.axoft.com/25ar/facturas_gv), [Notas de crédito](https://ayudas.axoft.com/25ar/emisionc_gv) y [Notas de débito](https://ayudas.axoft.com/25ar/emisionnd_gv).

###### Asignación a artículos

Una vez asignada las percepciones a los clientes debe hacer lo propio con los artículos. Para ello ingrese al proceso [Actualización de artículos](https://ayudas.axoft.com/25ar/articulo_carp_st) para asignarle el código de percepción definible y la respectiva alícuota que se le debe liquidar dentro de la pantalla Impuestos (bajo el título Percepciones definibles).  
En caso de tener que liquidar distintas alícuotas en función del tipo de cliente consulte [¿Para qué se utiliza la clasificación para percepciones definibles?](?p=27041/#puesta-en-marcha)

###### Adaptación de los tipos de asiento

En caso de querer desglosar contablemente los importes correspondientes a percepciones definidas, ingrese al proceso [Tipos de asiento](https://ayudas.axoft.com/25ar/tipoasiento_gv) y agregue nuevos renglones para detallar las cuentas a imputar. Para cada una de ellas indique el código de percepción y la alícuota correspondiente.

##### Detalle del circuito

Una vez terminada la etapa de puesta en marcha, los procesos donde se realiza el cálculo de las percepciones definibles son los siguientes: [Facturas](?p=19327), [Notas de crédito](?p=19289) y [Notas de débito](?p=19290), además de los procesos relacionados con la [facturación de pedidos](?p=72911/#facturacion-de-pedidos).  
Tenga en cuenta que las percepciones también son calculadas por los procesos [Ingreso de pedidos](?p=19344) y [Generación de cotizaciones](?p=19316).

**¿Cómo se consultan durante la emisión de comprobantes?  
**Las percepciones definibles se muestran acumuladas en el campo Otras percepciones junto al resto de los impuestos calculados. Para consultar el detalle por cada tipo de percepción pulse la tecla <ALT + D>.  
Desde [Facturador](?p=18393) puede consultar las percepciones calculadas en el comprobante ingresando desde la solapa Pagos a la opción Más acciones y luego al ítem Impuestos o también presionando <F6>.

**¿Cómo se imprimen?  
**Si trabaja con controladores o impresoras fiscales, las percepciones (ya sea que utilice percepciones definibles o percepciones a través de alícuotas) se detallarán al pie del comprobante, agrupadas según su tipo: IVA, impuestos internos, ingresos brutos y otras. Si desea detallar cada una de las percepciones definibles del comprobante ingrese a [Parámetros de Ventas](?p=19401) y en la pantalla Valores por defecto para controlador e impresora fiscal indique las variables de reemplazo que quiere utilizar dentro de la zona denominada Pie.  
Si trabaja con impresoras tradicionales, puede optar por imprimirlas agrupadas según su tipo o detallarlas individualmente.  
Para más información sobre este tema consulte [Variables para percepciones definibles](?p=21184) para conocer las variables de impresión que debe utilizar.

**¿Cómo se pueden consultar las percepciones generadas una vez que se emitió el comprobante?  
**El principal informe que detalla los impuestos calculados por el sistema es el de [Impuestos registrados](?p=21546/#impuestos-registrados). Para consultar el total de impuestos calculados para este tipo de percepciones seleccione la opción Incluye percepciones definibles.  
Otros informes y procesos donde se puede consultar el impuesto calculado son:

  * [Libro IVA Ventas](?p=21546): detallando individualmente las percepciones de tipo otras y acumulando el resto según su tipo (IVA, impuestos internos e ingresos brutos).
  * [Comprobantes emitidos](?p=21546/#comprobantes-emitidos): acumulados en la columna otros impuestos.



También puede consultarlas desde los procesos de [Consulta de comprobantes](?p=21172) y [Consulta de cotizaciones](?p=19259).

**¿Cómo se genera el soporte magnético que requiere la autoridad de aplicación de la percepción?  
**Previo a la generación del soporte magnético (archivo ASCII) debe:

  * Definir el [formato del archivo ASCII](?p=21184).
  * Asignar el formato a la percepción a través del proceso [Percepciones definibles](?p=19407).



Una vez que las percepciones tienen asignado su respectivo modelo para ASCII ejecute el proceso [Generación de archivo ASCII](?p=21458). Puede optar por generar el archivo para cada código de percepción o generarlo para un modelo de formato en particular. En este último caso, puede ocurrir que genere información de distintas percepciones calculadas (si dichas percepciones tienen el mismo código de modelo).

##### Diagrama de la lógica del circuito de percepciones definibles

[](https://ayudas.axoft.com/wp-content/uploads/2020/07/percep_defin1.png)Clic en la imagen para expandir

Para más información vea el [esquema de la lógica](?p=27045).

##### Contenido dependiente

  * [Esquema de la lógica de percepciones definibles](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_percepdefin_gv/guia_percdef_introduccion_gv/)



##### Contenidos relacionados

  * [Clasificación de percepciones](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/clasifpercepdefin_gv/)

  * [Generación de archivo ASCII para percepciones definibles (Ventas)](https://ayudas.axoft.com/25ar/ayudas/gv/procperiodico_carp_gv/percepdefin_carp_gv/generarchasciipercepdefin_gv/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/retencpercep_gral_vid/)
