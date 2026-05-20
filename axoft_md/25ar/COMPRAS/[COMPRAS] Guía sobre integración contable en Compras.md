# Guía sobre integración contable en Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_integrcontabl_cp2/

## Contenido

# Guía sobre integración contable en Compras

Esta guía está orientada al usuario de Contabilidad. A continuación, se detallan los pasos y el orden de configuración a seguir para implementar la integración contable entre el módulo Compras y el módulo Contabilidad.

__Nota

Si usted es usuario de **Contabilidad** , le recomendamos la lectura de esta guía antes de empezar a operar con el módulo **Compras**. Recuerde que la tecla rápida <F3> permite realizar la búsqueda de un texto en el menú de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

##### Puesta en marcha

Al integrar con el módulo Contabilidad, usted debe definir algunos datos necesarios y obligatorios. Otros valores son opcionales, aunque ayudan a que la información contable sea más rica a la hora de realizar análisis contables.

  * Indique desde la [opción monedas](?p=11956), la moneda corriente y la moneda extranjera contable, necesarias para la integración con el módulo de Contabilidad y para la integración con otros módulos como Activo Fijo y Tesorería.
  * Defina en [parámetros contables](?p=11964) del módulo Procesos generales la moneda extranjera contable habitual.
  * Ingrese los datos contables necesarios [cuentas contables](?p=11850), [tipos de asiento](?p=11994), [auxiliares contables](?p=11835), [reglas de apropiación](?p=11974) para poder crear modelos de asientos de compras.Tenga en cuenta que debe habilitar las cuentas, los tipos de asientos y las reglas de aplicación o de apropiación para el módulo Compras.
  * Complete los [parámetros contables](https://ayudas.axoft.com/25ar/paramcontparam_cp2) del módulo Compras, si genera asiento con el ingreso del comprobante o lo genera luego, etc.
  * Ingrese los [modelos de asientos](https://ayudas.axoft.com/25ar/paramcontmodasiento_cp2) y la parametrización contable de los [tipos de comprobantes](https://ayudas.axoft.com/25ar/paramcontipocomprob_cp2).
  * En forma opcional, usted puede definir parámetros contables para [proveedores,](https://ayudas.axoft.com/25ar/paramcontproveed_cp2) artículos, [conceptos](https://ayudas.axoft.com/25ar/paramcontconcepcp_cp2) o [para tipo de gastos](https://ayudas.axoft.com/25ar/paramcontipogasto_cp2).



Luego de completar los pasos anteriores, usted está en condiciones de comenzar a generar asientos contables para las operaciones de Compras.

##### Detalle del circuito

En este capítulo se detalla las distintas variantes que puede presentar el circuito de asientos para el módulo Compras y su integración con Contabilidad.  
Este circuito puede tener más o menos pasos, dependiendo del escenario seleccionado.

**Primer escenario:**

  * Generación de asientos junto con el ingreso de comprobante
  * Exportación de asiento a Contabilidad a la misma base de datos



**Segundo escenario:**

  * No existe generación de asientos con el ingreso del comprobante.
  * Generación de asientos contable
  * Exportación de asientos a Contabilidad a la misma base de datos



**Tercer escenario:**

  * Generación de asientos junto al ingreso de comprobante.
  * Exportación de asiento a Contabilidad a otra base de datos.
  * Importación de asiento a Contabilidad.



**Cuarto escenario:**

  * No hay generación de asientos con el ingreso del comprobante.
  * Generación de asientos contables.
  * Exportación de asientos a Contabilidad a otra base de datos.
  * Importación de asiento a Contabilidad.



[/axcond][/axcond] 

**Generación de asientos en el ingreso del comprobante  
**En caso de activar el parámetro Genera asiento en el ingreso del comprobante en [parámetros contables](https://ayudas.axoft.com/25ar/paramcontparam_cp2) del módulo Compras, al ingresar un nuevo comprobante de factura, nota de débito o nota de crédito, se generará el asiento correspondiente.

  * Si es posible modificar el asiento en el ingreso: porque el [perfil de facturación](https://ayudas.axoft.com/25ar/perffacturacp_cp2) o el [tipo de comprobante](https://ayudas.axoft.com/25ar/paramcontipogasto_cp2) lo permite, al terminar la carga del comprobante se abrirá automáticamente la pantalla del asiento, usted podrá consultar el asiento generado, realizar modificaciones e informar las apropiaciones en los casos que se requiera.  
El sistema completa esta pantalla tomando los datos del [modelo de asiento](https://ayudas.axoft.com/25ar/paramcontmodasiento_cp2), o tomando los datos de artículos, artículos con escalas, [conceptos](https://ayudas.axoft.com/25ar/paramcontconcepcp_cp2), [proveedores](https://ayudas.axoft.com/25ar/paramcontproveed_cp2).  
Si el renglón reemplaza una cuenta contable, tomará la cuenta particular del proveedor, del artículo o del concepto.
  * El asiento siempre se genera en la moneda del comprobante: si el comprobante se ingresa en moneda corriente, el asiento se mostrará en moneda corriente, y si el comprobante se ingresa en moneda extranjera se mostrará en moneda extranjera. Denominamos moneda extranjera contable a aquella definida como habitual en [parámetros contables](?p=11964) de Procesos generales.  
Si la cuenta contable del renglón del asiento tiene apertura en auxiliares y tiene asociados auxiliares contables, se habilita en el asiento la columna "Auxiliares".  
El sistema completa esta pantalla:



  * Toma las apropiaciones de artículos, artículos con escalas, [conceptos](https://ayudas.axoft.com/25ar/paramcontconcepcp_cp2) o [proveedores](https://ayudas.axoft.com/25ar/paramcontproveed_cp2).
  * Toma las apropiaciones del [modelo de asiento](https://ayudas.axoft.com/25ar/paramcontmodasiento_cp2).
  * Toma las apropiaciones de la relación de [cuenta - tipo auxiliar](?p=11827) del módulo Procesos generales.


* Si no es posible modificar el asiento en el ingreso: no se abrirá la pantalla del asiento al terminar la carga del comprobante, pero el asiento será igualmente generado.

Para poder grabar un asiento, el sistema controla que éste balancee. Usted nunca podrá grabar asientos desbalanceados, independientemente de que haya accedido o no a la pantalla de asiento.

**Generación de asientos luego del ingreso del comprobante  
**En caso de no activar el parámetro Genera asiento en el ingreso del comprobante, al ingresar un nuevo comprobante de factura, nota de débito o nota de crédito, el comprobante se grabará sin generar el asiento correspondiente.

__Nota

Todos los movimientos de tesorería (ya sean ordenes de pago, cancelación de documentos o cancelación de facturas de crédito) toman la parametrización establecida en el módulo Tesorería.

Para poder generar los asientos pendientes ejecute el proceso [Generación de asientos contables.](https://ayudas.axoft.com/25ar/generasientcont_cp2) Este proceso filtra los comprobantes con asientos sin generar, y los genera en forma masiva, teniendo en cuenta el modelo de asiento asociado al comprobante y la configuración de artículos, artículos con escalas, conceptos, proveedores.  
Al finalizar, el proceso mostrará la cantidad de asientos generados, y una grilla de resultados con aquellos comprobantes en los que se encontraron problemas para generar el asiento.  
Haciendo doble clic sobre un renglón de la grilla, el sistema lo llevará a la modificación de comprobantes, allí debe ingresar a la pantalla de asiento para corregir los datos necesarios para generar el asiento contable.  
Para poder visualizar el asiento desde el subdiario de asientos y transferir la información a Contabilidad, es necesario generar todos los asientos.

**¿Cómo modificar asientos?  
**Realice altas o modificaciones de asientos contables durante las siguientes instancias.

_Durante el ingreso del comprobante  
_En caso de estar permitido, al ingresar un nuevo comprobante de facturación (factura, nota de crédito, nota de débito), usted accede a la pantalla del asiento para modificar o completar las apropiaciones de los auxiliares contables.  
Para más información sobre configuración de parámetros contables consulte [Parámetros contables](https://ayudas.axoft.com/25ar/paramcontparam_cp2), [Tipos de comprobantes](https://ayudas.axoft.com/25ar/tipocomprobante_cp2), [Perfiles de facturas de compras](https://ayudas.axoft.com/25ar/perffacturacp_cp2).  
Para más información sobre la modificación de asientos en el ingreso de comprobantes consulte [Imputación contable](?p=15557#imputcontablcont).

_Con posterioridad al ingreso del comprante  
_Una vez ingresado el comprobante, usted puede acceder a la pantalla de asientos desde la opción [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modificomprob_cp2) para:

  * Modificar el asiento generado en el ingreso de comprobante.
  * Generar el asiento pendiente, porque se canceló en el ingreso del comprobante o porque se realiza con posterioridad al ingreso con el proceso [Generación de asientos contables.](https://ayudas.axoft.com/25ar/generasientcont_cp2)
  * Modificar los parámetros de la cabecera del comprobante, cambiar la opción Genera asiento o cambiar el Modelo de asiento asociado al comprobante. Al cambiar el modelo el sistema pide confirmación al usuario para regenerar el asientos contables.



En caso de modificación de asientos ya exportados, no se verán reflejados en contabilidad y viceversa. Sugerimos identifique el número de asiento asignado en contabilidad, mediante la ficha del comprobante. Esto es de utilidad si se generan asientos resúmenes, para luego eliminar el asiento en la contabilidad, realizar la modificación en el módulo y por último exportar nuevamente hacia contabilidad.

**¿Cómo consultar información contable desde Compras?  
**Usted puede consultar información contable desde los siguientes procesos:

_Subdiario de asientos de compras  
_Desde este proceso podrá visualizar el detalle de los comprobantes que podrían formar parte de un asiento resumen, esto es de utilidad si no necesita generar un asiento por cada comprobante.  
Además, podrá verificar que los asientos estén balanceados, comprobar la utilización de cuentas inexistentes en la contabilidad y aquellos comprobantes que están pendientes de contabilizar. También aquí podrá incluir o filtrar información de auxiliares y subauxiliares.

_Consultas Live  
_Para realizar consultas sobre la información contable con funcionalidad analítica. Por defecto usted cuenta con las siguientes opciones.

  * Detalle por comprobante:  
Obtenga el detalle de las imputaciones contables, y tipo de auxiliares que ha recibido cada comprobante, según los parámetros en la consulta.
  * Detalle por cuenta:  
Puede consultar detalles del comprobantes definiendo un rango de comprobantes que participan en los movimientos de cada cuenta, e ingresando los importes del debe, haber o saldo.
  * Detalle por auxiliar:  
Consulte las imputaciones, agrupadas por auxiliares contables. Conozca el porcentaje de apropiación seleccionando los importes debe, haber o saldo.
  * Detalle por subauxiliar:  
Obtenga un detalle de los tipo de auxiliares que se encuentran agrupados, y consulte, entre otros, datos como imputaciones contable o apropiaciones, ingresando por los importes debe, haber o saldo.
  * Contabilización de comprobantes:  
Obtenga información sobre la contabilización de un comprobante y acceda a su ficha, desde el campo número de comprobante.
  * Multidimensional de asientos:  
Confeccione una consulta multidimensional con datos del comprobante, proveedor, imputación contable, tipos de auxiliares y subauxiliares, entre otros, para un determinado rango.



_Ficha del comprobante  
_Acceda a la misma desde [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modificomprob_cp2) o desde una consulta Live, donde encontrará información relacionada con: artículos, vencimientos, imputaciones contables, valores y totales, entre otros.  
Desde la ficha del comprobante, podrá tener acceso al asiento generado en la contabilidad.

__Nota

Tenga presente que los datos pueden diferir de los registrados en la contabilidad, ya sea porque el asiento ha sido modificado (en la contabilidad o en el módulo luego de su exportación), o porque se generó la exportación agrupando en asientos resúmenes los comprobantes y no un asiento por cada comprobante.

**¿Cómo ver informes de control?  
**Consulte los siguientes procesos de control desde informes o consultas Live, ellos le permitirán ver el estado de los asientos contables: pendientes de generar, pendientes de exportar y número de asiento asignado.

_Subdiario de asientos de compras  
_Desde este proceso podrá visualizar el detalle de los comprobantes que lo agrupan, ver comprobantes en los cuales sus asientos no balancean, que contengan cuentas inexistentes en contabilidad y aquellos comprobantes que están pendientes de contabilizar. También aquí podrá incluir o filtrar información de auxiliares y subauxiliares.  
Es especialmente útil si genera asientos resumen.

_Exportación de asientos contables  
_Obtenga información de los asientos generados en este procesos seleccionado la opción Visualiza asientos exportados.

_Consultas Live  
_Desde aquí podrá ver información de control utilizando el siguiente proceso Live.

  * Contabilización de comprobantes:  
Obtenga información sobre la contabilización del mismo y acceda a su ficha, desde el campo número de comprobante.



**¿Cómo eliminar asientos?  
**Puede realizar la [eliminación de asientos contables](https://ayudas.axoft.com/25ar/elimiasientcont_cp2) del módulo Compras desde la opción Contabilización disponible desde Procesos periódicos, utilizando los siguientes criterios de selección: por fecha de emisión o contable, comprobantes con asiento generado o exportado.  
Complete la grilla con los comprobantes obtenidos, en caso de necesitar hacer una selección individual utilice las opciones del botón derecho del mouse para seleccionar o deseleccionar todos los comprobantes.

**Exportación de asientos a Contabilidad  
**Una vez generados los asientos de todos los comprobantes, está en condiciones se realizar la [Exportación de asientos contables](https://ayudas.axoft.com/25ar/exportasientcontab_cp2) al módulo Contabilidad.  
Puede controlar los comprobantes que no tienen asientos generados utilizando el subdiario de asientos, o desde el proceso de exportación.  
Los destinos de exportación posibles son:

  * Base de datos actual: para el caso en que tenga instalado el módulo Contabilidad, el traspaso será directo a contabilidad, y no será necesario realizar una importación de asientos.
  * Otra base de datos: si no tiene instalado el módulo Contabilidad debe seleccionar esta. El proceso generará un archivo denominado por defecto "Asiento_CP.zip" que será importado desde el módulo Contabilidad.



Para más información sobre el circuito general de asientos y su integración con los módulos Procesos generales y Contabilidad consulte la [Guía de implementación para integración contable](?p=11899).

**Importación de asientos contables  
**Si en la exportación de asiento usted seleccionó 'otra base de datos' como destino de exportación, después de generar el archivo zip debe importarlo desde el proceso [Importación de asientos contables](?p=9789) del módulo Contabilidad. Si el archivo a importar proviene de un sistema que se integra con Contabilidad seleccione 'Formato Tango Astor' y módulo 'Proveedores/Compras'.  
Para obtener más más información sobre la integración del sistema, consulte [Herramientas para situación contable](?p=11936) del módulo Procesos generales.  
Al importar un archivo con 'Formato Tango Astor' usted puede controlar si el lote ya fue importado, o si el detalle de comprobantes está participando de algún asiento ingresado.  
Cuando el proceso de importación finaliza, se emite una grilla con los resultados de la importación, asientos importados, y asientos rechazados.

##### Contenidos relacionados

  * [Video sobre automatización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Videos sobre auxiliares contables y contabilidad por proyectos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/conproyectos_cna_vid/)
