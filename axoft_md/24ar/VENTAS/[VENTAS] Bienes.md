# Bienes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=5033/

## Contenido

# Bienes

Registre los datos y parámetros de los bienes para **Activo Fijo**.

La ventana del proceso se organiza sus datos en las siguientes solapas:

  * Principal para bienes, con los datos de identificación, clasificación, registración e inventario de bienes.
  * Origen del bien, con los datos de los comprobantes compras.
  * Valoraciones, con los datos en la moneda del bien y de los tipos de valoraciones asociados al bien y los parámetros necesarios para el cálculo de depreciación y de ajuste por inflación, si correspondiera.
  * Cuentas contables, con la configuración de cuentas contables para la contabilización de la registración de movimientos del bien.
  * Datos complementarios, con los datos del seguro y otras identificaciones adicionales propias del bien, si correspondiera.
  * Agrupaciones auxiliares, se indican las agrupaciones obligatorias y/o únicas para agrupar bienes.
  * Observaciones, con el comentario o texto que haya ingresado, en forma opcional, para el bien.



##### Principal

Complete los datos que identifican al bien:

_**Código:**_ ingrese un código que identifique el bien. Su ingreso es obligatorio.

Si usted activa la codificación automática de bienes en [Parámetros de Activo Fijo](?p=5948), este campo muestra deshabilitado y se completa en forma automática.

_**Descripción:** _si lo desea, ingrese una referencia o texto para el código del bien. Su ingreso es opcional.

_**Descripción detallada:**_ para ingresar más detalles del bien. Su ingreso es opcional.

Complete los datos que permiten clasificar al bien:

_**Rubro:**_ seleccione el rubro asociado al bien. Su ingreso es obligatorio.

_**Tipo de bien: **_seleccione el tipo de bien asociado al bien. Su ingreso es obligatorio.

_**Bien principal:** _seleccione el bien principal asociado al bien. Su ingreso es opcional.

_**Estado:**_ seleccione el estado asociado al bien. Su ingreso es opcional.

Complete los datos que permiten registrar el bien:

_**Fecha de alta:**_ este campo lo completa el sistema de manera automática.

_**Fecha de compra:** _por defecto se propone la fecha del día, pudiendo modificarla. Su ingreso es obligatorio.

_**Fecha de activación:**_ si se trata de un bien nuevo no complete este campo, pero complete esta fecha si se trata de un bien con carga inicial. El sistema controla que la fecha de activación sea mayor o igual a la fecha de compra del bien.

_**Fecha de baja:** _si se trata de un bien nuevo no complete este campo, en cambio, complételo si se trata de un bien con carga inicial. El sistema controla que la fecha de baja sea mayor o igual a la fecha de activación del bien.

_**Fecha de desafectación:** _si se trata de un bien nuevo no complete este campo, en cambio, complételo si se trata de un bien con carga inicial. El sistema controla que la fecha de desafectación sea mayor o igual a la fecha de activación del bien.

Complete los datos de inventario del bien:

_**Número de serie:** _ingrese el número de serie que permite identificar al bien para el mismo artículo asociado .Su ingreso es opcional.

_**Ubicación:** _seleccione la ubicación real (física) donde se encuentra el bien. Su ingreso es opcional.

_**Departamento:**_ seleccione el departamento de la empresa al que se afectará el bien. Su ingreso es opcional.

_**Responsable:**_ seleccione el responsable que tendrá a su cargo el bien. Su ingreso es opcional.

##### Origen del bien

En esta solapa usted puede especificar el origen del bien, puede optar por informar si el origen del bien proviene de 'Datos de compra' o del 'Valor contable'.

  * Por defecto está activa la opción 'Valor contable' esto significa que el valor del bien proviene del balance contable o del valor de libros.
  * Si selecciona la opción 'Datos de la compra', se habilita la grilla para ingresar los comprobantes de compras del bien.



Usted puede ingresar los comprobantes en forma 'Manual' o 'Automática'

Si ingresa la información en forma 'Manual' se habilitan las siguientes columnas de la grilla:

_**Proveedor:** _es un dato opcional, puede optar entre seleccionar un proveedor ya existente o ingresar un nuevo proveedor.

