# Guía sobre integración contable en Ventas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=27201/

## Contenido

# Guía sobre integración contable en Ventas

Esta guía está orientada al usuario de Contabilidad. A continuación, se detallan los pasos y el orden de configuración a seguir para implementar la integración contable entre el módulo **Ventas** y el módulo **Contabilidad**.

__Nota

Si usted es usuario de **Contabilidad** , le recomendamos la lectura de esta guía antes de empezar a operar con el módulo **Ventas**.

__Nota

Recuerde que la tecla rápida _< F3>_ permite realizar la búsqueda de un texto en el menú de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

##### Puesta en marcha

Al integrar con el módulo Contabilidad, usted debe definir algunos datos necesarios y obligatorios. Otros valores son opcionales, aunque ayudan a que la información contable sea más rica a la hora de realizar análisis contables.

  * Indique desde la opción [Monedas](?p=11956), la moneda corriente y la moneda extranjera contable, necesarias para la integración con el módulo de Contabilidad y para la integración con otros módulos como Activo Fijo y Tesorería.
  * Defina en [parámetros contables](?p=11964) del módulo Procesos generales la moneda extranjera contable habitual.
  * Ingrese los datos contables necesarios: [cuentas contables](?p=11850), [tipos de asientos](?p=11994), [auxiliares contables](?p=11969), [reglas de apropiación](?p=11974) para poder crear modelos de asientos de ventas. Tenga en cuenta que debe habilitar las cuentas, los tipos de asientos y las reglas de aplicación o de apropiación para el módulo Ventas.
  * Complete los [parámetros contables](https://ayudas.axoft.com/25ar/paramcontab_gv) del módulo Ventas, si genera asiento con el ingreso del comprobante o lo genera luego, etc.
  * Ingrese los [modelos de asientos](https://ayudas.axoft.com/25ar/modeloasientoparamcont_gv) y la parametrización contable de los [tipos de comprobantes](https://ayudas.axoft.com/25ar/tipocomprobparamcont_gv).
  * En forma opcional, usted puede definir parámetros contables para [clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv), [artículos](https://ayudas.axoft.com/25ar/articulo_carp_st), o para tipo de gastos.



Tipo de gastos:

Desde esta opción se pueden asignar a los tipos de gastos, un modelo de asiento defecto según el tipo de comprobante donde sea utilizado.

Invoque esta opción si previamente definió la integración con el módulo Contabilidad, configuración que se realiza desde [Herramientas para integración contable](?p=11936) en el módulo Procesos generales.

Luego de completar los pasos anteriores, usted está en condiciones de comenzar a generar asientos contables para las operaciones de Ventas.

##### Detalle del circuito

En este capítulo se detalla las distintas variantes que puede presentar el circuito de asientos para el módulo Ventas y su integración con Contabilidad.  
Este circuito puede tener más o menos pasos, dependiendo del escenario seleccionado.

**Primer escenario:**

  * Generación de asientos junto con el ingreso de comprobante.
  * Exportación de asiento a Contabilidad a la misma base de datos.



**Segundo escenario:**

  * No existe generación de asientos con el ingreso del comprobante.
  * Generación de asientos contable.
  * Exportación de asientos a Contabilidad a la misma base de datos.



**Tercer escenario:**

  * Generación de asientos junto al ingreso de comprobante.
  * Exportación de asiento a Contabilidad a otra base de datos.
  * Importación de asiento a Contabilidad.



**Cuarto escenario:**

  * No hay generación de asientos con el ingreso del comprobante.
  * Generación de asientos contables.
  * Exportación de asientos a Contabilidad a otra base de datos.
  * Importación de asiento a Contabilidad.



###### Generación de asientos en el ingreso del comprobante

En caso de activar el parámetro Genera asiento en el ingreso del comprobante en [parámetros contables](?p=19399) del módulo Ventas, al ingresar un nuevo comprobante de factura, nota de débito o nota de crédito, se generará el asiento correspondiente.

**Si es posible modificar el asiento en el ingreso:** porque el [perfil de facturación](?p=19399) o el tipo de comprobante lo permite, al terminar la carga del comprobante se abrirá automáticamente la pantalla del asiento, usted podrá consultar el asiento generado, realizar modificaciones e informar las apropiaciones en los casos que se requiera.

Ejemplo de asiento de factura:

El sistema completa esta pantalla tomando los datos del [modelo de asiento](?p=19368), o tomando los datos de [artículos](https://ayudas.axoft.com/25ar/articulo_carp_st) y [clientes](?p=19444).

__Nota

Si el renglón reemplaza una cuenta contable, tomará la cuenta particular del clientes, del artículo o del concepto.

**El asiento siempre se genera en la moneda del comprobante:** si el comprobante se ingresa en moneda corriente, el asiento se mostrará en moneda corriente, y si el comprobante se ingresa en moneda extranjera se mostrará en moneda extranjera.

__Nota

Denominamos moneda extranjera contable a aquella definida como habitual en parámetros contables de Procesos generales.

Si la cuenta contable del renglón del asiento tiene apertura en auxiliares y tiene asociados auxiliares contables, se habilita en el asiento la columna "Auxiliares".  
Como ejemplo. la siguiente pantalla muestra dos tipos de auxiliares, uno con auxiliares "Centro de costos" y otro con subauxiliares "Canal de venta".

El sistema completa esta pantalla:

  1. Toma las apropiaciones de [artículos](https://ayudas.axoft.com/25ar/articulo_carp_st) o [clientes](?p=19444).
  2. Toma las apropiaciones del [modelo de asiento](?p=19368).
  3. Toma las apropiaciones de la relación de [cuenta - tipo auxiliar](?p=11827) del módulo Procesos generales.



Funcionalidades de la pantalla de asientos:

**Botones de la grilla**

  * **Primero** (ir a la primera fila).
  * **Anterior** (ir a la fila anterior).
  * **Siguiente** (ir a la fila siguiente).
  * **Último** (ir a la última fila).
  * **Insertar nueva fila** <Ctrl + Ins>.
  * **Eliminar fila actual** <Ctrl + Del>.



Diferencia: corresponde al total del debe menos el total del haber. No es posible grabar un asiento con diferencia distinta a cero.

**Si no es posible modificar el asiento en el ingreso:** no se abrirá la pantalla del asiento al terminar la carga del comprobante, pero el asiento será igualmente generado.

__Nota

Para poder grabar un asiento, el sistema controla que éste balancee. Usted nunca podrá grabar asientos desbalanceados, independientemente de que haya accedido o no a la pantalla de asiento.

###### Generación de asientos luego del ingreso del comprobante

En caso de no activar el parámetro Genera asiento en el ingreso del comprobante, al ingresar un nuevo comprobante de factura, nota de débito o nota de crédito, el comprobante se grabará sin generar el asiento correspondiente.

__Nota

Todos los movimientos de tesorería (ya sean órdenes de pago, cancelación de documentos o cancelación de facturas de crédito) toman la parametrización establecida en el módulo **Tesorería**.

Para poder generar los asientos pendientes ejecute el proceso [Generación de asientos contables](?p=21464). Este proceso filtra los comprobantes con asientos sin generar, y los genera en forma masiva, teniendo en cuenta el modelo de asiento asociado al comprobante y la configuración de artículos, conceptos, clientes.  
Al finalizar, el proceso mostrará la cantidad de asientos generados, y una grilla de resultados con aquellos comprobantes en los que se encontraron problemas para generar el asiento.  
Haciendo doble clic sobre un renglón de la grilla, el sistema lo llevará a la modificación de comprobantes, allí debe ingresar a la pantalla de asiento para corregir los datos necesarios para generar el asiento contable.  
Para poder visualizar el asiento desde el subdiario de asientos y transferir la información a Contabilidad es necesario generar todos los asientos.

###### ¿Cómo modificar asientos?

Realice altas o modificaciones de asientos contables durante las siguientes instancias:

**Durante el ingreso del comprobante  
**En caso de estar permitido, al ingresar un nuevo comprobante de facturación (factura, nota de crédito, nota de débito), usted accede a la pantalla del asiento para modificar o completar las apropiaciones de los auxiliares contables.  
Para más información sobre configuración de parámetros contables consulte [Parámetros contables](?p=19399).  
Para más información sobre la modificación de asientos en el ingreso de comprobantes consulte [Imputación contable](?p=19790).

**Con posterioridad al ingreso del comprobante  
**Una vez ingresado el comprobante, usted puede acceder a la pantalla de asientos desde la opción [Modificación de comprobantes](?p=20552) para:

  * Modificar el asiento generado en el ingreso de comprobante.
  * Generar el asiento pendiente, porque se canceló en el ingreso del comprobante o porque se realiza con posterioridad al ingreso con el proceso [Generación de asientos contables](?p=21464).
  * Modificar los parámetros de la cabecera del comprobante, cambiar la opción Genera asiento o cambiar el Modelo de asiento asociado al comprobante. Al cambiar el modelo el sistema pide confirmación al usuario para regenerar el asientos contables.



__Nota

En caso de modificación de asientos ya exportados, no se verán reflejados en contabilidad y viceversa. Sugerimos identifique el número de asiento asignado en contabilidad, mediante la ficha del comprobante. Esto es de utilidad si se generan asientos resúmenes, para luego eliminar el asiento en la contabilidad, realizar la modificación en el módulo y por último exportar nuevamente hacia contabilidad.

###### ¿Cómo consultar información contable desde Ventas?

Usted puede consultar información contable desde los siguientes procesos:

**Subdiario de asientos de Ventas:  
**Desde este proceso podrá visualizar el detalle de los comprobantes que podrían formar parte de un asiento resumen, esto es de utilidad si no necesita generar un asiento por cada comprobante.  
Además, podrá verificar que los asientos estén balanceados, comprobar la utilización de cuentas inexistentes en la contabilidad y aquellos comprobantes que están pendientes de contabilizar. También aquí podrá incluir o filtrar información de auxiliares y subauxiliares.

**Consultas Live:  
**Para realizar consultas sobre la información contable con funcionalidad analítica. Por defecto usted cuenta con las siguientes opciones.

  * **Detalle por comprobante:** obtenga el detalle de las imputaciones contables, y tipo de auxiliares que ha recibido cada comprobante, según los parámetros en la consulta.
  * **Detalle por cuenta:** puede consultar detalles del comprobantes definiendo un rango de comprobantes que participan en los movimientos de cada cuenta, e ingresando los importes del debe, haber o saldo.
  * **Detalle por auxiliar:** consulte las imputaciones, agrupadas por auxiliares contables. Conozca el porcentaje de apropiación seleccionando los importes debe, haber o saldo.
  * **Detalle por subauxiliar:** obtenga un detalle de los tipo de auxiliares que se encuentran agrupados, y consulte, entre otros, datos como imputaciones contable o apropiaciones, ingresando por los importes debe, haber o saldo.
  * **Contabilización de comprobantes:** obtenga información sobre la contabilización de un comprobante y acceda a su ficha, desde el campo número de comprobante.
  * **Multidimensional de asientos:** confeccione una consulta multidimensional con datos del comprobante, cliente, imputación contable, tipos de auxiliares y subauxiliares, entre otros, para un determinado rango.



**Ficha del comprobante  
**Acceda a la misma desde [Modificación de comprobantes](?p=20552) o desde una consulta Live (funcionalidad no disponible en productos Restô), donde encontrará información relacionada con: artículos, vencimientos, imputaciones contables, valores y totales, entre otros.  
Desde la ficha del comprobante, podrá tener acceso al asiento generado en la contabilidad.

Más información:

Tenga presente que los datos pueden diferir de los registrados en la contabilidad, ya sea porque el asiento ha sido modificado (en la contabilidad o en el módulo luego de su exportación), o porque se generó la exportación agrupando en asientos resúmenes los comprobantes y no un asiento por cada comprobante.

**Ejemplo...  
**Ingrese a la opción Ventas de Live.  
Genere una consulta de facturación de ventas, seleccionando Consulta dentro de la carpeta Facturación.  
Seleccione los filtros por los cuales buscará el comprobante.  
Realice un clic sobre el número del comprobante para acceder a la ficha correspondiente.  
Una vez en la ficha del comprobante, desde el menú acciones o desde el panel de acciones consulte el asiento contable para dicho comprobante.

###### ¿Cómo ver informes de control?

Consulte los siguientes procesos de control desde informes o consultas Live, ellos le permitirán ver el estado de los asientos contables: pendientes de generar, pendientes de exportar y número de asiento asignado.

**Subdiario de Ventas  
**Desde este proceso podrá visualizar el detalle de los comprobantes que lo agrupan, ver comprobantes en los cuales sus asientos no balancean, que contengan cuentas inexistentes en contabilidad y aquellos comprobantes que están pendientes de contabilizar. También aquí podrá incluir o filtrar información de auxiliares y subauxiliares.

**Exportación de asientos contables  
**Obtenga información de los asientos generados en este procesos seleccionado la opción Visualiza asientos exportados.

**Consultas Live  
**Desde aquí podrá ver información de control utilizando el siguiente proceso Live.

Contabilización de comprobantes: obtenga información sobre la contabilización del mismo y acceda a su ficha, desde el campo número de comprobante.

###### ¿Cómo eliminar asientos?

Puede realizar la [eliminación de asientos contables](?p=21193) utilizando los siguientes criterios de selección: por fecha de emisión o contable, comprobantes con asiento generado o exportado.  
Complete la grilla con los comprobantes obtenidos, en caso de necesitar hacer una selección individual utilice las opciones del botón derecho del mouse para seleccionar o deseleccionar todos los comprobantes.

###### Exportación de asientos a Contabilidad

Una vez generados los asientos de todos los comprobantes, está en condiciones se realizar la [Exportación de asientos contables](?p=27238) al módulo Contabilidad.  
Puede controlar los comprobantes que no tienen asientos generados utilizando el subdiario de asientos, o desde el proceso de exportación.  
Los destinos de exportación posibles son:

  * **Base de datos actual:** para el caso en que tenga instalado el módulo Contabilidad, el traspaso será directo a contabilidad, y no será necesario realizar una importación de asientos.
  * **Otra base de datos:** si no tiene instalado el módulo Contabilidad debe seleccionar esta. El proceso generará un archivo denominado por defecto "Asiento_GV.zip" que será importado desde el módulo Contabilidad.



Para más información sobre el circuito general de asientos y su integración con los módulos Procesos generales y Contabilidad consulte la [Guía sobre implementación para integración contable](?p=11899) en la ayuda del módulo Procesos generales.

###### Importación de asientos contables

Si en la exportación de asiento usted seleccionó 'otra base de datos' como destino de exportación, después de generar el archivo zip debe importarlo desde el proceso [Importación de asientos contables](?p=9789) del módulo Contabilidad.  
Seleccione 'Formato Astor' y el módulo. Para obtener más más información sobre la integración del sistema, consulte [Herramientas para situación contable](?p=11936) del módulo Procesos generales.  
Al importar un archivo con 'Formato Astor' usted puede controlar si el lote ya fue importado, o si el detalle de comprobantes está participando de algún asiento ingresado.  
Cuando el proceso de importación finaliza, se emite una grilla con los resultados de la importación, asientos importados, y asientos rechazados.

##### Contenidos relacionados

  * [Video sobre automatización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Video sobre parametrización contable centralizada](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralizaparamcontab_gral_vid/)

  * [Videos sobre auxiliares contables y contabilidad por proyectos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/conproyectos_cna_vid/)
