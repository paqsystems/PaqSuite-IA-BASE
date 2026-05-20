# Guía sobre integración contable en IVA + Ingresos Brutos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_iv/guia_integrcontabl_guia_iva/

## Contenido

# Guía sobre integración contable en IVA + Ingresos Brutos

Esta guía está orientada a aquellas personas que generen o consulte información contable dentro del módulo Liquidador de IVA. A continuación detallamos los pasos para configurar el sistema, conocer el circuito contable completo y qué informes y consultas puede utilizar para visualizar información contable.

##### Puesta en marcha de la integración contable en el módulo IVA + Ingresos Brutos

  * Indique desde la opción [monedas](?p=11956) la moneda corriente y la moneda extranjera contable, necesarias para la integración con el módulo Contabilidad.
  * Defina en [parámetros contables](?p=11964) del módulo Procesos generales la moneda extranjera contable habitual.
  * Ingrese los datos contables necesarios [cuentas contables](?p=11850), [tipos de asientos](?p=11994), [auxiliares contables](?p=11969), [reglas de apropiación](?p=11974) para poder crear los modelos de ingreso de comprobantes del Liquidador de IVA. Tenga en cuenta que debe habilitar las cuentas, los tipos de asientos y las reglas de apropiación para el módulo Liquidador de IVA.
  * Complete los [parámetros contables](?p=8424) del módulo Liquidador de IVA si genera asiento con el ingreso del comprobante o lo genera luego, etc.
  * Ingrese la parametrización contable de los [tipos de comprobantes](?p=8444).
  * En forma opcional, usted puede definir parámetros contables para [clientes](?p=19444) y [proveedores](?p=14686).



Luego de completar los pasos anteriores, usted está en condiciones de comenzar a generar asientos contables para los comprobantes registrados en el módulo Liquidador de IVA.

##### Detalle del circuito de integración contable en el módulo IVA + Ingresos Brutos

En este capítulo se detalla las distintas variantes que puede presentar el circuito de asientos para el módulo Liquidador de IVA y su integración con Contabilidad.

Este circuito puede tener más o menos pasos, dependiendo del escenario seleccionado.

**Primer escenario:**

  * Generación de asientos junto con el ingreso de comprobante
  * Exportación de asiento a Contabilidad a la misma base de datos



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

En caso de activar el parámetro Genera asiento en el ingreso del comprobante en [parámetros contables](?p=8424) del módulo Liquidador de IVA, al ingresar un nuevo comprobante se generará el asiento correspondiente.

  * Si es posible modificar el asiento en el ingreso: porque el [tipo de comprobante](?p=8444) lo permite, al terminar la carga del comprobante se abrirá automáticamente la pantalla del asiento, usted podrá consultar el asiento generado, realizar modificaciones e informar las apropiaciones en los casos que se requiera.
  * Si no es posible modificar el asiento en el ingreso: no se abrirá la pantalla del asiento al terminar la carga del comprobante, pero el asiento será igualmente generado.



**Ejemplo de asiento de factura:**

Si el renglón reemplaza una cuenta contable, tomará la cuenta particular del cliente o proveedor dependiendo del tipo de comprobante ingresado.

__Nota

Para poder grabar un asiento, el sistema controla que éste balancee. Usted nunca podrá grabar asientos desbalanceados, independientemente de que haya accedido o no a la pantalla de asiento.

###### Generación de asientos luego del ingreso del comprobante

En caso de no activar el parámetro Genera asiento en el ingreso del comprobante, éste se grabará sin generar el asiento correspondiente.

Para poder generar los asientos pendientes ejecute el proceso [Generación de asientos contables](?p=8364). Este proceso filtra los comprobantes con asientos sin generar, y los genera en forma masiva, teniendo en cuenta el modelo de ingreso asociado al comprobante y la configuración de clientes y proveedores.

Al finalizar, el proceso mostrará la cantidad de asientos generados, y una grilla de resultados con aquellos comprobantes en los que se encontraron problemas para generar el asiento.

Haciendo doble clic sobre un renglón de la grilla, el sistema lo llevará a la modificación de comprobantes, allí debe ingresar a la pantalla de asiento para corregir los datos necesarios para generar el asiento contable.

Para poder visualizar el asiento desde el subdiario de asientos y transferir la información a Contabilidad, es necesario generar todos los asientos.

###### ¿Cómo modificar asientos?

Realice altas o modificaciones de asientos contables durante las siguientes instancias:

Durante el ingreso del comprobante:

En caso de estar permitido, al ingresar un nuevo comprobante, usted accede a la pantalla del asiento para modificar o completar las apropiaciones de los auxiliares contables.

Para más información sobre configuración de parámetros contables consulte [Parámetros contables](?p=8424).

Con posterioridad al ingreso del comprobante:

na vez ingresado el comprobante, usted puede acceder a la pantalla de asientos desde la opción [Registración de comprobantes](?p=8433) para:

  * Modificar el asiento generado en el ingreso de comprobante.
  * Generar el asiento pendiente, porque se canceló en el ingreso del comprobante o porque se realiza con posterioridad al ingreso con el proceso [Generación de asientos contables](?p=8364).
  * Modificar los parámetros de la cabecera del comprobante, cambiar la opción Genera asiento.



__Nota

En caso de modificación de asientos ya exportados, no se verán reflejados en contabilidad y viceversa. Sugerimos identifique el número de asiento asignado en contabilidad, mediante la ficha del comprobante. Es de utilidad si se generan asientos resúmenes, para luego eliminar el asiento en la contabilidad, realizar la modificación en el módulo y por último exportar nuevamente hacia contabilidad.

