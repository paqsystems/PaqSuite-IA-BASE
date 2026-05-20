# Registración de movimientos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=6749/

## Contenido

# Registración de movimientos

Desde este proceso usted puede registrar en el sistema todas las variaciones que puede sufrir el bien a lo largo del tiempo. 

Los tipos de movimientos posibles son: Activación, Adecuación, Ajuste por inflación, Baja, Baja por venta, Depreciación, Depreciación extraordinaria, Mejora, Revalúo, Transferencia.

Para poder ingresar al proceso de Regisración de movimientos usted tendrá que configurar los siguientes datos

  * Tiene que crear un [Ejercicio](?p=5927) en estado 'Abierto' para la fecha de carga de movimientos.
  * Configurar parámetros de puesta en marcha y carga inicial, parametrización contable y codificación automática de bienes desde [Parámetros de Activo Fijo](?p=5948).
  * Crear [Bienes](?p=5033).



##### Datos del movimiento

En esta sección se describen los datos comunes a todos los tipos de movimiento que se pueden realizar en el sistema.

Tipo: seleccione el tipo de movimiento que desea realizar. Este dato es de ingreso obligatorio. Según el tipo de movimiento seleccionado se completan los siguientes datos por defecto: Estado, Talonario, Concepto, Tipo de cotización.

Estado: por defecto muestra el estado inicial para el tipo de movimiento, usted puede modificarlo. Los estados posibles para un nuevo movimiento son: 'Ingresado' o 'Definitivo'. Este dato es de ingreso obligatorio.

Talonario: por defecto muestra el talonario habitual seleccionado para el tipo de movimiento, usted puede modificarlo. Este dato es de ingreso obligatorio.

Número: este campo no es editable cuando usted ingresa un nuevo movimiento y el sistema lo genera en forma automática de acuerdo al talonario asociado al movimiento proponiendo el próximo número para el talonario. Una vez grabado el movimiento si el talonario permite editar el número de movimiento usted puede modificarlo. El sistema controla que no ingrese un número ya utilizado para el talonario. Este dato es de ingreso obligatorio.

Número interno: los movimientos tienen siempre una numeración interna correlativa, que se corresponde con el orden de carga. Este número no es modificable y el sistema lo asigna en forma automática cuando usted acepta o graba el movimiento.

Fecha: el sistema propone la fecha del sistema, pero es posible modificarla. Este dato es de ingreso obligatorio. El sistema controla que la fecha del movimiento, esté comprendida en el rango de vigencia de un [ejercicio](?p=5927) en estado 'Abierto'.

Haga clic en el botón correspondiente para acceder al calendario.

Fecha anulación: este campo se habilita cuando usted quiere cambiar el estado del movimiento a 'Anulado'. El sistema controla que la fecha de anulación sea mayor o igual a la fecha. Este dato es de ingreso obligatorio.  
Haga clic en el botón correspondiente para acceder al calendario.  
Haga clic en el botón correspondiente para consultar la lista de monedas de tipo 'Alternativa' o 'Extranjeras' utilizadas en el movimiento.  
Por defecto el sistema propone el tipo de cotización habitual del tipo de movimiento. En caso de no tener informado el tipo de cotización habitual el sistema propone el tipo de cotización informado en la moneda. Si no existe la cotización para alguna de las monedas deberá informarla para poder grabar el movimiento.

Concepto: por defecto muestra el concepto habitual para el tipo de movimiento, usted puede modificarlo. Este dato es de ingreso opcional.

##### Datos contables del movimiento

El sistema puede generar asiento contable cuando tiene la información necesaria del tipo de valoración contable y además el movimiento tiene activada la marca Genera asiento.  
Los tipos de movimientos que pueden generar asiento contable son los siguientes: Activación, Adecuación, Ajuste por inflación, Baja, Baja por venta, Depreciación, Depreciación extraordinaria, Mejora y Revalúo.

Genera asiento: por defecto se muestra habilitado y se activa según el tipo de movimiento seleccionado. Si este parámero está activo, se habilitan los siguientes datos: 'Modelo de asiento', 'Fecha asiento', 'Fecha anulación del asiento'. Si este parámetro está desactivado estos campos se muestran deshabilidados. Si se trata de un nuevo movimiento.

Modelo de asiento: si está activo el parámetro Genera asiento, este campo muestra por defecto el modelo de asiento habitual asociado al tipo de movimiento. Si está activo en el tipo de movimiento el parámetro Edita asiento entonces es posible modificar el modelo de asiento. Es un campo de ingreso obligatorio.

Fecha asiento: si está activo el parámetro Genera asiento, este campo muestra por defecto la fecha del sistema. Usted puede modificarla. Es un campo de ingreso obligatorio. El sistema controla que la fecha del asiento sea mayor o igual a la fecha del movimiento.

Fecha anulación: este campo se habilita cuando se cambia el estado del movimiento a 'Anulado' y por defecto propone la misma fecha del asiento. Usted puede modificarla. Es un campo de ingreso obligatorio. El sistema controla que la fecha de anulación del asiento sea mayor o igual a la fecha de anulación del movimiento.

