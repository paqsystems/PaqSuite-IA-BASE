# Guía sobre la integración de Activo Fijo con otros módulos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_ivasimple_gv/?p=5938/

## Contenido

# Guía sobre la integración de Activo Fijo con otros módulos

El módulo Activo Fijo le permite administrar de la manera más eficiente los bienes de su empresa. Su integración con Compras le permite dar de alta los bienes en forma automática y a su valor correspondiente. Además, podrá generar los asientos contables de activación, depreciaciones, ajuste por inflación, revalúos y bajas para ser incorporados al módulo Contabilidad.

A continuación se detallan los pasos y el orden de configuración a seguir para implementar la integración con el módulo de Activo Fijo como así también la administración de los bienes.

##### Puesta en marcha de la integración de Activo Fijo

Para implementar la integración con los módulos Stock y Compras, siga los siguientes pasos:

  * Configuración de parámetros de Activo Fijo para la codificación de bienes.
  * Definición de los artículos que representan bienes.
  * Definición de los conceptos de compras que representen gastos para bienes.
  * Configuración de los accesos a bienes desde el administrador de roles.



A continuación se detallan cada uno de esos puntos.

**Parámetros de Activo Fijo para la codificación de bienes**

Parametrice cómo desea codificar los bienes desde el proceso de [Parámetros de Activo Fijo](?p=5948).  
Esta configuración servirá para el alta automática de bienes desde el módulo de Compras, como así también para la importación de bienes desde planilla Excel.  
Puede seleccionar una codificación manual o automática.  
Para más información consulte [Codificación de bienes en el proceso de Parámetros de Activo Fijo](?p=5948#codifbienes).

**Definición de los artículos que representan bienes**

Defina qué artículos representan bienes para su empresa, desde los procesos [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) y [Artículos con Escalas](?p=17094), independientemente del perfil del artículo, seleccionando la opción Identificar el Artículo como un Bien.  
Es posible indicar qué [Tipo de bien](?p=5955) representa, a fines de asignar valores por defecto al momento de crear los bienes en el módulo de Activo Fijo.  
Para más información vea el siguiente ejemplo o consulte el tópico [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st).  
Como ejemplo de artículos identificados como bienes de uso se pueden definir:

  * PC
  * Automóvil
  * Maquinaria



Al ingresar una factura de compras podrá crear los bienes en forma automática teniendo en cuenta las cantidades y precios de los artículos identificados como bienes.  
Para más información sobre la creación automática de bienes consulte [Ingreso de factura de artículos](?p=5901).

**Definición de los conceptos de Compras que representan gastos para bienes**

Defina qué [Conceptos de compra](?p=14626) (opcional) representan para su empresa otros gastos que corresponden a la puesta en marcha de bienes.  
Son ejemplos de gastos: fletes, instalación y otros gastos como seguros, honorarios del despachante de aduana, trámites en el registro, costos de la función de compra, construcción de plataformas, el montaje, la puesta a punto, ensayos de puesta en marcha, entrenamiento del personal, etc.  
Para más información sobre la afectación de gastos a los datos de origen de bienes consulte [Ingreso de factura de conceptos](?p=5901).

Más información:

Es importante aclarar que la integración con estos módulos es opcional. Usted puede crear los bienes en forma manual e imputarles gastos desde el módulo de Activo Fijo.  
En el caso que se realice en forma automática desde la integración con Stock y Compras, el comprobante quedará referenciado en el historial de los datos de origen del bien.

**Parametrización de accesos a bienes desde el Administrador de roles**

Parametrice desde el [Administrador de roles](?p=9113), disponible en el módulo Administrador, el acceso a la administración de los Bienes, desde Activo Fijo como también desde el módulo de Compras.

Desde el módulo de Activo Fijo:

  * [Bienes](?p=5033)



Desde el módulo de Compras:

  * [Alta automática de bienes](?p=5901) para Activo Fijo
  * [Alta automática de gastos para bienes](?p=5902) de Activo Fijo



Más información:

En el caso que para un rol desee crear bienes sólo desde los comprobantes ingresados en el módulo de Compras, no deberá dar acceso a Bienes y sí habilitar el acceso a los permisos de Alta automática de bienes para Activo Fijo y Alta automática de gastos para bienes de Activo Fijo. 

##### Detalle del circuito de integración de Activo Fijo

Para comprender la integración de Activo Fijo con los otros módulos puede consultar el siguiente gráfico.

A través de los siguientes links puede profundizar sobre cada uno de los puntos:

[Integración con el módulo Stock](?p=5938/#integracion-de-activo-fijo-con-stock):

  * Integración de artículos con Activo Fijo



[Integración con el módulo Compras](?p=5938/#integracion-de-activo-fijo-con-compras):

  * Integración de gastos de compras con el módulo Activo Fijo
  * Ingreso de factura de artículos
  * Ingreso de factura de conceptos



[Integración con Procesos generales](?p=5938/#integracion-con-procesos-generales):

  * Herramientas para integración contable
  * Parámetros generales
  * Ingreso de datos contables



[Integración con Contabilidad](?p=5938/#integracion-con-contabilidad):

  * Modelos de asientos de Activo Fijo
  * Generación y exportación de asientos a Contabilidad
  * Importación de asientos



**Activo Fijo:**

  * **[Bienes](?p=5033)** : registre los datos y parámetros de los bienes para Activo Fijo.
  * [**Registración de movimientos**](?p=6749): desde aquí usted puede registrar en el sistema todas las variaciones que puede sufrir el bien a lo largo del tiempo.



###### Integración de Activo Fijo con Stock

En el módulo **Activo Fijo** es posible crear automáticamente bienes referidos a su inventario.

**Integración de artículos con el módulo Activo Fijo**

Si su sistema posee el módulo de Activo Fijo, es posible (opcionalmente) crear automáticamente bienes en el módulo de Activo Fijo, cuando en el comprobante registrado se especifican renglones de artículos que estén identificados como bienes.  
El alta automática se puede realizar desde la registración de comprobantes de los procesos de:

  * Factura-Remito, factura, factura de importación
  * Nota de débito



Los bienes creados, quedan registrados con los datos de origen según la factura o nota de débito ingresada en Compras.

Más información:

Los bienes que se dan de alta quedarán pendientes de activar. La [activación](?p=6749) deberá realizarse con posterioridad desde el módulo Activo Fijo, utilizando un tipo de comprobante para tal fin.

Al finalizar el ingreso del comprobante de factura / nota de débito, se mostrará un mensaje con la leyenda "Existen Artículos identificados como bienes para el módulo Activo Fijo. ¿Desea crearlos automáticamente en este momento con la registración del Comprobante".

  * En caso de no realizar el alta automática, puede igualmente crear los bienes en forma manual desde el proceso [Bienes](?p=5033) en el módulo de Activo Fijo, relacionando el bien con el comprobante existente en Compras.
  * En caso de confirmar el alta automática, se abre una nueva pantalla con los artículos contenidos en el comprobante que están identificados como bienes, teniendo en cuenta las cantidades y precios de los artículos identificados como bienes. Por cada unidad de producto comprada del artículo, es posible crear un determinado bien (según la cantidad especificada para el artículo en el renglón del comprobante).



Para más información sobre la creación automática de bienes consulte [Ingreso de factura de artículos](?p=5901).

###### Integración de Activo Fijo con Compras

De forma similar que sucede con los artículos, usted puede definir conceptos de gastos.

**Integración de gastos de compras con el módulo de Activo Fijo**

**Para Activo Fijo**

De forma similiar que para los artículos, defina opcionalmente qué conceptos representan para su empresa otros gastos que corresponden a la puesta en marcha de bienes, seleccionando la opción Identificar el concepto como un gasto para la puesta en marcha de bienes.

__Nota

Son ejemplos de gastos: instalación y otros gastos como seguros, honorarios del despachante de aduana, trámites en el registro, costos de la función de compra, construcción de plataformas, el montaje, la puesta a punto, ensayos de puesta en marcha, entrenamiento del personal, etc.

Si su sistema posee el módulo de Activo Fijo, es posible (opcionalmente) asociar automáticamente importes de comprobantes de conceptos a bienes existentes en el módulo de Activo Fijo, cuando en el comprobante registrado se especifican renglones de conceptos que estén identificados.  
El alta automática se puede realizar desde la registración de comprobantes de los procesos de:

  * Factura de conceptos
  * Nota de débito de conceptos



Los importes de estos conceptos, quedan referenciados en los datos de origen de los bienes afectados, según la factura o nota de débito ingresada en Compras.

__Nota

Los importes de comprobantes de conceptos de compras pueden afectarse a bienes que están pendientes de activar en el módulo **Activo Fijo**.

Al finalizar el ingreso del comprobante de factura / nota de débito, se mostrará el siguiente mensaje:  
_"Existen conceptos identificados como gastos para la puesta en marcha de bienes en el módulo**Activo Fijo**. ¿Desea afectar los gastos a los datos de origen de los bienes en este momento con la registración del comprobante?"  
_En caso de no realizar la afectación de gastos puede realizar la distribución y afectación a los bienes en forma manual desde el proceso [Bienes](?p=5033) en el módulo de Activo Fijo, relacionando el bien con el comprobante existente en Compras.  
En caso de confirmar la afectación de gastos se abrirá una nueva pantalla con los conceptos contenidos en el comprobante que estén identificados para Activo Fijo.  
Se podrá afectar el 100% o una parte del gasto a uno o varios bienes existentes en el módulo de Activo Fijo.

**Ingreso de factura de artículos**

Opcionalmente es posible crear automáticamente bienes en el módulo **Activo Fijo** , cuando en el comprobante registrado se especifican renglones de artículos que estén identificados como bienes.  
El alta automática se puede realizar desde la registración de comprobantes de los procesos de:

  * Factura-remito, factura, factura de importación.
  * Nota de débito.



**En caso de confirmar el alta automática** , se abrirá una nueva pantalla con los artículos contenidos en el comprobante que estén identificados como bienes. Se mostrará y podrá generar por cada unidad de producto comprada del artículo, un determinado bien (según la cantidad especificada para el artículo en el renglón del comprobante).

**Otros datos necesarios para el alta del bien son los siguientes:**

Los datos del comprobante de compras (Código y Razón Social del Proveedor, Tipo y número del comprobante, Fecha de compra) quedan registrados en la solapa de [Origen del bien](?p=5033) disponible en la ficha del Bien del módulo **Activo Fijo**.

_**Fecha de alta:** _se registra la fecha de sistema al momento de la carga del comprobante.

_**Fecha de compra:** _corresponde a la fecha de emisión del comprobante de compras.

_**Moneda del bien, cotización y valor del bien:**_ la moneda de registración del comprobante de compras determina la moneda del bien dado de alta. En caso que el comprobante de Compras se haya registrado en moneda extranjera, en el bien se guardará la cotización en relación a la moneda corriente. El valor del bien quedará expresado siempre en la moneda corriente (es decir, en la Moneda base definida en el módulo **Procesos Generales**.

_**Genera:** _se proponen tantos bienes como cantidades se haya indicado en el renglón del comprobante para cada artículo. Se podrá marcar o desmarcar los bienes que correspondan crear en el módulo **Activo Fijo**.

_**Código del bien:** _es un código obligatorio con el que se identificará unívocamente el bien creado en **Activo Fijo**. Se puede especificar manualmente al momento de realizar el alta automática de bienes, como así también es posible generarlo automáticamente según se haya indicado en los [Parámetros de Activo Fijo](?p=5948).

_**Descripción del bien:** _por defecto se propone la descripción del artículo. En caso que no se modifiquen las descripciones, todos los bienes creados tendrán la misma descripción, y podrán modificarse desde el ítem Bienes en el módulo **Activo Fijo**.

_**Tipo de bien:**_ se asigna por defecto el tipo de bien indicado para el artículo. Los bienes creados conservan por defecto los siguientes datos especificados en el tipo de bien:  
Características para depreciación: se parametriza si el bien está habilitado para el cálculo de depreciación o no, y en caso de corresponder, los valores para el método de depreciación, unidad para la vida útil, vida útil, el método de depreciación, Porcentaje depreciable, Frecuencia y Valor fin vida útil.  
Cuentas contables para movimientos: cuenta del bien, cuenta de compra, cuenta depreciación, cuenta depreciación extraordinaria, cuenta depreciación acumulada, cuenta para mejoras, cuenta revalúo, cuenta de baja, cuenta resultado ajuste, cuenta resultado por tenencia.  
Identificaciones adicionales: se asignan al bien las características comunes indicadas para el tipo de bien. Puede especificar cada valor particular referente al bien, en forma posterior al alta automática, desde el item [Bienes](?p=5033) en el módulo **Activo Fijo**.

Número de serie: este dato es único por cada bien. Es posible modificar o cargar las series en caso que en los Parámetros de Stock no se haya parametrizado un Ingreso de Series Obligatorio, caso contrario se visualizan las series indicadas en el comprobante para los artículos definidos con 'Lleva serie'.

Costo: por defecto se propone como importe que afecta al valor de origen del bien, el precio neto del artículo para el comprobante. Este importe puede modificarse para el alta de bienes. En caso de indicarse otro importe, en el item [Bienes](?p=5033) en el módulo **Activo Fijo** , se visualizará el Importe del renglón original para el comprobante, y el Importe indicado para afectar el valor de origen del bien. El importe está expresado en la moneda del comprobante.

**Ejemplo...**

Factura de compra  
Artículo 1 código 0200200031 cantidad 3 unidades (identificado como bien)  
Artículo 2 código 0200200032 cantidad 2 unidades (identificado como bien)  
Artículo 3 código 0200200033 cantidad 1 unidad (no representa un bien)

En este ejemplo, la codificación automática de bienes es según el código de artículo, con "-" como separador y completando con ceros a izquierda.  
Al confirmar el alta automática de bienes luego del ingreso de la factura de compras, se sugiere el alta de los siguientes bienes para el módulo de Activo Fijo, con las siguientes características:

Artículo 1 código 0200200031: se sugiere la creación de 3 códigos de bienes:  
\- código bien 0200200031-00001  
\- código bien 0200200031-00002  
\- código bien 0200200031-00003

Artículo 2 código 0200200032: se sugiere la creación de 2 códigos de bienes:  
\- código bien 0200200032-00001  
\- código bien 0200200032-00002

**Ingreso de factura de conceptos**

Opcionalmente es posible asociar automáticamente importes de comprobantes de conceptos a bienes existentes en el módulo Activo Fijo, cuando en el comprobante registrado se especifican renglones de conceptos que estén identificados.

El alta automática se puede realizar desde la registración de comprobantes de los procesos de:

  * Factura de conceptos
  * Nota de débito de conceptos



__Nota

Mediante esta opción no se realiza creación de bienes; es posible realizar una asociación de importes de comprobantes para la puesta en marcha de bienes.  
Indique mediante la opción _Considera el importe del gasto para el cálculo del valor de origen_ si el importe imputado a cada bien incrementa el valor de origen de cada bien.  
Los bienes posibles de seleccionar para la afectación de gastos son aquellos existentes en el módulo **Activo Fijo** (ya sea se hayan creado desde [Bienes](?p=5033) en **Activo Fijo** o bien desde el [Alta automática de bienes para Activo Fijo](?p=5901)), siempre y cuando estén pendientes de activar.  


En caso de confirmar la afectación de gastos, se abrirá una nueva pantalla con los conceptos contenidos en el comprobante que estén identificados para **Activo Fijo**.

Se podrá afectar el 100% o una parte del gasto a uno o varios bienes existentes en el módulo **Activo Fijo**.

Moneda del bien, cotización y valor del bien: la moneda de registración del comprobante de Compras determina la moneda del bien dado de alta. En caso que el comprobante de Compras se haya registrado en moneda extranjera, en el bien se guardará la cotización en relación a la moneda corriente. El valor del bien quedará expresado siempre en la moneda corriente (es decir, en la [Moneda base](?p=11956) definida en el módulo Procesos generales).

Otros datos necesarios para la distribución de gastos a bienes son los siguientes:

Datos del comprobante de compras (Código y Razón Social del Proveedor, Tipo y número del comprobante, Fecha de compra, Concepto de compra) quedan registrados en la solapa de [Origen del bien](?p=5033#origenbien) disponible en la ficha de [Bienes](?p=5033) del módulo Activo Fijo.

Código del bien: seleccione los bienes pendientes de activar, que desea afectar los importes de los conceptos de compras.

Porcentaje e Importe: para cada bien indique el porcentaje o el importe de participación que corresponde del total del importe del concepto de compras.  
Si se indica el 100% significa que la totalidad del concepto se afectará al bien seleccionado.  
Por defecto se propone el 100% del precio neto del concepto del comprobante como importe que afecta a los datos de origen del bien. Este importe puede modificarse.  
La suma total de los porcentajes asignados no debe superar el 100% para cada concepto de compras.  
Si el porcentaje es inferior al 100%, quedará un porcentaje restante pendiente de imputación (sin asignar a ningún bien). Este porcentaje pendiente de imputación podrá afectarse con posterioridad al alta automática de gastos, seleccionando el comprobante de compras desde la solapa [Origen del bien](?p=5033#origenbien) disponible en el ítem [Bienes](?p=5033) del módulo Activo Fijo, y se visualizará en este caso el Importe del renglón original para el comprobante y el Importe afectado a los datos de origen del bien.

El importe está expresado en la moneda del comprobante.

Más información:

Cuando en el mismo comprobante existen varios conceptos afectados al módulo Activo Fijo, para agilizar la distribución, es posible seleccionar -previamente a la distribución propiamente dicha- los bienes que se desean afectar, indicando para cada uno un porcentaje determinado por defecto.  
Luego presione el botón "Completar distribución de gastos…" y los importes de los conceptos de compras se distribuirán con la misma proporción entre los bienes indicados. Luego es posible modificar la distribución de gastos a generar por bien. 

**Ejemplo...**

Factura de conceptos  
Concepto HONORARIOS  
Importe = 500  
(afectado a Activo Fijo)  
Concepto SEGURO  
Importe = 600  
(afectado a Activo Fijo)

Al confirmar el alta automática de gastos para bienes, luego del ingreso de la factura de compras, se realiza la siguiente distribución:  
Concepto HONORARIOS (Importe = 500):  
código bien 0200200031-00001 90% = 450  
código bien 0200200031-00002 10% = 50

Concepto SEGURO (Importe = 600):  
código bien 0200200032-00001 90% = 540  
código bien 0200200032-00002 10% = 60

###### Integración con Procesos generales

Para una integración con el módulo Procesos generales, tenga en cuenta los siguientes puntos.

  * [Herramientas para integración contable](?p=11936)
  * [Parámetros contables](?p=11964)



**Ingreso de datos contables**

Para el ingreso de datos contables, ya sea para el bien, para el tipo de bien o para el modelo de asiento, usted debe definir las cuentas contables, los tipos de auxiliares y los ejercicios contables desde el módulo Procesos generales.

  * [Cuentas contables](?p=11850)
  * [Tipos de auxiliares](?p=11835)
  * Ejercicios: invoque esta opción para especificar los datos propios de cada ejercicio contable de la empresa.

Número de ejercicio: es un número arbitrario, mayor a cero. El sistema valida que no existan números repetidos de ejercicio. Este dato es obligatorio y puede ingresar hasta 9 dígitos.  
Si se trata de un nuevo ejercicio, haga clic en el botón correspondiente para obtener el próximo número de ejercicio a aplicar.

Vigencia del ejercicio: ingrese el rango Desde fecha - Hasta fecha que marca la duración del ejercicio. Este dato es obligatorio. El sistema valida que no haya superposiciones de fechas entre ejercicios distintos.

Estado: los estados posibles de un ejercicio son: 'Abierto' o 'Cerrado'. Por defecto, se propone el estado 'Abierto'. Este estado corresponde al estado propiamente dicho en que se encuentra el ejercicio.

Habilitado: este campo se exhibe tildado para indicar que el ejercicio está habilitado para la carga movimientos. Si corresponde, desmarque este parámetro para inhabilitar el ejercicio. Puede utilizar este dato para inhabilitar la carga de movimientos en forma temporal, para un ejercicio que se encuentra con estado 'Abierto' Luego, puede volver a cambiar el valor a 'Habilitado'.

Si usted cuenta con el módulo **Tango Astor Contabilidad** esta información será compartida por ambos módulos.

__Nota

El sistema valida que el ejercio se encuentre 'Abierto' para la fecha del movimiento que se desea agregar, modificar, anular o eliminar

[Ejercicios](javascript:;)

[Ver menos...](javascript:;)




###### Integración con Contabilidad

Para una integración con el módulo **Contabilidad** , tenga en cuenta los [modelos de asientos de Activo Fijo](?p=5933).

**Generación y exportación de asientos a Contabilidad**

Si en [Parámetros de Activo Fijo](?p=5948) se activa la marca Genera asiento en el ingreso de movimientos usted tiene la posibilidad de ir consultando el asiento a medida que ingresa los movimientos de bienes desde el proceso de [Registración de movimientos](?p=6749), mediante el ícono Asiento.

Si este parámetro está desactivado no se puede consultar el asiento contable hasta que se genere el asiento desde el proceso de [Generación de asientos contables de Activo Fijo](?p=5914).  
Para mayor información sobre los asientos que corresponden a los movimientos de Activo Fijo consulte la ayuda [Datos contables del movimiento](?p=6749).  
Una vez que los movimientos de Activo Fijo estén Contabilizados (es decir, se haya generado un asiento contable o "mini-asiento" dentro del módulo de Activo Fijo, por cualquiera de ambos circuitos) es posible realizar la [Exportación de asientos contables de Activo Fijo](?p=5913) al módulo **Contabilidad**. Luego de realizada la exportación, los asientos de los movimientos quedan con el estado de 'Transferido'.  
Los asientos que intervienen en una exportación quedan bajo la referencia de un número de lote de exportación. Puede consultar los lotes de exportación generados desde el módulo Activo Fijo mediante el proceso [Lotes contables generados](?p=5932).

Tenga en cuenta, además, los siguientes temas:

  * [Generación de asientos contables de Activo Fijo](?p=5914)
  * [Exportación de asientos contables de Activo Fijo](?p=5913)
  * [Lotes contables generados](?p=5932)



**Importación de asientos**

Mediante este proceso es posible importar a la contabilidad los asientos que corresponden a la contabilización de movimientos del módulo de Activo Fijo, según el proceso de [Exportación de asientos contables de Activo Fijo](?p=5913).  
La información puede provenir de un sistema Tango o externo.  
Los asientos importados quedan aceptados con el origen de Activo Fijo.  
Para mayor información consulte [Importación de asientos contables](?p=9789).  
Los asientos aceptados resultantes de efectuar la importación de asientos quedan bajo la referencia de un número de lote de recepción o importación. Puede consultar los lotes de importación recibidos desde el módulo Contabilidad mediante el proceso [Lotes contables recibidos](?p=9800).  
Desde el asiento contable, consulte [Ficha Detalle de asientos contables](?p=9755) a fines de conocer el origen de los movimientos de Activo Fijo que corresponden al asiento contable importado.

##### Contenidos relacionados

  * [Videos sobre bienes de uso](https://ayudas.axoft.com/24ar/videos/afa_carp_vid/bienes_afa_vid/)