###### ¿Cómo consultar información contable desde Liquidador de IVA?

Usted puede consultar información contable desde los siguientes procesos:

Subdiario de asientos de Liquidador de IVA

Desde este proceso podrá visualizar el detalle de los comprobantes que podrían formar parte de un asiento resumen, esto es de utilidad si no necesita generar un asiento por cada comprobante.

Además, podrá verificar que los asientos estén balanceados, comprobar la utilización de cuentas inexistentes en la contabilidad y aquellos comprobantes que están pendientes de contabilizar. También aquí podrá incluir o filtrar información de auxiliares y subauxiliares.

Consultas Live

Para realizar consultas sobre la información contable con funcionalidad analítica. Por defecto usted cuenta con las siguientes opciones.

  * Detalle por comprobante: obtenga el detalle de las imputaciones contables, y tipo de auxiliares que ha recibido cada comprobante, según los parámetros en la consulta.
  * Detalle por cuenta: puede consultar detalles del comprobantes definiendo un rango de comprobantes que participan en los movimientos de cada cuenta, e ingresando los importes del debe, haber o saldo.
  * Detalle por auxiliar: consulte las imputaciones, agrupadas por auxiliares contables. Conozca el porcentaje de apropiación seleccionando los importes debe, haber o saldo.
  * Detalle por subauxiliar: obtenga un detalle de los tipos de auxiliares que se encuentran agrupados, y consulte, entre otros, datos como imputaciones contables o apropiaciones, ingresando por los importes debe, haber o saldo.
  * Contabilización de comprobantes: obtenga información sobre la contabilización de un comprobante y acceda a su ficha, desde el campo número de comprobante.
  * Multidimensional de asientos: confeccione una consulta multidimensional con datos del comprobante, cliente, imputación contable, tipos de auxiliares y subauxiliares, entre otros, para un determinado rango.



Ficha del comprobante

Desde la ficha del comprobante, podrá tener acceso al asiento generado en la contabilidad.

__Nota

Tenga presente que los datos pueden diferir de los registrados en la contabilidad, ya sea porque el asiento ha sido modificado (en la contabilidad o en el módulo luego de su exportación), o porque se generó la exportación agrupando en asientos resúmenes los comprobantes y no un asiento por cada comprobante.

###### ¿Cómo ver informes de control?

Consulte los siguientes procesos de control desde informes o consultas Live, ellos le permitirán ver el estado de los asientos contables: pendientes de generar, pendientes de exportar y número de asiento asignado.

**Subdiario de asientos de Liquidador de IVA**

Desde este proceso podrá visualizar el detalle de los comprobantes que lo agrupan, ver comprobantes en los cuales sus asientos no balancean, que contengan cuentas inexistentes en contabilidad y aquellos comprobantes que están pendientes de contabilizar. También aquí podrá incluir o filtrar información de auxiliares y subauxiliares.

**Exportación de asientos contables**

Obtenga información de los asientos generados en este proceso, seleccionando la opción Visualiza asientos exportados.

**Consultas Live**

Desde aquí podrá ver información de control utilizando el siguiente proceso Live.

Contabilización de comprobantes

Obtenga información sobre la contabilización del mismo, y acceda a su ficha desde el campo número de comprobante.

###### ¿Cómo eliminar asientos?

Puede realizar la [eliminación de asientos contables](?p=8375) utilizando criterios de selección.

Los criterios de selección son los siguientes: por fecha de emisión o contable, comprobantes con asiento generado o exportado.

Complete la grilla con los comprobantes obtenidos, en caso de necesitar hacer una selección individual utilice las opciones del botón derecho del mouse para seleccionar o deseleccionar todos los comprobantes.

###### Exportación de asientos a Contabilidad

Una vez generados los asientos de todos los comprobantes, está en condiciones se realizar la [Exportación de asientos contables](?p=8380) al módulo Contabilidad.

Puede controlar los comprobantes que no tienen asientos generados utilizando el subdiario de asientos, o desde el proceso de exportación.

Los destinos de exportación posibles son:

  * Base de datos actual: para el caso en que tenga instalado el módulo Contabilidad, el traspaso será directo a contabilidad, y no será necesario realizar una importación de asientos.
  * Otra base de datos: si no tiene instalado el módulo Contabilidad debe seleccionar esta opción. El proceso generará un archivo denominado por defecto "Asiento_IV.zip" que será importado desde el módulo Contabilidad, o un archivo llamado "ExpIV42.zip" en el caso de seleccionar formato Tango, para ser luego importado desde Contabilidad.



Para más información sobre el circuito general de asientos y su integración con los módulos Procesos generales y Contabilidad consulte la [Guía sobre implementación para integración contable](?p=11899) correspondiente al módulo Procesos generales.

###### Importación de asientos contables

Si en la exportación de asiento usted seleccionó 'otra base de datos' como destino de exportación, después de generar el archivo zip debe importarlo desde el proceso Importación de asientos contables del módulo Contabilidad.

Para importarlo seleccione cómo módulo de origen 'Liquidador de IVA'.

Para obtener más más información sobre la integración del sistema, consulte [Herramientas para situación contable](?p=11936) del módulo Procesos generales.

Cuando el proceso de importación finaliza, se emite una grilla con los resultados de la importación, asientos importados, y asientos rechazados.

##### Contenidos relacionados

  * [Video sobre automatización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/25ar/videos/iva_carp_vid/)

  * [Videos sobre auxiliares contables y contabilidad por proyectos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/conproyectos_cna_vid/)