Más información:

Si en [Parámetros de Activo Fijo](?p=5948) se activa la marca Genera asiento en el ingreso de movimientos usted tiene la posibilidad de ir consultando el asiento a medida que ingresa los renglones de bienes.  
Si este parámetro está desactivado no se puede consultar el asiento contable hasta que se genere el asiento desde el proceso de [Generación de asientos contables de Activo Fijo](?p=5914).  
Si en [Parámetros de Activo Fijo](?p=5948) se activa la marca Respeta definición del modelo de asiento, usted no tiene la posibilidad de modificar la estructura del asiento definida en el asiento modelo. Puede informar el detalle de auxiliares.  
Desde el botón correspondiente puede configurar la apertura automática, puede configurar para el ingreso de un nuevo movimiento la apertura de la pantalla de asiento en forma automática.  
Puede consultar el asiento de registración <Ctrl + S> o el asiento de anulación <Ctrl + N> generado para el movimiento.  
Puede consultar información de control acerca del ingreso y la última modificación del asiento de registración <Ctrl + U + 1> o de anulación <Ctrl + U + 2> del movimiento. Para cada situación, se exhibe el usuario, fecha y terminal en la que se realizó la operación.  
Si se trata de un asiento exportado a Contabilidad o a otro sistema, se exhiben otros datos referidos al origen de la exportación (origen, número de lote de exportación, usuario, fecha y terminal).  
Los tipos de movimientos que no pueden generar asiento son: Transferencia y Cambio de método de depreciación. En este caso en la pantalla de [Registración de movimientos](?p=6749) se muestran deshabilitados.

**Datos de los renglones del asiento  
**Los datos se exhiben en formato grilla, de acuerdo a la definición del modelo de asiento y de los bienes ingresados en el movimiento podrán existir más o menos líneas.  
Al pie de la grilla, se exhibe la suma de los importes en la columna "Debe", la suma de los importes en la columna "Haber" y la diferencia entre ambas.  
Cada renglón se compone de los siguientes datos:

Número: es el número de renglón del asiento. Este dato no es editable.

Código de cuenta: ingrese o seleccione el código de cuenta contable. Este dato es de ingreso obligatorio. En caso de poder editar la cuenta o de poder agregar más renglones usted puede seleccionar una cuenta contable habilitada para el módulo de Activo Fijo.

Descripción de cuenta: este dato se completa automáticamente al completar la columna "Código de cuenta".

Debe / Haber: por defecto el importe se completará automáticamente de acuerdo al movimiento. Usted puede editar el importe. El sistema realiza los siguientes controles: el asiento deberá tener dos líneas como mínimo, el asiento deberá balancear, no se permite ingresar importes negativos, ni dejar renglones con importe en cero, los importes del asiento deben coincidir con los valores ingresados en el movimiento. El ingreso de este dato es obligatorio.  
Si ingresa el importe en la columna "Debe", se deshabilita la edición de la columna "Haber" y viceversa.  
Haga clic en el botón correspondiente para abrir la calculadora.

Auxiliares: el valor de este campo depende de la definición del parámetro Usa auxiliares contables en la cuenta contable.

Si para la terminal activa la Apertura automática de auxiliares, al ingresar el importe para la cuenta seleccionada y presionando <Enter>, se abrirá en forma automática la pantalla de auxiliares y subauxiliares contables para agilizar su imputación.  
Haga clic en el botón correspondiente para ingresar o consultar las imputaciones a auxiliares y subauxiliares contables de la cuenta contable en la que está posicionado. Las imputaciones pueden ser manuales o bien, basadas en reglas de apropiación automáticas asociadas a la cuenta - tipo de auxiliar.  
Es posible ingresar el Porcentaje y que se calcule en forma automática el Importe, o viceversa. Si la imputación a auxiliares contables queda pendiente por el total del importe de la línea o renglón del asiento, el Porcentaje será igual a 100% para el auxiliar 'Sin Asignar'.  
Usted puede seleccionar una regla de apropiación, puede elegir una regla que esté habilitada para el módulo Activo Fijo.

Leyenda: el sistema exhibe la leyenda definida en el modelo de asiento, será posible modificarla.

Detalle de auxiliares

Auxiliares: el valor de este campo depende de la definición del parámetro Usa auxiliares contables en la cuenta contable.

Si para la terminal activa la Apertura automática de auxiliares, al ingresar el importe para la cuenta seleccionada y presionando <Enter> se abrirá en forma automática la pantalla de auxiliares y subauxiliares contables para agilizar su imputación.  
Haga clic en el botón correspondiente para ingresar o consultar las imputaciones a auxiliares y subauxiliares contables de la cuenta contable en la que está posicionado. Las imputaciones pueden ser manuales o bien, basadas en reglas de apropiación automáticas asociadas a la cuenta - tipo de auxiliar.  
Es posible ingresar el Porcentaje y que se calcule en forma automática el Importe, o viceversa. Si la imputación a auxiliares contables queda pendiente por el total del importe de la línea o renglón del asiento, el Porcentaje será igual a 100% para el auxiliar 'Sin Asignar'.  
En la asignación de reglas el sistema prioriza la definición realizada en el bien o en el modelo de asiento, y en última instancia asigna la definición de reglas del módulo Procesos generales.

