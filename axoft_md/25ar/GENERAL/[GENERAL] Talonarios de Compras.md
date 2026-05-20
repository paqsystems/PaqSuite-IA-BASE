# Talonarios de Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiacamposadicionales_gla/?p=14699/

## Contenido

# Talonarios de Compras

Este proceso permite definir los distintos talonarios a utilizar en aquellas opciones en las que se emiten comprobantes. La asignación de talonarios facilita el control de la impresión y la numeración de los comprobantes.

Los comprobantes que utilizan talonarios para su emisión son: 

  * Retenciones y/o constancias provisionales de retención
  * Solicitudes de compra
  * Órdenes de compra
  * Recepción (informe de recepción en el ingreso de remitos)
  * Devoluciones
  * Órdenes de importación
  * Recepción por despacho
  * Retenciones y/o constancias provisionales de retención
  * Órdenes de pago
  * Órdenes de pago de aceptación de factura de crédito



##### Principal

En la solapa Principal se van a ingresar los datos comunes a todos los tipos de talonario, los mismos se detallan a continuación.

Número de talonario: número que identifica al talonario.

Descripción: es un campo opcional. Puede utilizarlo para describir el talonario definido.

Tipo de comprobante: defina aquí el tipo de comprobantes que va a generar con el talonario.

Sucursal asociada: en el caso de las solicitudes de compra y de órdenes de importación, el número de comprobante estará formado por 13 dígitos. Los primeros 5 que son fijos por talonario corresponden a la sucursal, y se deben ingresar en este campo.  
Esto permite que se habiliten distintos talonarios de solicitud de compra o de importación por cada sucursal o sector. En el caso de los otros comprobantes que utilizan talonarios (recepción y devolución), el número de comprobante se compondrá de 8 dígitos numéricos. En las retenciones, ingrese la sucursal que formará parte del número de certificado. Para las retenciones generadas de IVA y Ganancias, este dato es requerido por SIAp-SICORE. 

__Nota

No es posible generar varios talonarios para órdenes de pago utilizando el mismo número de sucursal.

__Nota

Defina el criterio más apropiado de acuerdo al uso del talonario.

Edita numeración durante el ingreso de comprobantes: permite indicar si el comprobante se numera en forma automática o si se permite la modificación manual en el momento del ingreso. Para las retenciones no está disponible esta opción. 

Rango de números habilitados: estos campos indican el primer y último número habilitado de cada talonario y se utilizan para control en los procesos de emisión de comprobantes.

Próximo número a emitir: indica cuál será el próximo número de comprobante a emitir al utilizar el talonario.

Sucursal destino: informe la sucursal destino a la que serán enviadas las órdenes de compra o los remitos para continuar su circuito. Este valor será tomado por defecto para el ingreso de las órdenes de compra y los remitos, el cual luego se utiliza para filtrar la exportación. En la importación también se valida que sea la sucursal correcta. Si al realizar la transferencia no informa la sucursal destino no se aplicará el filtro por sucursal y podrán ser importadas en cualquier sucursal.

Método de exportación de órdenes de compra: este control permite definir cómo y en qué empresa se continua el circuito de la orden de compra, es decir, si al exportar una orden de compra se factura y/o Remite en la empresa origen o en destino.

__Importante

Importante: una vez que las órdenes de compra se exporten, quedarán de la siguiente manera, según el método de exportación configurado en el talonario.

Valores posibles:

  * **Remite y factura en destino:** al exportar las órdenes de compra, en la empresa origen quedarán con las cantidades remitidas y facturadas. En empresa destino quedarán pendientes de remitir y de facturar.
  * **Remite en sucursal de origen y factura en destino:** al exportar las órdenes de compra, en origen quedarán pendientes de remitir y con las cantidades ya facturadas. Y en destino pendientes de facturar y con las cantidades remitidas.
  * **Factura en sucursal de origen y remite en destino:** al exportar las órdenes de compra, en origen quedarán pendientes de facturar y con las cantidades remitidas. Y en destino pendientes de remitir y con las cantidades ya facturadas.
  * **No controla:** las órdenes de compra podrán ser remitidas y/o facturadas en la empresa destino solo cuando no haya cantidades facturadas ni remitidas.



__Nota

Tenga en cuenta que en el caso de dar de alta talonarios usando API, el método de exportación deberá ser 'No controla' para los talonarios que no sean de orden de compra. Y para el caso de modificación de talonarios de órdenes de compra si se modifica el método de exportación, no se actualizará el método de exportación a las órdenes de compra pendientes.

##### Impresión