_**Comprobante de compra: **_es un dato obligatorio, puede ingresar el tipo de comprobante, la letra, la sucursal y el nro de comprobante. Por ejemplo: FAC A0001 - 00000564.

_**Fecha: **_es un dato opcional, corresponde a la fecha del comprobante de compra.

_**Moneda: **_es un dato opcional, corresponde a la moneda del comprobante de compra. Si desea informar el importe del comprobante es necesario informar este campo.

_**Cotización:** _si la moneda del comprobante de compra es distinta a la moneda base configurada en el módulo Global, se habilita este campo para que pueda ingresar la cotización de la moneda. Si desea informar el importe del comprobante es necesario informar este campo.

_**Importe: **_es un dato opcional.

_**Artículo: **_deberá definir si se trata de un artículo o de un concepto de gasto. Sólo podrá haber un renglón de artículo por bien.

_**Renglón: **_es un valor obligatorio y será único al asociar más de una vez el mismo comprobante de compras.

Si usted optó por asociar comprobantes de compras en forma 'Automática':

Haciendo clic sobre el botón "..." de la columna "Comprobante de compra" puede acceder a la siguiente pan

talla para poder consultar comprobantes del módulo **Compras**.

En esta consulta se pueden visualizar todos los comprobantes con importes pendientes o con cantidades pendientes de asociar a bienes. Para ello tiene que habilitar los artículos en el módulo **Stock **y conceptos en el módulo **Compras **que afectan al módulo **Activo Fijo**.

Seleccione un renglón de la consulta de comprobantes y haciendo doble clic o presionando "Aceptar" se asociará automáticamente el comprobante al bien, completándose la siguiente información: _Proveedor, Comprobante de compra, Fecha, Moneda, Cotización, Importe renglón, Importe, Importe moneda base, Artículo, Concepto_ y _Renglón_.

Si se trata de un artículo asociado, en la columna "Importe" se muestra el precio unitario del renglón. Si el importe del comprobante de compra del artículo asociado posee algún costo financiero incluido usted puede corregir el costo del artículo editando la columna "Importe". El sistema controla que no pueda ingresar un importe mayor al importe del renglón.

Si se trata de un concepto de compra, en la columna "Importe" se muestra el importe total del renglón. Si el importe del comprobante de compra del concepto se va a distribuir entre más de un bien, usted puede modificar el valor de la columna "Importe".

Si usted seleccionó la opción _Datos de la compra_ , ya sea 'Manual' o 'Automática', se muestra el total del importe en moneda base. Al pasar a la solapa de Valoraciones y al completar la moneda del bien, el sistema propone por defecto este total calculado.

__Nota

Es importante aclarar que si su licencia posee el módulo **Activo Fijo** , la creación de bienes y la asociación de comprobantes a la ficha de origen del bien, puede generarse automáticamente desde el módulo **Compras** , junto con el ingreso de facturas y notas de débito. Los bienes se crearán según los renglones de artículos identificados como bienes para el módulo **Activo Fijo** , como así también la asociación de los gastos a bienes pendientes de activar. Para más información consulte la [Guía sobre la integración de Activo Fijo con otros módulos](?p=5938).

##### Valoraciones

En esta solapa usted puede informar los valores del bien según su moneda y según los tipos de valoración asociados al bien.

Moneda: seleccione la moneda del bien, este valor es obligatorio y dependerá del tipo de valoración configurada para contabilizar asientos.

Cotización: si la moneda seleccionada es distinta a la moneda base definida en el módulo **Procesos Generales** , debe ingresar la cotización para la moneda, en este caso será un valor obligatorio.

Valor: si usted informó para el bien 'Datos de la compra', el sistema propone automáticamente el total del importe en moneda base de la grilla de la solapa 'Origen bien', calculando el valor según la moneda seleccionada y la cotización ingresada para el bien. Usted puede modificar este valor.

Carga inicial: en caso de querer informar saldos iniciales para el bien, deberá informar la fecha de activación del bien, de esta forma usted puede marcar esta opción para ingresar los valores de las columnas de la grilla de valoraciones: "Origen", "Vida útil residual" y "Depreciación acumulada".