##### Renglones del movimiento

En esta grilla muestra el detalle del movimiento. De acuerdo al tipo de movimiento seleccionado se muestran más o menos columnas.  
Se muestran las columnas habilitadas con otro color de fondo.  
No es posible grabar un movimiento sin renglones.  
A continuación puede consultar la ayuda según el tipo de movimiento interno.

**Activación  
**Este movimiento será el inicial para todo bien independientemente que deprecie o no.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Haga clic en el botón correspondiente para acceder al seleccionador de bienes para asignar bienes al movimiento.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

Moneda: se muestra la moneda asociada al bien. Este dato no es editable.

Valor: se muestra el valor ingresado para el bien en la moneda asociada al bien. Este dato no es editable.

_Datos para cada valoración:_

Valor origen: el sistema propone el valor ingresado para la moneda del bien convertido a la moneda del tipo de valoración. Usted no puede modificar el valor para el tipo de valoración que contabiliza en [Parámetros de Activo Fijo](?p=5948). Para el resto de las valoraciones es posible modificar el valor propuesto por el sistema.

__Nota

Si la moneda del bien corresponde a dólares (moneda alternativa) y la moneda del tipo de valoración es pesos (moneda base), entonces toma el valor en la moneda del bien y lo multiplica por la cotización de la moneda, y le asigna el resultado al valor origen del tipo de valoración.  
El sistema valida que la fecha del movimiento de 'Activación' no puede ser menor a la fecha de compra del bien.  
Al grabar el movimiento se actualiza la fecha de activación en el bien y los saldos del bien.

Reemplazo del bien: puede indicar si el nuevo bien reemplaza a otro bien que fue dado de baja.

Movimiento de reemplazo: usted puede asociar el movimiento de baja realizado en el sistema del bien reemplazado.

**Movimiento de activación para informar el saldo inicial del bien  
**Para poder ingresar bienes con carga inicial es necesario completar los datos para la puesta en marcha en [Parámetros de Activo Fijo](?p=5948).  
Este movimiento se puede ingresar en forma automática con la carga de un nuevo bien con el parámetro Carga inicial activado, o desde la [Registración de movimientos](?p=6749).  
Haga clic en el botón correspondiente para poder ingresar un movimiento de carga inicial.  
En este caso se muestran para la moneda del bien y para cada tipo de valoración, el valor origen y la depreciación acumulada a la fecha de saldo inicial.  
Se recomienda no generar asiento si ya está implementado el módulo Contabilidad, para no duplicar los saldos contables.  
Si el tipo de movimiento es de 'Carga inicial', toma el tipo de movimiento y la fecha del movimiento de [Parámetros de Activo Fijo](?p=5948), y sólo puede ingresar los bienes pendiente de inicializar en el sistema y son de carga inicial.  
El comportamiento de este movimiento es similar al movimiento de 'Activación'.

__Nota

Este tipo de movimiento definido para carga inicial no se habilita para un movimiento de activación sin carga inicial. Su uso es exclusivo para informar carga inicial.

**Adecuación  
**Las columnas a completar en los renglones del movimiento son aquellas que están habilitadas y tienen un color de fondo distinto que blanco.  
El ingreso de un tipo de comprobante de adecuación permite actualizar los valores de los bienes a moneda homogénea en caso que el proceso de ajuste por inflación se haya realizado por fuera del sistema y se requiera incorporar los valores de los bienes actualizados.  
Se permite actualizar el valor del bien, la depreciación acumulada y el valor residual. Opcionalmente y como información para generar la registración contable, se detallan los importes de ajuste correspondiente al bien y a las depreciaciones acumuladas adecuadas.  
A partir de la carga de un movimiento de adecuación todas aquellas registraciones posteriores que se vinculen al bien tomarán como base, el nuevo valor origen y el importe acumulado de depreciación adecuado.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.  
Haga clic en el botón correspondiente para acceder al seleccionador de bienes para asignar bienes al movimiento.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

Moneda: se muestra la moneda asociada al bien. Este dato no es editable.

Valor del bien adecuado: ingrese el valor actualizado del bien que contempla el valor de origen con sus movimientos de mejora y/o revalúo, si los hubiere, más el ajuste por inflación generados por dichos importes. Debe ser un valor positivo, no puede ser cero. Esta columna se habilita si el ingreso es en 'Moneda del bien'.

Depreciación acumulada adecuada: ingrese el valor actualizado del acumulado por depreciaciones del bien, de movimientos de depreciaciones extraordinarias existentes y el ajuste por inflación correspondiente a ambos . Debe ser un valor positivo. Esta columna se habilita si el ingreso es en 'Moneda del bien'.

