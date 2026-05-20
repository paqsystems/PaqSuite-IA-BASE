# Datos fijos de la liquidación

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_integrcontabl_cp/?p=13052/

## Contenido

# Datos fijos de la liquidación

Para proceder a la liquidación de haberes, es requerido un conjunto de datos de características comunes a todas las liquidaciones que se confeccionen para cada empleado.

Mediante este proceso se ingresan los datos particulares de cada liquidación, llamados datos fijos de la liquidación, a realizar en una fecha determinada.

##### Principal

Identifique la liquidación determinando el Tipo de liquidación y el Nro. de liquidación, según haya configurado la numeración de liquidaciones en el proceso [Parámetros de Sueldos](?p=13208).

Estado: el dato fijo de una liquidación puede tomar uno de los siguientes estados:

  * Abierta: la liquidación está en condiciones de ser liquidada o reliquidada. Corresponde a la etapa administrativa del proceso de liquidación, pues permite trabajar con las liquidaciones y la emisión de recibos a medida que las liquidaciones son revisadas, si tiene activa la opción Autoriza Liquidaciones en el proceso [Parámetros de Sueldos](?p=13208).
  * Cerrada: indica que su contenido ya puede generar presentaciones legales o depósitos en banco. Corresponde a las tareas posteriores al proceso de liquidación y su asentamiento en los papeles de Sueldos y Contabilidad. Utilícelo a discreción para permitir o inhibir modificaciones, a efectos de inhabilitar o autorizar su pago. No son permitidas las reliquidaciones, salvo retroceso al estado ‘Abierta’.
  * Transferida: es aquel dato fijo ya asentado en Contabilidad.



__Nota

Al modificar el estado del dato fijo a 'Transferida' y solo cuando el mismo no haya sido exportado a contabilidad, se habilita una opción denominada Estado de liquidación sin exportar a contabilidad donde es posible seleccionar entre 'Cambiar el estado a exportado' o 'Conservar el estado actual', este último es el valor defecto al generar la apertura por Excel o API.  


