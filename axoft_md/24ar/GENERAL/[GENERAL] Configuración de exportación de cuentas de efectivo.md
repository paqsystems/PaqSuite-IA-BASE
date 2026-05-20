# Configuración de exportación de cuentas de efectivo

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_transfer_reut/guias_gestioncentral_transf_reut/?p=11845/

## Contenido

# Configuración de exportación de cuentas de efectivo

La configuración de exportación de cuentas en efectivo le permite indicar para cada cuenta de efectivo, el importe que quedará disponible en cada sucursal al momento de exportar comprobantes de tesorería para su gestión centralizada.

Esta configuración es necesaria si va a utilizar el circuito de transferencia de valores incluyendo cuentas de efectivo, es decir, si va a recaudar dinero en efectivo de sus sucursales y desea transferir los movimientos en forma automática.

__Nota

La información especificada en este proceso sólo se aplica al exportar comprobantes desde sucursales. Es necesario que las cuentas de tesorería que defina existan en las sucursales donde se aplique esta configuración.

Cuenta y Descripción: indique el código de cuenta de tesorería. En la descripción se muestra el nombre de la cuenta indicada.  
Sólo se visualizan para seleccionar las cuentas definidas como de tipo 'Otras', de 'Tesorería' y con el campo exporta activado.

__Nota

Si en las columnas de porcentaje o importe se dejan valores en cero, al momento de exportar los comprobantes de tesorería para gestión central, el saldo de la cuenta quedará en cero.

La configuración se divide en dos secciones: sección Defecto y sección Excepció.

__Nota

La sección Excepción sólo se visualiza cuando se encuentra trabajando en una empresa definida como 'Sucursal'.

Sección defecto: es el valor que siempre se dejará en la cuenta al momento de exportar. Los datos de esta sección son obligatorios.

Tipo: indique el tipo de valor con el cual se va a calcular el monto de la cuenta a dejar en la sucursal. Los tipos de valor pueden ser importe ('I') o porcentaje ('P').

Importe: si en Tipo seleccionó 'Importe', indique el importe que se deja en la cuenta de la sucursal al momento de exportar comprobantes de tesorería para gestión central.  
El importe que se considera es el correspondiente al saldo actual en moneda corriente de la cuenta.

Porcentaje: si en Tipo seleccionó 'Porcentaje', indique el porcentaje que se va a utilizar para calcular el monto a dejar en la cuenta de la sucursal al momento de exportar los comprobantes de tesorería para gestión central.  
Si en las columnas de porcentaje o importe se dejan valores en cero, al momento de exportar los comprobantes de tesorería para gestión central, el saldo de la cuenta quedará en cero.

Sección excepción: es el valor que se dejará en la cuenta al momento de exportar, pero sólo cuando la fecha en que se realice la exportación esté comprendida en el rango de fechas de la excepción.  
Se informan los mismos datos que en la sección defecto, con el agregado del rango de fechas que comprende la excepción. La información de estos datos no es obligatoria y la configura cada sucursal.

Tipo de fecha: indique el tipo de fecha que va a tomar para configurar el rango de excepción.  
Los tipos de fecha que puede seleccionar son:

  * Definido por el usuario
  * Primer día mes actual
  * Quinto día mes actual
  * Décimo día mes actual
  * Último día mes actual
  * Primer día semana actual
  * Último día semana actual
  * Primer semana mes actual
  * Última semana mes actual
  * Primer quincena mes actual
  * Última quincena mes actual
  * Sin fecha de excepción



Fecha Desde - Hasta: si en la columna Tipo de Fecha seleccionó 'Definido por el usuario', indique el rango de fechas que comprende la excepción.  
Para el resto de los tipos de fechas no es necesario informar los rangos ya que los calcula automáticamente el sistema.

**Ejemplo de corrección según criterios...**  
Luego de exportar comprobantes de tesorería para gestión central, donde intervenga la cuenta de tipo efectivo '2 - Caja Mostrador', le quedará un saldo de $200 en la sucursal (configuración que se realiza en la sección Defecto), pero hay un día del mes que se necesita contar con más efectivo, ya que en la sucursal se deben realizar pagos a proveedores, entonces para ese día se configuran los valores en la sección Excepción.  
Luego de exportar comprobantes para gestión central para el día 19/10/2019 y donde intervenga la cuenta '2 - Caja Mostrador' , a la cuenta le va a quedar un saldo de $5000.00.

Al importar Tablas Generales en una sucursal, se van a pisar los valores configurados desde casa central, correspondientes a la Sección Defecto, no siendo así para la Sección Excepción donde se mantienen los valores definidos por la sucursal.

##### Contenidos relacionados

  * [Video sobre multicaja en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/multicaja_gv_vid/)

  * [Videos sobre transferencia de valores](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfvalor_gral_vid/)