Valor residual adecuado: ingrese el valor actualizado del valor residual del bien, el cual debe ser la diferencia entre el valor de origen adecuado y el de depreciaciones acumuladas adecuadas. Debe ser un valor positivo. Esta columna se habilita si el ingreso es en 'Moneda del bien'.

Valor ajuste del bien adecuado: ingrese el importe que corresponde al ajuste realizado sobre el valor de origen del bien, a través de este dato el sistema podrá procesar el asiento contable relacionado al movimiento. El importe debe ser distinto de 0.

Valor ajuste de depreciación acumulada adecuada: ingrese el importe que corresponde al ajuste realizado sobre el valor de depreciación acumulada del bien, a través de este dato el sistema podrá procesar el asiento contable relacionado al movimiento. El importe debe ser distinto de 0.

Si alguno de las valoraciones asociadas al bien y que deprecia tiene asociado el método interno de depreciación por capacidad de producción, se habilitan las siguientes columnas.

Medida: seleccione una unidad de medida para el bien habilitada para el módulo Activo Fijo.

Cantidad: ingrese la cantidad de capacidad de producción del bien.

_Datos para cada valoración:_

Por cada valoración habilitada corresponde asignar valor a los siguientes campos.

Valor del bien adecuado: ingrese el valor actualizado del bien que contempla el valor de origen con sus movimientos de mejora y/o revalúo, si los hubiere, más el ajuste por inflación generados por dichos importes. Debe ser un valor positivo, no puede ser cero.

Depreciación acumulada adecuada: ingrese el valor actualizado del acumulado por depreciaciones del bien, de movimientos de depreciaciones extraordinarias existentes y el ajuste por inflación correspondiente a ambos. Debe ser un valor positivo. Esta columna se habilita si el ingreso es en 'Moneda del bien'.

Valor residual adecuado: ingrese el valor actualizado del valor residual del bien, el cual debe ser la diferencia entre el valor de origen adecuado y el de depreciaciones acumuladas adecuadas. Debe ser un valor positivo. Esta columna se habilita si el ingreso es en 'Moneda del bien'.

Si la valoración asociada al bien, deprecia y además tiene asignado un método de depreciación interno 'Lineal' se habilitan las siguientes columnas:

Unidad vida útil: el sistema muestra la unidad 'Meses'. Este dato no se puede modificar.

Vida útil: por defecto se propone la vida útil residual del bien. Puede modificar este dato. El sistema controla que la vida útil del revalúo no supere la vida útil del bien al momento de la activación.

**Tenga en cuenta:**

  * No se puede ingresar valores negativos.
  * La grabación de este movimiento actualiza el saldo del bien.
  * El sistema valida que la fecha del movimiento de la 'Adecuación' sea posterior a la fecha de compra y a la fecha de activación del bien.
  * El sistema valida que los bienes asignados para el tipo de movimiento se ajustan por inflación y tengan un índice asociado.
  * Solo es posible asignar bienes para adecuar si su valor residual es mayor a cero al momento de la registración del movimiento.



**Ajuste por inflación  
**Usted no puede ingresar un movimiento de ajuste por inflación desde [Registración de movimientos](?p=6749).  
El ingreso de este movimiento se realiza desde el proceso [Ajuste por inflación de Activo Fijo](?p=5900), se genera siempre en estado 'Definitivo'.  
Este movimiento afecta a los saldos de las valoraciones, no afecta a los saldos en moneda del bien.  
Todos los valores que se muestran a continuación son el resultado de la diferencia del valor histórico y el valor ajustado por el coeficiente de actualización.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

_Datos para cada valoración:_

Valor origen: muestra el ajuste del valor origen del bien para la valoración. Este dato no es editable.

Valor mejora: muestra el ajuste del valor mejora del bien para la valoración. Este dato no es editable.

Valor revalúo: muestra el ajuste del valor revalúo del bien para la valoración. Este dato no es editable.

Depreciación: muestra el ajuste de la depreciación del bien para la valoración. Este dato no es editable.

Depreciación acumulada: muestra el ajuste de la depreciación acumulada del bien para la valoración. Este dato no es editable.

Resultado: muestra el ajuste del resultado de la baja del bien para la valoración. Este dato no es editable.

Usted no puede modificar el contenido de los renglones de este movimiento generado automáticamente.  
Puede modificar los datos contables.  
Puede anularlo en caso que el movimiento lo considere incorrecto. Una vez que el movimiento está en estado 'Anulado', usted puede eliminar el movimiento.

**Baja  
**En este tipo de movimiento, se habilitan todos los datos de cabecera y los datos contables, usted puede ingresar un movimiento de baja para reflejar las siguientes situaciones: baja total del bien por incendio, robo, extravío, o cualquier otra situación que hace a la pérdida del bien.  
En caso que la pérdida del bien sea parcial, usted no puede dar de baja una parte del bien, para eso deberá utilizar un movimiento de revalúo ingresando un valor negativo para el bien.  
Las columnas a completar en los renglones del movimiento son aquellas que están habilitadas y tienen un color de fondo distinto al blanco.  
Una vez dado de baja el bien en el sistema, no se pueden realizar otras operaciones incluyendo ese bien, primero debe calcular las depreciaciones pendientes y luego debe dar de baja el bien.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Haga clic en el botón para acceder al seleccionador de bienes para asignar bienes al movimiento.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

