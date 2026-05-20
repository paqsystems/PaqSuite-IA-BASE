# Guía de Restó sobre percepciones definibles

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_percepdefin_gv3/

## Contenido

# Guía de Restó sobre percepciones definibles

Esta opción permite definir distintos tipos de percepciones. Su beneficio radica en su mayor flexibilidad (más bases de cálculo, asignación de alícuotas o bases de cálculo de acuerdo a distintas clases de clientes) y la oportunidad de asociarle un modelo de formato de archivo ASCII para la generación de soportes magnéticos requeridos por la autoridad de aplicación del impuesto.

Las percepciones definibles pueden combinarse con "clasificaciones auxiliares" que permiten condicionar la aplicación de la percepción de acuerdo a la clasificación indicada en el cliente, en el artículo y en la propia percepción definible. Dicha clasificación permite por ejemplo aplicar una base de cálculo determinada para responsables inscriptos y otra para el resto de los clientes.  
Desde la vista del Facturador en Tango Restó, puede consultar las percepciones calculadas en el comprobante de venta a generar desde la opción Mas | Impuestos. Tenga en cuenta que esta opción estará habilitada siempre y cuando se encuentre tildado el parámetro Calcula percepciones que se encuentra en la subsolapa General dentro de la solapa Percepciones.

**¿Por qué conviene definir las percepciones?  
**Las percepciones definibles le permite definir distintos tipos de percepciones. Su beneficio radica en su mayor flexibilidad (más bases de cálculo, asignación de alícuotas o bases de cálculo de acuerdo con distintas clases de clientes) y la oportunidad de asociarle un modelo de formato de archivo ASCII para la generación de soportes magnéticos requeridos por la autoridad de aplicación del impuesto.

##### Puesta en marcha

A continuación, se explicarán los pasos necesarios para implementar correctamente el circuito de percepciones definibles.

**Creación de las percepciones definibles**  
Ingrese al proceso [Percepciones definibles](?p=32893) para crear el nuevo impuesto. Indique los datos identificatorios del nuevo impuesto (código y descripción) y a continuación seleccione la base de cálculo a utilizar, el modelo del archivo ASCII a generar según lo requerido por la autoridad de aplicación (este dato es opcional y puede ingresarse con posterioridad) y las alícuotas de la percepción.

**¿Para qué se utiliza la clasificación para percepciones definibles?  
**Si bien en la mayoría de los casos no es necesario utilizarla, esta clasificación permite flexibilizar la aplicación y cálculo de las percepciones definibles. Dicha clasificación puede utilizarse para:

  * Aplicar distintas bases de cálculo de acuerdo al tipo de cliente: por ejemplo, existen regímenes de percepción que requieren utilizar la base de cálculo Total del comprobante para un determinado tipo de cliente mientras que para otros se debe aplicar Neto Gravado + IVA. En este caso, debe definir dos clasificaciones para asignar una base de cálculo particular para cada una de ellas en el proceso [Percepciones definibles](?p=32893).  
Tenga en cuenta que sólo es necesario que clasifique los clientes con un comportamiento diferente al general. Para el resto de los clientes sólo debe definir una base de cálculo no asignada a una clasificación específica.  
Basándonos en lo mencionado en el párrafo anterior, bastaría con definir, por ejemplo, una clasificación para los clientes cuya base de cálculo sea Total del comprobante. De esta forma evita tener que clasificar a todos los clientes de la empresa.  
Recomendamos definir como base de cálculo habitual (sin clasificación) a aquella que se aplique a la mayor cantidad de clientes de su empresa.
  * Aplicar distintas alícuotas del impuesto de acuerdo al artículo y tipo de cliente: otros regímenes requieren aplicar una alícuota de percepción para una determinada combinación cliente / artículo. Por ejemplo, el régimen de percepción de productos alimenticios de la provincia de Bs.As. indica que se deben aplicar las siguientes alícuotas:


  *     * Una alícuota del ## % cuando se facture a mayoristas.
    * Otra alícuota diferente cuando se facture a confiterías.



