# Parámetros de Activo Fijo

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_integrcontabl_cp/?p=5948/

## Contenido

# Parámetros de Activo Fijo

En esta opción, usted define los parámetros de uso exclusivo para el módulo Activo Fijo.

Los parámetros son de aplicación opcional y en caso de definirlos, serán propuestos por defecto por el sistema en los distintos procesos.

Activo Fijo divide los datos para el ingreso de parámetros en dos solapas: Principal y Codificación de bienes.

####  Principal

Si usted desea empezar a trabajar con el módulo y trasportar los saldos de los bienes deberá configurar los siguientes parámetros:

Fecha carga inicial: ingrese una fecha para la cual se informará el saldo inicial de los bienes en la puesta en marcha del módulo.

Tipo de movimiento para carga inicial: seleccione un tipo de movimiento de activación para ingresar el saldo inicial de los bienes en la puesta en marcha del módulo Activo Fijo.

Para poder contabilizar los movimientos será necesario definir los siguientes parámetros:

Tipo de valoración para contabilizar: seleccione un tipo de valoración para generar los asientos contables.

Genera asiento en el ingreso de movimientos: por defecto este parámetro está activado y afecta a los movimientos que generan asiento. En caso de desactivarlo se deberá generar el asiento desde el proceso [Generación de asientos contables de Activo Fijo](?p=5914).

Respeta definición del modelo de asiento: por defecto este parámetro está activado y afecta a los movimientos que generan asiento. Significa que no podrá modificar la configuración del modelo de asiento asociado al movimiento, no se podrán agregar o eliminar líneas del asiento, no podrá modificar los importes, se podrá cambiar una cuenta por otra y se podrán modificar el detalle de auxiliares.

Para cada bien se definirá una moneda que será propia, desde los movimientos es posible visualizar los valores en la moneda del bien. Defina la cantidad de decimales para visualizar esos valores.

Cantidad de decimales: ingrese un valor comprendido entre cero y cuatro (0-4). Por defecto, se propone utilizar dos (2) decimales.

Fecha base para el ajuste del bien: la configuración de este campo determinará el índice base que se considerará para el ajuste por inflación de los bienes (y sus depreciaciones).

Los valores posibles del campo son:

  * **1 - Fecha de compra:** el valor de los activos fijos dados de alta se ajustará por inflación a partir del mes de compra de los bienes (y, consiguientemente, sus depreciaciones).
  * **2 - Fecha de activación:** el ajuste se realizará a partir del mes de activación.



**Nota**

El campo _Fecha base para el ajuste del bien_ modifica el índice base que tomará el sistema para el ajuste por inflación de activos fijos. Si no sigue un criterio uniforme al respecto, la información de sus activos fijos podría resultar inconsistente.

####  Codificación de bienes

Usted puede codificar en forma automática los bienes de acuerdo a los siguientes parámetros:

Usa código incremental: por defecto este parámetro esta desactivado, en el caso de activarlo enumerará a los bienes a partir del 1 en forma incremental.

Incluye prefijo: por defecto este parámetro esta deshabilitado. Se habilita en caso de activar la opción Usa código incremental. Si incluye prefijo para la codificación de bienes, puede seleccionar entre las siguientes prefijos: 'Código de artículo', 'Código de rubro' o 'Código de tipo de bien'.

Usa separador después del prefijo: por defecto este parámetro se presenta desactivado. Se habilita cuando se activa la opción Incluye prefijo. Los posibles separadores son: 'Punto', 'Guión' o 'Blanco'.

Completa con ceros a izquierda: por defecto este parámetro esta deshabilitado, se habilita cuando se activa la opción Usa código incremental. En caso de activarlo, completará con ceros a la izquierda del código incremental.

La codificación de bienes podrá configurarse antes o después de la carga de bienes.