Para más información acerca del estado de una liquidación en particular, consulte el ítem [Estados posibles de una liquidación](?p=13037/#estados-posibles-de-una-liquidacion).

Afecta SICOSS: cuando el estado de la liquidación deja de ser operativo y pasa a Cerrada / Transferida, es posible indicar si se tiene en cuenta en la generación del archivo ASCII al SIAp - SICOSS,ASCII a Libro Sueldo Digital o (ejemplo: podrá excluir aquellas liquidaciones no remunerativas de tickets).

Los datos fijos de liquidaciones de 'Tipo 9-Contribuciones' (que corresponden a a las contribuciones del empleador) también pueden considerarse para generar los datos de 'Aporte adicional OS' e 'Importe adicional OS', cuando en el proceso Datos de empleados para SICOSS existan conceptos parametrizados de 'Tipo 8-Contribución'.  
El Número de orden es utilizado por el sistema para llevar un orden de las liquidaciones y tener un control de los importes acumulados de las mismas, que posteriormente, a la hora de la generación de los archivos de libro sueldo digital se defina el nombre de cada txt y facilite el orden de la subida de este a la página de ARCA. También es utilizado en algunas variables básicas disponibles.

Libro de sueldos digital generado: si está tildado indica que el libro ya fué generado.

Nro. de orden: este número no necesariamente debe ser correlativo, pero es fundamental que se coloque en el campo Nro. de orden el orden real en el que ocurren las liquidaciones en el sistema. Por ejemplo, si hay una liquidación de vacaciones y luego una mensual, es importante que el número de orden de la liquidación de vacaciones sea inferior al número de orden del dato fijo de la liquidación mensual. En cambio, si primero se liquida la mensual y luego la liquidación de vacaciones, la liquidación mensual deberá tener un número de orden inferior al que tiene la liquidación de vacaciones.  
Los valores permitidos son entre '1' y '998'. Y en caso de utilizar libro de sueldo digital este campo será utilizado, junto con la jurisdicción del legajo liquidado, para conformar el número de liquidación para libro de sueldos digital.

__Importante

Tenga en cuenta que, para trabajar con apertura en Excel, los campos “período de liquidación” y “Nro. de orden” no pueden modificar su valor desde el proceso importación de Excel. En caso de editarlo en la planilla e importar, se interpretará como un nuevo registro por ser campos de una clave compleja, parte de una validación estricta del proceso.  
En caso de necesitar modificar el campo de Nro. de orden, puede hacerlo desde la pantalla principal.  


__Nota

Si en el proceso _Parámetros de Sueldos_ usted optó por la opción _Genera historial laboral al cerrar un dato fijo_ , al grabar el cierre de un dato fijo se ejecutará el proceso _Generación de historial laboral_ para los empleados cuya condición esté asociada al tipo de liquidación del dato fijo procesado, tomando el mes/año del dato fijo.

Datos de la liquidación

Fecha: indique la fecha de la liquidación, como referencia. Pueden realizarse varias liquidaciones para una misma fecha, por ejemplo, mensual y aguinaldo. Los informes consideran esta fecha para determinar aquellas liquidaciones dentro de un rango de fechas.

Período: es el liquidado, es decir, mes y año. Este dato establece el cálculo de determinadas variables de fórmula, la obtención de valores sujetos a ganancias y los topes vigentes por el método de lo devengado, la necesidad del cálculo de cantidad de familiares de los legajos, etc.

Desde fecha y Hasta fecha: determinan la pertinencia de los contenidos de la liquidación, respecto de los siguientes ítems:

  * Legajos activos para la liquidación según el rango especificado.
  * Conceptos particulares de legajos según las fechas de vigencia ingresadas.
  * Acumulación de novedades en el rango indicado, para variables de novedades.



Datos del pago

Ingrese la fecha en la que se produce el pago y una descripción aclaratoria.  
La fecha de pago se considera además, en la liquidación del impuesto a las ganancias por el método de lo percibido, para la obtención de valores sujetos a ganancias y los topes vigentes.

Habilitado para el pago: para las liquidaciones con estado 'Cerrada' o 'Transferida', utilice este campo si desea que la liquidación esté disponible para el pago automático, a través del proceso [Generación de archivo ASCII para depósito de haberes](?p=13021).

Impuesto a las ganancias

Topes vigentes: indique si los topes vigentes a considerar para el impuesto a las ganancias corresponden al período de liquidación o a diciembre.

Tablas utilizadas: indica la fecha de los topes vigentes informados en el paso anterior para el impuesto a las ganancias que corresponden al período de liquidación o a diciembre.

Aplica deducciones anuales: tilde esta opción para incorporar a la liquidación aquellas deducciones y/o pagos a cuenta que estén definidos como 'Forma de liquidación anual' en la [Configuración de deducciones](?p=13041). Aquellas que estén definidas como 'Forma de liquidación mensual' se liquidan siempre.

SAC RG 4003/17 Anexo II C: esta opción está activa de manera predeterminada, y se utiliza para que el sistema incremente una doceava parte la ganancia bruta y las retenciones en el momento de liquidar el impuesto a las ganancias, para dar cumplimiento con la RG 4003/17 Anexo II inc. C.

Tipo de SAC: independientemente de que sea una liquidación de tipo '6-Aguinaldo' o no, si liquida un concepto marcado como SAC es necesario informar si es primera cuota o segunda cuota para determinar la exposición del valor liquidado. La opción de tipo de SAC está siempre disponible pero debe utilizarse sólo en los casos en que corresponda a un pago de aguinaldo.

Liquidación anual: esta opción estará habilitada para los casos en que el período sea Diciembre (12/yyyy). Tilde esta opción en caso de querer efectuar la liquidación anual del impuesto a las ganancias.

Se permitirá para dicho período sólo dos datos fijos con la marca de liquidación anual.

Ajuste según promedio anual: al tildar esta opción, el sistema recalculará la situación de bonos por productividad, fallos de caja o similar naturaleza de exento a gravado, o por el contrario de gravado a exento. Además, ajusta situación de SAC de exento a gravado, o por el contrario de gravado a exento, según corresponda.

##### Datos del último depósito

Puede registrar la fecha, el período y el banco correspondientes al depósito de contribuciones que realizó la empresa de la liquidación próxima pasada.  
Para obtener más información acerca de los bancos, consulte el ítem [Bancos](?p=11836) en el manual del módulo Procesos generales.

##### Datos contables

Modelo de asiento y Fecha contable: si genera los asientos contables de las liquidaciones, especifique estos datos.

##### Contenidos relacionados

  * [Configuración de deducciones](https://ayudas.axoft.com/25ar/ayudas/sua/archivos_carp_sua/impuestoganancias_carp_sua/confdeducciones_sua/)

  * [Video sobre liquidación de contribuciones patronales](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/liqcontribpatr_sua_vid/)

  * [Video sobre pago automático de haberes](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/pagoautomhaber_sua_vid/)

  * [Video sobre vacaciones](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/vacaciones_sua_vid/)

  * [Videos sobre asientos contables en Sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/asientocontabl_sua_vid/)

  * [Videos sobre modernización laboral - Cambios en Sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/modernlaboral_sua_vid/)