Moneda: se muestra la moneda asociada al bien. Este dato no es editable.

Valor: se muestra el valor origen en la moneda del bien. Este dato no es editable.

Depreciación acumulada: se muestra el valor de las depreciaciones acumuladas en la moneda del bien. Este dato no es editable.

Resultado: el sistema calcula la diferencia entre las dos columnas anteriores, valor y depreciación acumulada. Este dato no es editable.

_Datos para cada valoración:_

Valor origen: se muestra el valor origen para la valoración del bien. Este dato no es editable.

Depreciación acumulada: se muestra las depreciaciones acumuladas para la valoración del bien. Este dato no es editable.

Resultado: el sistema calcula la diferencia entre las dos columnas anteriores, valor origen y depreciación acumulada. Este dato no es editable.

Si usted tiene asegurado el bien, y la baja del bien está cubierta por este seguro, usted puede incorporar esta información en el movimiento de baja.

Valor asegurado: el sistema verifica si el bien está asegurado y propone por defecto el valor asegurado que está guardado en el bien. En caso de no contar con esta información usted puede ingresarla manualmente.

La grabación de este movimiento actualiza el saldo del bien.  
El sistema valida que la fecha del movimiento de 'Baja' sea posterior a cualquier otro movimiento registrado en el sistema para el bien.

**Baja por venta  
**En este tipo de movimiento, se habilitan todos los datos de cabecera y los datos contables, usted puede ingresar un movimiento de baja por venta para reflejar la baja del bien cuando se vende. La baja del bien es total. Usted puede informar los datos de la factura de venta en forma manual, ingresando los datos del cliente, los datos del comprobante de venta, la moneda y el precio de venta.  
Las columnas a completar en los renglones del movimiento son aquellas que están habilitadas y tienen un color de fondo distinto al blanco.  
Una vez dado de baja el bien en el sistema no se pueden realizar otras operaciones incluyendo ese bien, primero debe calcular las depreciaciones pendientes y luego debe dar de baja el bien.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Haga clic en el botón para acceder al seleccionador de bienes para asignar bienes al movimiento.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

Moneda: se muestra la moneda asociada al bien. Este dato no es editable.

Valor: se muestra el valor origen en la moneda del bien. Este dato no es editable.

Depreciación acumulada: se muestra el valor de las depreciaciones acumuladas en la moneda del bien. Este dato no es editable.

Resultado: el sistema calcula la diferencia entre las dos columnas anteriores, valor y depreciación acumulada. Este dato no es editable.

_Datos para cada valoración:_

Valor origen: se muestra el valor origen para la valoración del bien. Este dato no es editable.

Depreciación acumulada: se muestra las depreciaciones acumuladas para la valoración del bien. Este dato no es editable.

Resultado: el sistema calcula la diferencia entre las dos columnas anteriores, valor origen y depreciación acumulada. Este dato no es editable.

_Datos de la venta:_

Código del Cliente: puede ingresar un código de cliente o puede seleccionar un código de la lista.

Razón social cliente: puede ingresar la razón social del cliente, si selecciona un cliente de la lista este campo se completa automáticamente.

Datos del comprobante: puede ingresar el tipo de comprobante, la letra, la sucursal y el número de comprobante. Por ejemplo: FAC A0001 - 00000564.

Moneda: seleccione la moneda del comprobante de venta.

Cotización: este campo se habilita cuando la moneda seleccionada es distinta a la moneda base. Usted debe ingresar la cotización para poder ingresar precio de venta del bien.

Precio venta: ingrese el precio de la factura de venta.

La grabación de este movimiento actualiza el saldo del bien.  
El sistema valida que la fecha del movimiento de 'Baja' se posterior a cualquier otro movimiento registrado en el sistema para el bien.  
Si posee el módulo de Ventas, primero debe ingresar la factura en Ventas y luego debe ingresar el movimiento de baja en Activo Fijo.

##### Cambio de método de depreciación

Este movimiento registra los cambios de método de depreciación, frecuencia o porcentaje depreciable para el bien que afectará el cálculo de depreciación del bien.  
Si usted todavía no generó ningún movimiento de depreciación, puede realizar la modificación de estos parámetros desde la pantalla de [Bienes](?p=5033) o desde el proceso de [Actualización masiva de bienes](?p=5895).  
El sistema controla que sólo se puede ingresar un movimiento de cambio de método por ejercicio contable. También controla que estén todos los períodos de depreciación calculados para el bien y la valoración sobre la cual desea realizar el cambio de parámetros.  
La grabación de este movimiento actualiza los datos en el bien.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

