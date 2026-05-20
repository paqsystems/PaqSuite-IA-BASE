# Guía sobre comprobantes con diferencias

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_comprobdifer_cp2/

## Contenido

# Guía sobre comprobantes con diferencias

El circuito de comprobantes con diferencias está apuntado a detectar dos tipos de diferencias, las mismas son aquellas provocadas por:

**1\. Precios**

  * Precios facturados mayor a los precios definidos en las listas de precios
  * Bonificación facturada menor a la bonificación definida en la lista de precios



**2\. Cantidad**

  * Para Factura-Remito como para Remitos: cantidad facturada mayor a la cantidad recibida



De no detectarse estas diferencias provocarían un pago mayor al correspondiente.  
Si está activo el [Parámetro de Stock](?p=17198) Lleva doble unidad de medida, se considerarán las cantidades expresada en la unidad de medida de stock 1.  
A continuación se detallan los pasos y el orden de configuración a seguir para implementar el control de diferencias en facturas y el control de diferencias en remitos.

##### Primer paso

Módulo Compras - Parámetros de Compras Dentro de parámetros generales se encuentran los siguientes campos que debe configurar:

Controla comprobantes con diferencias: configure este parámetro como 'Flexible' o 'Estricto' para activar el control de diferencias.  
Si configura este parámetro como 'Flexible', el sistema emitirá un mensaje indicando que se está generando una diferencia, en ese momento puede optar por corregir dicha diferencia o continuar (en esta modalidad el comprobante queda marcado con diferencia).  
En cambio, si se configura como 'Estricto', el sistema emitirá un mensaje de aviso pero no permitirá continuar hasta que se salve la diferencia.  
Luego, defina para cada comprobante ('FP': Factura / Factura de Importación o 'FS': Factura - Remito, 'RP': Remito de Proveedores), el tipo de diferencia a controlar.  
Los tipos de diferencias posibles de controlar son los siguientes:

  * **Diferencia por cantidad:** es la diferencia que se genera por haber recibido un comprobante de un proveedor por una cantidad facturada o a facturar mayor a la cantidad recepcionada.
  * **Diferencia por precio:** esta diferencia se genera por haber recibido un comprobante: 
    * en el que el precio de uno o más artículos es mayor al precio definido en la lista de precios.
    * también se genera diferencia por precio cuando se recibe un comprobante en el que el descuento de uno o más artículos es menor al descuento definido en la lista de precios seleccionada en el comprobante.



Remite cantidades mayores a las facturadas: configure este parámetro como 'Flexible' o 'Estricto' para activarlo. Si se activa, durante la carga del comprobante se va a permitir ingresar para cada artículo una cantidad remitida mayor a la facturada.

Asume cantidad remitida igual a la facturada: al activar este parámetro en la carga de los comprobantes se completa por defecto la cantidad remitida con el mismo valor que la cantidad facturada pudiendo ser editada.

En el siguiente cuadro se resume para cada comprobante, el tipo de diferencia posible de controlar:

Tipo de Comprobante | Controlar  
---|---  
Factura | Diferencias por precio  
Factura - Remito | Diferencias por precio  
Factura - Remito | Diferencias por cantidad  
Factura de importación | Diferencias por precio  
Remito | Diferencia por cantidad  
Remito | Diferencias por precio  
  
__Nota

Las facturas pueden presentar una diferencia por cantidad trasladada desde un remito con diferencia referenciada.

##### Segundo paso

Módulo Compras - Actualización de Precios Individual  
Para que los comprobantes controlen diferencias de precios, debe existir una lista de precios creada para el proveedor y el artículo que se está facturando/remitiendo, y en el comprobante se debe utilizar la lista de precios correspondiente.  
Por lo tanto el segundo paso consiste en crear una lista de precios para cada proveedor que contenga los artículos que se le suelen comprar.

##### Tercer paso

Módulo Compras - Alta de Facturas  
A medida que se van ingresando los artículos, y de acuerdo a lo configurado en los parámetros generales, el sistema recorre cada uno de los renglones informando si se genera una diferencia de precio o de cantidad, y el monto de dicha diferencia.  
En caso que el control de diferencias se haya configurado como 'estricto', el sistema informa de la situación e impide continuar hasta que se corrijan los valores para que no se provoquen las diferencias. De lo contrario, si se configura como 'flexible', se informa al usuario la diferencia que se va a generar en caso de continuar con la operación.  
Mientras que la factura se encuentre con diferencia de precio o cantidad, la misma no podrá ser pagada. En el momento que se seleccione para pagar, se emitirá un mensaje informando la situación de la factura.

##### Cuarto paso

Módulo Compras - Alta de nota de crédito  
Una de las maneras de resolver las diferencias generadas en las facturas, es mediante el reclamo al proveedor de la nota de crédito que resuelva dicha diferencia.  
Si alguna de las facturas con diferencia referenciadas, tiene algún Remito asociado con diferencia, también podrá resolver la misma.

