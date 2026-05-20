# Tipos de valorización

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=9821/

## Contenido

# Tipos de valorización

Utilice esta opción para definir los distintos tipos de valorización de las [unidades adicionales](?p=9824) no monetarias.

Ejemplo: si define la unidad adicional 'TRIGO', un tipo de valorización puede ser el precio internacional.  
Contabilidad divide los datos de definición de un tipo de valorización en dos solapas: [Principal](?p=9821#principal) y Observaciones.

##### Principal

Código: ingrese un código que identifique el tipo de valorización a definir. Su ingreso es obligatorio.

Descripción: si lo desea, ingrese una referencia o texto.

Moneda: elija la [moneda](?p=9806) a considerar en el ingreso de la [valorización de las unidades adicionales](?p=9825).  
Ejemplo: el precio internacional del TRIGO está expresado en _Euros_.  
Si cambia la moneda de un tipo de valorización y existen movimientos o valorizaciones ingresadas con esa moneda, el sistema exhibe un mensaje para su confirmación.

Condiciones para eliminar un tipo de valorización:

Es posible eliminar un tipo de valorización sólo si:

  * No existen asientos de unidades adicionales que tengan asociado el tipo de valorización a eliminar;
  * No existen unidades adicionales que utilicen ese tipo de valorización.



Al eliminar un tipo de valorización, se borrarán también las [valorizaciones](?p=9825) definidas. En este caso, el sistema solicita su confirmación para continuar.

##### Contenidos relacionados

  * [Videos sobre parametrización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/paramcontab_gral_vid/)