Medida: este campo se habilita cuando el método de depreciación nuevo para alguna de las valoraciones corresponde a 'Capacidad de producción'. Usted debe seleccionar la unidad de medida del bien. Este campo es un valor obligatorio.

Cantidad: este campo se habilita cuando el método de depreciación nuevo para alguna de las valoraciones corresponde a 'Capacidad de producción'. Usted debe ingresar la cantidad residual del bien al momento de realizar el cambio de método. Este es un valor obligatorio.

_Datos para cada valoración:_

_Anterior_

Método de depreciación: muestra el método actual asociado al bien para la valoración. No es posible modificar este campo.

Porcentaje depreciable: muestra el porcentaje depreciable actual ingresado en el bien para la valoración. No es posible modificar este campo.

Frecuencia depreciación: muestra la frecuencia actual asociado al bien para la valoración. No es posible modificar este campo.

_Nuevo_

Método de depreciación: seleccione el nuevo método de depreciación del bien para la valoración.

Porcentaje depreciable: ingrese el nuevo porcentaje depreciable del bien para la valoración.

Frecuencia depreciación: seleccione la nueva frecuencia de depreciación del bien para la valoración.

Unidad vida útil: en caso se seleccionar un método distinto al método actual y si el nuevo método es el método de depreciación 'Lineal', se habilita este campo. Seleccione la unidad de vida útil que puede ser 'Años' o 'Meses'. Este es un valor obligatorio.

Vida útil: en caso se seleccionar un método distinto al método actual y si el nuevo método es el método de depreciación 'Lineal', se habilita este campo. Ingrese la vida útil residual del bien al momento de realizar el cambio de método. Este es un valor obligatorio.

##### Depreciación

Usted no puede ingresar un movimiento de depreciación desde [Registración de movimientos](?p=6749).  
El ingreso de este movimiento se realiza desde el proceso [Depreciación de bienes](?p=5910), se genera siempre en estado 'Definitivo'.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

Moneda: se muestra la moneda asociada al bien. Este dato no es editable.

Depreciación: muestra el valor calculado desde el proceso en la moneda del bien. Este dato no es editable.

_Datos para cada valoración:_

Depreciación: muestra el valor calculado desde el proceso para el tipo de valoración. Este dato no es editable.

Usted no puede modificar el contenido de los renglones de este movimiento generado automáticamente.  
Puede modificar los datos contables.  
Puede anularlo en caso que el movimiento lo considere incorrecto.  
Una vez que el movimiento está en estado 'Anulado', usted puede eliminar el movimiento.

##### Depreciación extraordinaria

En este tipo de movimiento, se habilitan todos los datos de cabecera, los datos contables y además el tipo de ingreso, usted puede ingresar el valor de la depreciación extraordinaria en moneda del bien o en la moneda de la valoración contable.  
Las columnas a completar en los renglones del movimiento son aquellas que están habilitadas y tienen un color de fondo distinto al blanco.  
El sistema propone al agregar un nuevo bien, el valor residual que le queda al bien a la fecha del movimiento. Este valor sale de la diferencia entre el valor del bien y las depreciaciones acumuladas para el bien.  
Usted no puede ingresar un valor mayor al propuesto por el sistema, no puede ingresar depreciaciones menores que cero, debe completar el valor de depreciación para alguno de los tipos de valoración asociadas al bien.  
En este movimiento se habilita el ingreso de importes en moneda del bien o en la moneda del tipo de valoración contable.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Haga clic en el botón para acceder al seleccionador de bienes para asignar bienes al movimiento.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

Moneda: se muestra la moneda asociada al bien. Este dato no es editable.

Depreciación extraordinaria: por defecto se habilita esta columna y se propone el valor residual del bien.

Esta columna aparece habilitada sólo si se selecciona la opción ingreso en "Moneda del bien" y se deshabilita si se selecciona la opción ingreso en 'Valoración contable'.  
En el caso de ingresar un valor en la moneda del bien, ese valor se reexpresa para la valoración contable.  
_Datos para cada valoración:_

Depreciación extraordinaria: por defecto se asigna el valor residual del bien al momento de movimiento. Es posible modificar este valor. El sistema controla que el valor ingresado no supere el valor residual del bien calculado.

No se pueden ingresar valores negativos.  
La grabación de este movimiento actualiza el saldo del bien.  
Es importante resaltar que este tipo de movimiento reemplaza el cálculo de depreciación para el periodo al que afecta.

##### Mejora

En este tipo de movimiento, se habilitan todos los datos de cabecera, los datos contables y además el tipo de ingreso, usted puede ingresar el valor de la mejora en moneda del bien o en la moneda de la valoración contable.  
Las columnas a completar en los renglones del movimiento son aquellas que están habilitadas y tienen un color de fondo distinto que blanco.  
Si ingresa un movimiento de mejora, la misma queda siempre relacionada al bien, y se tendrá en cuenta en el saldo del bien y en el proceso de [Depreciación de bienes](?p=5910).  
En caso de querer darle un tratamiento diferente al bien y a la mejora, debe ingresarse como un nuevo bien y relacionarlo con el bien principal. De esta manera, se tratan como bienes independientes a la hora realizar el cálculo de depreciación y de guardar los saldos.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Haga clic en el botón para acceder al seleccionador de bienes para asignar bienes al movimiento.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

