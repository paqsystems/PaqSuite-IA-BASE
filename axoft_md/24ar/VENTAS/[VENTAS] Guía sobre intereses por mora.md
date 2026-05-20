# Guía sobre intereses por mora

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_intermora_gv/

## Contenido

# Guía sobre intereses por mora

Es posible generar notas de débito correspondiente a intereses por mora en forma automática.

Principales características de este circuito:

  * Definición de políticas para el cálculo de interés, que pueden asignarse a un cliente, a una condición de venta, o a nivel general por [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes). Estas políticas le permiten definir distintas tasas de interés, mínimos sobre los que se debe cobrar la mora, modalidad de cálculo (teniendo en cuenta la fecha de vencimiento y/ o incluyendo la fecha de los valores si alguno de los vencimientos estuviera cancelado), modalidad de imputación al comprobante original, cargos adicionales, leyendas para la impresión, etc.
  * Posibilidad de generar e imprimir las notas de débito por mora desde el [ingreso de cobranzas](https://ayudas.axoft.com/24ar/ingresocobranza_gv) o desde el nuevo proceso [Gestión de débitos por mora](https://ayudas.axoft.com/24ar/gestiondebitomora_gv). Entre las principales características de este proceso podemos destacar: 
    * Posibilidad de asignar, eliminar y/o cambiar la política de los comprobantes para calcular el interés.
    * Simulación del interés por mora que se debe generar; permitiendo incluso el ingreso de las fechas de los valores que entregaría el cliente.
    * Exportación a Excel de la hoja de trabajo (facturas incluidas, notas de débito e importes que se van a generar).
    * Emisión de un reporte en formato PDF con el detalle del cálculo de interés por mora correspondiente a cada nota de débito emitida.
    * Generación y emisión de notas de débito (la emisión de notas de débito requiere un permiso específico).
    * Consulta Live de notas de débito generadas por mora.



##### Puesta en marcha

  * Defina el método de cálculo a utilizar, ingresando al menos una [política de interés por mora](?p=19419).
  * Defina un [tipo de comprobante](?p=19573) de débito, indicando que registra intereses por mora.
  * Configure en [Parámetros de Ventas](?p=19401/#parametros-para-comprobantes) el comportamiento de los datos necesarios para generar las notas de débito por mora en forma automática.
  * Asigne la política de mora a utilizar, pudiendo hacerlo en forma general para todos los clientes asignando un valor en [Parámetros de Ventas](?p=19401), y/o en las [condiciones de ventas](?p=19255) y/o a cada uno de los [clientes](?p=19444).
  * Si la asignación de políticas de mora se realiza en los [clientes](?p=19444) es posible hacerlo en forma masiva desde el asistente para [Asignación masiva de clientes a interés por mora](?p=19209) o individualmente en el proceso de [actualización de clientes](?p=19444).



__Nota

Luego de completar los pasos anteriores, usted está en condiciones de comenzar a generar notas de débito por mora en el caso que se incurran en atrasos en los pagos, o bien que se realicen con valores posdatados.

##### Detalle del circuito

Una vez realizada la puesta en marcha, usted está en condiciones de comenzar a generar notas de débito de interés por mora.  
Es posible generarlas desde tres procesos diferentes:

###### Ventas Cuenta Corriente Cobranzas

Si se encuentra habilitado el [parámetro de Ventas](?p=19401) genera mora en la cobranza, y si se realiza una cobranza que incluye facturas vencidas se generará en forma automática el cálculo de interés por mora, con la posibilidad de emitir la o las notas de débitos correspondientes al finalizar el ingreso del recibo. También se pueden generar notas de débito por mora si la [política de interés por mora](?p=19419) que está utilizando está configurada para que tenga en cuenta los valores (cheques diferidos) de la cobranza.  
En el caso de que una cuota con fechas alternativas de vencimiento sea abonada posteriormente a la última fecha de vencimiento, se generará en el mismo momento de la cobranza el ajuste por cobro en fecha alternativa, y luego de confirmado el recibo, se generará la nota de débito por mora (calculada desde la última fecha alternativa).

Para más información consulte [Cobranzas](?p=21323).

###### Ventas Cuenta Corriente Gestión de débitos por mora

Este proceso cuenta con un asistente que lo ayudará a calcular los débitos por mora a generar sobre facturas vencidas, o cobradas con atraso.  
Seleccionando un cliente en particular, es posible simular el ingreso de valores, tanto para comprobantes vencidos como para aquellos que aún no lo están, de esta manera se calculará el interés por la entrega de valores diferidos.  
Para la selección de facturas puede optar entre la fecha de emisión, vencimiento, o cobranza (si se generaron recibos en el período ingresado).  
El sistema le propone todas las facturas (comprendidas dentro de los filtros seleccionados) en condiciones de generar interés. Usted puede seleccionar sobre cuales desea generar la mora. Una vez propuestas las notas de débito a generar, es posible desmarcar aquellas que no desea generar.  
Tenga en cuenta que el cálculo de interés por mora se genera a partir de la última fecha de vencimiento.  
Por lo tanto, cuando una factura con fechas alternativas de vencimiento genere interés por mora, se incluirá en el cálculo el ajuste por cobro en fecha alternativa más la mora correspondiente a los días de atraso desde la última fecha de vencimiento hasta el día del efectivo pago.  
Es posible modificar el importe final de la nota de débito a generar, siempre que se encuentre activado este [parámetro de Ventas](?p=19401).  
Los comprobantes que se muestran en la grilla pueden filtrar, agrupar y ordenar la información.  
Brinda la posibilidad emitir un informe con los datos que dieron origen al cálculo, de modo que pueda explicar claramente al cliente los motivos de la mora. Dicha información se puede consultar luego desde la ficha Live de la nota de débito.  
Una vez confirmadas las facturas sobre las que se calculará mora, será posible emitir las notas de débito a los clientes seleccionados, siempre que el operador tenga permiso para para generar esos comprobantes. En el caso de no contar con este permiso, sólo podrá consultar el interés calculado y realizar simulaciones de ingreso de valores.

Para más información consulte [Gestión de débitos por mora](?p=21387).

###### Ventas Facturación Notas de débito

Ingrese un [tipo de comprobante](?p=19573) que tenga activo el parámetro registra intereses por mora.  
Puede realizar referencia a una factura a la que imputar el débito por mora. En este caso se genera el historial correspondiente al interés cobrado a la factura, registrando cuál fue la última fecha en que se calculó interés para esa factura.  
En el caso de no realizar referencia a ningún comprobante, puede hacerlo posteriormente en el proceso Imputación de comprobantes, generando el historial de interés por mora en este momento.

Importante:

Tenga en cuenta que desde este proceso el cálculo del interés no se realiza en forma automática, se debe ingresar el importe por el cual se generara el comprobante.

Para más información consulte [Emisión de notas de débito](?p=19290).

##### Preguntas frecuentes

**¿Cómo defino la tasa y el método de cálculo de interés a aplicar a mis clientes?  
**Defina una [política de interés por mora](?p=19419). Este proceso le permite configurar diversas modalidades para el cálculo de interés por mora (políticas).

**¿Qué es una política de interés por mora?  
**Es la definición del método de cálculo que se utiliza para generar el interés por mora.  
Brinda la posibilidad de configurar distintos modos de obtener el importe de interés para luego asignar a un cliente, a una condición de venta o a nivel general por [Parámetros de Ventas](?p=19401).  
Es posible configurar distintas tasas de interés, mínimos sobre los que se debe cobrar la mora, modalidad de cálculo (teniendo en cuenta la fecha de vencimiento solamente o incluyendo la fecha de los valores), modalidad de imputación al comprobante original, cargos adicionales, leyendas para la impresión, etc.  
Son de utilidad para el caso en que usted tenga características especiales para ciertos clientes (por ejemplo, clientes VIP a los que aplica una tasa menor que al resto), o distintos grupos a los que desee aplicar un cálculo de interés con características similares.

**¿Cómo se utilizan las políticas de interés por mora?  
**Una vez que se realizó la puesta en marcha del circuito de intereses por mora, las facturas en cuenta corriente que pertenecen a clientes que generan débitos por mora quedan asociadas a una política de interés (*).  
La asignación de la política al comprobante se realiza teniendo en cuenta el siguiente orden de prioridades:

  * En primer lugar se utiliza la política del [cliente](?p=19444) si éste tiene alguna asignada.
  * En segundo lugar se utiliza la política de la condición de venta si ésta tiene alguna asignada.
  * En tercer lugar, se utiliza la política definida a nivel general, en [Parámetros de Ventas](?p=19401).



(*) La política asignada en [Parámetros de Ventas](?p=19401) se utiliza también en los casos en que una factura se haya generado sin asignación de política (por ser de una versión anterior o por pertenecer a un cliente que no genera débitos por mora), para realizar la asignación luego de su emisión. En el caso que cuente con permiso de edición, puede optar por elegir otra política en el momento de generar la nota de débito desde [Gestión de débitos por mora](?p=21387).

**¿Cómo indico que las operaciones de uno o varios clientes generan débitos por mora?  
**Para ello, tiene dos opciones:

  * Active para cada [cliente](?p=19444) el parámetro débitos por mora. Es posible, también, asignar una política particular para el cliente.
  * Desde el proceso [Asignación masiva de clientes a interés por mora](?p=19209) seleccione a qué clientes desea modificarles este atributo.



**¿Cómo indico que un grupo de clientes utiliza la misma política de interés por mora?  
**Utilice el proceso [Asignación masiva de clientes a interés por mora](?p=19209) para asignar en forma global a un grupo de clientes la política deseada.

**¿Cómo se calcula el interés por mora?  
**El cálculo se realiza según la configuración que utilice para la [política de interés por mora](?p=19419). Para más información consulte la ayuda de este proceso, donde puede encontrar ejemplos de aplicación según las diferentes configuraciones.

**¿Puedo definir cargos adicionales al interés?  
**En la definición de la [política de interés por mora](?p=19419) puede asignar un concepto o cargo adicional, el mismo será incluido en la generación del débito por mora. Este adicional puede ser definido como un importe fijo, o un porcentaje del interés calculado.

**¿En qué momentos se puede generar una nota de débito por mora?  
**Se puede generar interés por mora en los siguientes procesos: [Ingreso de cobranzas](?p=21323), [Gestión de débitos por mora](?p=21387), [Nota de débitos](?p=19290).

**¿Puedo consultar el interés a cobrar sin llegar a generar una nota de débito real?  
**Puede efectuar esta consulta ingresando al proceso [Gestión de débitos por mora](?p=21387) y mediante la selección de filtros, obtener la información deseada. Cancele el proceso sin llegar a generar la nota de débito.  
Cuenta con permisos especiales de usuario para habilitar el proceso sólo para consultas o simulaciones.

**En el caso de que el cliente informe que efectuará su pago con valores posdatados ¿Puedo simular una cobranza para expedirle el interés resultante?  
**Puede efectuar esta simulación ingresando al proceso [Gestión de débitos por mora](?p=21387).  
Seleccione el cliente, y demás filtros que pueda necesitar (facturas, fecha de vencimiento, etc.) y utilizando el botón "Simulación de ingreso de valores" puede obtener esta información.  
Puede cancelar el proceso sin llegar a generar la nota de débito, u optar por generarla en este momento para tenerla disponible en el momento que el cliente realmente efectúe el pago.  
Cuenta con permisos especiales de usuario, para habilitar el proceso sólo para consultas o simulaciones.

**¿Cómo genero una nota de débito por mora?**

Puede generar una nota de débito por mora desde alguno de estos tres procesos:

  * Ventas | Cuenta Corriente | Cobranzas.  
Si se encuentre habilitado el [Parámetro de Ventas](?p=19401) genera mora en la cobranza, y si se realiza una cobranza que incluye facturas vencidas se generará en forma automática el cálculo de interés por mora, con la posibilidad de emitir la o las notas de débitos correspondientes al finalizar el ingreso del recibo. También se pueden generar notas de débito por mora si la [política de interés por mora](?p=19419) que está utilizando está configurada para que tenga en cuenta los valores (cheques diferidos) de la cobranza.  
Para más información consulte [Cobranzas](?p=21323).
  * Ventas | Cuenta Corriente | Gestión de débitos por mora:  
Este proceso cuenta con un asistente que lo ayudará a calcular los débitos por mora a generar sobre facturas vencidas, o cobradas con atraso.  
Seleccionando un cliente en particular, es posible simular el ingreso de valores, tanto para comprobantes vencidos como para aquellos que aún no lo están, de esta manera se calculará el interés por la entrega de valores diferidos.  
Para la selección de facturas puede optar entre la fecha de emisión, vencimiento, o cobranza (si se generaron recibos en el período ingresado).  
El sistema le propone todas las facturas (comprendidas dentro de los filtros seleccionados) en condiciones de generar interés. Usted puede seleccionar sobre cuales desea efectivamente generar la mora. Una vez propuestas las notas de débito a generar, es posible desmarcar aquellas que no desea generar.  
Es posible modificar el importe final de la nota de débito a generar, siempre que se encuentre activado este [Parámetro de Venta](?p=19401).  
Los comprobantes que se muestran en la guilla pueden filtrar, agrupar y ordenar la información.  
Brinda la posibilidad de emitir un informe con los datos que dieron origen al cálculo, de modo que pueda explicar claramente al cliente los motivos de la mora. Dicha información se puede consultar luego desde la ficha Live de la nota de débito.  
Una vez confirmadas las facturas sobre las que se calculará mora, será posible emitir las notas de débito a los clientes seleccionados siempre que el operador tenga permiso para para generar esos comprobantes. En el caso de no contar con este permiso, sólo podrá consultar el interés calculado y realizar simulaciones de ingreso de valores.  
Para más información consulte [Gestión de débitos por mora](?p=21387).
  * Ventas | Facturación | Notas de débito:  
Ingrese un tipo de comprobante que tenga activo el parámetro registra intereses por mora.  
Puede realizar referencia a una factura a la que imputar el débito por mora. En este caso se genera el historial correspondiente al interés cobrado a la factura, registrando la última fecha en que se calculó interés para esa factura.  
En el caso de no realizar referencia a ningún comprobante, puede hacerlo posteriormente en el proceso [Imputación de comprobantes](?p=21365), generando el historial de interés por mora en este momento.  
Para más información consulte [Emisión de notas de débito](?p=19290).



Importante:

Tenga en cuenta que desde este proceso el cálculo del interés no se realiza en forma automática, se debe ingresar el importe por el que se generara el comprobante.

**¿Cómo puedo informar a mi cliente el cálculo que efectuó Tango para generar su nota de débito por mora?  
**Al generar notas de débito por mora desde los procesos [Cobranzas](?p=21323) o [Gestión de débitos](?p=21387)[ por mora](?p=21395) puede consultar la columna "Detalle del cálculo" incluida en el asistente para la generación. Esta columna exhibe un archivo de tipo .PDF con información referida al método de cálculo y datos que dan origen al interés calculado, que puede imprimir o guardar para una posterior consulta.

__Nota

Tenga en cuenta que el tamaño de impresión de este archivo es A4.

**¿Puedo consultar nuevamente esta información una vez generada la nota de débito?  
**Una vez generada la nota de débito, puede volver a imprimir el detalle del cálculo accediendo a la ficha Live del comprobante, o desde la consulta Notas de débito de interés por mora.

**¿Qué hago si me equivoqué en la aplicación de una nota de débito?  
**Puede revertir la imputación desde el proceso [Imputación de comprobantes](?p=21365).  
Este proceso le brinda la posibilidad de marcar la factura para que ya no vuelva a generar interés. En el caso que opte por seguir generando, al revertir la imputación de la nota de débito, puede anular este comprobante, y volver a generar interés desde cualquier proceso que permita esta opción.

**¿Es posible definir una leyenda en la factura informando que devengará mora si incurre en atraso en el pago?  
**En el proceso [Políticas de interés por mora](?p=19419) defina un texto en el ítem leyenda en facturas. Incluya la variable de impresión **@LN** en el formulario (Typ) de las facturas, para que se imprima este texto en las facturas asociadas a la política. Por ejemplo: "En el caso de incurrir en mora se aplicará un 2% mensual".

**¿Cómo puedo generar una nota de débito de interés en forma automática sobre facturas que inicialmente no tuvieron política de interés por mora asignada?  
**Desde el proceso [Gestión de débitos por mora](?p=21387), utilizando el botón "Incluir otras facturas" puede incorporar a este circuito comprobantes que fueron emitidos con anterioridad a la versión 9.90.000, asignándoles una [Política de interés por mora](?p=19419).

**¿Cómo puedo dejar de generar mora a facturas que tienen una política de interés asignada?  
**En el caso que no desee calcular mora sobre alguna de las facturas incluidas en la grilla de [Gestión de débitos por mora](?p=21387), desmárquela utilizando la columna "Selección". En el momento de pasar a la siguiente pantalla, el sistema le consulta si desea seguir calculando interés sobre las facturas que desmarcó. Puede decidir que a partir de este momento ya no continúen generando mora en forma automática. En el caso de haber desmarcado varias facturas, se presenta una ventana secundaria donde puede dejar pendientes algunas para que calculen interés en otra ocasión.

__Nota

Tenga en cuenta que siempre puede volver a considerarlas para el cálculo de interés, utilizando el botón Incluir otras facturas.

En el caso de haberle imputado previamente una nota de débito por mora, puede revertir la imputación desde [Imputación de comprobantes](?p=21365), indicando en este momento que ya no desea continuar generando mora sobre la factura de referencia.

**¿Cómo cambio la política de interés asignada originalmente a una factura?  
**Desde el proceso [Gestión de débitos por mora](?p=21387) es posible asignar otra política de interés a la relacionada originalmente a los comprobantes a procesar, para ello ingrese en la solapa Parámetros, en Opciones avanzadas ingrese la política de interés por mora y seleccione el ítem Aplicar a todas las facturas seleccionadas.

__Nota

Tenga en cuenta que esta opción no reemplaza la política originalmente grabada, sólo se utiliza para generar el cálculo de interés.

**¿Es posible tener en cuenta la fecha de los valores con que se efectúa una cobranza para calcular los días de atraso sobre los que corresponde cobrar interés?  
**Tilde la opción Considera la fecha de los valores incluidos en el recibo para el cálculo de los días de atraso, en el proceso [Política de interés por mora](?p=19419). Para más información consulte la ayuda de este proceso, en la que puede encontrar ejemplos de aplicación según las diferentes configuraciones.

**¿Qué información o avisos puedo obtener referida al interés por mora (generado o a generar)?**

  * **Consulta Live de notas de débito generadas por mora**.
  * **Ficha de comprobantes:** puede consultar, en la solapa Vencimientos, información referida al historial de mora relacionado con las cuotas de cada factura.
  * **Ingreso de cobranzas:** puede configurar el sistema para que en el caso de cobrar facturas vencidas, Tango emita un aviso informando que los comprobantes incluídos en la operación generan mora.
  * **Gestión de débitos por mora:** puede utilizar este proceso para consultar el interés que corresponde cobrar a un cliente, o sobre ciertas facturas. Cancele el proceso sin llegar a generar la nota de débito.  
Cuenta con permisos especiales de usuario para habilitar el proceso sólo para consultas o simulaciones.
  * **Detalle del cálculo de interés por mora:** al generar notas de débito por mora desde los procesos [Cobranzas](?p=21323) o [Gestión de débitos por mora](?p=21387) puede consultar la columna "Detalle del cálculo" incluida en el asistente para la generación. Esta columna exhibe un archivo de tipo .PDF con información referida al método de cálculo y datos que dan origen al interés calculado, que puede imprimir o guardar para una posterior consulta.



Una vez generada la nota de débito, puede volver a imprimir el detalle del cálculo accediendo a la ficha Live del comprobante o desde la consulta Notas de débito de interés por mora.

**¿Cómo se realiza el cálculo de impuestos de una nota de débito de interés por mora?  
**Indique la alícuota que se aplicará a las notas de débito a generar desde el proceso [Gestión de débitos por mora](?p=21387). Puede definir un valor por defecto en el proceso Parámetros de Ventas, indicando si desea que sea editable.

__Nota

No es posible tomar todos los impuestos del comprobante de referencia.

En el caso que mi política de interés sea la misma para todos los clientes ¿cómo debo configurar el sistema?  
Defina la política general a utilizar en [Parámetros de Ventas](?p=19401).

**¿Cómo indico que un cliente utiliza una política de interés por mora en particular?  
**Active el parámetro Débitos por mora del proceso [Clientes](?p=19444) y especifique el código de [política de interés por mora](?p=19419) a utilizar. Este código se asigna automáticamente a las facturas en el momento de emitirlas.

**¿Cómo indico que una condición de venta utiliza una política de interés por mora en particular?  
**Active el parámetro Genera débitos por mora en el proceso [Condiciones de venta](?p=19255) y especifique el código de política de interés por mora a utilizar. Este código se asigna automáticamente a las facturas en el momento de emitirlas.

**¿Qué condiciones deben cumplirse para que una factura devengue interés por mora?  
**En el momento de efectuar una factura a un [cliente](?p=19444) que genera débitos por mora, se le asigna automáticamente una política de interés (*), guardando un historial de la tasa definida en el momento de su utilización. Esta es la tasa que se utilizará en el caso que corresponda generar interés sobre ese comprobante.

(*) La asignación de la política al comprobante se realiza teniendo en cuenta el siguiente orden de prioridades: En primer lugar se utiliza la política del cliente, si éste tiene alguna asignada. En segundo lugar se utiliza la política de la [condición de venta](?p=19255), si ésta tiene alguna asignada. En tercer lugar, se utiliza la política definida a nivel general, en [Parámetros de Ventas](?p=19401).

Es importante destacar que debe definir qué [clientes](?p=19444) generan débitos por mora. Puede hacerlo individualmente, o desde el proceso [Asignación masiva de clientes a interés por mora](?p=19209).  
Puede efectuar el cálculo del interés desde [Cobranzas](?p=21323) o seleccionar facturas, en forma masiva, desde el proceso [Gestión de débitos por mora](?p=21387).  
La factura debe estar vencida y la mora calculada debe superar los mínimos establecidos en la [política de interés por mora](?p=19419) que tiene relacionada.  
En el caso de políticas que consideran la fecha de los valores incluidos en los recibos, si los valores exceden la fecha de cobranza es posible que la factura genere mora aún cuando la cuota se haya cobrado al día o anticipada.  
Si indicó que la política efectúa descuentos del total del interés por las cuotas anticipadas, y éstas cuotas se abonan en conjunto con otras que generan mora por cobrarse vencidas, o debido a la fecha diferida de los valores incluidos en la cobranza, es posible realizar una compensación en el cálculo de mora, haciendo un descuento del total a cobrar (*).

(*) Siempre que el total de la nota de débito sea positivo. No es posible generar créditos en concepto de descuentos por pronto pago.

En el caso de políticas cuya base de cálculo sea el Importe cobrado de la cuota vencida la factura debe tener cobranzas efectuadas para generar interés por mora.

Más información:

Tenga en cuenta que las facturas que se generaron anteriormente a la puesta en marcha para la generación de intereses por mora no tienen política asignada y en consecuencia no devengarán interés, aún cuando se cobren vencidas.  
Es posible, sin embargo, asignarles una política y comenzar a generar mora sobre los comprobantes que asi lo requieran, utilizando el proceso Gestión de débitos por mora.

##### Contenidos relacionados

  * [Guía sobre fechas alternativas de vencimiento](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_fechalternat_gv/)

  * [Video sobre interés por mora](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/interesmora_gv_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)