Destino de impresión: el uso de este campo es opcional. Permite definir un destino de impresión que será tomado por defecto al realizar un comprobante.  
Puede indicar la impresora por defecto en la que desea imprimir los comprobantes. Si no ingresa ninguna, debe indicar el destino al emitir el comprobante.  
Si no encuentra la impresora que desea utilizar, pulse el botón "Actualizar".  
En el momento de emitir el comprobante, el sistema valida que exista la impresora indicada. Si existe, imprimirá directamente en la impresora correspondiente al talonario. Si la impresora no existe, informará el inconveniente y permitirá seleccionar la impresora a utilizar, sugiriendo la impresora por defecto de Windows.

Más información:

En el caso de utilizar impresoras de red, es muy importante que todos los usuarios utilicen el mismo nombre para identificar a cada impresora por la que se emitirán comprobantes.  
Tenga en cuenta que las impresoras que se muestran después de actualizar son aquellas que pertenecen a la terminal Tango donde se esta accediendo.

Cantidad máxima de renglones durante el ingreso de un comprobante: en este campo se ingresará la cantidad máxima de renglones que puede tener un comprobante. En el caso que el comprobante deba imprimirse en un solo formulario, esta cantidad debe ser igual a la cantidad de iteraciones indicada en la definición del formulario correspondiente. En todos los casos, esta cantidad debe ser menor o igual a 100. Si la cantidad es mayor a la indicada en la definición del formulario, el sistema realizará transporte en forma automática, utilizando más de una hoja para el mismo comprobante. 

Formularios: en esta grilla usted puede indicar el formulario a utilizar para los diferentes tipos de comprobantes, definiendo de esta manera el formato de impresión de cada uno. Es posible elegir un formulario para ser utilizado por defecto en el momento de emitir el comprobante.  
El sistema habilita los tipos de comprobante de acuerdo al campo Tipo de comprobante ingresado en la [solapa Principal](https://ayudas.axoft.com/25ar/talonario_cp2#principal) del talonario.  
Si el tipo de comprobante ingresado es una orden de pago, el sistema habilita dos formularios para ser utilizados. Un formulario para ser utilizado en la impresión de la orden de pago respectivamente y un formulario para la aceptación de facturas de crédito.  
Para emitir un comprobante con un dibujo diferente, realice los siguientes pasos:

  1. Desde el módulo Procesos generales acceda a [Formulario de Compras](?p=11869) para configurar los formularios para los tipos de comprobantes de compras utilizando las variables de control e impresión disponibles para cada tipo en particular.
  2. Luego seleccione en la grilla el nombre del formulario correspondiente al dibujo a aplicar.
  3. Ingrese el tipo de comprobante.



Dibujar: seleccione este comando para abrir el formulario asociado y acceder al formato de impresión, desde allí le será posible realizar los cambios que necesite en el diseño del comprobante.  
Para confeccionar el modelo de los distintos formularios, consulte las palabras de control, las [variables de reemplazo](?p=14483).

Generación / envío de comprobantes en formato PDF

Para talonarios asociados a órdenes de compra, órdenes de pago, retenciones, puede completar opcionalmente los parámetros para generación y envío de comprobantes en formato PDF[/axcond]retenciones[/axcond].

Imagen de fondo: defina la imagen que utilizará como fondo en la generación del archivo en formato PDF. Puede seleccionar archivos .bmp y .jpg.

Ingrese el directorio y la imagen de fondo (*.bmp, *.jpg) del PDF: ruta válida con la imagen que utilizará como fondo en la generación del archivo en formato PDF. Únicamente utilizable si se definió en versión Tango T19 o anterior.

Copia del archivo PDF:

Guarda Copia: active este parámetro para guardar una copia de todos los comprobantes emitidos en formato PDF. Este parámetro permite mantener una copia de todos los comprobantes emitidos con el talonario, independientemente del destino de impresión que seleccione al emitirlos.

Directorio: ingrese una ruta válida para el almacenamiento en el disco o en un servidor de los archivos. Si utiliza un directorio compartido, todos los usuarios que generen comprobantes deben tener acceso a dicho directorio.

Subdirectorio: seleccione una clasificación para el almacenamiento en el disco de los archivos en formato PDF. Serán ordenados por código de proveedor o por comprobantes.  
Esta opción muestra como ejemplo la ruta seleccionada por el usuario para el almacenamiento. Está conformada por el directorio válido y el subdirectorio seleccionado.

##### Observaciones

Permite ingresar referencias para el nuevo talonario o en aquel talonario que usted esté modificando.

##### Contenidos relacionados

  * [Video sobre imágenes en formularios](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/imgform_gral_vid/)

  * [Video sobre parámetros de Compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/parametros_cp2_vid/)

  * [Video sobre solicitudes de compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/solicitudes_cp2_vid/)

  * [Video sobre órdenes de compra](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/ordencompra_cp2_vid/)

  * [Videos de centralización y transferencia de órdenes y remitos de compras](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralordencompra_cp2_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/retencpercep_gral_vid/)

  * [Videos sobre órdenes de pago individual y masivo](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/ordenpago_cp2_vid/)