Moneda: se muestra la moneda asociada al bien. Este dato no es editable.

Valor mejora: ingrese el valor del mejora, puede ser un valor positivo, no puede ser cero. Este columna se habilita si el ingreso es en 'Moneda del bien'.

Valor mejora: se muestra el valor ingresado para el bien en la moneda asociada al bien. Este dato no es editable.

Si alguno de las valoraciones asociadas al bien y que deprecia tiene asociado el método interno de depreciación por capacidad de producción, se habilitan los siguientes columnas.

Medida: seleccione una unidad de medida para el bien habilitada para el módulo de Activo Fijo

Cantidad: ingrese la cantidad de capacidad de producción del bien.

_Datos para cada valoración:_

Valor mejora: se asigna el valor ingresado para el bien de acuerdo a la moneda del tipo de valoración. Este dato no es editable.

__Importante

Si la moneda del bien es dólares (moneda alternativa) y la moneda del tipo de valoración es pesos (moneda base) entonces toma el valor en la moneda del bien y lo multiplica por la cotización de la moneda, y le asigna el resultado al valor origen del tipo de valoración.

Si la valoración asociada al bien, deprecia y además tiene asignado un método de depreciación interno 'Lineal' se habilitan las siguientes columnas:

Unidad vida útil: el sistema muestra la unidad 'Meses'. Este datos no es posible modificarlo.

Vida útil: por defecto se propone la vida útil residual del bien. Este dato puede modificarlo. El sistema controla que la vida útil de la mejora no supere la vida útil del bien al momento de la activación.

_Datos de la compra:_

Usted puede ingresar los datos del comprobante de compras en forma manual o en forma automática consultando los comprobantes del módulo Compras.  
Están disponibles para completar las siguientes columnas en la grilla:

Código del proveedor: es un dato opcional, puede optar entre seleccionar un proveedor ya existente o ingresar un nuevo proveedor.

Razón social del proveedor: si selecciona un proveedor existente, este campo se completa en forma automática.

Datos del comprobante: es un dato opcional, puede ingresar el tipo de comprobante, la letra, la sucursal y el número de comprobante. Por ejemplo: FAC A0001 - 00000564.

Haga clic en el botón correspondiente para acceder a la consulta de comprobantes del módulo Compras.  
Si selecciona un comprobantes desde esta consulta se completarán en forma automática todas las columnas de 'Datos de la compra'.

Moneda: es un dato opcional, corresponde a la moneda del comprobante de compra. Si desea informar el importe del comprobante es necesario informar este campo.

Cotización: si la moneda del comprobante de compra es distinta a la moneda base configurada en el módulo **Procesos Generales** se habilita este campo para que pueda ingresar la cotización de la moneda. Si desea informar el importe del comprobante es necesario informar este campo.

Importe pendiente: es un dato opcional. No se puede ingresar valores negativos.

La grabación de este movimiento actualiza el saldo del bien.  
El sistema valida que la fecha del movimiento de la 'Mejora' sea posterior a la fecha de compra y a la fecha de activación del bien.

##### Revalúo

En este tipo de movimiento, se habilitan todos los datos de cabecera, los datos contables y además el tipo de ingreso, usted puede ingresar el valor de la mejora en moneda del bien o en la moneda de la valoración contable.  
Las columnas a completar en los renglones del movimiento son aquellas que están habilitadas y tienen un color de fondo distinto que blanco.  
Si ingresa un movimiento de revalúo, la misma queda siempre relacionada al bien, y se tendrá en cuenta en el saldo del bien y en el proceso de [Depreciación de bienes](?p=5910).  
En caso de querer darle un tratamiento diferente al bien y al revalúo, debe ingresarse como un nuevo bien y relacionarlo con el bien principal. De esta manera, se tratan como bienes independientes a la hora realizar el cálculo de depreciación y de guardar los saldos.

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Haga clic en el botón correspondiente para acceder al seleccionador de bienes para asignar bienes al movimiento.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

Moneda: se muestra la moneda asociada al bien. Este dato no es editable.

Valor revalúo: ingrese el valor del revalúo, puede ser un valor positivo o negativo, no puede ser cero. Este columna se habilita si el ingreso es en 'Moneda del bien'.

Si alguno de las valoraciones asociadas al bien y que deprecia tiene asociado el método interno de depreciación por capacidad de producción, se habilitan los siguientes columnas.

Medida: seleccione una unidad de medida para el bien habilitada para el módulo de Activo Fijo

Cantidad: ingrese la cantidad de capacidad de producción del bien.

_Datos para cada valoración:_

Valor revalúo: ingrese el valor del revalúo, puede ser un valor positivo o negativo, no puede ser cero. Este columna se habilita si el ingreso es en 'Valoración contable'.