Fecha saldo inicial: este valor no puede modificarse, se completará en forma automática en el momento de ingresar el movimiento de Activación, que se puede hacer al grabar el bien o luego desde la [Registración del movimientos](registracionmovimientos_afa). Deberá parametrizar previamente en [Parámetros de Activo Fijo](?p=5948), los datos referidos a puesta en marca, como ser la fecha carga inicial y el tipo de movimiento para carga inicial.

**Datos referidos a las valoraciones del bien:**

Si posee tipos de valoración con el parámetro activo 'Valoración defecto', esta grilla se completará automáticamente con los datos del tipo de valoración y los datos parametrizados para el tipo de bien.

En esta grilla puede asociar hasta 3 tipos de valoración por bien. Es obligatorio para el bien tener al menos un tipo de valoración asociado

Valoración: es un valor obligatorio, muestra el tipo de valoración y puede modificarse.

Moneda: muestra la moneda del tipo de valoración y no puede modificarse, significa que todos los valores informados para la valoración del bien están expresados en esta moneda.

Cotización: si el tipo de valoración tiene definido una moneda distinta a la moneda base se habilita esta columna y su ingreso es obligatorio, puede modificarse. Por defecto propone la cotización para el tipo de cotización de la moneda del tipo de valoración y para la fecha de alta del bien.

**Valores del bien que se pueden informar:**

Origen: este campo se habilita si está activado el parámetro de _Carga inicial_ y por defecto propone el valor de la moneda del bien convertido a la moneda del tipo de valoración.

Mercado: puede ingresar el valor de referencia del bien de acuerdo a su valor en el mercado. Este valor es opcional.

Recupero: este valor es opcional, corresponde al valor que se estima que el bien tendrá al finalizar su utilización. Usted puede informar un valor o puede informar un porcentaje depreciable del valor del bien.

__Nota

Una vez registrado el movimiento de activación, los valores de estos campos no pueden ser agregados o modificados.

**Parámetros del bien referidos a la depreciación del bien:**

Deprecia: este campo se habilita siempre y toma el valor por defecto del tipo de bien, puede modificarse. Si está activado este parámetro se habilitan todas las columnas relacionadas con el cálculo de depreciación que están a continuación de esta.

Criterio: este campo se habilita si está activado el parámetro Deprecia, por defecto propone el criterio 'Alta', puede modifarse. Las opciones habilitadas por el sistema son: 'Alta' o 'Baja'. Este valor es obligatorio.

Método: este campo se habilita si está activado el parámetro _Deprecia _y toma el valor por defecto del tipo de bien, puede modificarse. Este valor es obligatorio.

Frecuencia: este campo se habilita si está activado el parámetro _Deprecia _y toma el valor por defecto del tipo de bien, puede modificarse. Los valores posibles son: 'Anual', 'Bimestral', 'Cuatrimestral', 'Mensual', 'Semestral' o 'Trimestral'. Este valor es obligatorio.

Unidad vida útil: este campo se habilita si está activado el parámetro _Deprecia _y el método de depreciación corresponde al método 'Lineal'. Por defecto toma el valor para el tipo de bien. Las unidades posibles habilitadas por el sistema son: 'Años' o 'Meses'.

Vida útil: este campo se habilita si está activado el parámetro _Deprecia _y el método de depreciación corresponde al método 'Lineal'. Por defecto toma el valor para el tipo de bien.

Vida útil residual: este campo se habilita si está activado el parámetro _Deprecia_ , el método de depreciación corresponde al método 'Lineal' y además está activado el parámetro _Carga inicial_. Por defecto toma el valor para el tipo de bien para la vida útil. Puede modificarse.

Depreciación acumulada: este campo se habilita si está activado el parámetro _Deprecia _y si está activado el parámetro _Carga inicial_. Para poder ingresar un valor el sistema valida que la vida útil sea distinta a la vida útil residual para el caso que el método seleccionado sea 'Lineal' y valida que la cantidad sea distinta para la cantidad residual para el caso que el método seleccionado sea 'Por capacidad de producción'.

**Parámetros del bien referidos al ajuste por inflación:**