Para este caso debe definir dos clasificaciones para asignarle dos alícuotas de percepción diferentes (al mismo artículo) en el proceso Actualización de artículos asignado un modelo de percepción.

__Importante

Recuerde que si necesita utilizar el concepto de clasificación para [percepciones definibles](?p=32893) debe asignarla a cada uno de los clientes, artículos y bases de cálculo que así lo requieran.  


__Nota

A modo de resumen podemos afirmar que las clasificaciones para percepciones definibles actúan como condicionantes de las bases de cálculo y las alícuotas.  


**Asignación a clientes  
**Si trabaja con clasificación para percepciones definibles, debe asignársela a cada uno de los clientes que así lo requieran. De lo contrario sólo se le calculará el impuesto al cliente si existe una alícuota (asignada al artículo) y una base de cálculo (de la percepción definible) que no tengan una clasificación asociada.  
En caso de tener que aplicar distintas bases de cálculo en función del tipo de cliente consulte ¿Para qué se utiliza la clasificación para percepciones definibles?

**Definición de modelos de percepciones  
**Antes de poder aplicar percepciones definibles a los artículos, es necesario crear al menos un modelo de percepción, donde se establecen los siguientes parámetros:

  * El tipo de percepción (por ejemplo, Ingresos Brutos).
  * Las bases de cálculo sobre las que se aplicará la percepción (importe neto, importe total, etc.).
  * Las alícuotas correspondientes, que pueden ser generales o clasificadas por tipo de cliente/artículo.
  * La opción de clasificación (si se requiere tratar de forma diferenciada según criterios definidos para clientes o artículos).



**Asignación a artículos  
**Una vez asignadas las percepciones a los clientes y definidos los modelos de percepciones, debe asignar a los artículos el modelo de percepción que le corresponda. Para ello ingrese al proceso [Actualización masiva de perfil de artículos](?p=24529) para asignarle el código del modelo de percepción definible.  
En caso de tener que liquidar distintas alícuotas en función del tipo de cliente consulte ¿Para qué se utiliza la clasificación para percepciones definibles?

**¿Cómo configurar el uso de padrones AGIP y ARBA?  
**Desde la configuración de la Terminal, en la subsolapa Padrones AGIP y Padrones ARBA dentro de la solapa Percepciones, es posible parametrizar los valores y datos necesarios para el uso de los padrones de AGIP y ARBA.  
Adicionalmente, en la solapa General (también dentro de Percepciones), se puede definir el tipo de control sobre los padrones:

  * Estricto
  * Flexible
  * Sin control de padrones



Este parámetro afecta a todos los procesos del sistema que intervienen en el cálculo de percepciones, tales como:

  * Precuenta
  * Emisión de comprobantes de venta



**Padrones AGIP**

Para todos los padrones: defina si actualiza las alícuotas de los clientes de acuerdo a la provincia de la dirección de entrega o por el CUIT del cliente en forma independiente de la provincia.

Solo régimen general: defina los parámetros para el padrón de régimen general de AGIP.

Provincia asociada para padrón régimen general: seleccione la provincia para asociar al padrón régimen general de AGIP.  
La provincia asociada es necesaria en operaciones alcanzadas por el régimen general con contribuyentes pasibles de percepción no incluidos en el archivo del padrón de régimen general de AGIP (RG 421/16).

__Nota

Si usted no selecciona una provincia asociada o la elimina, no se realizará la asignación de alícuota general a clientes no incluidos en el padrón.  


Asigna alícuota general a clientes no incluidos en el padrón: defina si actualiza la alícuota general en los clientes no incluidos dentro del padrón de régimen general. Seleccione una opción según los criterios, ya sea direcciones de entrega con igual provincia a la provincia asociada al padrón o en todas las direcciones de entrega independientemente de la provincia asociada.

__Nota

Al eliminar la provincia asociada y luego actualizar las alícuotas en los clientes (en aquellos que ya tuvieran la alícuota general asignada con anterioridad) el proceso de actualización las eliminará dado que no existe una provincia asociada en la empresa.  


