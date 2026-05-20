# Modelos de ingreso de comprobantes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_cuentcorrpago_posgv/?p=10275/

## Contenido

# Modelos de ingreso de comprobantes

Esta opción permite definir prototipos o modelos de ingreso, que luego pueden ser utilizados en el ingreso de comprobantes en el módulo Tesorería.

Estos modelos agilizan y facilitan el ingreso, ya que permiten configurar valores por defecto para los distintos datos del encabezado como de los renglones de los movimientos.  
Al parametrizar todos los campos de un modelo, quedarían como datos pendientes de ingreso, el importe de cada cuenta y la apropiación de auxiliares (si la cuenta no usa auxiliares automáticos o si no tiene reglas de apropiación asignadas).  
Desde el proceso [Movimientos de Tesorería](?p=10296) se podrá ingresar un comprobante sin una configuración previa o bien, hacer referencia a un modelo de ingreso.  
Es posible cambiar la clase de un modelo sólo si no fueron ingresadas las cuentas en la solapa Detalle del comprobante. Caso contrario, elimine las cuentas definidas en esa solapa y luego, modifique la clase del modelo.  
Para eliminar un modelo de ingreso de comprobantes, no deben existir movimientos de tesorería asociados al modelo.  
Tesorería presenta los datos de un modelo de ingreso de comprobantes en las siguientes solapas: Principal, Cotizaciones, Parámetros de la clase, Detalle del comprobante, Parámetros contables, Usuarios y Observaciones.

##### Principal

Esta solapa reúne la definición de los datos generales del encabezado y de los renglones del comprobante.  
Al crear un modelo de ingreso de comprobante, usted debe asignarle un código y una clase. Por ejemplo; puede definir un modelo con código "INGRESOS" y asignarle la clase 1 - Cobros, para ser utilizado en los comprobantes con los que registra el ingreso de valores desde el módulo Tesorería.  
Para cada dato, usted indica su comportamiento; es decir: si se edita durante el ingreso o bien, si sólo se muestra. También, se le solicita el ingreso de un valor por defecto.  
Para el encabezado del comprobante, se define el comportamiento de los siguientes datos: tipo de comprobante, fecha, concepto del asiento, clasificación, tipo de relación, código relacionado y cotización.  
Para los renglones del comprobante, configure el comportamiento de los siguientes datos: cuenta principal, cotización de otras monedas, código de operación, leyenda y código relacionado.

Valor del tipo de comprobante: el sistema valida que el tipo de comprobante ingresado afecte el módulo Tesorería y tenga asociada la misma clase que el modelo o bien, permita la edición de su clase. Para más información, consulte el proceso [Tipos de comprobante](?p=10253).

Valor de la clasificación: si está activo el [parámetro general](?p=10293) Utiliza clasificación, el sistema valida que el código ingresado de clasificación esté habilitado para el módulo Tesorería y para la clase asociada al modelo. Para más información, consulte el proceso Clasificación de comprobantes del módulo Procesos generales.

Valor del tipo de relación: si está activo el [parámetro general](?p=10293) Ingresa código de relación, elija uno de los siguientes tipos de relación: 'Cliente', 'Proveedor', 'Legajo' o 'Código de relación'. Para más información, consulte el proceso [Códigos de relación](?p=10159).

##### Cotizaciones

Ingrese las monedas a utilizar en el modelo y el tipo de cotización a aplicar.  
En esta grilla, usted selecciona las monedas de tipo 'Extranjeras contables' u 'Otra moneda'.  
Para más información, consulte los procesos Monedas y Tipos de cotización en el módulo Procesos generales.

##### Parámetros de la clase

Si la clase del modelo está comprendida entre la clase 1 y la clase 7, en esta solapa podrá definir el comportamiento de la cuenta principal y de las contracuentas.  
Si su modelo tiene asignada la clase 8 - Transferencia de cheques diferidos a banco o la clase 9 - Transferencia entre carteras, esta solapa no estará disponible ya que estas clases no son configurables.  
Para más información, consulte el proceso [Parámetros de Tesorería](?p=10293), solapa Parámetros por clase de comprobantes.

##### Detalle del comprobante

En esta solapa, usted ingresa el detalle de las [cuentas de Tesorería](?p=10235) a utilizar en el modelo.  
Es decir que podrá ingresar una cuenta principal y una o más contracuenta.  
El sistema valida que el código de cuenta ingresado exista y afecte el módulo Tesorería.  
Además, se aplicarán las validaciones correspondientes a las cuentas según la clase del modelo.  
Según la configuración del [parámetro general](?p=10293) respectivo, se solicita el ingreso del código de operación, código de relación y clasificación de cada una de las cuentas.  
Es posible ingresar la leyenda de cada renglón del comprobante.

##### Parámetros contables

Esta solapa estará habilitada sólo si su sistema se integra con el módulo Contabilidad.  
Los parámetros a configurar son los siguientes:

  * Modifica asiento en el ingreso de comprobantes: permitie editar el asiento en el momento del ingreso del comprobante.
  * Imprime asiento en el ingreso de comprobantes: permite realizar la impresión del asiento al momento de ingresar el comprobante.



Si usted permite la modificación del asiento en el ingreso de comprobantes, podrá configurar además los siguientes ítems:

  * Respeta la definición del movimiento: este parámetro afecta a los comprobantes que generan asiento. En caso de estar activo, no será posible agregar, eliminar líneas del asiento o modificar los importes. Sin embargo, podrá modificar cuentas contables según la configuración del parámetro Edita Cuenta contable del asiento.  
Este parámetro sólo permite modificar los códigos de cuenta. No es posible agregar o borrar renglones del movimiento ni modificar importes.
  * Edita cuenta contable del asiento: si genera asiento en el ingreso del comprobante, y activa este parámetro, podrá cambiar la cuenta contable.



##### Usuarios

En esta solapa se asignan los usuarios que tendrán permiso para utilizar un modelo de ingreso de comprobante.  
Por defecto, se propone el usuario "SUPERVISOR".

##### Contenidos relacionados

  * [Video sobre modelo de ingreso de comprobantes](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/modeloingrcompr_sb_vid/)

  * [Video sobre parámetros de Tesorería](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/parametrosb_sb_vid/)

  * [Video sobre usuarios, roles y permisos](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/perfiles_gral_vid/)