Afecta: este campo se habilita, por defecto está desactivado.

Indice: este campo se habilita si está activado el parámetro _Afecta_ , por defecto propone el índice del tipo de valoración, puede modificarse. Este valor es obligatorio.

Si usted seleccionó para alguna valoración, el método de depreciación interno 'Por capacidad de producción' se habilitan los campos que están situados debajo de la grilla de valoraciones.

Informa capacidad de producción: este parámetro se activa cuando alguna de las valoraciones asociadas al bien tienen la marca 'Deprecia' y además utilizan un método interno de depreciación 'Por capacidad de producción'. No puede modificarse.

Unidad de medida: este parámetro se habilita cuando se activa la opción 'Informa capacidad de producción'. Usted puede seleccionar la unidad de medida de producción para el bien. Es un valor obligatorio.

Cantidad: este parámetro este parámetro se habilita cuando se activa la opción 'Informa capacidad de producción', ingrese la capacidad total de producción del bien. Es un valor obligatorio.

Cantidad residual: este parámetro este parámetro se habilita cuando se activa la opción 'Informa capacidad de producción' y además está activo el casillero _Carga inicial_ , ingrese la capacidad residual de producción del bien a la fecha del saldo inicial. Es un valor obligatorio.

**Saldos por tipo de valoración:**

En la parte inferior de esta solapa se muestra una consulta de saldos por tipo de valoración.

A continuación de detallan algunas características de la consulta:

  * Estos campos no son editables.
  * Los saldos están expresados en la moneda del tipo de valoración.
  * Si el bien y el tipo de valoración no están afectados por ajuste por inflación el valor histórico será igual al valor ajustado.
  * Cargando el movimiento de Activación usted puede empezar a ver los saldos del bien por tipo de valoración.
  * Sólo puede visualizar los saldos para el tipo de valoración asociado al bien.
  * Haciendo clic sobre el icono de la lupa usted puede acceder al detalle de cada saldo para ver todos los movimientos que afectan el saldo del bien.



Valor del bien: este valor está compuesto por todos los movimientos que afectan el valor del bien como ser activación, mejoras y revalúos.

Valor del bien ajustado: este valor está compuesto por todos los movimientos ajustados por inflación que afectan el valor del bien como ser activación, mejoras y revalúos.

Depreciación acumulada: este valor está compuesto por todos los movimientos que afectan el valor de la depreciación acumulada del bien como ser activación, depreciaciones y depreciaciones extraordinarias.

Depreciación acumulada ajustada: este valor está compuesto por todos los movimientos ajustados que afectan el valor de la depreciación acumulada del bien como ser activación, depreciaciones y depreciaciones extraordinarias.

Valor residual: este valor muestra la diferencia entre el valor del bien y la depreciación acumulada del bien.

Valor residual ajustado: este valor muestra la diferencia entre el valor del bien ajustado y la depreciación acumulada ajustada del bien.

##### Cuentas contables

En esta ficha usted define las cuentas contables para contabilizar los movimientos del bien.

Sólo puede seleccionar cuentas contables que estén habilitadas para el módulo de Activo Fijo y que no afecten ajuste por inflación del módulo de Contabilidad Tango Astor.

Usted puede definir en forma opcional las siguientes cuentas: cuenta del bien, cuenta de compra, cuenta depreciación, cuenta depreciación extraordinaria, cuenta depreciación acumulada, cuenta para mejoras, cuenta revalúo, cuenta de baja, cuenta resultado ajuste, cuenta resultado por tenencia.

Estas cuentas se utilizarán en la generación del asiento contable según los distintos movimientos ingresados en [Registración de movimientos](registracionmovimientos_afa).

##### Datos complementarios

En esta solapa se informan los datos complementarios del bien, si el bien está asegurado y las identificaciones adicionales específicas del bien.

Datos referidos al seguro del bien:

Bien asegurado: por defecto este parámetro está desactivado, al activarlo se habilitan otros campos dependientes.

Seguro: se habilita cuando se activa la marca de Bien asegurado. Es un valor opcional. Usted puede informar el nombre de la empresa aseguradora.

Número de póliza: se habilita cuando se activa la marca de Bien asegurado. Es un valor opcional. Usted puede ingresar si lo desea el número de la póliza del seguro.