**Padrones ARBA**

Actualiza alícuotas según: defina si actualiza las alícuotas de los clientes de acuerdo a la provincia de cada dirección de entrega o por el CUIT del cliente en forma independiente de la provincia.

Provincia asociada al padrón: indique la provincia que corresponda con el padrón de ARBA. Este campo es obligatorio si definió que se actualicen alícuotas según la provincia del cliente o dirección de entrega.

Asigna alícuota a clientes no incluidos en el padrón: seleccione esta opción si necesita definir una alícuota a incorporar masivamente, a los clientes que estén fuera del padrón de ARBA.

Actualiza alícuotas según: defina si actualiza las alícuotas de los clientes que no están en el padrón, de acuerdo a la provincia de cada dirección de entrega o tomando en cuenta el CUIT del cliente -en forma independiente de la provincia-.

Código de percepción: seleccione del listado la percepción de ingresos brutos de jurisdicción provincial que desea agregar a los clientes que no existan en el padrón de ARBA.

Código alícuota: seleccione del listado la alícuota de percepción que desea agregar a los clientes que no estén incluidos en el padrón de ARBA, es decir, aquella alícuota de percepción que tiene indicado en el campo Padrón la opción 'Sin Padrón', en la solapa Alícuotas del proceso [Percepciones](?p=13099).

Parámetro Calcula percepciones**:** una vez finalizada la configuración previa indicada en la puesta en marcha, será necesario activar el parámetro Calcula percepciones en la configuración de la terminal. Este se encuentra en la subsolapa General, dentro de la solapa Percepciones.  
Este parámetro le indica al sistema que debe calcular percepciones al momento de generar los comprobantes de ventas.

__Nota

Tenga en cuenta que, aunque se haya completado correctamente toda la parametrización previa, si el parámetro Calcula percepciones se encuentra desmarcado, Tango Restó no realizará el cálculo de percepciones al emitir los comprobantes de ventas.  


Además para configurar el servidor, hacé clic en el botón "Obtener" y verificá que esta acción complete automáticamente los campos Servidor y Puerto, necesarios para establecer la conexión con el servicio.

__Importante

Esta configuración debe realizarse directamente desde el servidor de aplicaciones.  
Recuerde que, además, debe estar seleccionada la opción Calcula percepciones para que el sistema active el circuito de percepciones durante la facturación.  


**Variables de impresión  
**A continuación, se detallan las nuevas variables de impresión disponibles para comandas y comprobantes de ventas, que pueden utilizarse en la configuración de los formularios de impresión:

Variable | Tema | Subtema | Longitud | **Descripción**  
---|---|---|---|---  
PT | Factura | Totales |  11 | Importe total de las percepciones definibles  
PT | Nota de crédito | Totales |  11 | Importe total de las percepciones definibles  
PT | Comandas | Totales |  11 | Importe total de las percepciones definibles  
I8 | Factura | Detalle de las percepciones definibles |  2 | Código de la percepción definible  
I8 | Nota de crédito | Detalle de las percepciones definibles |  2 | Código de la percepción definible  
FB | Factura | Detalle de las percepciones definibles | 30 | Descripción de la percepción definible  
FB | Nota de crédito | Detalle de las percepciones definibles |  30 | Descripción de la percepción definible  
I2 | Factura | Detalle de las percepciones definibles | 9 | Porcentaje de la alícuota de la percepción definible.  
I2 | Nota de crédito | Detalle de las percepciones definibles | 9 | Porcentaje de la alícuota de la percepción definible.  
I3 | Factura | Detalle de las percepciones definibles |  30 | Descripción de la alícuota de la percepción definible.  
I3 | Nota de crédito | Detalle de las percepciones definibles |  30 | Descripción de la alícuota de la percepción definible.  
FI | Factura | Detalle de las percepciones definibles |  11 | Importe de la percepción definible.  
FI | Nota de crédito | Detalle de las percepciones definibles |  11 | Importe de la percepción definible.  
FJ | Factura | Detalle de las percepciones definibles |  10 | Jurisdicción de la percepción definible.  
FJ | Nota de crédito | Detalle de las percepciones definibles |  10 | Jurisdicción de la percepción definible.  
FT | Factura | Detalle de las percepciones definibles | 15 | Tipo de percepción definible.  
FT | Nota de crédito | Detalle de las percepciones definibles | 15 | Tipo de percepción definible.  
BF | Factura | Detalle de las percepciones definibles |  20 | Provincia de la percepción definible.  
BF | Nota de crédito | Detalle de las percepciones definibles |  20 | Provincia de la percepción definible.  
FR | Factura | Detalle de las percepciones definibles |  3 | Régimen de la percepción definible.  
FR | Nota de crédito | Detalle de las percepciones definibles | 3 | Régimen de la percepción definible.  
FK | Factura | Datos del cliente | 6 | Clasificación de la percepción definible del cliente.  
FK | Nota de crédito | Datos del cliente |  6 | Clasificación de la percepción definible del cliente.  
FL | Factura | Datos del cliente |  20 | Descripción de la clasificación de la percepción definible del cliente.  
FL | Nota de crédito | Datos del cliente |  20 | Descripción de la clasificación de la percepción definible del cliente.  
P5 | Factura | Totales |  11 | Total grabado + total IVA + total impuestos internos + total percepciones + propina  
P5 | Nota de crédito | Totales |  11 | Total grabado + total IVA + total impuestos internos + total percepciones + propina  
KF | Factura | Datos del cliente |  10 | Código postal de la dirección de entrega  
KF | Nota de crédito | Datos del cliente |  10 | Código postal de la dirección de entrega  
KF | Comandas | Datos del cliente |  10 | Código postal de la dirección de entrega  
KG | Factura | Datos del cliente |  100 | Teléfono principal. Dato de la entrega  
KG | Nota de crédito | Datos del cliente |  100 | Teléfono principal. Dato de la entrega  
KG | Comandas | Datos del cliente |  100 | Teléfono principal. Dato de la entrega  
  
##### Detalle del circuito

Tango Restô calcula percepciones cuando la comanda y/o factura tiene asignado un cliente habitual y se utiliza alguna de las siguientes modalidades de facturación:

  * Modalidad 1: Salón, Mostrador, Delivery.
  * Modalidad 2: Salón, Mostrador, Delivery.
  * Facturar mesa.



__Nota

No se calculan percepciones en los circuitos de facturación con modalidad 0, 3, ni en los procesos de facturación remota, facturación con Mobile o desde el módulo de mozo ni en comprobantes emitidos a clientes ocasionales.  


Las percepciones se calculan al visualizar la factura o al solicitar la generación de la precuenta, siempre que se cumplan todas las siguientes condiciones:

  * La comanda tenga asignado un cliente habitual.
  * La dirección de entrega tenga asociada al menos una percepción.
  * Al menos uno de los artículos incluya un modelo de percepción.



Tenga en cuenta que durante la carga de artículos en la comanda, los montos mostrados en pantalla no incluyen percepciones.

Una vez que las percepciones tienen asignado su respectivo modelo para ASCII ejecute el proceso Generación de archivo ASCII. Puede optar por generar el archivo para cada código de percepción o generarlo para un modelo de formato en particular. En este último caso, puede ocurrir que genere información de distintas percepciones calculadas (si dichas percepciones tienen el mismo código de modelo).

**Diagrama de la lógica del circuito de percepciones definibles**

