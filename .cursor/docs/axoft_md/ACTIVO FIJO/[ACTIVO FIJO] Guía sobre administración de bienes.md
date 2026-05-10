# Guía sobre administración de bienes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guia_administracionbienes/

## Contenido

# Guía sobre administración de bienes

Con esta guía usted puede conocer mejor las funcionalidades del módulo Activo Fijo para reflejar en el sistema los posibles movimientos que pueden sufrir los bienes a lo largo de su ciclo de vida.

__Nota

Recuerde que la tecla rápida _< F3>_ permite realizar la búsqueda de un texto en el menú de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

##### Puesta en marcha de administración de bienes

Para la puesta en marcha del módulo usted tiene que definir algunos datos que son necesarios, mientras que hay otros que son opcionales pero que ayudan a que el módulo tenga un mejor desempeño.  
Como datos necesarios relativos al sistema en su conjunto tenemos:

  * Definir desde la opción [Monedas](?p=11955), la moneda corriente y la moneda extranjera contable, necesarias para la integración con el módulo Compras y para la integración con el módulo Contabilidad.
  * Definir un ejercicio contable desde la opción [Ejercicio](?p=5927) del módulo Activo Fijo o desde la opción [Ejercicio](?p=9779) del módulo Contabilidad.
  * Definir en [Parámetros contablles](?p=11964) del módulo Procesos generales la moneda extranjera contable habitual.
  * Definir los datos contables necesarios [Cuentas](?p=11849), [Tipos de asientos,](?p=11994) [Auxiliares contables](?p=11969), [Reglas de apropiación](?p=11974), para poder crear los [Modelos de asientos de Activo Fijo](?p=5933).
  * Definir los datos necesarios para la creación de bienes como por ejemplo [Tipos de valoración](?p=5956), [Métodos de depreciación](?p=5945), [Rubros](?p=5951), [Tipos de bienes](?p=5955), [Identificaciones adicionales](?p=5939).
  * Definir otros datos necesarios, como ser [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) en el módulo Stock, para el alta de bienes desde el módulo Compras o para la asociación de comprobantes de compras desde el origen del bien en el módulo Activo Fijo. Para más información sobre el tema consulte el tópico [Definición de artículos que representan bienes](?p=5938/#puesta-en-marcha-de-la-integracion-de-activo-fijo).
  * Definir aquellos [Conceptos de Compras](?p=14626) que se activan junto con el bien. Estos se pueden distribuir y asociar desde el módulo Compras con el alta del comprobante o se pueden asociar desde el origen del bien en el módulo Activo Fijo. Para más información sobre el tema consulte [Definición de los conceptos de compras que representan gastos para bienes](?p=5938/#puesta-en-marcha-de-la-integracion-de-activo-fijo).
  * Definir los datos propios para la [Registración de movimientos](?p=6749) del bien como ser [Talonarios](?p=5953) o [Conceptos de movimientos](?p=5908).
  * Definir otras configuraciones en [Parámetros de Activo Fijo](?p=5948) para la codificación automática de bienes, para la carga inicial de bienes y para la contabilización de movimientos.
  * Crear todas las clasificaciones o características necesarias que usted desea utilizar para agrupar a los bienes, como por ejemplo: [Departamentos](?p=11852), [Ubicaciones](?p=5957), [Responsables](?p=5950), [Estados](?p=5912) y [Agrupaciones auxiliares](?p=5898). Estos no son datos obligatorios, por lo tanto usted puede hacerlo luego de dar de alta los bienes.



Una vez completos los pasos anteriores, usted está en condiciones para la creación de bienes. Para más información consulte [¿Cómo crear bienes?.](?p=5922/#%c2%bfcomo-crear-bienes)

##### Detalle del circuito de administración de bienes

En este capítulo se describen algunos temas fundamentales para el uso y el manejo del módulo Activo Fijo.  
A continuación expondremos las respuestas a algunos interrogantes que se pueden presentar.

###### ¿Cómo crear bienes?

Una vez realizada la [Puesta en marcha](?p=5922/#puesta-en-marcha-de-administracion-de-bienes) descripta en esta guía usted puede proceder a crear bienes.

**Creación de bienes activados en otros sistemas o que provienen de una planilla auxiliar.  
**Para la incorporación de bienes que la empresa adquirió con anterioridad a la puesta en marcha del módulo, que pueden estar activados y registrados en otro sistema externo o en alguna planilla auxiliar de Excel, usted puede optar:

  * Cargar los bienes en forma manual, informando la fecha de activación (momento en el cual pasa a ser parte del activo de la empresa y en el caso que el bien deprecie será la fecha a partir de la cual se comience a depreciar), tildando la marca de carga inicial y completando los saldos iniciales, valor de origen (compuesto por el valor de origen más mejoras y revalúos ajustados a la fecha de puesta en marcha de [Parámetros de Activo Fijo](?p=5948)).
  * Cargar los bienes desde la opción importar datos desde Excel, completando la plantilla con los datos requeridos para los bienes. Para más información consulta la ayuda [Importar datos desde Excel](?p=5940).



**Creación de un nuevo bien que la empresa adquiere con posterioridad a la puesta en marcha del módulo.  
**Si posee los módulos Stock y Compras, usted puede optar por los siguientes circuitos:

  * Cargar la factura de compras del artículo y crear el bien desde el módulo Compras. Para más información sobre este circuito consulte la ayuda [Integración de artículos con el módulo de Activo Fijo](?p=5938/#integracion-de-activo-fijo-con-stock) y [Alta automática de bienes para Activo Fijo](?p=5901).
  * Cargar la factura de compras y en otro momento crear el bien en forma manual y asociarle al bien desde la solapa origen del bien los comprobantes de compras. Para más información sobre este circuito consulte la ayuda [Integración de artículos con el módulo de Activo Fijo](?p=5938/#integracion-de-activo-fijo-con-stock) y [Bienes](?p=5933).



Si no posee los módulos Stock y Compras sólo podrá dar de alta los bienes desde el maestro de [Bienes](?p=5933).

**Asociación de otros gastos como parte del valor del bien.  
**Además del comprobante de compra del artículo que dio origen al bien, usted puede asociar otros gastos como parte del costo del bien.  
Si posee los módulos Stock y Compras, usted puede optar por los siguientes circuitos:

  * Cargar la factura con conceptos que afecten al módulo Activo Fijo y asociarle en ese momento el gasto al bien o a los bienes. Para poder realizar este circuito consulte la ayuda [Integración de gastos de compras con el módulo Activo Fijo](?p=5938/#integracion-de-activo-fijo-con-compras) y [Alta automática de gastos para bienes de Activo Fijo](?p=5902).
  * Cargar la factura con conceptos que afecten al módulo Activo Fijo y en otro momento asociar esos comprobantes al bien o los bienes en forma manual, desde la solapa de origen del bien en el módulo Activo Fijo. Para más información sobre este circuito consulte la ayuda [Integración de gastos de compras con el módulo de Activo Fijo](?p=5938/#integracion-de-activo-fijo-con-compras) y [Bienes](?p=5933).



Si no posee los módulos Stock y Compras sólo podrá asociar otros comprobantes de gastos desde el maestro de [Bienes](?p=5933).

###### ¿Qué tipos de movimientos se pueden registrar?

Para comprender el ciclo de vida habitual de un bien puede consultar el siguiente esquema:

En este esquema se describen todos los tipos de movimientos posibles que se pueden registrar para un bien en el módulo Activo Fijo.  
El primer movimiento que usted debe realizar en el sistema es la [Activación](?p=6749#activacion) del bien. Este movimiento habilita al bien a guardar sus saldos, a depreciarlo en caso que lo requiera y a realizar otros movimientos que se describen en el sistema.  
En caso de tratarse de un bien comprado con posterioridad a la puesta en marcha del módulo Activo Fijo, debe ingresar el bien, no completar su fecha de activación y luego en un segundo paso ingresar un movimiento de Activación, sólo se pueden incluir en este tipo de movimiento, bienes pendientes de activar.  
En caso de tratarse de un bien comprado con anterioridad a la puesta en marcha del módulo Activo Fijo, debe ingresar el bien, completar la fecha de activación (si es que el bien está en uso) y tildar la opción Carga inicial, ello lo habilita a ingresar los saldos iniciales del bien a una fecha dada configurada en [Parámetros de Activo Fijo.](?p=5948) Al guardar los datos de este nuevo bien, el sistema propone que usted genera en forma automática el movimiento de Activación. En caso de no querer generarlo en ese momento, desde la [Registración de movimientos](?p=6749) usted tiene la posibilidad de hacerlo luego ingresando un movimiento de carga inicial.  
Para más información sobre el tema, consulte la ayuda de [Activación](?p=6749#activacion).  
Si el bien está activado y si está configurado para depreciar usted puede ejecutar el proceso de [Depreciación de bienes](?p=5910). Sólo se pueden registrar movimientos de depreciación desde este proceso, no es posible ingresar un movimiento de depreciación en forma manual.  
Para más información sobre este tema, consulte la ayuda de [Depreciación](?p=6749#depreciacion).  
Si el bien está activado puede ingresar otros movimientos que van a afectar el valor del bien y/o la vida útil del bien. Para más información sobre este tema, consulte la ayuda de [Mejora](?p=6749#mejora) y [Revalúo](?p=6749#revaluo).  
Otro movimiento que el bien puede registrar son las depreciaciones extraordinarias, se ingresan cuando el bien sufre una eventualidad que afecta la cuota ordinaria de depreciación del bien y que de otra forma no es posible reflejarlo en el sistema. Usted ingresa en forma manual una cuota de depreciación para el bien que no puede superar nunca el valor residual del bien.  
En este caso este tipo de movimiento sustituye al movimiento automático generado desde la [Depreciación de bienes](?p=5910).  
Para más información sobre este tema, consulte el tópico [Depreciación extraordinaria](?p=6749#deprextra).  
Otros movimientos que usted puede reflejar en el sistema son la [Baja](?p=6749#baja) y la [Baja por venta](?p=6749#bajaventa). El primero corresponde cuando un bien se pierde, se roba o se destruye, de tal manera que ya no tiene utilidad. El segundo corresponde cuando la empresa quiere remplazar un bien por otro más moderno y además puede obtener un ingreso por el mismo, o simplemente cuando el bien ya no es necesario para la empresa y la empresa decide venderlo para recuperar algo del costo del mismo. Una vez dado de baja un bien no puede volver a registrar movimientos con él, salvo que se anulen los movimientos de Baja o Baja por venta. Para más información consulte la ayuda del ítem en cuestión [Registración de movimientos](?p=6749).  
Existen otros movimientos que no afectan el saldo del bien, como por ejemplo el movimiento de [Trasferencia](?p=6749#transferencia) aplicable desea registrar los movimientos de bienes entre sectores o entre sucursales (departamento, ubicación y responsable). Para más información consulte la ayuda del ítem [Transferencias](?p=6749#transferencia).  
También puede registrar movimientos de cambios de métodos de depreciación, el sistema permite solamente un cambio de método por ejercicio contable.  
Para más información, consulte el tópico [Cambio método de depreciación](?p=6749#cambiometodo).

**¿Qué estados pueden tener los movimientos?**

  * Estado Ingresado: donde el usuario puede modificar los renglones del movimiento (agregar, modificar o eliminar bienes).
  * Estado Definitivo: donde el usuario no puede modificar los renglones, sólo podrá anular el movimiento.
  * Estado Anulado: en este estado no puede modificar nada y no se toma en cuenta para los procesos.



Al ingresar un nuevo movimiento, el estado se propone por defecto de acuerdo al estado inicial del tipo de movimiento. Para un nuevo movimiento los estados posibles son: 'Ingresado' o 'Definitivo', no es posible registrar un nuevo movimiento en estado 'Anulado'.  
No es necesario que todos los movimientos pasen por el estado 'Ingresado' para pasar al 'Definitivo'. Un nuevo movimiento puede nacer en estado 'Definitivo'.  
Tampoco es necesario que todos los comprobantes pasen al estado 'Definitivo' para tomarlos en cuenta desde los proceso de [Depreciación de bienes](?p=5910) o de [ajuste por inflación de Activo Fijo](?p=5900).  
Los procesos periódicos de [Depreciación de bienes](?p=5910) y de [Ajuste por inflación](?p=6749) generarán comprobantes en estado 'Definitivo', el usuario podrá anular el comprobante en caso de error o podrá modificar el asiento para informar apropiaciones o para re-imputar cuentas.

**Resumiendo:  
**El movimiento puede nacer 'Ingresado', luego pasar a 'Definitivo' y por último a 'Anulado'.  
_Ingresado - > Definitivo -> Anulado_

El movimiento puede nacer 'Ingresado', luego pasar a 'Anulado'.  
_Ingresado - > Anulado_

El movimiento puede nacer 'Definitivo', luego pasar a 'Anulado'.  
_Definitivo - > Anulado_

**¿Qué estados pueden tener los asientos de los movimientos?**

  * Sin generar: el movimiento no tiene asiento generado de registración y/o de anulación. Estos movimientos están pendientes de contabilizar.
  * Generado: el movimiento tiene asiento generado de registración y/o de anulación. Estos asientos están pendientes de exportarse a Contabilidad.
  * Exportado: el movimiento tiene asiento generado de registración y/o de anulación, y está exportado a Contabilidad. Esto significa que participó de un lote contable generado desde la exportación de asientos de Activo Fijo.



El asiento de un nuevo movimiento se puede generar con el ingreso del mismo, cuando tiene activado el tilde Generación con el ingreso del movimiento en [Parámetros de Activo Fijo](?p=5948), o puede generarse luego del ingreso por medio del proceso [Generación de asientos contables de Activo Fijo](?p=5914).  
El estado del asiento se maneja en forma independiente del estado movimiento. Por ejemplo; puedo tener un movimiento en estado 'Anulado' con el asiento de registración 'Exportado' y el asiento de anulación 'Generado'.  
El asiento de registración de un movimiento se puede modificar siempre que el estado del movimiento sea distinto a 'Anulado' y que el asiento no esté 'Exportado a Contabilidad'. Además el usuario debe tener habilitado en el administrador general para su rol el permiso Modificación de asientos de movimientos.  
El asiento de anulación de un movimiento es la reversión del asiento de registración y no es posible modificarlo.  
Para el caso que el movimiento esté en estado 'Ingresado' y con el asiento generado de registración, al agregar, modificar o eliminar renglones de bienes, el sistema espera confirmación del usuario para regenerar el asiento. Si el usuario confirma la regeneración entonces podrá guardar las modificaciones realizadas.

**¿Cuándo se puede eliminar un movimiento?  
**Es posible eliminar un movimiento cuando el estado del mismo sea 'Ingresado' o 'Anulado'.  
En algunos casos se valida que no existan movimientos posteriores que dependan de este movimiento, por ejemplo, si se desea eliminar un movimiento de 'Activación' de un bien que ya tiene movimientos de depreciación con fecha posterior.  
En el caso que asiento esté transferido a Contabilidad por más que estado se encuentre en estado 'Ingresado' no se permite la eliminación del movimiento.

###### ¿Cómo se realiza la depreciación de un bien?

Una vez activados los bienes y configurados aquellos bienes que se van a depreciar usted está en condiciones de ejecutar el proceso de [Depreciación de bienes](?p=5910).  
En caso de haber asociado al bien un método de capacidad de producción deberá informar la cantidad producida para cada período, para ello deberá ingresar en la opción [Datos complementarios según métodos de depreciación](?p=5909).  
Una vez en el proceso el sistema propone datos por defectos para facilitar su ejecución, como ejercicio actual y período mensual actual correspondiente a la fecha actual del sistema.  
El proceso tomará todos los movimientos desde la activación hasta las mejoras, revalúos y depreciaciones extraordinarias en estado 'Ingresado' o 'Definitivo' hasta el periodo mensual actual para calcular las depreciaciones correspondientes.  
En caso que la activación tenga un fecha posterior al periodo mensual seleccionado, el proceso avisa que no es posible realizar ningún cálculo.  
Si usted selecciona la opción a la frecuencia el sistema genera un movimiento de depreciación según cada frecuencia.

**Ejemplo:** si el bien tiene asociada una frecuencia mensual, el bien se activa el 20/01/2018 y el periodo mensual seleccionado es 03/2018. El proceso genera 3 movimientos de depreciación, el primero con fecha 31/01/2018, el segundo con fecha 29/02/2018 y el tercero 31/03/2018.

Si usted selecciona la opción a la fecha del proceso el sistema genera un movimiento para todos los periodos hasta el periodo mensual ingresado.

**Ejemplo:** si el bien tiene asociada una frecuencia mensual, el bien se activa el 20/01/2018 y el periodo mensual seleccionado es 03/2018. El proceso genera 1 movimiento de depreciación con fecha 31/03/2018.

Para más información sobre el proceso consulte la ayuda [Depreciación de bienes](?p=5910).

###### ¿Cómo se pueden conocer los "valores actuales" de un bien?

Usted puede consultar en cualquier momento los valores actuales de los bienes utilizando para eso el maestro de [Bienes](?p=5033) y consultar la solapa Valoraciones.  
Esta pantalla muestra el resumen de los saldos de todos los movimientos relacionados con el bien.  
Si usted hace clic sobre el icono de la lupa podrá conocer en detalle los movimientos que integran cada ítem enunciado.  
Si usted hace doble clic sobre un renglón de la consulta puede acceder en forma automática al detalle del movimiento.  
Otra opción para conocer los valores actuales de los bienes es utilizar las consultas Live. Una de las consultas que muestra los valores actuales es la de Inventario valorizado.

###### ¿Cómo puede consultar información sobre bienes y movimientos?

Usted puede consultar en cualquier momento los datos de los bienes. Para ello puede ingresar al maestro de [Bienes](?p=5033) o acceder a la consulta Live: Detalle de bienes.  
Si usted quiere además consultar los bienes y sus movimientos puede ingresar a la consulta Live de Movimientos por bien, esta consulta muestra todos los movimientos en estado 'Ingresado' o 'Definitivo' que están relacionados con el bien, o la consulta Live de Movimientos que afectan saldo, se muestran todos los movimientos en estado 'Ingresado' o 'Definitivo' que sólo afectan el saldo de bien (se excluyen Transferencias y Cambio de método de depreciación).

##### Contenidos relacionados

  * [Videos sobre bienes de uso](https://ayudas.axoft.com/24ar/videos/afa_carp_vid/bienes_afa_vid/)