Fecha de vencimiento: se habilita cuando se activa la marca de Bien asegurado. Es un valor opcional. Usted puede informar la fecha de vencimiento del seguro.

Porc. asegurado: se habilita cuando se activa la marca de Bien asegurado. Es un valor opcional. Usted puede informar el porcentaje del bien asegurado.

Moneda: seleccione la moneda del valora asegurado. Es un valor obligatorio.

Valor asegurado: informe el valor a cobrar por el seguro expresado en la moneda seleccionada. Es un valor obligatorio.

Datos referidos a las identificaciones adicionales del bien:

Estas identificaciones sirven para informar otras especificaciones para el bien.

Por defecto se asocian al bien las identificaciones adicionales relacionadas con el tipo de bien.

Estos valores son valores opcionales.

Usted puede agregar o eliminar [Identificaciones adicionales](identif_adicionales) en cualquier momento.

##### Agrupaciones auxiliares

La Agrupación de un bien es un criterio de clasificación y está disponible en el Seleccionador de bienes del módulo Activo Fijo.

Agrupaciones: asocie los grupos a los que pertenece el bien. Para clasificar el bien en grupos, pulse el botón "Asociar grupo", elija las agrupaciones propuestas y luego, ingrese el o los grupos en los que desea incluir al bien. Tango Astor valida que no incluya al bien en más de un grupo, si la agrupación es única, y que todo bien esté asociado a un grupo, si la agrupación es obligatoria. Utilice el proceso [Agrupaciones auxiliares](agrup_auxiliares) de Activo Fijo para definir las agrupaciones que necesite.

__Condiciones para eliminar un bien

  * Es posible eliminar un bien sólo si no existen movimientos registrados para el bien.
  * Si el bien tiene asociados movimientos deberá primero eliminar esos movimientos y luego eliminar el bien.[/axoft_box]



##### Importar datos desde Excel

En esta sección explicaremos cómo se puede facilitar la carga inicial de los bienes para la puesta en marcha del módulo Activo Fijo.