[](https://ayudas.axoft.com/wp-content/uploads/2020/07/percep_defin1.png)Clic en la imagen para expandir

Para más información vea el [esquema de la lógica](?p=27045).

##### Detalle Circuito emisión notas de crédito

Solo si el parámetro Calcula percepciones de la solapa Percepciones, en la configuración de la terminal, se encuentra marcado, una vez definidos los parámetros para generar la nota de crédito, el sistema preguntará si desea calcular percepciones. Si la respuesta es afirmativa, procederá a calcularlas; en caso contrario, generará la nota de crédito sin incluir ningún tipo de percepción.  
Tenga en cuenta que las notas de crédito que calculan percepciones se emiten para clientes habituales. Si la nota de crédito se genera de manera referenciada, la dirección de entrega utilizada será la misma que la de la factura original.  
En caso de que la nota de crédito se genere sin referencia, el sistema tomará la dirección de entrega habitual del cliente.

##### Preguntas frecuentes

**¿Cómo se consultan durante la emisión de comprobantes?**  
Las percepciones definibles se visualizan acumuladas junto al resto de los impuestos calculados en la vista del Facturador. Para consultarlas, debe seleccionar la opción Más y luego hacer clic en Impuestos.

**¿Cómo se imprimen?**  
Si trabaja con controladores o impresoras fiscales, las percepciones definibles se detallarán solo al pie del comprobante, agrupadas según su tipo: IVA, impuestos internos, ingresos brutos y otras.  
Si trabaja con impresoras tradicionales, puede optar por imprimirlas agrupadas según su tipo al pie del comprobante.  
Para más información sobre este tema consulte las [variables para facturas y notas de crédito](?p=37960) para conocer las variables de impresión que debe utilizar.

**¿Cómo se pueden consultar las percepciones generadas una vez que se emitió el comprobante?**  
El principal informe que detalla los impuestos calculados por el sistema es el de[ Impuestos registrados](?p=24628/#impuestos-registrados). Para consultar el total de impuestos calculados para este tipo de percepciones seleccione la opción Incluye percepciones definibles.  
Otros informes y procesos donde se puede consultar el impuesto calculado son:

  * [**Libro IVA Ventas:**](?p=24628/#iva-ventas) detallando individualmente las percepciones de tipo otras y acumulando el resto según su tipo (IVA, impuestos internos e ingresos brutos).  
Comprobantes emitidos: acumulados en la columna otros impuestos.
  * [**Comprobantes emitidos:**](?p=24628/#comprobantes-emitidos) acumulados en la columna otros impuestos.



**¿Cómo se genera el soporte magnético que requiere la autoridad de aplicación de la percepción?**  
Previo a la generación del soporte magnético (archivo ASCII) debe:

  * Definir el formato del archivo ASCII.
  * Asignar el formato a la percepción a través del proceso [Percepciones definibles](?p=33765).



**¿Se puede elegir una dirección de entrega al momento de emitir una nota de crédito no referenciada?  
**No. El sistema tomará la dirección de entrega que se encuentre definida como habitual.

**¿Con qué dirección de entrega se genera la nota de crédito que calcule percepción cuando la nota de crédito es referenciada?  
**La nota de crédito se generará con la misma dirección de entrega utilizada al emitir la factura.

**¿En qué modalidades de facturación se calculan las percepciones?**

  * Modalidad 1
  * Modalidad 2
  * Facturar mesa
  * Facturar cliente.



__Nota

No se calculan percepciones en comprobantes emitidos desde: las modalidades de facturación ciegas (0 o 3), ni desde Mobile, ni desde el módulo de mozo o ni facturación remota.  


**¿Durante la carga de artículos en la comanda se visualizan las percepciones que se están calculando?  
**No. Durante la carga de artículos en la comanda, las percepciones no se calculan ni se visualizan. Sin embargo, al emitir la precuenta o al ingresar a la vista del Facturador, el sistema calcula automáticamente las percepciones correspondientes para la comanda.

**¿Puedo seleccionar una dirección de entrega distinta a la habitual para un cliente que ya se encuentra asociado a la comanda?  
**Sí. Una vez que haya asociado el cliente a la comanda, podrá seleccionar una dirección de entrega distinta a la habitual.  
Para hacerlo, desde la vista del Facturador y con el cliente ya asociado, acceda a la opción Modificar cliente. Luego, en la solapa Dirección de entrega, seleccione la dirección que desea asignar al cliente para la generación del comprobante de venta y, finalmente, presione "Aceptar".

**¿Puedo generar comprobantes de ventas que calculen percepciones con clientes ocasionales?  
**No, las percepciones se calculan solo para clientes habituales.

**He realizado la puesta en marcha del circuito, pero no se están calculando percepciones en el comprobante de venta.  
**Verifique lo siguiente:

  * Que el parámetro Calcula percepciones se encuentre marcado en la configuración de la terminal, dentro de la solapa Percepciones.
  * Que el cliente, el artículo, la percepción y el modelo compartan la misma clasificación.



**¿Las precuentas incluyen las percepciones?  
**Sí. En cualquier proceso o circuito donde se visualice o imprima la precuenta, esta incluirá el cálculo de las percepciones definibles asociadas a la comanda.

**¿Cómo se visualizan los montos de las percepciones en los comprobantes de venta?**

  * En Tango Restó, las percepciones definibles se visualizan al pie del comprobante de venta, agrupadas por tipo.
  * En el caso de las precuentas, se muestra un gran total del monto calculado en concepto de percepciones, sin detallar su tipo.



__Nota

Para que las percepciones se visualicen correctamente en los formularios de impresión, recuerde configurar dichos formularios incluyendo las variables de reemplazo correspondientes que el sistema pone a disposición.  


**¿Qué necesita Tango Restó para calcular percepciones en un comprobante de venta?**

  * Haber realizado correctamente los pasos de la puesta en marcha del circuito.
  * Tener marcado el parámetro Calcula percepciones en la solapa Percepciones de la configuración de la terminal.
  * Que la comanda tenga asociado un cliente habitual.
  * Que la dirección de entrega seleccionada para el cliente tenga al menos una percepción asociada.
  * Que la modalidad de facturación sea 1, 2, Facturar mesa o Facturar cliente.



**¿Las propinas se incluyen en el cálculo de percepciones?  
**No. Las propinas están excluidas del cálculo de percepciones. Durante el proceso de cálculo, el sistema no las considera como parte de la base imponible para determinar percepciones.

**En los informes o consultas, ¿se visualizan los montos de las percepciones calculadas?  
**En los informes o consultas Live, los montos de las percepciones calculadas se visualizan únicamente en los relacionados con facturación y en aquellas comandas que ya hayan sido cobradas o facturadas. Tenga en cuenta que en los informes o consultas Live que detallan información de artículos, no se visualizarán los montos correspondientes al cálculo de percepciones.

**¿Puedo modificar las percepciones en el momento de generar un comprobante de venta?  
**No. Las percepciones que se calcularán durante la generación del comprobante serán las que correspondan según la dirección de entrega asociada al cliente en ese momento.  
Si desea que una percepción sea incluida o excluida del comprobante, deberá modificar previamente las percepciones asociadas a la dirección de entrega del cliente, antes de emitirlo.  
Esto puede hacerse desde el proceso Clientes en Cloud o desde el proceso Clientes en Tango Restó.

**¿El circuito "Facturar cliente" calcula percepciones?**  
Sí, pero solo si se selecciona una única comanda.  
Si intenta seleccionar más de una comanda mientras el parámetro Calcula percepciones está activo (en la configuración de la terminal, solapa Percepciones), el sistema mostrará un mensaje indicando que no es posible continuar con el circuito mientras haya más de una comanda seleccionada.

__Nota

Para que el cálculo de percepciones funcione correctamente, asegúrese de trabajar con una sola comanda cuando este parámetro esté habilitado.  


##### Contenidos relacionados

  * [Clasificación de percepciones (Restô)](https://ayudas.axoft.com/25ar/ayudas/gv3/archivo_carp_gv3/percepcion_gv3/clasifpercepdefin_gv3/)

  * [Generación de archivo ASCII (Restô)](https://ayudas.axoft.com/25ar/ayudas/gv3/procesoperiodico_carp_gv3/percepdefin_carp_gv3/generarchasciipercepdefin_gv3/)