Si la valoración asociada al bien, deprecia y además tiene asignado un método de depreciación interno 'Lineal' se habilitan las siguientes columnas:

Unidad vida útil: el sistema muestra la unidad 'Meses'. Este dato no se puede modificar.

Vida útil: por defecto se propone la vida útil residual del bien. Puede modificar este dato. El sistema controla que la vida útil del revalúo no supere la vida útil del bien al momento de la activación.

No se puede ingresar valores negativos.  
La grabación de este movimiento actualiza el saldo del bien.  
El sistema valida que la fecha del movimiento del 'Revalúo' sea posterior a la fecha de compra y a la fecha de activación del bien.

##### Transferencias

Usted puede registrar en el sistema y a lo largo del tiempo las dintintas asignaciones del bien, cambios de departamento, cambios de ubicación y cambios de responsables a lo largo del tiempo.  
Si no le interesa conservar la historia del bien, puede realizar la modificación de estos datos directamente desde el maestro de [Bienes](?p=5033) o desde el proceso de [Actualización masiva de bienes](?p=5895).

_Datos del bien:_

Número: es el número de renglón del movimiento. Este dato no es editable.

Código de bien: ingrese o seleccione el código de bien. Este dato es de ingreso obligatorio.

Haga clic en el botón correspondiente para acceder al seleccionador de bienes para asignar bienes al movimiento.

Descripción de bien: este dato se completa automáticamente al completar la columna "Código de bien".

_Datos de origen:_

Ubicación: se muestra por defecto la ubicación grabado en el bien, puede ser que esté dato en blanco, esta valor no es obligatorio en el bien y no es posible modificarlo en el movimiento.

Departamento: se muestra por defecto el departamento grabado en el bien, puede ser que esté dato en blanco, esta valor no es obligatorio en el bien y no es posible modificarlo en el movimiento.

Responsable: se muestra por defecto el responsable grabado en el bien, puede ser que esté dato en blanco, esta valor no es obligatorio en el bien y no es posible modificarlo en el movimiento.

_Datos de destino:_

Ubicación: seleccione la nueva ubicación del bien. Es un campo de ingreso obligatorio.

Departamento: seleccione el nuevo departamento al cual quiere asignar el bien. Es un campo de ingreso obligatorio.

Responsable: seleccione el nuevo responsable al cual quiere asignar el bien. Es un campo de ingreso obligatorio.

Si están completos los valores de origen el sistema valida que alguno de los tres haya cambiado.  
El sistema valida que la fecha del movimiento de trasferencia sea posterior a la fecha de compra del bien.  
Se pueden trasferir todos los bienes que estén en el inventario, no se pueden transferir bienes dados de baja.  
Este movimiento no puede generar asiento contable.  
La grabación de este movimiento actualiza los datos del bien.

Funcionalidad de la grillas:

Al operar con la grilla de renglones de movimientos, de asientos, están disponibles las siguientes funciones:

  * Primero (ir a la primera fila)
  * Anterior (ir a la fila anterior)
  * Siguiente (ir a la fila siguiente)
  * Ultimo (ir a la última fila)
  * Insertar nueva fila <Ins>
  * Eliminar fila actual <Del>
  * Mover al principio.
  * Mover renglón hacia arriba <Alt + Up>
  * Mover renglón hacia abajo <Alt + Down>
  * Mover al final.



En la grilla de renglones de movimiento se agrega:

  * Asignar bienes <Ctrl + Alt + A>



En la grilla de renglones de asiento se agrega:

  * Invertir importes (cambia de columna el importe) <F4>
  * Asignar importe por la diferencia <F3>
  * Apertura automática / manual de auxiliares.



Para acceder a estas funciones, haga clic en el botón correspondiente que se exhibe al pie de la grilla en movimientos, en asientos y en el detalle de auxiliares.

##### Importación de movimientos

Se habilita la opción de importación desde Excel sólo para el tipo de movimiento de adecuación.  
Para configurar correctamente el archivo Excel para ser importado, se debe generar la plantilla con los campos necesarios para realizar el proceso.  
La cabecera del comprobante se registra solo en la primera línea de la plantilla incluyendo los datos del primer bien, a partir del segundo y subsiguientes se completan solo los datos de los bienes a actualizar.  
Solo es posible importar un movimiento de adecuación por plantilla, por lo que, si se desea diversificar el ajuste de los bienes en diferentes movimientos, se deberán asignar en distintas plantillas.

##### Importación de plantilla de bienes

Se permite seleccionar la plantilla con la información de los bienes que se desean incorporar al movimiento.  
El proceso registrará el comprobante lo cual actualizará los valores del saldo del bien por los impuestos a través de los registros importados, de lo contrario indicará mediante distintos mensajes de validación las inconsistencias encontrados.

##### Contenidos relacionados

  * [Videos sobre bienes de uso](https://ayudas.axoft.com/25ar/videos/afa_carp_vid/bienes_afa_vid/)