Para poder utilizar esta herramienta para la importación de bienes desde un archivo externo de Excel siga los siguentes pasos:

  * Configurar toda la información requerida y relacionada con los bienes como se indica en la [Puesta en marcha](?p=5016/#puesta-en-marcha-de-activo-fijo) o en la [Guía de administración de bienes.](?p=5922)
  * Generar la plantilla de importación desde Excel. El sistema provee una plantilla con las columnas que puede completar y el formato del tipo de dato.



No es obligatorio completar todas las columnas, sólo deberán informarse aquellas columnas que son obligatorias.  
La plantilla tiene la siguiente estructura: se agrupan las columnas en grupos según la forma en que se almacenan los datos, como ser Bienes, Comprobantes compras, Valoraciones, Identificaciones adicionales y Agrupaciones auxiliares.  
El formato de la celda viene dado según el tipo de dato aceptado por la base de datos para almacenar esa información. Usted puede consultar ese formato desde la plantilla posicionado sobre una celda de la plantilla y presionando botón derecho 'Formato de celda'.  
Cuando tenga completa la plantilla con los datos de los bienes, usted puede importar los bienes desde Excel desde la pantalla de [Bienes](?p=5033). La importación procesará los datos contenidos en el archivo y realizará todas las validaciones necesarias realizadas desde la carga manual. En caso de encontrar un dato no válido en un registro, este será rechazado, si el registro no presenta ningún dato inválido será aceptado.

__Nota

El proceso valida para poder realizar la importación de bienes que no se encuentre activo el código incremental de Parámetros de Activo Fijo. Para más información consulte [Codificación de bienes de Parámetros de Activo Fijo](?p=5948).

Una vez importados todos los bienes, para poder empezar a trabajar, usted debe ingresar desde la [Registración de movimientos](?p=6749), un movimiento de _Activación_ (bienes que no tienen fecha de activación) o un movimiento de _Carga inicial_ (bienes que tienen fecha de activación con anterioridad a la puesta en marcha del módulo **Activo Fijo**). Para más información consulte la ayuda de [Activación](?p=6749).  
A continuación se explica cómo completar la planilla generada en Excel para importar bienes, que campos serán requeridos para la grabación de un bien en el sistema, los valores conque se deben completar los campos y desde qué procesos podrá generar la plantilla.  
Para la importación de bienes se debe tener en cuenta que existen tres tipos de datos a completar indistintamente del proceso seleccionado.

  * Datos del tipo obligatorios: son aquellos que el sistema necesita para dar de alta un bien con sus detalles dentro del sistema.
  * Datos en los cuales se debe informar alguno dentro de las opciones posibles: son aquellos que no son requeridos, pero al completarlos deben cumplir con ciertos formatos o condiciones. Por ejemplo: Origen del bien (Datos de la compra/Valor contable).
  * Datos complementarios que agregan funcionalidad: son datos que al ser cargados en el bien habilitan procesos para la generación de información por medio de la utilización de datos ya ingresados, cómo ser si informa cantidades, si deprecia o no, entre otros.



###### Bienes

**Campo** | **Obligatorio** | **Tipo de dato** | **Longitud** | **Consideraciones**  
---|---|---|---|---  
Código bien | Si | Alfanumérico | 20 | Debe estar desactivada la codificación automática en [Parámetros de Activo Fijo](?p=5948). No.  
Descripción bien | No | Alfanumérico | 60 |   
Descripción detallada | No | Alfanumérico | 1000 |   
Cód. rubro | Si | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Rubros](?p=5951).  
Cód. tipo de bien | Si | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Tipos de bienes](?p=5955).  
Cód. bien principal | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Bienes](?p=5033).  
Cód. estado del bien | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Estados del bien](?p=5912).  
Fecha alta | No | Fecha | 10 | Formato DD/MM/AAAA. Fecha de alta del bien en el sistema.  
Fecha compra | Si | Fecha | 10 | Formato DD/MM/AAAA. Fecha de adquisión del bien.  
Fecha activación | No | Fecha | 10 | Formato DD/MM/AAAA. Completar sólo si Carga inicial = S sino dejarla en blanco.  
Fecha baja | No | Fecha | 10 | Formato DD/MM/AAAA. Este campo debe estar en blanco  
Fecha desafectación | No | Fecha | 10 | Formato DD/MM/AAAA. Esta fecha debe completarse sólo si el bien está totalmente depreciado  
Nro. de serie | No | Alfanumérico | 30 |   
Artículo asociado | No | Alfanumérico | 17 | Se completa con valores existentes en el proceso Artículos. Los artículos deben estar definidos como bienes de uso.  
Cód. ubicación | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Ubicaciones](?p=5957).  
Cód. departamento | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Departamentos](/htm_departamentos).  
Cód. responsable | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Responsables](?p=5950).  
Origen del bien | Si | Texto | 15 | Valores posibles Datos de la compra / Valor contable.  
Cód. moneda del bien | Si | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Monedas](/htm_monedas).  
Cotización | No | Numérico | 16 | Este valor pasa a ser obligatorio si la moneda del bien es distinta al tipo 'Corriente'.  
Valor del bien | Si | Numérico | 16 | Completar con el valor de compra + gastos para la puesta en marcha expresado en la moneda del bien.  
Carga inicial | Si | Texto | 1 | Valores posibles S/N. Si el bien tiene fecha de activación anterior a la fecha de la puesta en marcha del módulo toma el valor S sino N.  
Informa cantidades | Si | Texto | 1 | Valores posibles S/N. Si se completa con S se valida que se completen en forma obligatoria la unidad de medida y la cantidad.  
Unidad de medida | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Unidades de medida](/htm_unidadesdemedida). Las unidades de medida deben estar habilitadas para el módulo **Activo Fijo**. Este valor pasa a ser obligatorio si Informa cantidades = S.  
Cantidad | No | Numérico | 16 | Este valor pasa a ser obligatorio si el bien Informa cantidades = S.  
Cantidad residual | No | Numérico | 16 | Este valor pasa a ser obligatorio si Informa cantidades = S y Carga inicial = S.  
Cód. cuenta del bien | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Cód. cuenta de compra | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Cód. cuenta depreciación | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Cód. cuenta depreciación extraordinaria | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Cód. cuenta depreciación acumulada | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Cód. cuenta para mejoras | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Cód. cuenta revalúos | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Cód. cuenta de baja | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Cód. cuenta rdo. ajuste inflación | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Cód. cuenta rdo. tenencia | No | Alfanumérico | 20 | Se completa con valores existentes en el proceso [Cuentas](/htm_cuentas). Las cuentas deben estar habilitadas para el módulo **Activo Fijo**.  
Bien asegurado | Si | Texto | 1 | Valores posibles S/N. Si el bien está asegurado toma el valor S sino N.  
Seguro | No | Alfanumérico | 40 |   
Nro. de polliza | No | Alfanumérico | 40 |   
Fecha de vencimiento | No | Fecha | 10 | Formato DD/MM/AAAA. Se completa si Bien asegurado = S.  
Porc. asegurado | No | Numérico | 6 | Formato XXX.XX. Este valor debe ser entre 0 y 100.  
Cód. moneda seguro | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Monedas](/htm_monedas). Es obligatorio si Bien asegurado = S.  
Valor asegurado | No | Numérico | 16 | Este valor pasa a ser obligatorio si el Bien asegurado = S  
Observaciones | No | Alfanumérico | 1000 |   
  