Módulo Compras - Alta factura  
Las diferencias generadas en los remitos, se resuelven al momento de ingresar la factura referenciada al remito.

  * Facturación total del remito: si se factura el total de la unidades de cada uno de los artículos del remito, el remito queda con la diferencia resuelta.
  * Facturación parcial del remito: en caso que el remito se facture parcialmente, se emitirá un mensaje preguntando si desea resolver la diferencia. En caso de decidir resolver la diferencia, el remito se modifica en forma automática quedando sin diferencia, caso contrario seguirá manteniendo la diferencia, esperando a ser resuelta en el ingreso de una nueva factura o cuando no queden unidades pendientes de facturar.  
Si se ingresa una factura con referencia a un remito que posee diferencia y al menos existe un renglón cuya cantidad a facturar sea mayor a la pendiente de facturar, además de resolver la diferencia en el remito, se traslada la diferencia a la factura.



__Nota

Una factura con diferencia de cantidad trasladada desde un Remito con diferencia referenciado, no será resuelta al desimputar dicho Remito.  
Si se ingresa una factura con referencia a un Remito que no presenta diferencias, pero la cantidad facturada es mayor a la pendiente de facturar, la factura no se guarda con diferencia, sino que queda pendiente de recibir.

**Módulo Compras - Alta remito** Para resolver la diferencia que ha sido trasladada a una factura al referenciar un Remito con diferencia de cantidad, puede ingresar un Remito en referencia a dicha factura por el saldo pendiente.

**Módulo Compras - Modificación de comprobantes  
**Las diferencias generadas en las facturas se pueden eliminar manualmente desde este proceso.  
Las diferencias generadas en los remitos asociados a la factura se pueden resolver mediante la función Dif. en Remitos.

##### Quinto paso

Live - Compras:

Facturas:  
Desde el módulo Compras se puede listar el informe de comprobantes con diferencia, donde se pueden observar tanto las facturas que poseen diferencia como aquellas donde la diferencia fue resuelta.  
Aquellas facturas cuya diferencia son resueltas manualmente, mediante la opción de modificación de comprobantes, no se visualizan en esta consulta.

Remitos:  
Desde el módulo Compras se puede listar el informe de remitos con diferencias.

##### Sexto paso. Opcional: verifica desvío en precios

Módulo Compras - Parámetros de Compras Desde parámetros generales se puede definir si se contempla un desvío para los precios, el campo a configurar es el siguiente:

Verifica desvío en precios: este parámetro se aplica en los comprobantes de Factura - Remito, Factura sobre remito y Factura de Importación y Remitos.

Para activar el control en la modificación de precios, y que se considere para el cálculo de diferencias, configure este campo como flexible, ya que en caso de configurarlo como estricto no se generará una diferencia por precio, dado que el control de desvío de precios se efectúa antes que el control de diferencia por precio.  
Si verifica desvío de precios, para el cálculo de las diferencias en facturas / remitos por precio, se considera el desvío configurado en la lista de precios.

Módulo Stock - Artículos

Usa desvío en precios: activando este parámetro en el ingreso de comprobantes de compras se va a realizar el control sobre la modificación del precio, con respecto al precio informado en la lista de precios de Compras.

Módulo Compras - Actualización de Precios Individual  
Seleccione el proveedor y la lista de precios y configure el desvío permitido para cada artículo.

Desvío: a medida que usted se desplace por los renglones de la lista de precios, si está activo el parámetro Verifica Desvío de Precios (en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2)) y el artículo tiene activado el parámetro Usa Desvío en Precios (en el proceso Artículos del módulo Stock), accede a la ventana de Desvío de Precios para su configuración. Defina el tipo de desvío a aplicar: 'Por Porcentaje' o bien, 'Por Precio' e ingrese el valor correspondiente (porcentaje o importe).

**Ejemplo 1:** para un artículo con precio igual a 100, se configura lo siguiente:

  * **Tipo de desvío:** por Porcentaje del 20%  
En este caso, se permite modificar el precio hasta un importe de $120.



**Ejemplo 2:** para un artículo con precio igual a 100, se define:

  * **Tipo de desvío:** por Precio por $10  
En este caso, se permite modificar el precio hasta un importe de $110.



Si usted definió que Usa desvío en precios, el control en la modificación de precios de artículos se aplicará sobre el precio más el porcentaje o importe de desvío.  
Durante el ingreso de comprobantes, si está activo el parámetro general Controla comprobantes con diferencias (del proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-controles)), se efectúa dicho control cuando en la factura se modifique el precio de los artículos.

##### Contenidos relacionados

  * [Facturas de importación](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/comprobfactura_cp2/factimport_cp2/)

  * [Ingreso de remitos](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/remitos_carp_cp2/ingresoremito_cp2/)

  * [Notas de crédito de artículos](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/notacreditoprov_cp2/ncarticulo_cp2/)

  * [Notas de crédito de conceptos](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/notacreditoprov_cp2/ncconcepto_cp2/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre remitos y facturas de compra](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/remitofactura_cp2_vid/)