Para poder importar el bien en el caso de haber seleccionado el valor "Datos de la compra" en origen del bien, es necesario que como mínimo informe un renglón correspondiente a un comprobante de compras. Por cada importación debe agregar un nuevo renglón en la planilla sin necesidad de tener que repetir los datos correspondientes al bien. El sistema controla que no exista más de un comprobante del tipo artículo por cada bien.

###### Comprobantes compras

**Campo** | **Obligatorio** | **Tipo de dato** | **Longitud** | **Consideraciones**  
---|---|---|---|---  
Automático | Si | Texto | 1 | Valores posibles S/N. Si Origen del bien = Datos de la compra entonces debe infomar al menos un renglón. Si el comprobante de compras existe en el sistema toma el valor S sino N.  
Proveedor | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Proveedores](/htm_proveedores1). Si Automático = N este valor puede quedar en blanco.  
Razón social | No | Alfanumérico | 60 | Si Automático = N es posible completar este dato.  
Tipo | Si | Texto | 1 | Valores posibles D/C. Si el comprobante corresponde a un débito como factura o notas de débito toma el valor D sino C.  
Comprobante compra | Si | Alfanumérico | 20 | Ingresar los valores correspondientes al tipo y número de comprobante de compra. Ejemplo: FAC A0001- 00000569  
Fecha | No | Fecha | 10 | Formato DD/MM/AAAA. Corresponde a la fecha del comprobante de compra. Si Automático = S debe estar completa.  
Moneda | Si | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Monedas](/htm_monedas).  
Cotización | No | Numérico | 16 | Este valor pasa a ser obligatorio si la moneda del comprobante es distinta al tipo 'Corriente'.  
Importe renglón | No | Numérico | 16 | Corresponde al importe del renglón en la moneda del comprobante. Si Automático = S la moneda sólo puede ser la correspondiente al tipo 'Corriente' o 'Extranjera contable' del sistema. Si Automático = N este campo debe estar en blanco.  
Importe | Si | Numérico | 16 | Corresponde al importe aplicado al bien en la moneda del comprobante. Si Automático = S la moneda sólo puede ser la correspondiente al tipo 'Corriente' o el tipo 'Extranjera contable' del sistema.  
Importe moneda corriente | Si | Numérico | 16 | Corresponde al importe aplicado al bien en la moneda corriente del sistema.  
Renglón | Si | Numérico | 9 | Corresponde al número del renglón del comprobante.  
Artículo | Si | Texto | 1 | Valores posibles S/N. Si el bien corresponde a un artículo toma el valor S sino N.  
Concepto | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Conceptos de compras](/conceptos_de_compra). Los conceptos deben estar definidos en el sistema como 'Gasto' para la puesta en marcha. Completar sólo si Automático = S, caso contrario dejar en blanco.  
Comprobante interno | No | Numérico | 9 | Corresponde al número interno del comprobante asignado por el sistema. Completar sólo si Automático = S, caso contrario dejar en blanco.  
  
Es necesario para poder importar un bien que tenga al menos un tipo de valoración informado. Como máximo se pueden informar hasta 3 tipos de valoración. Por cada uno debe agregar un nuevo renglón en la planilla sin necesidad de tener que repetir los datos correspondientes al bien.

###### Valoraciones

**Campo** | **Obligatorio** | **Tipo de dato** | **Longitud** | **Consideraciones**  
---|---|---|---|---  
Valoración | Si | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Tipos de valoración](?p=5956).  
Cotización | No | Numérico | 16 | Este valor pasa a ser obligatorio si la moneda del tipo de valoración es distinta al tipo 'Corriente'.  
Origen | No | Numérico | 16 | Si el bien Carga inicial = S este valor debe ser mayor a 0 sino 0.  
Mercado | SI | Numérico | 16 | Si no informa este valor poner 0.  
Recupero | SI | Numérico | 16 | Si no informa este valor poner 0.  
Deprecia | Si | Texto | 1 | Valores posibles S/N. Si el bien se deprecia toma el valor S sino N.  
Criterio | No | Alfanumérico | 10 | Valores posibles Alta/Baja. Si Deprecia = S entonces este valor pasa a ser obligatorio.  
Método | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Métodos de depreciación](?p=5956). Si Deprecia = S entonces este valor pasa a ser obligatorio.  
Frecuencia | No | Alfanumérico | 16 | Valores posibles Anual, Bimestral, Cuatrimestral, Mensual, Semestral, Trimestral. Si Deprecia = S entonces este valor pasa a ser obligatorio.  
Unidad vida útil | No | Alfanumérico | 10 | Los valores posibles con MESES y AÑOS, unidades de medida que proporciona el sistema. Si Deprecia = S entonces este valor pasa a ser obligatorio.  
Vida útil | No | Numérico | 3 | Si Deprecia = S entonces este valor pasa a ser obligatorio.  
Vida útil residual | No | Numérico | 3 | Si Deprecia = S y Carga inicial = S entonces este valor pasa a ser obligatorio.  
Dep. acumulada | No | Numérico | 16 | Si Deprecia = S, Carga inicial = S y Vida útil residual es menor a Vida útil entonces este valor pasa a ser obligatorio  
Porc. depreciable | No | Numérico | 6 | Formato XXX.XX. Si Deprecia = S entonces este valor pasa a ser obligatorio y debe ser mayor a 0 y menor o igual a 100.  
Afecta | Si | Texto | 1 | Valores posibles S/N. Si el bien es ajustable entonces toma el valor S sino N.  
Indice | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Indices](/htm_indices). Pasa a ser obligatorio si Afecta = S.  
  
Opcionalmente, usted puede informar una o más identificaciones adicionales. Por cada una debe agregar un nuevo renglón en la planilla sin necesidad de tener que repetir los datos correspondientes al bien.

###### Identificaciones adicionales

**Campo** | **Obligatorio** | **Tipo de dato** | **Longitud** | **Consideraciones**  
---|---|---|---|---  
Identificación adicional | Si | Numérico | 9 | Se completa con valores existentes en el proceso [Identificaciones adicionales](?p=5939).  
Valor | No | Alfanumérico | 100 |   
Leyenda | No | Alfanumérico | 100 |   
  
Al igual que las identificaciones adicionales, se pueden informar en forma opcional las agrupaciones que puede tener un bien. Usted puede informar varias o ninguna. Por cada una debe agregar un nuevo renglón en la planilla sin necesidad de tener que repetir los datos correspondientes al bien.

###### Agrupaciones auxiliares

**Campo** | **Obligatorio** | **Tipo de dato** | **Longitud** | **Consideraciones**  
---|---|---|---|---  
Cód. grupo | No | Alfanumérico | 10 | Se completa con valores existentes en el proceso [Agrupaciones auxiliares](?p=5898).  
  
##### Contenidos relacionados

  * [Videos sobre bienes de uso](https://ayudas.axoft.com/24ar/videos/afa_carp_vid/bienes_afa_vid/)
